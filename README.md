# Weather

from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']

def get_weather(city):
	result=requests.get(url.format(city, api_key))
	if result:
		json=result.json()
		city=json['name']
		country=json['sys']['country']
		temp_kel=json['main']['temp']
		temp_cel=(temp_kel-273.15)
		temp_fah=(temp_kel-273.15)*9/5+32
		icon=json['weather'][0]['icon']
		weather=json['weather'][0]['main']
		final=(city, country, temp_cel, temp_fah, icon, weather)
		return final
	else:
		return None




def search():
	city=city_text.get()
	weather=get_weather(city)
	if weather:
		location_lbl['text']='{}, {}'.format(weather[0], weather[1])
		image['bitmap']='urllib3/{}.png'.format(weather[4])
		temp_lbl['text']='{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
		weather_lbl['text']=weather[5]
	else:
		messagebox.showerror('Error.','Cannot find city {}'.format(city))



app=Tk()
app.title("Weather App")
HEIGHT = 300
WIDTH = 600

canvas = Canvas(app,height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file=r"C:\Users\Titli\Desktop\landscape.png")
background_label = Label(image=background_image)
background_label.place(relwidth=1, relheight=1)

city_text=StringVar()
city_entry=Entry(app, textvariable=city_text)
city_entry.pack()
search_btn=Button(app, text='Search Weather',width=15,command=search).pack()

location_lbl=Label(app, text='Location').pack()

temp_lbl=Label(app, text='Temperature').pack()

weather_lbl=Label(app, text='Weather').pack()




app.mainloop()
