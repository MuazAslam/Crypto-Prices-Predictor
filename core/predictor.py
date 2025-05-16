import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class PricePredictor:
    def __init__(self, close_prices: np.ndarray, dates: pd.Series = None):
        self.df = pd.DataFrame(close_prices, columns=["Close"])
        if dates is not None:
            self.df["Date"] = pd.to_datetime(dates)
        else:
            self.df["Date"] = pd.to_datetime("today") + pd.to_timedelta(np.arange(len(self.df)), 'D')
        self.__model = LinearRegression()
        self.__trained = False

    def prepare_data(self):
        # Calculate Moving Averages
        self.df["Prev_Close"] = self.df["Close"].shift(1)
        self.df["5_MA"] = self.df["Close"].rolling(window=5).mean()
        self.df["10_MA"] = self.df["Close"].rolling(window=10).mean()

        # Drop NaN values created by shifting or rolling
        self.df.dropna(inplace=True)

        # Prepare feature (X) and target (y)
        self.__X = self.df[["Prev_Close", "5_MA", "10_MA"]].values
        self.__y = self.df["Close"].values

        print("[INFO] Data prepared using moving averages.")

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.__X, self.__y, test_size=0.2, random_state=42)
        self.__model.fit(X_train, y_train)
        self.__trained = True

        y_pred = self.__model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"[INFO] Model trained.")
        print(f"MSE: {mse:.4f}")
        print(f"MAE: {mae:.4f}")
        print(f"R²: {r2:.4f}")

    def predict_next(self, days_ahead):
        if not self.__trained:
            raise Exception("Model not trained yet. Call train_model() first.")

        # Ensure the index is datetime
        if not isinstance(self.df.index, pd.DatetimeIndex):
            self.df.index = pd.to_datetime(self.df.index)

        last_row = self.df.iloc[-1]
        input_features = np.array([[last_row["Close"], last_row["5_MA"], last_row["10_MA"]]])

        future_prices = []
        future_dates = []
        today = pd.Timestamp.today().normalize()  


        for i in range(1, days_ahead + 1):
            prediction = self.__model.predict(input_features)
            future_prices.append(prediction[0])
            future_dates.append(today + pd.Timedelta(days=i))

            # Update moving averages
            next_5_MA = np.mean([last_row["Close"], prediction[0]])
            next_10_MA = np.mean([last_row["Close"], prediction[0]])
            input_features = np.array([[prediction[0], next_5_MA, next_10_MA]])

            last_row = last_row.copy()
            last_row["Close"] = prediction[0]
            last_row["5_MA"] = next_5_MA
            last_row["10_MA"] = next_10_MA

        return future_dates, future_prices

    def get_model(self):
        return self.__model
