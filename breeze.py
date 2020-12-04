import requests
from flask import Flask, render_template, request


app = Flask(__name__)
app.config["SECRET KEY"] = 'aacdddfdsf'

city = " "


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        city = request.form.get('cityName')
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9f9d3fdc199327d2a35fb5285bf2bc9c"
        r = requests.get(url.format(city)).json()
        weather = {
            'city': city,
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]['description'],
            'icon': r["weather"][0]["icon"]
        }
        
        
    return render_template('index.html', city=city, weather=weather)
    

    if __name__ == "__main__":
       app.run(debug=True)