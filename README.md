# Supply Chain Management Dashboard

## Project Overview
This project is part of my internship at **Unified Mentors**, where I am working on analyzing the supply chain of a Fashion and Beauty startup that sells makeup products. The goal is to use data analysis to gain insights into product performance, customer behavior, and the overall supply chain. The project involves cleaning the data, exploring it, creating new features, and building an interactive dashboard using Streamlit to visualize important metrics.



You can view the live dashboard here: [Supply Chain Management Dashboard](https://supply-chain-management-dashboard-analysis-project-nstdf4xfnlp.streamlit.app)

## Features
- Interactive dashboard to view key supply chain metrics.
- Insights into product performance, shipping efficiency, and customer demographics.
- Metrics like profit margins, shipping costs, and lead times.
- Data cleaning and preparation to ensure accurate analysis.
- Comprehensive exploration of data to identify patterns and trends.

## Technologies Used
- Python
- Pandas (for data handling)
- NumPy (for numerical calculations)
- Matplotlib and Seaborn (for data visualizations)
- Plotly (for interactive charts)
- Streamlit (for the dashboard)

## Dataset
The dataset used in this project contains various features, including:
- Product Type
- SKU (Stock Keeping Unit)
- Price
- Availability
- Number of Products Sold
- Revenue Generated
- Customer Demographics
- Stock Levels
- Lead Times
- Order Quantities
- Shipping Times
- Shipping Carriers
- Shipping Costs
- Supplier Name
- Location
- Manufacturing Costs
- Defect Rates

## Setup Instructions
1. Clone the project repository:
   ```bash
   git clone https://github.com/carinadesouza/Supply-Chain-Management-Dashboard-Analysis-Project.git
   cd supply-chain-dashboard
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage:
1. Place the dataset (supply_chain_data.csv) in the project directory.
2. Run the Streamlit application:
   ```bash
    streamlit run app.py
   ```
3. Open your browser and navigate to http://localhost:8501 to access the dashboard.

## Data Preparation

The data was cleaned and prepared by:

Handling missing values and removing duplicate entries.
Identifying and treating outliers using the Interquartile Range (IQR) method.
Standardizing categorical data for consistency across the dataset.

## Exploratory Data Analysis (EDA)

To understand the data, we performed the following:

Histograms to analyze the distribution of numerical features.
Boxplots to detect outliers in the dataset.
Correlation heatmaps to visualize relationships between different variables.

## Feature Engineering

We created the following features to enhance our analysis:

Profit Margin: Measures product profitability.
Price-to-Revenue Ratio: Assesses pricing strategy efficiency.
Lead Time Efficiency: Evaluates how effectively lead times are managed.
Shipping Cost per Unit: Calculates the cost of shipping per product.
Days in Inventory: Measures how long stock lasts based on order quantities.

##Conclusion

This project provides valuable insights into the efficiency of the supply chain, product performance, and customer demographics. The findings will help the startup optimize their operations, reduce costs, and improve profitability. This project is an important part of my internship at Unified Mentors, and I am proud to contribute meaningful insights that can drive business decisions.






