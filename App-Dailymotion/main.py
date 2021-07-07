from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/music')
def music():
    DatosUrl = requests.get("https://api.dailymotion.com/videos?channel=music&limit=10")
    DatosObtenidosJson = DatosUrl.json()
    return render_template('music.html', ListVideo = DatosObtenidosJson["list"])

@app.route('/sport')
def sport():
    datosSport = requests.get("https://api.dailymotion.com/videos?channel=sport&limit=10")
    sportJson = datosSport.json()
    return render_template("sport.html", listSport = sportJson["list"])

@app.route("/news")
def news():
    datosNews = requests.get("https://api.dailymotion.com/videos?channel=news&limit=10")
    datosNewsJson = datosNews.json()
    return render_template("news.html", listNews = datosNewsJson["list"])


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
