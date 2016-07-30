from flask import Flask, jsonify, render_template, request, json
import requests, random

app = Flask(__name__)

app.config['DEBUG'] = True 

# http://www.programmableweb.com/api/cat-facts

url = "http://catfacts-api.appspot.com/api/facts?number=1"

@app.route("/", methods=["GET", "POST"])
def hello():
 
    print requests.get(url).json()
    response_dict = requests.get(url).json()
    print response_dict
    quote = response_dict["facts"][0]
    num = random.randrange(0, 10)
    return_dict = [quote, num]
    print num
    return render_template("hello.html", api_data=return_dict)
   

if __name__ == '__main__':
	app.run(host='0.0.0.0')