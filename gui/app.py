import tkinter as tk
from tkinter import ttk, messagebox,PhotoImage
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from datetime import datetime,date

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.fetcher import StockFetcher
from core.predictor import PricePredictor
from core.graph import GraphPlotter
from database import db_connection


class StockApp:
    def __init__(self,root,user_id,user_name):
        self.root=root
        self.userid=user_id
        self.username=user_name
        self.icon=PhotoImage(file='D:\\StockPredictor\\assets\\icons\\logo_black.png')
        self.root.title("Stock Prices Predictor")
        self.root.geometry("1920x1080")
        self.root.iconphoto(True,self.icon)
        self.root.state('zoomed')
    
        self.top_frame=tk.Frame(self.root,bg='#191c24',width=1920,height=100)
        self.top_frame.place(x=0,y=0)
        
        self.icon=PhotoImage(file='D:\\StockPredictor\\assets\\icons\\logo_white.png')
        self.top_label=tk.Label(self.top_frame,text="    Stocks Prices Predictor",font=('Arial',18,'bold'),bg='#191c24',fg='red',image=self.icon,compound='left')
        self.top_label.place(x=20,y=10)
        self.top_label.image = self.icon

        self.left__frame=tk.Frame(self.root,bg='#191c24',width=250,height=980)
        self.left__frame.place(x=0,y=100)

        self.user_icon=PhotoImage(file="D:\\StockPredictor\\assets\\icons\\User_icon.png").subsample(2,2)
        self.title_label=tk.Label(self.left__frame,text=f"  Welcome\n {self.username}",font=("Arial",12,'bold'),fg='white',bg='#191c24',compound='left',justify='center',image=self.user_icon)
        self.title_label.place(x=20,y=20)
        self.title_label.image = self.user_icon

        # Home Button
        home_icon=PhotoImage(file='D:\\StockPredictor\\assets\\icons\\home_icon.png').subsample(15,15)
        search_icon=PhotoImage(file='D:\\StockPredictor\\assets\\icons\\search_icon.png').subsample(15,15)
        info_icon=PhotoImage(file='D:\\StockPredictor\\assets\\icons\\info_icon.png').subsample(15,15)

        buttons=[('Home',self.home,home_icon),('Predict',self.predict,search_icon),('Ticker Info',self.info,info_icon)]
        btn_space=0
        for button in buttons:
            button=tk.Button(self.left__frame,text=button[0] ,font=("Arial",12,'bold'), width=200, bg= 'black' , fg= 'red' , activebackground='black' , activeforeground='red',image=button[2],relief='flat',compound='left',command=button[1])
            button.place(x=0,y=120+btn_space,height=50)
            btn_space+=100
            button.image=home_icon,search_icon,info_icon


        self.home()
    
    def init_right_frame(self):
        self.right_frame = tk.Frame(self.root, bg='black', width=1670,height=980)
        self.right_frame.place(x=250, y=100)
        self.right_frame.grid_propagate(False)

    def home(self):
        self.init_right_frame()
        self.upper_frame=tk.Frame(self.right_frame,bg='#191c24',height=475,width=1650)
        self.upper_frame.place(x=10,y=10)
        tk.Label(self.upper_frame,text="Active Stocks",font=("Arial",14,'bold'),fg='white',bg='#191c24').place(x=10,y=10)

        #Selection Dropdown
        self.coin_var=tk.StringVar(value='Select Coin')
        
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Custom.TCombobox",
        fieldbackground="black",     
        background="black",          
        foreground="red",            
        arrowcolor="red",
        )

        style.map("Custom.TCombobox",
        fieldbackground=[('readonly', 'black')],
        background=[('readonly', 'black')],
        foreground=[('readonly', 'red')],
        selectbackground=[('readonly', 'black')],  
        selectforeground=[('readonly', 'red')]
        )
        
        self.coin_dropdown=ttk.Combobox(self.upper_frame,textvariable=self.coin_var,font=("Arial",14),state='readonly',style="Custom.TCombobox")
        self.coin_dropdown['values'] =  [
        "BTC-USD", "ETH-USD", "USDT-USD", "BNB-USD", "SOL-USD", "XRP-USD", "USDC-USD", "DOGE-USD", "ADA-USD", "AVAX-USD",
        "TON-USD", "SHIB-USD", "WTRX-USD", "DOT-USD", "WBTC-USD", "TRX-USD", "LINK-USD", "BCH-USD", "NEAR-USD", "LTC-USD"
        ]
        
        self.coin_dropdown.place(x=1350,y=10,height=30)
        self.coin_dropdown.bind("<<ComboboxSelected>>",self.update_graph)

        #Graph Frame
        self.graph_frame=tk.Frame(self.upper_frame,bg='#191c24',height=400,width=1610)
        self.graph_frame.place(x=20,y=60)
        #Graph Frame Label
        self.no_coin_label = tk.Label(self.graph_frame, text="No Coin Selected", font=("Arial", 24),
                              fg='white', bg='#191c24')
        self.no_coin_label.place(relx=0.5, rely=0.5, anchor='center')

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TProgressbar",
                        orient="horizontal",
                        mode="indeterminate",
                        background='green',  # Green color for the progress bar
                        )
       
       #Lower Frame
        self.lower_frame=tk.Frame(self.right_frame,bg='#191c24',height=475,width=1650)
        self.lower_frame.place(x=10,y=495)
        tk.Label(self.lower_frame,text="Recent Stocks",font=("Arial",12,'bold'),fg='white',bg='#191c24').place(x=10,y=10)

        self.recent_stock_frame=tk.Frame(self.lower_frame,bg='#191c24',height=345,width=1610)
        self.recent_stock_frame.place(x=20,y=45)

        # Treeview Style Configuration for dark theme
        style.configure("Treeview",
                background="#161b22",
                foreground="#687194",
                rowheight=25,
                fieldbackground="#161b22",
                font=("Segoe UI", 12),
                bordercolor='white',
                borderwidth=2)
        style.map("Treeview", background=[("selected", "red")])

        style.configure("Treeview.Heading",
                background="#21262d",
                foreground='white',
                font=("Segoe UI", 12, "bold"))
        style.map("Treeview.Heading", background=[], foreground=[], relief=[])

        columns = ("Ticker", "Price Date","View Date","Open Price", "High Price", "Low Price", "Close Price", "Volume")
        tree = ttk.Treeview(self.recent_stock_frame, columns=columns, show="headings",height=12)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")
        
        def handle_resize(event):
            if tree.identify_region(event.x, event.y) == "separator":
                return "break"
        tree.bind("<Button-1>", handle_resize)

        # Recent_stocks
        recent_stocks=db_connection.get_user_recent_stocks(self.userid)
        if recent_stocks != []:
            for stock in recent_stocks:
                ticker,price_date, open_price, close_price, high_price, low_price, volume, view_date = stock
                if isinstance(price_date, (datetime, date)):
                    price_date = price_date.strftime("%d-%m-%Y")
                if isinstance(view_date, (datetime, date)):
                    view_date = view_date.strftime("%d-%m-%Y")
                tree.insert("", "end", values=(ticker,price_date,view_date,open_price,high_price,low_price,close_price,volume))
        else:
            tk.Label(self.recent_stock_frame,text="No Recent Stocks",font=("Times New Roman",24,'bold'),foreground='white',background='#191c24').place(x=670,y=170)

        tree.place(x=0,y=0)

    def show_loading(self):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        self.progress = ttk.Progressbar(self.graph_frame, style="TProgressbar",length=800)
        self.progress.place(relx=0.5, rely=0.5, anchor='center',height=30)
        self.progress.start()

    def hide_loading(self):
        self.progress.stop()
        self.progress.destroy()


    def update_graph(self,event):
        self.no_coin_label.destroy()
        self.show_loading()
        threading.Thread(target=self.fetch_and_plot_graph, daemon=True).start()
        
    def fetch_and_plot_graph(self):
        try:
            selected_coin = self.coin_var.get()
            fetcher = StockFetcher(selected_coin)
            data = fetcher.fetch_data()
            if data.empty:
                messagebox.showerror("Error", " No Data for Provided Coin")
            else:
                closing_price = fetcher.get_close_prices()

                stock=data.tail(1)

                Price_Date=stock.index[0]
                open_price = stock.iloc[-1]['Open'].values[0]
                close_price = stock.iloc[-1]['Close'].values[0]
                high_price = stock.iloc[-1]['High'].values[0]
                low_price = stock.iloc[-1]['Low'].values[0]
                volume = stock.iloc[-1]['Volume'].values[0]

                recent=db_connection.recent_stock(self.userid,selected_coin,Price_Date,open_price,close_price,high_price,low_price,volume)
                
                graph = GraphPlotter()
                graph.set_close_prices(closing_price)
                self.graph_frame.after(0, self.display_graph, graph, selected_coin)
        except Exception as e:
            print(f"Error while updating graph: {e}")
            self.graph_frame.after(0, lambda e=e: messagebox.showerror("Error",str(e) ))
        finally:
            self.graph_frame.after(0, self.hide_loading)

    def display_graph(self,graph,selected_coin):
        fig=graph.close_prices(selected_coin)
        self.home()
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()   
        toolbar = NavigationToolbar2Tk(canvas, self.graph_frame)
        toolbar.update()
        toolbar.config(bg='#191c24')

        for child in toolbar.winfo_children():
            child.config(bg='#191c24', bd=1)
            if isinstance(child, tk.Button):
                child.config(fg='white', activebackground='black', activeforeground='white', relief='flat')
        toolbar.place(x=0,y=360)
        canvas.get_tk_widget().place(x=0,y=0)
        
    
    def predict(self):
        self.init_right_frame()
        self.center_frame=tk.Frame(self.right_frame,bg='#191c24',height=500,width=500)
        self.center_frame.place(x=585,y=240)
        title_frame=tk.Frame(self.center_frame,bg='#191c24',height=100,width=500)
        title_frame.place(x=0,y=0)
        user_edit=PhotoImage(file="D:\\StockPredictor\\assets\\icons\\user_edit.png").subsample(9,9)
        title_label=tk.Label(title_frame,text="   Stock Market Predictor",font=("Arial",18,'bold'),fg='Red',bg="#191c24",image=user_edit,compound="left")
        title_label.place(x=40,y=40)
        title_label.image=user_edit

        tk.Label(self.center_frame,text="Ticker Name",font=("Arial",14,'bold'),fg='white',bg="#191c24").place(x=40,y=120)

        self.coin_var=tk.StringVar(value='Select Coin')
        
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Custom.TCombobox",
        fieldbackground="black",     
        background="black",          
        foreground="red",            
        arrowcolor="red",
        )

        style.map("Custom.TCombobox",
        fieldbackground=[('readonly', 'black')],
        background=[('readonly', 'black')],
        foreground=[('readonly', 'red')],
        selectbackground=[('readonly', 'black')],  
        selectforeground=[('readonly', 'red')]
        )
        
        self.coin_dropdown=ttk.Combobox(self.center_frame,textvariable=self.coin_var,font=("Arial",14),state='readonly',style="Custom.TCombobox",width=33)
        self.coin_dropdown['values'] =  [
        "BTC-USD", "ETH-USD", "USDT-USD", "BNB-USD", "SOL-USD", "XRP-USD", "USDC-USD", "DOGE-USD", "ADA-USD", "AVAX-USD",
        "TON-USD", "SHIB-USD", "WTRX-USD", "DOT-USD", "WBTC-USD", "TRX-USD", "LINK-USD", "BCH-USD", "NEAR-USD", "LTC-USD"
        ]
        
        self.coin_dropdown.place(x=40,y=170,height=50)
        

        tk.Label(self.center_frame,text="No. of Days (2-30)",font=("Arial",14,'bold'),fg='white',bg="#191c24").place(x=40,y=250)

        def only_numbers(char):
            return char.isdigit()
        
        vcmd = (self.root.register(only_numbers), '%S')

        self.days_entry = tk.Entry(self.center_frame, validate='key', validatecommand=vcmd,fg='Red',bg='black',width=34,font=("Arial",14),insertbackground='Red',insertwidth=5)
        self.days_entry.place(x=40,y=300,height=50)

        predict_button=tk.Button(self.center_frame,text='Predict',font=("Arial",14),fg='white',bg='Red',activeforeground="Red",activebackground="white",width=31,command=self.prediction)
        predict_button.place(x=40,y=400)

    def prediction(self):
        coin=self.coin_var.get()
        days=self.days_entry.get()
        if coin=='Select Coin' or not days:
           return messagebox.showerror("Error","Enter all fields!")
        if int(days) < 2 or int(days) > 30:
           return messagebox.showerror("Error","Days should be between 2 and 30!")
        days=int(days)
        fetcher = StockFetcher(coin)
        data = fetcher.fetch_data()
        if data.empty:
            return messagebox.showerror("Error",f"No Data Found for symbol {coin}")
        closing_prices = fetcher.get_close_prices()
        dates=data.index
        predictor = PricePredictor(closing_prices.values,dates)
        predictor.prepare_data()
        predictor.train_model()
        future_dates,future_prices=predictor.predict_next(days)
        graph=GraphPlotter()

        self.init_right_frame()

        self.upper_frame=tk.Frame(self.right_frame,bg='#191c24',height=475,width=1650)
        self.upper_frame.place(x=10,y=10)
        tk.Label(self.upper_frame,text=f"Recent Stock Prices of {coin}",font=("Arial",12,'bold'),fg='white',bg='#191c24').place(x=10,y=10)
        self.graph_frame=tk.Frame(self.upper_frame,bg='#191c24',height=400,width=1610)
        self.graph_frame.place(x=20,y=60)
        fig=graph.plot_last_year_comparison(predictor,coin)
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()   
        toolbar = NavigationToolbar2Tk(canvas, self.graph_frame)
        toolbar.update()
        toolbar.config(bg='#191c24')

        for child in toolbar.winfo_children():
            child.config(bg='#191c24', bd=1)
            if isinstance(child, tk.Button):
                child.config(fg='white', activebackground='black', activeforeground='white', relief='flat')
        toolbar.place(x=0,y=360)
        canvas.get_tk_widget().place(x=0,y=0)

        #Lower Frame
        self.lower_frame=tk.Frame(self.right_frame,bg='#191c24',height=475,width=1650)
        self.lower_frame.place(x=10,y=495)
        tk.Label(self.lower_frame,text=f"Predicted Stock Prices of {coin} for next {days} days",font=("Arial",12,'bold'),fg='white',bg='#191c24').place(x=10,y=10)
        self.predicted_frame=tk.Frame(self.lower_frame,bg='#191c24',height=345,width=1610)
        self.predicted_frame.place(x=20,y=45)

        fig1=graph.plot_future_predictions(future_dates, future_prices)
        
        canvas = FigureCanvasTkAgg(fig1, master=self.predicted_frame)
        canvas.draw()   
        toolbar = NavigationToolbar2Tk(canvas, self.predicted_frame)
        toolbar.update()
        toolbar.config(bg='#191c24')

        for child in toolbar.winfo_children():
            child.config(bg='#191c24', bd=1)
            if isinstance(child, tk.Button):
                child.config(fg='white', activebackground='black', activeforeground='white', relief='flat')
        toolbar.place(x=0,y=300)
        canvas.get_tk_widget().place(x=0,y=0)

    def info(self):
        self.init_right_frame()
        self.main_frame=tk.Frame(self.right_frame,bg='#191c24',height=970,width=1630)
        self.main_frame.place(x=20,y=20)
        tk.Label(self.main_frame,text=f"All Tickers",font=("Arial",12,'bold'),fg='white',bg='#191c24').place(x=10,y=10)
        self.stock_frame=tk.Frame(self.main_frame,bg='#191c24',height=920,width=1590)
        self.stock_frame.place(x=20,y=50)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                background="#161b22",
                foreground="#687194",
                rowheight=25,
                fieldbackground="#161b22",
                font=("Segoe UI", 12),
                bordercolor='white',
                borderwidth=2)
        style.map("Treeview", background=[("selected", "red")])

        style.configure("Treeview.Heading",
                background="#21262d",
                foreground='white',
                font=("Segoe UI", 12, "bold"))
        style.map("Treeview.Heading", background=[], foreground=[], relief=[])

        columns = ("symbol", "name","description","launch_date")
        tree = ttk.Treeview(self.stock_frame, columns=columns, show="headings",height=40)

        tree.heading("symbol", text="Symbol")
        tree.heading("name", text="Name")
        tree.heading("description", text="Description")
        tree.heading("launch_date", text="Launch Date")
        
        tree.column("symbol", width=150, anchor="center")   
        tree.column("name", width=200, anchor="center")             
        tree.column("description", width=1000, anchor="w")
        tree.column("launch_date",width=230,anchor="center")
        
        def handle_resize(event):
            if tree.identify_region(event.x, event.y) == "separator":
                return "break"
        tree.bind("<Button-1>", handle_resize)

        stocks=db_connection.get_stocks()
        for stock in stocks:
            _,symbol,name,description,launch_date = stock
            tree.insert("", "end", values=(symbol,name,description,launch_date))

        tree.place(x=0,y=0)
