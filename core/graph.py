import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from core import predictor

class VisualizerBase:
    def plot(self, data, symbol):
        raise NotImplementedError("Subclasses must implement this method.")

class GraphPlotter(VisualizerBase):
    def __init__(self):
        self.__closing_price = None

    def set_close_prices(self, closing_price):
        self.__closing_price = closing_price

    def close_prices(self, symbol):
        if self.__closing_price is not None:
            df = self.__closing_price.copy()

            plt.figure(figsize=(14, 3))  
            fig = plt.gcf()
            fig.patch.set_facecolor('#14151b')  
            ax = plt.gca()
            ax.set_facecolor('#14151b')  
        
            plt.plot(df.index, df['Close'], color='orange', linewidth=2, label="Close Price")

            plt.title(f"Close Prices of {symbol.upper()} Over Time", fontsize=14, color='white', fontname="Arial", weight='bold')
            plt.xticks(rotation=45, color='white', fontsize=10, fontname="Arial") 
            plt.yticks(color='white', fontsize=10, fontname="Arial")

            
            plt.grid(True, linestyle='--', color='white')  

            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['bottom'].set_visible(False)

            
            plt.tight_layout()

        
            return fig
        else:
            print("[WARNING] No closing price data to plot.")

    
    def plot_last_year_comparison(self,predictor, symbol):
        df = predictor.df.copy()

        last_year_data = df.tail(365)

        X_last_year = last_year_data[["Prev_Close", "5_MA", "10_MA"]].values
        y_true = last_year_data["Close"].values
        y_pred = predictor.get_model().predict(X_last_year)
        dates = last_year_data["Date"]

        plt.figure(figsize=(14, 3))
        fig = plt.gcf()
        fig.patch.set_facecolor('#14151b')
        ax = plt.gca()
        ax.set_facecolor('#14151b')

        plt.plot(dates, y_true, label="Actual", color='orange', linewidth=2)
        plt.plot(dates, y_pred, label="Predicted", color='#636ef9', linestyle='--', linewidth=2)

        plt.title(f"Actual vs Predicted Close Prices - {symbol.upper()} (Last Year)", fontsize=14, color='white', fontname="Arial", weight='bold')
        plt.xticks(rotation=45, color='white', fontsize=10, fontname="Arial")
        plt.yticks(color='white', fontsize=10, fontname="Arial")

        plt.grid(True, linestyle='--', color='white')
        plt.legend(facecolor='#14151b', edgecolor='white', fontsize=10,labelcolor='white')

        # Hide spines
        for spine in ax.spines.values():
            spine.set_visible(False)

        plt.tight_layout()
        return fig
    
    def plot_future_predictions(self,dates, prices, label="Predicted Price"):
        plt.figure(figsize=(14,2.5))
        fig = plt.gcf()
        fig.patch.set_facecolor('#14151b')  
        ax = plt.gca()
        ax.set_facecolor('#14151b')  

        plt.plot(dates, prices, color='cyan', linewidth=2, label=label)

        plt.title("Future Price Predictions", fontsize=14, color='white', fontname="Arial", weight='bold')
        plt.xticks(rotation=45, color='white', fontsize=10, fontname="Arial") 
        plt.yticks(color='white', fontsize=10, fontname="Arial")

        plt.grid(True, linestyle='--', color='white')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        plt.tight_layout()
        return fig