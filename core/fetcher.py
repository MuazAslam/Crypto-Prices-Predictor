import yfinance as yf
from datetime import datetime

class StockFetcher:
    def __init__(self, symbol):
        self.__symbol = symbol 
        self.__end_date = datetime.now()                 
        self.__start_date = datetime(self.__end_date.year-1, self.__end_date.month, self.__end_date.day)
        self.__data = None
    
    def fetch_data(self): 
        try:
            print(f"Fetching data for {self.__symbol}...")
            self.__data = yf.download(self.__symbol, start=self.__start_date, end=self.__end_date,threads=False)
            if self.__data.empty:
                raise ValueError("No data found for the provided symbol.")
            return self.__data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return self.__data

    def get_close_prices(self):
        if self.__data is not None:
            return self.__data[['Close']]

