#imports, fastapi for server and yf for stock data
from fastapi import FastAPI  
import yfinance as yf

#creates the actual applciation object
app = FastAPI()

#makes sure if someone visits the site root, this function runs
@app.get("/")
def read_root():
    return {"message": "Wall Street API is running"}

#makes the URL dynamic so stock data depends on whichever symbol (stock) is entered
#function to get stock data
@app.get("/quote/{symbol}")
def get_stock(symbol: str):
    #makes the input uppercase as all tickers are uppercase only
    ticker = symbol.upper()
    
    #creates a variable that gets data from yfinance for whatever stock is requested
    stock = yf.Ticker(ticker)

    #requests a month of stock data
    #pandas dataframe
    history = stock.history(period="1mo")
    #checks to see if there is not history, will trigger when invalid stock is entered
    if history.empty:
        return {"error": "Invalid stock symbol or no data available."}
    #fetches the most price column, then the latest price from that column
    else:
        current_price = history['Close'].iloc[-1]
        #creates a list for charting purposes
        price_list = history['Close'].tolist()
        return {
            "symbol": ticker, 
            "current_price": current_price,
            "history": price_list 
        }
    