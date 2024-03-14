from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image
from geopy.geocoders import Nominatim
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz

# def on_entry(event):
#     """Function to handle entry focus events."""
#     if event.type == '9' and textfield.get() == "Search":  # FocusIn event
#         textfield.delete(0, tk.END)
#         textfield.config(fg="black")  # Set text color to black when focused
#     elif event.type == '10' and not textfield.get():  # FocusOut event
#         textfield.insert(0, "Search")
#         textfield.config(fg="#AAAAAA")


def on_entry_focus_in(event):
    """Function to handle entry focus in event."""
    if textfield.get() == "Search":
        textfield.delete(0, tk.END)
        textfield.config(fg="black")  # Set text color to black when focused

def on_entry_focus_out(event):
    """Function to handle entry focus out event."""
    if not textfield.get():
        textfield.insert(0, "Search")
        textfield.config(fg="#AAAAAA")

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="my_weather_api")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api_key = "0b863b0ddda8ec337d93e20846986e50" 
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data["weather"][0]['main']
        description = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","Feels","Like",temp,"°"))

        
        w.config(text= wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        t.config(text="....")
        c.config(text="....")

        
        w.config(text= "....")
        h.config(text="....")
        d.config(text="....")
        p.config(text="....")
        messagebox.showwarning("Weather APP","No Match Found")



def on_click(event):
    getWeather()


root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(True,True)

# SearchBox
search = PhotoImage(file='S1.png')
myimage = Label(image=search)
myimage.place(x=10,y=10)

textfield = tk.Entry(root,justify="center",width=17,font=("poppings",25,"bold"),highlightthickness=0,bd=0)
# textfield.config(highlightthickness=0.0,highlightbackground=root.cget('bg'))
textfield.place(x=50,y=40)
textfield.insert(0,"Search")
textfield.config(fg="#AAAAAA")
textfield.bind("<FocusIn>",on_entry_focus_in)
textfield.bind("<FocusOut>",on_entry_focus_out)
#trying to use the search button
pi = PhotoImage(file='si.png',palette='#FFFFFF')
search_label = Label(root,image=pi,highlightthickness=0,bd=0,cursor="hand2")
search_label.place(x= 495, y=35,width=50, height=50)
search_label.bind("<Button-1>", on_click)

#logo
# logo_img = Image.open('logo.png')
# Png = logo_img.convert("RGBA")
# Png.save("OPT.png")
l = PhotoImage(file="Copy of logo.png")
logo = Label(root,image=l)
logo.place(x = 160, y = 120 )

#box
dowm_img = PhotoImage(file="Copy of box.png")
down_label = Label(image=dowm_img)
down_label.pack(padx=5,pady=5,side='bottom')

#time wala box
name = Label(root,font=("arial",15,"bold"))
name.place(x=20,y=130)
clock = Label(root,font=("Helvetica",20))
clock.place(x=20,y=165)


#label
label1 = Label(root,text="Wind",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=125,y=406)

label1 = Label(root,text="Humidity",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=260,y=406)

label1 = Label(root,text="Description",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=450,y=406)

label1 = Label(root,text="Pressure",font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=650,y=406)

t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=480,y=150)
c = Label(font=("arial",15,"bold"))
c.place(x=480,y=250)


w = Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=130,y=430)
h = Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=290,y=430)
d = Label(text="  ....  ",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p = Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=680,y=430)




root.mainloop()