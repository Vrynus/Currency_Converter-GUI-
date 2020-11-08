import requests
import json
import tkinter
from tkinter import Entry

#request exchange rate info and convert strings into floats
req = requests.get('https://api.exchangeratesapi.io/latest')
rate_info = json.loads(req.text)
rates = rate_info['rates']
rate_try, rate_usd  = float(rates['TRY']), float(rates['USD'])

#creating gui 
root = tkinter.Tk()
root.title('Convert_v1')
canvas = tkinter.Canvas(root, height = 450, width = 650 ,bg = "grey")
canvas.pack()

#functions to convert currencies
def eur_try():
    info_label['text'] = f'Value: {round(float(entry1.get()) * rate_try, 3)} TRY'

def eur_usd():
    info_label['text'] = f'Value: {round(float(entry1.get()) * rate_usd, 3)} USD'
    
def usd_try():
    info_label['text'] = f'Value: {round(float(entry1.get()) * (rate_try/rate_usd), 3)} TRY'

def try_usd():
    info_label['text'] = f'Value: {round(float(entry1.get()) * (rate_usd/rate_try), 3)} USD'
    
def usd_eur():
    info_label['text'] = f'Value: {round(float(entry1.get()) * (1/rate_usd), 3)} EUR'
    
def try_eur():
    info_label['text'] = f'Value: {round(float(entry1.get()) * (1/rate_try), 3)} EUR'

#we will put buttons and label on these
frame_left = tkinter.Frame(canvas, bg = '#00c7c8')
frame_left.place(relheight = 1, relwidth = 0.5)

frame_right = tkinter.Frame(canvas, bg = '#00c7c8')
frame_right.place(relheight = 1, relwidth = 0.5, relx = 0.5)

#buttons to trigger functions
button1 = tkinter.Button(frame_left, text = 'EUR - TRY', font = ('Courier', 10), command = eur_try)
button1.place(relx = 0.2, rely = 0.2)

button2 = tkinter.Button(frame_left, text = 'EUR - USD', font = ('Courier', 10), command = eur_usd)
button2.place(relx = 0.2, rely = 0.3)

button3 = tkinter.Button(frame_left, text = 'USD - TRY', font = ('Courier', 10), command = usd_try)
button3.place(relx = 0.2, rely = 0.4)

button4 = tkinter.Button(frame_left, text = 'TRY - USD', font = ('Courier', 10), command = try_usd)
button4.place(relx = 0.2, rely = 0.5)

button5 = tkinter.Button(frame_left, text = 'USD - EUR', font = ('Courier', 10), command = usd_eur)
button5.place(relx = 0.2, rely = 0.6)

button6 = tkinter.Button(frame_left, text = 'TRY - EUR', font = ('Courier', 10), command = try_eur)
button6.place(relx = 0.2, rely = 0.7)

value1 = tkinter.DoubleVar()
entry1 = tkinter.Entry(frame_right, font = ('Courier' , 18), textvariable = value1)
entry1.place(relx = 0.2, rely = 0.1, relheight = 0.1, relwidth = 0.6)

#to see the values which calculated by functions
info_label = tkinter.Label(frame_right, text = 'Welcome.\n Type a value to convert.', bg = 'white')
info_label.place(relx = 0.2, rely = 0.3, relheight = 0.5, relwidth = 0.6)

root.mainloop()
