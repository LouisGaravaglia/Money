from flask import Flask, request, render_template, session, make_response, redirect, flash, jsonify
from random import choice, randint
from forex_python.converter import CurrencyRates
from unittest import TestCase
from flask_debugtoolbar import DebugToolbarExtension
from decimal import *

app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 
# app.config["TESTING"] = True
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

debug = DebugToolbarExtension(app)

c = CurrencyRates(force_decimal=True)



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
    
    result = c.convert(f'{start_curr}', f'{end_curr}', Decimal(f'{amount}'))
    # start_symbol = c.get_symbol('{start_curr}')
    # end_symbol = c.get_symbol('{end_curr}')
    end_symbol = "$"
    
    # if not start_symbol:
    #     flash("The converting from currency code is not valid.")
    # if not end_symbol:
    #     flash("The converting to currency code is not valid.")
            

    return render_template("response.html", result=result, end_symbol=end_symbol)

