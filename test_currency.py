from unittest import TestCase
from currency import CurrencyMethods
from app import app
from flask import session
from decimal import *

currency_method = CurrencyMethods()

class FlaskTests(TestCase):

    def setUp(self):
        """ Stuff to do before every test. """

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page(self):
        """ Making sure that the home page renders correct html. """

        with self.client as client:
            res = self.client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(">Convert</button", html)

    def test_converting(self):
        """ Making sure that the method to check whether the currency code
        entered is a valid currency code. """

        with self.client as client:
        
            res = self.client.post("/response", data={"converting-from": "USD", "converting-to": "USD", "amount": "10"})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>The current currency exchange rate is: US$10.00</h1>", html)
            
            res = self.client.post("/response", data={"converting-from": "EUR", "converting-to": "EUR", "amount": "8.48"})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn("<h1>The current currency exchange rate is: €8.48</h1>", html)
 
    def test_converting_to(self):
        """ Making sure that the method to check whether the currency code
        entered is a valid currency code. """

        self.assertEqual(currency_method.checking_converting_to("USD"), "US$")
        self.assertEqual(currency_method.checking_converting_to("EUR"), "€")
        self.assertEqual(currency_method.checking_converting_to("JPY"), "¥")

    def test_checking_all(self):
        """ Making sure that the method to check whether the currency code
        entered is a valid currency code. """

        self.assertEqual(currency_method.checking_all("USD", "USD", "10"), Decimal('10.00'))
        self.assertEqual(currency_method.checking_all("EUR", "EUR", "5.49"), Decimal('5.49'))
        self.assertEqual(currency_method.checking_all("JPY", "JPY", "999444120.43"), Decimal('999444120.43'))
        self.assertEqual(currency_method.checking_all("EUR", "EUR", "100540"), Decimal('100540.00'))
        self.assertEqual(currency_method.checking_all("USD", "USD", "0.01"), Decimal('0.01'))
