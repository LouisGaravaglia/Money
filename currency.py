"""Utilities related to Boggle game."""
from flask import Flask, request, render_template, session, make_response, redirect, flash, jsonify
from random import choice
import string
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes


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
            return flash("The converting from currency code is not valid.", "error")
            
        return start_symbol

    def checking_converting_to(self, currencies, end_curr):
        """Read and return all words in dictionary."""

        if end_curr in currencies:
            end_symbol = code.get_symbol(end_curr)  
        else:
            return flash("The converting to currency code is not valid.", "error")
            
        return end_symbol