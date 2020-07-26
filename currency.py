"""Utilities related to Boggle game."""
from flask import Flask, request, render_template, session, make_response, redirect, flash, jsonify
from random import choice
import string
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from decimal import *

code = CurrencyCodes()
c = CurrencyRates(force_decimal=True)

currencies = {"XCD", "MWK", "MGA", "MOP", "MOP", "LRD", "ZAR", "CHF", "KES", "KZT", "JOD", "JPY", "JMD", "ILS", "IQD", "IRR", "IDR", "ISK", "HUF", "HKD", "HNL", "HTG", "GYD", "XOF", "GNF", "GBP", "GTQ", "XCD", "DKK", "GIP", "GHS", "GEL", "GMD", "XAF", "XPF", "FJD", "DKK", "FKP", "ETB", "ERN", "XAF", "SVC", "EGP", "DOP", "XCD", "DJF", "DKK", "XOF", "CZK", "ANG", "CUP", "CUC", "HRK", "CRC", "NZD", "XAF", "CDF", "KMF", "COU", "COP", "AUD", "CNY", "CLP", "CLF", "XAF", "KYD", "CAD", "XAF", "KHR", "CVE", "BIF", "XOF", "BGN", "BND", "BRL", "NOK", "BWP", "BAM", "BOV", "BOB", "INR", "BTN", "BMD", "XOF", "BZD", "BYN", "BBD", "BDT", "BHD", "BSD", "AZN", "AUD", "AWG", "AMD", "ARS", "XCD", "AOA", "EUR", "USD", "DZD", "ALL", "AFN"}


class CurrencyMethods():

    # def __init__(self):

    #     self.words = self.read_dict("words.txt")

    def checking_converting_from(self, start_curr):
        """Read and return all words in dictionary."""

        if start_curr in currencies:
            start_symbol = code.get_symbol(start_curr)
        else:
            flash("The converting from currency code is not valid.", "error")
            

    def checking_converting_to(self, end_curr):
        """Read and return all words in dictionary."""

        if end_curr in currencies:
            end_symbol = code.get_symbol(end_curr)  
        else:
            flash("The converting to currency code is not valid.", "error")
            end_symbol = ""
            
        return end_symbol
    
    def checking_amount_validity(self, amount):
        """Read and return all words in dictionary."""

        if amount == "" or amount == "0":
            flash("Not a valid amount", "error")  
            

    def checking_all(self, start_curr, end_curr, amount):
        """Read and return all words in dictionary."""

        rounded = "..."
        
        if start_curr in currencies and end_curr in currencies and amount != "" and amount != "0": 
            result = c.convert(f'{start_curr}', f'{end_curr}', Decimal(f'{amount}'))
            rounded = round(result,2)
        
        return rounded