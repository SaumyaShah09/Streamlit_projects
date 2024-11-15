import streamlit as st
import yfinance as yf
import plotly.express as px
import datetime
import numpy as np
import pandas as pd

st.title("Stock Dashboard")

# Input fields
ticker = st.sidebar.text_input("Ticker", value="AAPL")  # Default value for testing
start_date = st.sidebar.date_input("Start Date", value=datetime.date(2023, 1, 1))  # Correct date format
end_date = st.sidebar.date_input("End Date", value=datetime.date(2023, 12, 31))  # Correct date format

# Fetch stock data using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Handle data
if data.empty:
    st.error("No data found. Check the ticker or date range.")
else:
    # Ensure 'Adj Close' is 1-dimensional
    adj_close = data['Adj Close'].squeeze()  # Convert to 1D if it's 2D
    fig = px.line(data_frame=data, x=data.index, y=adj_close, title=f"{ticker} Stock Prices")
    st.plotly_chart(fig)

    pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

    with pricing_data:
        st.header("Pricing Movements")
        data2 = data.copy()  # To prevent modifying the original data
        data2['%Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
        data2.dropna(inplace=True)
        st.write(data2)

        annual_return = data2['%Change'].mean() * 252 * 100  # Approximate annual return
        st.write("Annual Return is:", annual_return, "%")

        stdev = np.std(data2['%Change']) * np.sqrt(252)  # Approximate annualized standard deviation
        st.write("Standard Deviation is:", stdev * 100, "%")

        risk_adjusted_return = annual_return / (stdev * 100)
        st.write("Risk Adjusted Return is:", risk_adjusted_return)

    with fundamental_data:
        st.header("Fundamental Data")

        try:
            # Get fundamental data using yfinance
            stock = yf.Ticker(ticker)

            # Fetch financial data
            financials = stock.financials
            balance_sheet = stock.balance_sheet
            cash_flow = stock.cashflow

            if financials.empty:
                st.warning("No income statement (financials) data available.")
            else:
                st.subheader("Income Statement (Financials)")
                st.write(financials)

            if balance_sheet.empty:
                st.warning("No balance sheet data available.")
            else:
                st.subheader("Balance Sheet")
                st.write(balance_sheet)

            if cash_flow.empty:
                st.warning("No cash flow data available.")
            else:
                st.subheader("Cash Flow Statement")
                st.write(cash_flow)

        except Exception as e:
            st.error(f"Error fetching fundamental data: {e}")

    with news:
        st.header(f"News of {ticker}")

        try:
            # Get news using yfinance
            stock = yf.Ticker(ticker)
            news_data = stock.news

            if not news_data:
                st.warning("No news data available.")
            else:
                for i in range(min(10, len(news_data))):
                    st.subheader(f"News {i + 1}")
                    st.write(news_data[i]['title'])
                    st.write(news_data[i]['link'])
                    st.write(news_data[i]['publisher'])
                    st.write(news_data[i].get('published', 'No date available'))

        except Exception as e:
            st.error(f"Error fetching news: {e}")
