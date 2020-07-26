"""Utilities related to Boggle game."""
from flask import Flask, request, render_template, session, make_response, redirect, flash, jsonify
from random import choice
import string
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from decimal import *

code = CurrencyCodes()
c = CurrencyRates(force_decimal=True)

class CurrencyMethods():

    # def __init__(self):

    #     self.words = self.read_dict("words.txt")

    def checking_converting_from(self, currencies, start_curr):
        """Read and return all words in dictionary."""

        if start_curr in currencies:
            start_symbol = code.get_symbol(start_curr)
        else:
            flash("The converting from currency code is not valid.", "error")
            

    def checking_converting_to(self, currencies, end_curr):
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
            

    def checking_all(self, start_curr, currencies, end_curr, amount):
        """Read and return all words in dictionary."""

        rounded = "..."
        
        if start_curr in currencies and end_curr in currencies and amount != "" and amount != "0": 
            result = c.convert(f'{start_curr}', f'{end_curr}', Decimal(f'{amount}'))
            rounded = round(result,2)
        
        return rounded