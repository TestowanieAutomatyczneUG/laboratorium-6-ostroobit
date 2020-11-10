import unittest
from src.statement import statement

class TestStatement(unittest.TestCase):
    def test_statement_value_error(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 35
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "top1zlychtypowsztuk"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        
        self.assertRaises(ValueError, statement, invoice, plays)
    
    def test_statement_tragedy_greater_than_30(self):
        invoice = {
            "customer": "DurzaFi",
            "performances": [
                {
                    "playID": "othello",
                    "audience": 47
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        self.assertEqual(statement(invoice, plays), "Statement for DurzaFi\n Othello: $570.00 (47 seats)\nAmount owed is $570.00\nYou earned 17 credits\n")
    
    def test_statement_tragedy_less_than_30_or_equal_30(self):
        invoice = {
            "customer": "K.W. Firma",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 25
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }

        self.assertEqual(statement(invoice, plays), "Statement for K.W. Firma\n Hamlet: $400.00 (25 seats)\nAmount owed is $400.00\nYou earned 0 credits\n")

    def test_statement_comedy_greater_than_20(self):
        invoice = {
            "customer": "Spułka zoo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 25
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }

        self.assertEqual(statement(invoice, plays), "Statement for Spułka zoo\n As You Like It: $500.00 (25 seats)\nAmount owed is $500.00\nYou earned 5 credits\n")

    def test_statement_comedy_less_than_20_or_equal_20(self):
        invoice = {
            "customer": "Lubimy komedię w mniej niż 20 osób sp. z.o.o.",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 20
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }

        self.assertEqual(statement(invoice, plays), "Statement for Lubimy komedię w mniej niż 20 osób sp. z.o.o.\n As You Like It: $360.00 (20 seats)\nAmount owed is $360.00\nYou earned 4 credits\n")