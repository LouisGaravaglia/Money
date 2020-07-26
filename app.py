from flask import Flask, request, render_template, session, make_response, redirect, flash, jsonify
from random import choice, randint
from forex_python.converter import CurrencyRates
from unittest import TestCase
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 
# app.config["TESTING"] = True
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

debug = DebugToolbarExtension(app)

c = CurrencyRates(force_decimal=False)


@app.route('/')
def home_page():
    """shows home page"""


    return render_template("index.html")

@app.route('/response', methods=["POST"])
def result_page():
    """shows currency exchange rate"""
    
    start_curr = request.form["converting-from"]
    end_curr = request.form["converting-to"]
    amount = request.form["amount"]
    
    result = c.convert('USD', 'INR', amount)
    symbol = c.get_symbol('{end_curr}')

    return render_template("response.html", result=result, symbol=symbol)

