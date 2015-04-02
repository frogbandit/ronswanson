from flask import Flask, jsonify, render_template, request, json
import requests, random

app = Flask(__name__)

app.config['DEBUG'] = True 

url = "http://ron-swanson-quotes.herokuapp.com/quotes"

@app.route("/", methods=["GET", "POST"])
def hello():
 
    response_dict = requests.get(url).json()
    print response_dict
    quote = response_dict["quote"]
    num = random.randrange(0, 10)
    return_dict = [quote, num]
    print num
    return render_template("hello.html", api_data=return_dict)
   

if __name__ == '__main__':
	app.run(host='0.0.0.0')