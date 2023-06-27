from datetime import date
from dateutil.relativedelta import relativedelta
import streamlit as st 
import yfinance as yf 

st.title("yfinance")
st.header("::wolf:: Market Data")
st.write("---")

POPULAR_STOCK = ["MSFT", "TSLA", "GOOGL", "AAPL", "AMZN", "NVDA", "META", "NFLX", "INTC", "COIN"]

today = date.today()
three_year_ago = today - relativedelta(years=2)

if "tickers" not in st.session_state:
    st.session_state["tickers"] = ["GOOGL", "AAPL"]

if "dates" not in st.session_state:
    st.session_state["dates"] = [today - relativedelta(years=3), today]
    
if "interval" not in st.session_state:
    st.session_state["interval"] = "1mo"

tickers = st.multiselect("Choose ticker", POPULAR_STOCK, key="tickers")
start, end = st.slider("Date range:", key="dates")
interval = st.select_slider("Interval",["1d", "5d","1wk", "1mo", "3mo"], key="interval")


data = yf.Tickers(" ".join(tickers))

# get all stock info
# data.info
# show meta information about the history (requires history() to be called first)
# data.history_metadata

# get historical market data based on interval from start date, end date 
df = data.history(start=start, end=end, interval=interval)

with st.expander("Raw Data"):
    st.write(df)
    
st.line_chart(df.Close)
st.line_chart(df.Volume)