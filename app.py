from flask import Flask, render_template, redirect, request, flash
import requests
import json

app = Flask(__name__)
app.secret_key = 'Me and donald duck'
api_key = "e67b1d47163e59ac104324e1bb4fbca4"

@app.route('/', methods= ["GET", "POST"])
def index():
    if request.method == "POST":
        try:  
            city = request.form["city"]
            country = request.form["country"]
            weather_url = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial")
            weather = weather_url.json()

            if weather['cod'] == '404':
                return render_template("index.html")
            temp = round((round(weather['main']['temp']) - 32) * 5/9)
            humidity = weather['main']['humidity']
            wind_speed = weather['wind']['speed']
            weather_main = weather['weather'][0]['main']
            weather_cast = weather['weather'][0]['description']
            countryx = weather['sys']['country']

            return render_template("weather.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, weather_main=weather_main, weather_cast=weather_cast, country=countryx)
        except KeyError:
            flash("Invalid input", "error")
    return render_template("index.html")

@app.route('/home', methods= ["GET", "POST"])
def home():
    return redirect("/")
