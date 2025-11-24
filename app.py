#libraries
import streamlit as st
import requests
import pandas as pd

#sets title and layout of page
st.set_page_config(page_title = "Wall street dashboard", layout = "centered")
st.title("API-Powered Stock Dashboard")

#makes sure sesssion doesnt start from scratch every time, stores memory
if 'price' not in st.session_state:
    st.session_state.price = None
    st.session_state.history = []
    st.session_state.symbol = ""

    #portfolio information
    st.session_state.cash = 10000.00
    st.session_state.portfolio = {}
    st.session_state.log = []

#creates a sidebar that puts the elements on the left
st.sidebar.header("Controls")
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL").upper()

#triggers API call
#if statement checks if button is pressed
if st.sidebar.button("Get Quote"):
    #creates spinner for real life server/website effect
    with st.spinner("Talking to Backend..."):
        #define the API URL and point to localhost where uvicorn server is running
        api_url = f"https://stock-api-44lt.onrender.com/quote/{ticker}"
        #makes the call and gets all ticker data
        response = requests.get(api_url)
        #makes variable for pulled ticker data
        data = response.json()
        if 'error' not in data:
        #gets all data
            st.session_state.symbol = data['symbol']
            st.session_state.price = data['current_price']
            st.session_state.history = data['history']
            st.success("Data retrieved successfully!")

        else:
            st.error("Ticker does not exist")

st.markdown("Portfolio")
col_cash, col_cal, col_net = st.columns(3)

#displauys cash
col_cash.metric("Cash Balance", f"${st.session_state.cash:.2f}")

if st.session_state.price:
    st.markdown("---")
    st.subheader(f"Trading: {st.session_state.symbol} @ ${st.session_state.price:.2f}")

    trade_col1, trade_col2 = st.columns([2,1])

    with trade_col1:
        st.line_chart(st.session_state.history)

    with trade_col2:
        #quantity input
        quantity = st.number_input("Quantity", min_value=1, value = 1, step=1)
        total_cost = quantity * st.session_state.price

        st.write(f"Total Cost: ${total_cost:.2f}")

        #buy and sell buttons
        b_col, s_col = st.columns(2)

        #buy logic
        if b_col.button("Buy"):
            if st.session_state.cash >= total_cost:
                #deduct cash
                st.session_state.cash -= total_cost
                #add to portfolio
                current_qty = st.session_state.portfolio.get(st.session_state.symbol, 0)
                st.session_state.portfolio[st.session_state.symbol] = current_qty + quantity
            else:
                st.error("Insufficient funds to complete purchase.")

        #sell logic
        if s_col.button("Sell"):
            current_qty = st.session_state.portfolio.get(st.session_state.symbol, 0)
            if current_qty >= quantity:
                #add cash
                st.session_state.cash += total_cost
                #deduct from portfolio
                st.session_state.portfolio[st.session_state.symbol] = current_qty - quantity
                #if sold everything, remove the ticker from the dictionary
                if st.session_state.portfolio[st.session_state.symbol] == 0:
                    del st.session_state.portfolio[st.session_state.symbol]
                    
                st.success(f"Sold {quantity} shares of {st.session_state.symbol}!")
                st.rerun()
            else:
                st.error("Insufficient shares to complete sale.")

st.markdown("---")
st.subheader("Current Stock Information")

if st.session_state.portfolio:
    df = pd.DataFrame(list(st.session_state.portfolio.items()), columns=["Symbol", "Quantity"])
    st.table(df)
else:
    st.info("No stocks in portfolio.")
