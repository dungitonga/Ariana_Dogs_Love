from flask import Flask, render_template, url_for
from dotenv import load_dotenv
import requests, os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    
    url = "https://api.thedogapi.com/v1/breeds"
    load_dotenv()
    headers = {"x-api-key" : os.getenv("API_KEY")}

    response = requests.get(url, headers=headers)

    posts = response.json()

    return render_template("home.html", posts=posts)

if __name__ == "__main__":
    app.run(port=os.getenv("PORT"))