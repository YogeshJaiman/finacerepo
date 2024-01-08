from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/process_form", methods = ['POST'])
def process_data():
    url = "https://www.alphavantage.co/query"
    param = {
        'function':request.form.get('function'),
        'symbol': request.form.get('symbol'),
        'interval': request.form.get('interval'),
        'apikey':request.form.get('apikey')
    }

    response = requests.get(url,params= param)
    data =  response.json()
    return f"data = {data}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)