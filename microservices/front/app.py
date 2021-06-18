from flask import Flask, jsonify
from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route("/") 
def home():
	return render_template("index.html")

@app.route("/search", methods=["POST", "GET"]) 
def search():
	if request.method == "POST":
		url = 'http://172.17.0.2:5000/query-pokemon?pokemon_number='+str(request.form["pokemon"])
		r = requests.get(url)
		data = r.json()
		name = data["name"][0]
		img = data["image"][0]
		enemies = data["image"][1:3]
		return render_template("search.html", name=name, img=img, enemies=enemies, zip=zip)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8000)


