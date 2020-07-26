from flask import Flask, request, render_template, session, make_response, redirect, flash, jsonify
from random import choice, randint
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from unittest import TestCase
from flask_debugtoolbar import DebugToolbarExtension
from decimal import *
from currency import CurrencyMethods

app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 
# app.config["TESTING"] = True
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

debug = DebugToolbarExtension(app)

c = CurrencyRates(force_decimal=True)
code = CurrencyCodes()
currency_method = CurrencyMethods()

currencies = {"XCD", "MWK", "MGA", "MOP", "MOP", "LRD", "ZAR", "CHF", "KES", "KZT", "JOD", "JPY", "JMD", "ILS", "IQD", "IRR", "IDR", "ISK", "HUF", "HKD", "HNL", "HTG", "GYD", "XOF", "GNF", "GBP", "GTQ", "XCD", "DKK", "GIP", "GHS", "GEL", "GMD", "XAF", "XPF", "FJD", "DKK", "FKP", "ETB", "ERN", "XAF", "SVC", "EGP", "DOP", "XCD", "DJF", "DKK", "XOF", "CZK", "ANG", "CUP", "CUC", "HRK", "CRC", "NZD", "XAF", "CDF", "KMF", "COU", "COP", "AUD", "CNY", "CLP", "CLF", "XAF", "KYD", "CAD", "XAF", "KHR", "CVE", "BIF", "XOF", "BGN", "BND", "BRL", "NOK", "BWP", "BAM", "BOV", "BOB", "INR", "BTN", "BMD", "XOF", "BZD", "BYN", "BBD", "BDT", "BHD", "BSD", "AZN", "AUD", "AWG", "AMD", "ARS", "XCD", "AOA", "EUR", "USD", "DZD", "ALL", "AFN"}


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
    rounded = "..."
    end_symbol = ""
    
    # if start_curr in currencies:
    #     start_symbol = code.get_symbol(start_curr)
    # else:
    #     flash("The converting from currency code is not valid.", "error")
    
    currency_method.checking_converting_from(currencies, start_curr)
    
    # if end_curr in currencies:
    #     end_symbol = code.get_symbol(end_curr)  
    # else:
    #     flash("The converting to currency code is not valid.", "error")
    
    end_symbol = currency_method.checking_converting_to(currencies, end_curr)
    
    # if amount == "" or amount == "0":
    #     flash("Not a valid amount", "error")  
    
    currency_method.checking_amount_validity(amount)
    
    # if start_curr in currencies and end_curr in currencies and amount != "" and amount != "0": 
    #     result = c.convert(f'{start_curr}', f'{end_curr}', Decimal(f'{amount}'))
    #     rounded = round(result,2)
    
    rounded = currency_method.checking_all(start_curr, currencies, end_curr, amount)
   
    

            

    return render_template("response.html", rounded=rounded, end_symbol=end_symbol)

