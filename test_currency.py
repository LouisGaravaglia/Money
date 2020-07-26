from unittest import TestCase
from currency import CurrencyMethods
from app import app
from flask import session


class FlaskTests(TestCase):

    def setUp(self):
        """ Stuff to do before every test. """

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page(self):
        """ Make sure all elements are appearing in the home page """

        with self.client as client:
            res = self.client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<button>Enter</button>", html)
            self.assertIn("board", session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score:', res.data)
            self.assertIn(b'Score:', res.data)
            self.assertIn(b'Seconds Left:', res.data)

