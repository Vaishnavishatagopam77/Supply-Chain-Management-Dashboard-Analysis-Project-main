import pandas as pd  # Importing pandas for data manipulation
import matplotlib.pyplot as plt  # For basic plotting
import seaborn as sns  # For advanced statistical visualizations
import plotly.express as px  # For interactive plots

# === Load Dataset ===
df = pd.read_csv('supply_chain_data.csv')  # Load the supply chain data CSV into a DataFrame

# === Data Preprocessing ===
missing_values = df.isnull().sum()  # Count missing values in each column
print("Missing Values:\n", missing_values)  # Print missing value count per column

print("First few rows of the dataset:")  # Print header text for preview
print(df.head())  # Show the first 5 rows

print("\nDataset Information:")  # Print header text for dataset info
df.info()  # Display column types, non-null counts

print("\nData types of columns:")  # Print header
print(df.dtypes)  # Show data types of each column

print("\nShape of the dataset (rows, columns):")  # Print header
print(df.shape)  # Show shape of dataset (rows, cols)

print("\nAre there any duplicate rows?:")  # Print header
duplicates = df.duplicated().any()  # Check for any duplicate rows
print(duplicates)  # Print True if duplicates found

if duplicates:  # If any duplicates
    df = df.drop_duplicates()  # Drop duplicate rows

print("\nIndex of the dataframe:")  # Print index of DataFrame
print(df.index)  # Display the index object

print("\nColumns of the dataframe:")  # Print header
print(df.columns)  # Show all column names

# === Type Conversion & Cleaning ===
numeric_columns = ['Price', 'Revenue generated', 'Stock levels', 'Lead times', 
                   'Order quantities', 'Shipping times', 'Shipping costs', 
                   'Manufacturing costs', 'Defect rates', 'Production volumes', 'Costs']  # List of numeric columns
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')  # Convert to numeric and handle errors

df['Product type'] = df['Product type'].str.strip().str.lower()  # Clean product type (strip & lowercase)
df['Supplier name'] = df['Supplier name'].str.strip().str.lower()  # Clean supplier name
df['Location'] = df['Location'].str.strip().str.lower()  # Clean location names

# === Outlier Detection ===
Q1 = df[['Price', 'Revenue generated', 'Manufacturing costs']].quantile(0.25)  # Q1 for selected cols
Q3 = df[['Price', 'Revenue generated', 'Manufacturing costs']].quantile(0.75)  # Q3
IQR = Q3 - Q1  # Calculate Interquartile Range

outliers = (df[['Price', 'Revenue generated', 'Manufacturing costs']] < (Q1 - 1.5 * IQR)) | \
           (df[['Price', 'Revenue generated', 'Manufacturing costs']] > (Q3 + 1.5 * IQR))  # Boolean mask of outliers
print("\nOutliers found in the dataset (True means outliers present):")  # Header
print(outliers.any())  # Print True for columns with outliers

# === Feature Inspection ===
print("\nUnique values in 'Customer demographics':")  # Print header
print(df['Customer demographics'].unique())  # Unique values in this column

invalid_defect_rates = df[(df['Defect rates'] < 0) | (df['Defect rates'] > 1)]  # Invalid percentages
print("\nInvalid Defect rates (if any):")  # Print header
print(invalid_defect_rates)  # Display invalid rows

df['Costs'] = pd.to_numeric(df['Costs'], errors='coerce')  # Ensure numeric type

# Force correct types
df['Price'] = df['Price'].astype(float)
df['Availability'] = df['Availability'].astype(int)

# === Feature Engineering ===
df['Profit Margin'] = (df['Revenue generated'] - df['Manufacturing costs']) / df['Revenue generated']  # Profit margin formula
df['Price to Revenue Ratio'] = df['Price'] / df['Revenue generated']  # Price/Revenue ratio
df['Lead Time Efficiency'] = df['Lead times'] / df['Shipping times']  # Lead time efficiency metric
df['Shipping Cost per Unit'] = df['Shipping costs'] / df['Order quantities']  # Cost per unit
df['Days in Inventory'] = df['Stock levels'] / df['Order quantities']  # Inventory duration
df['Defect Rate per Production Volume'] = df['Defect rates'] / df['Production volumes']  # Defects per unit

