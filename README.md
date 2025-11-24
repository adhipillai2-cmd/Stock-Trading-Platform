#  Wall Street Pro: Algorithmic Trading Platform

A full-stack financial dashboard that allows users to simulate stock trading with real-time market data. Built using a Microservices architecture to separate data ingestion from visualization.


![Stock Market Demo Image](https://github.com/user-attachments/assets/7ca967ab-2cb7-43fd-9b5b-0af495a09fb2)

##  Live Demo
**Try the App:** https://stock-trading-platform-5s4psjlta4zzz2es33wbmq.streamlit.app/

*(Note: The backend runs on a free instance, so please allow 45-60 seconds for the initial "Cold Start" wakeup).*

##  Architecture
The application follows a distributed Client-Server architecture:

* **Frontend (Streamlit):** Handles user session state, portfolio logic (Buy/Sell), and visualization.
* **Backend (FastAPI):** A RESTful API that acts as a gateway to Yahoo Finance, handling data normalization and error checking.
* **Communication:** The frontend consumes the backend via HTTP requests (JSON).

##  Tech Stack
* **Language:** Python 3.12
* **Backend:** FastAPI, Uvicorn, Yfinance
* **Frontend:** Streamlit, Pandas, Requests
* **Deployment:** Render (API) + Streamlit Cloud (UI)

##  Key Features
* **Real-Time Data:** Fetches live pricing via a custom API wrapper.
* **State Management:** Tracks User Cash & Portfolio holdings across sessions.
* **Visualization:** Interactive 30-day price history charts.
* **Robustness:** Handles API failures and invalid ticker symbols gracefully.
