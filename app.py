from flask import Flask
from flask import jsonify
import requests 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    response = {
        'response': 'Hello world! from Elango!!!'
    }

    #return jsonify(response)
    return '<h2>Hello world! from service1 main page!!! </h2>'   


#@app.route('/srv1', methods=['GET'])
#def service1_url():
#    """Base url to test API."""
#
#    response = {
#        'response': 'Hello world! from <h1>service1 !!! service1 !!! service1 !!! service1 !!!</h1>'
#    }
#
#    #return jsonify(response)
#    return 'Hello world! from <h1>service1 !!! service1 !!! service1 !!!</h1>'

@app.route("/test", methods=['GET'])
def service2_url():
    """Base url to test API."""

    response = {
        'response': 'Hello world! from <h1> Elango public alb !!!</h1> '
    }

    return 'Hello world! from <h1> public ALB</h1> '

#@app.route('/google')
#def hello():
#    r = requests.get('10.0.1.20:5000/hello','error : check service2 ')
#    return r.text

@app.route('/srv2')
def internal_home():
    #r = requests.get('http://zoo-708647630.us-east-1.elb.amazonaws.com')
    r = requests.get('http://internal-zoominfo-private-alb-1759215971.eu-west-1.elb.amazonaws.com')
    return r.text

@app.route('/srv2_google')
def internal_search():
    #r = requests.get('http://zoo-708647630.us-east-1.elb.amazonaws.com')
    r = requests.get('http://internal-zoominfo-private-alb-1759215971.eu-west-1.elb.amazonaws.com/search')
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
