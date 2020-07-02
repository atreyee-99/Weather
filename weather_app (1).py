from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os

import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

api_key = '8b7a74a615b2fefbb4050d07efedcdcc'


def get_weather(city):
    result = requests.get(url.format(city, api_key)) #accepts information(city name and api key) and requests connection with server
    if result:
        json = result.json() #converting result to json which makes extracting information easier
        #creating tupples of the information to bed displayed
        city = json['name']
        country = json['sys']['country']
        temp_max = json['main']['temp_max']
        temp_min = json['main']['temp_min']
        temp_h = (temp_max - 273.15) #converting temperature in celcius
        temp_l = (temp_min - 273.15)
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main'] #it is a list and we want the first element. Thus the 0th index.
        humid = json['main']['humidity']
        desc = json['weather'][0]['description']
        final = (city, country, temp_h, temp_l, icon, weather, humid, desc) #creating tupples from above information
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = 'City: {}'.format(weather[0])
        location_lbl1['text'] = 'Country: {}'.format(weather[1])
        temp_lbl['text'] = 'Temperature:   Max: {:.2f}°C;  Min: {:.2f}°C'.format(weather[2], weather[3])
        weather_lbl['text'] = 'Weather: {}'.format(weather[5])
        humid_lbl['text'] = 'Humidity: {}%'.format(weather[6])
        desc_lbl['text'] = 'Description: {}'.format(weather[7])
        i = 'weather_icons/' + weather[4] + '.png'
        img = Image.open(i)
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(app, image=img)
        panel.image = img
        panel.pack()
    else:
        messagebox.showerror('Error.', 'Cannot find city {}'.format(city)) #display error message if invalid input is given


app = Tk()
app.title("Weather App")
app.geometry('700x350')

#canvas = Canvas(app,height=350, width=700)
#canvas.pack()


background_image = PhotoImage(file=r"C:\Users\Titli\Desktop\landscape.png") 
background_label = Label(image=background_image) #provides background image
background_label.place(relwidth=1, relheight=1)


city_text = StringVar() #with this the user can input the city they are trying to search for
city_entry = Entry(app, textvariable=city_text) #entry
city_entry.pack() #placing the entry on the screen

search_btn = Button(app, text='Search Weather', width=12, command=search) #accepting parameters for search button
search_btn.pack() #placing the search button on the app window

location_lbl = Label(app, text='', font=('bold', 20)) #provides the city name and corresponding country name from backend
location_lbl.pack() #places the location details on screen

location_lbl1 = Label(app, text='', font=('bold', 20))
location_lbl1.pack()

temp_lbl = Label(app, text='') #provides the temperature from the backend
temp_lbl.pack() #places the temperature on screen

humid_lbl = Label(app, text='') #provides the humidity from the backend
humid_lbl.pack() #places the humidity on screen

weather_lbl = Label(app, text='') #provides the weather from the backend
weather_lbl.pack() #places the weather on screen

desc_lbl = Label(app, text='') #provides the weather description from the backend
desc_lbl.pack()  #places the weather des on screen



app.mainloop() #runs the application
