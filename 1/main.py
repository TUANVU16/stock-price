from tkinter import*
import requests
from PIL import Image, ImageTk
import json


window = Tk()
window.title("hello world")
window.config(padx=20, pady=20)


canvas = Canvas(height=200, width=320, bg="white")
img = ImageTk.PhotoImage(Image.open("1.jpg"))
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

share_label = Label(text="Share",  fg="black", font=("Ariel", 20))
share_label.grid(row=1, column=0)
share_entry = Entry(width=35)
share_entry.grid(row=1, column=1)

price_label = Label(text="yesterday close price",  fg="black", font=("Ariel", 20))
price_label.grid(row=2, column=0)
price_entry = Entry(width=35)
price_entry.grid(row=2, column=1)


def search():
    shareName = share_entry.get()
    
    price_entry.delete(0, END)


    STOCK_API ="IHUGPIH9E2KWJCMC"
    STOCK_ENDPOINT ="https://www.alphavantage.co/query"
    STOCK_NAME ="TSLA"

    stock_params ={
        "function":"TIME_SERIES_DAILY",
        "symbol": shareName,
        "apikey":STOCK_API,
    }

    response =requests.get(STOCK_ENDPOINT, params= stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_close =data_list[0]["4. close"]
    print(yesterday_close)
    price_entry.insert(0, yesterday_close)

    
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)









window.mainloop()