from flask import Flask
import requests

app = Flask(__name__)

form_html = """
    <h1>Random Emoji App</h1>
    <form action="/get-emoji" method="get">
        <button type="submit">Get Emoji</button>
    </form>
"""

@app.route("/")
def home():
    return form_html

@app.route("/get-emoji")
def get_emoji():
    url = "https://emojihub.yurace.pro/api/random"
    response = requests.get(url)
    data = response.json()
    return f"Your emoji: {data['htmlCode']}"

if __name__ == "__main__":
    app.run(debug=True)