df['Revenue per Product Type'] = df.groupby('Product type')['Revenue generated'].transform('sum')  # Total revenue by product
df['Average Shipping Time per Carrier'] = df.groupby('Shipping carriers')['Shipping times'].transform('mean')  # Avg time by carrier

df['Manufacturing Cost per Unit'] = df['Manufacturing costs'] / df['Production volumes']  # Cost per item
df['Stock Turnover Rate'] = df['Order quantities'] / df['Stock levels']  # Turnover rate
df['Cost to Revenue Ratio'] = df['Costs'] / df['Revenue generated']  # Cost efficiency ratio

# === Visualizations ===
df[numeric_columns].hist(bins=20, figsize=(14, 10), layout=(4, 3))  # Plot histograms for all numeric columns
plt.suptitle('Distribution of Numerical Features')  # Set title for all histograms
plt.show()  # Show plots

for col in numeric_columns:  # Loop through numeric columns
    plt.figure(figsize=(8, 4))  # Set figure size
    sns.boxplot(x=df[col])  # Boxplot for each column
    plt.title(f'Boxplot of {col}')  # Set title
    plt.show()  # Display plot

plt.figure(figsize=(10, 8))  # Set size for heatmap
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")  # Heatmap of correlations
plt.title("Correlation Heatmap of Numerical Features")  # Title
plt.show()  # Show heatmap

categorical_cols = ['Product type', 'Shipping carriers', 'Supplier name', 'Location']  # List of categorical columns
for col in categorical_cols:  # Loop over them
    plt.figure(figsize=(8, 5))  # Set plot size
    sns.countplot(x=df[col], palette='viridis')  # Count of each category
    plt.title(f'Distribution of {col}')  # Title
    plt.xticks(rotation=45)  # Rotate labels
    plt.show()  # Display plot

# === Pairwise Analysis Plots ===
plt.figure(figsize=(8, 6))  # Set figure size
sns.scatterplot(y=df['Price'], x=df['Revenue generated'])  # Scatter plot
plt.title('Price vs Revenue Generated')  # Title
plt.xlabel('Price')  # X-axis label
plt.ylabel('Revenue Generated')  # Y-axis label
plt.show()  # Display

plt.figure(figsize=(8, 6))
sns.scatterplot(y=df['Stock levels'], x=df['Order quantities'])
plt.title('Stock Levels vs Order Quantities')
plt.xlabel('Stock Levels')
plt.ylabel('Order Quantities')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Manufacturing costs'], y=df['Defect rates'])
plt.title('Manufacturing Costs vs Defect Rates')
plt.xlabel('Manufacturing Costs')
plt.ylabel('Defect Rates')
plt.show()

# === Grouped Insights ===
plt.figure(figsize=(10, 6))
sns.barplot(x=df['Revenue per Product Type'].value_counts().index, 
            y=df['Revenue per Product Type'].value_counts().values)
plt.title('Revenue per Product Type')
plt.xlabel('Product Type')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=df['Average Shipping Time per Carrier'].value_counts().index, 
            y=df['Average Shipping Time per Carrier'].value_counts().values)
plt.title('Average Shipping Time per Carrier')
plt.xlabel('Carrier')
plt.ylabel('Average Shipping Time')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Lead Time Efficiency'], y=df['Revenue generated'])
plt.title('Lead Time Efficiency vs Revenue Generated')
plt.xlabel('Lead Time Efficiency')
plt.ylabel('Revenue Generated')
plt.show()

# === Final Data Overview ===
print("\nData after cleaning:")
df.info()  # Final summary

df.to_csv('cleaned_supply_chain_data.csv', index=False)  # Save cleaned dataset
