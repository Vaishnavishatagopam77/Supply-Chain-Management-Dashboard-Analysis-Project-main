import streamlit as st  # Importing Streamlit for building the dashboard
import requests  # To send HTTP requests to our FastAPI backend
import pandas as pd  # For working with tabular data
import plotly.express as px  # For creating interactive plots

# === Streamlit App ===
st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")  # Configuring the page title and layout
st.title("📦 Supply Chain Analytics Dashboard")  # Setting the main title of the dashboard

# Sidebar filters for user input
st.sidebar.header("Filter")  # Sidebar section header
product_id = st.sidebar.text_input("Enter Product ID")  # User input for product ID

# Section to show complete sales data from MongoDB
st.subheader("📊 All Sales Data")  # Section header
if st.button("Load All Data"):  # Button to trigger data load
    response = requests.get("http://localhost:8000/all_data")  # Send GET request to FastAPI to fetch all data
    if response.status_code == 200:  # Check if request was successful
        data = response.json()  # Convert response to JSON
        df = pd.DataFrame(data)  # Convert JSON to pandas DataFrame
        st.dataframe(df)  # Display data in a scrollable table
        # Optional: Plot sales by product
        if "product_id" in df.columns and "sales_quantity" in df.columns:  # Check if necessary columns exist
            fig = px.bar(df, x="product_id", y="sales_quantity", title="Total Sales by Product")  # Bar chart
            st.plotly_chart(fig, use_container_width=True)  # Display the chart full width
    else:
        st.error("Failed to load data")  # Show error if API call fails

# Section to forecast demand using Prophet model
st.subheader("📈 Forecast Demand")  # Section header
if product_id and st.button("Get Forecast"):
    url = f"http://localhost:8000/forecast/{product_id}"  # Construct API URL with product ID
    response = requests.get(url)  # Send GET request to FastAPI
    if response.status_code == 200:  # If response is successful
        forecast_data = response.json()  # Load JSON data
        forecast_df = pd.DataFrame(forecast_data)  # Convert to DataFrame
        forecast_df["ds"] = pd.to_datetime(forecast_df["ds"])  # Convert date column to datetime

        # Line plot of forecasted demand
        fig = px.line(forecast_df, x="ds", y="yhat", title="Forecasted Sales for Next 30 Days",
                      labels={"ds": "Date", "yhat": "Predicted Sales"})  # Create line plot
        st.plotly_chart(fig, use_container_width=True)  # Display chart
    else:
        st.error("Could not fetch forecast.")  # Show error

# Section for Inventory Optimization using Reorder Point strategy
st.subheader("📦 Inventory Optimization")  # Section header
if product_id and st.button("Optimize Inventory"):
    url = f"http://localhost:8000/inventory_optimize/{product_id}"  # Construct API URL with product ID
    response = requests.get(url)  # Send GET request
    if response.status_code == 200:  # If request was successful
        result = response.json()  # Parse response JSON
        st.json(result)  # Display result in JSON format in the UI
    else:
        st.error("Inventory data not found")  # Show error message

# Section for Market Sentiment Analysis
st.subheader("💬 Market Sentiment Analysis")  # Section header
market_text = st.text_area("Enter market news or customer feedback")  # Text input area for user
if market_text and st.button("Analyze Market Trend"):
    response = requests.post("http://localhost:8000/market_analysis", params={"text": market_text})  # Send POST request with text
    if response.status_code == 200:  # If request was successful
        result = response.json()  # Parse response JSON
        st.write("**Sentiment:**", result["sentiment"])  # Show sentiment
        st.write("**Confidence Score:**", result["confidence"])  # Show confidence
        st.write("**Action:**", result["suggested_action"])  # Show recommended action
    else:
        st.error("Analysis failed")  # Show error if API fails
