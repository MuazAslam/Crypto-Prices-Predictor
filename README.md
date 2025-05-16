# Crypto Prices Predictor

A sophisticated desktop application that leverages machine learning to analyze cryptocurrency market data, visualize historical trends, and predict future price movements with remarkable accuracy.

## Table of Contents

- [📋 Overview](#-overview)
  - [Key Objectives](#key-objectives)
- [✨ Features](#-features)
  - [📊 Data Analysis & Visualization](#-data-analysis--visualization)
  - [🧠 Prediction Capabilities](#-prediction-capabilities)
  - [👤 User Management](#-user-management)
  - [💼 Cryptocurrency Information](#-cryptocurrency-information)
- [🖼️ Screenshots](#-screenshots)
- [🏗️ Architecture](#-architecture)
  - [Project Structure](#project-structure)
- [🛠️ Technology Stack](#-technology-stack)
  - [Dependencies](#dependencies)
- [⚡ Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Setup Steps](#setup-steps)
- [🚀 Usage](#-usage)
  - [Getting Started](#getting-started)
  - [Data Visualization Workflow](#data-visualization-workflow)
  - [Price Prediction Workflow](#price-prediction-workflow)
- [🧠 Machine Learning Approach](#-machine-learning-approach)
  - [Model Architecture](#model-architecture)
  - [Feature Engineering](#feature-engineering)
  - [Prediction Process](#prediction-process)
- [🗄️ Database Schema](#-database-schema)
  - [Core Entities](#core-entities)
  - [Database Diagram](#database-diagram)
- [About](#about)

## 📋 Overview

The Crypto Prices Predictor is a comprehensive data science application that processes historical cryptocurrency data to generate accurate price forecasts, helping investors make data-driven decisions in the volatile crypto market. The application combines advanced machine learning techniques with intuitive visualization tools to provide valuable insights into cryptocurrency price movements.

### Key Objectives

- Analyze real-time cryptocurrency market data from reliable sources
- Visualize historical price trends with interactive, customizable charts
- Predict future price movements using machine learning algorithms
- Provide a user-friendly interface for both technical and non-technical users
- Maintain user profiles and cryptocurrency viewing history
- Deliver detailed information about various cryptocurrencies

## ✨ Features

### 📊 Data Analysis & Visualization

- **📈 Historical Data Analysis**
  - Real-time data retrieval from Yahoo Finance API
  - Interactive time-series visualization with zoom/pan capabilities
  - Customizable date ranges and timeframes
  - Support for 20+ popular cryptocurrencies
  - Multi-threaded data processing for optimal performance

- **📉 Trend Analysis**
  - Moving averages visualization (5-day and 10-day)
  - Price comparison charts
  - Historical performance metrics
  - Actual vs. predicted price comparison

- **👁️ Viewing History**
  - Track recently viewed cryptocurrencies
  - Quick access to frequently analyzed assets
  - Detailed price information for each viewing instance
  - Timestamp tracking for all user interactions

### 🧠 Prediction Capabilities

- **🔮 Price Forecasting**
  - Machine learning-based price prediction
  - Customizable prediction timeframes (2-30 days)
  - Linear Regression model with moving averages
  - Model performance metrics (MSE, MAE, R²)
  - Future price visualization with trend analysis

- **📋 Prediction Accuracy**
  - Model validation against historical data
  - Performance metrics display
  - Confidence indicators
  - Comparison between predicted and actual values

### 👤 User Management

- **🔐 Authentication System**
  - Secure user registration and login
  - Password protection and validation
  - User profile management
  - Personalized dashboards for each user

- **💾 User Preferences**
  - Save favorite cryptocurrencies
  - Customize default viewing options
  - Track recent activity and searches
  - Profile management capabilities

### 💼 Cryptocurrency Information

- **🪙 Crypto Database**
  - Comprehensive information for 20+ cryptocurrencies
  - Detailed descriptions and launch dates
  - Symbol and name references
  - Historical market data

- **🔍 Information Lookup**
  - Quick search functionality
  - Detailed token information
  - Historical context for each cryptocurrency
  - Reference data for informed decision-making

## 🖼️ Screenshots

#### 🔐 Login & Registration

![bandicam 2025-05-16 09-40-13-595](https://github.com/user-attachments/assets/564cac75-3227-4837-8a43-c27fb17baba7)

![bandicam 2025-05-16 09-40-38-664](https://github.com/user-attachments/assets/929b7131-1b8d-460c-875e-e2aecb3a473c)

#### 📊 Main Dashboard

![bandicam 2025-05-16 09-42-58-313](https://github.com/user-attachments/assets/0803b013-9bb4-451a-8605-daa60d1e356d)

#### 🔮 Prediction Interface

![bandicam 2025-05-16 09-43-57-622](https://github.com/user-attachments/assets/2887e657-ceeb-4d99-a803-6b049b4a6dcf)


#### 🪙 Cryptocurrency Information

![bandicam 2025-05-16 09-44-08-422](https://github.com/user-attachments/assets/5472d7c4-5e89-4033-85a5-a870fe42c082)

## 🏗️ Architecture

The application follows a modular object-oriented architecture with clean separation of concerns:

### Project Structure

```
Crypto-Prices-Predictor/
├── core/                   # Core functionality modules
│   ├── fetcher.py          # Data retrieval from Yahoo Finance
│   ├── predictor.py        # ML model for price prediction
│   └── graph.py            # Visualization components
├── database/
│   └── db_connection.py    # Database interaction functions
|   |__StockPredictor.sql      # Database schema creation script
├── gui/
│   ├── app.py              # Main application UI
│   └── login.py            # Login and registration UI
├── assets/                 # Application icons and images
│   └── icons/
├── main.py                 # Application entry point
└── README.md              # Project documentation
```

## 🛠️ Technology Stack

- **Programming Language**: Python 3.8+
- **Data Processing**: NumPy, Pandas
- **Machine Learning**: Scikit-Learn (sklearn.linear_model.LinearRegression)
- **Data Visualization**: Matplotlib, FigureCanvasTkAgg, NavigationToolbar2Tk
- **User Interface**: Tkinter, ttk, Custom Dark Theme (#191c24)
- **Data Source**: Yahoo Finance API (yfinance)
- **Database**: Microsoft SQL Server
- **Database Connector**: pyodbc
- **Concurrency**: Python Threading Library

### Dependencies

```
numpy>=1.19.5
pandas>=1.3.0
scikit-learn>=0.24.2
matplotlib>=3.4.2
yfinance>=0.1.63
pyodbc>=4.0.30
```

## ⚡ Installation

### Prerequisites

- Python 3.8 or higher
- Microsoft SQL Server
- ODBC Driver 17 for SQL Server

### Setup Steps

1. **📥 Clone the Repository**
   ```bash
   git clone https://github.com/MuazAslam/Crypto-Prices-Predictor.git
   cd Crypto-Prices-Predictor
   ```

2. **📦 Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **🗄️ Database Setup**
   - Create a new database in SQL Server
   - Run the `StockPredictor.sql` script to create the necessary tables
   - Update the connection string in `database/db_connection.py`:
     ```python
     "SERVER=YOUR_SERVER_NAME;"
     "DATABASE=StockPredictor;"
     "Trusted_Connection=yes;"
     ```

4. **▶️ Run the Application**
   ```bash
   python main.py
   ```

## 🚀 Usage

### Getting Started

1. **🔐 Create an Account**
   - Launch the application
   - Register with your name, email, phone, and password
   - Login with your credentials

2. **🏠 Navigate the Dashboard**
   - View the main dashboard with active cryptocurrency data
   - Select a cryptocurrency from the dropdown menu
   - Explore historical price charts

### Data Visualization Workflow

1. **📊 Select Cryptocurrency**
   - Choose from 20+ available cryptocurrencies
   - View real-time closing price data
   - Analyze interactive price charts

2. **📈 Explore Historical Data**
   - Interact with time-series visualizations
   - Use toolbar options for zoom, pan, and save
   - View detailed price information

3. **📋 Review Recent Stocks**
   - Access your recently viewed cryptocurrencies
   - Track viewing history with timestamps
   - Compare historical data across different assets

### Price Prediction Workflow

1. **🔮 Access Prediction Tool**
   - Navigate to the Predict section
   - Select a cryptocurrency from the dropdown

2. **⚙️ Configure Prediction**
   - Set the number of days for prediction (2-30)
   - Generate predictions based on historical data

3. **📉 Analyze Results**
   - View comparison between historical and predicted prices
   - Examine future price predictions
   - Understand price trends and potential movements

## 🧠 Machine Learning Approach

### Model Architecture

The price prediction system utilizes a Linear Regression model from scikit-learn, optimized for time-series forecasting:

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Model initialization
model = LinearRegression()
```

### Feature Engineering

The system transforms raw price data into predictive features:

1. **Historical Close Prices**: Base data point for prediction
2. **Previous Day's Close**: Immediate price context
3. **5-Day Moving Average**: Short-term trend indicator
4. **10-Day Moving Average**: Medium-term trend indicator

```python
# Feature engineering example
df["Prev_Close"] = df["Close"].shift(1)
df["5_MA"] = df["Close"].rolling(window=5).mean()
df["10_MA"] = df["Close"].rolling(window=10).mean()
```

### Prediction Process

The prediction workflow follows these steps:

1. **Data Preparation**: Features are engineered from historical data
2. **Model Training**: 80% of data used for training, 20% for validation
3. **Model Evaluation**: Performance measured with MSE, MAE, and R²
4. **Future Prediction**: Recursive prediction for specified number of days
5. **Visualization**: Results displayed through interactive charts

## 🗄️ Database Schema

### Core Entities

The application uses a well-structured relational database with the following key tables:

- **👤 Users**: Stores user profiles and authentication details
- **🪙 Cryptocurrencies**: Contains information about available cryptocurrencies
- **📋 Recent_Stocks**: Tracks cryptocurrency price data points
- **👁️ User_Recent_Views**: Maintains user viewing history

### Database Diagram

The database follows a normalized structure with appropriate relationships:

![Blank diagram](https://github.com/user-attachments/assets/dd09283d-6fc2-468b-937d-74fd2399ffd1)

## About

Crypto Prices Predictor demonstrates the practical application of machine learning algorithms and data visualization techniques to solve real-world financial analysis problems. The application provides valuable insights for cryptocurrency investors, enabling more informed decision-making in this volatile market.

Special thanks to **Dr. Faiza Iqbal**, **Sir Sharjeel**, and **Muhammad Faizan Asim** for their guidance and support throughout the development process.

---

© 2025 Crypto Prices Predictor | Developed by Muaz Aslam
