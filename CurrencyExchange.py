import json
import requests
import time
from FileManager import FileManager
from HistoryMessages import HistoryMessages

class CurrencyExchange:
    def __init__(self, balance=0):
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"
        

    def write_to_history(self, hist_dict):
         
        # TODO:
        # Comment and refine the code below so that the dictionary 
        # from hist_dict is added to hist.json
    
        # self.file_manager 
        try:
            with open(self.hist_file_path, 'r') as hist_file:
                history = json.load(hist_file)
        except (FileNotFoundError, json.JSONDecodeError):
            history = []

        history.append(hist_dict)

        with open(self.hist_file_path, 'w') as hist_file:
            json.dump(history, hist_file, indent=4)

    def get_exchange_rates(self):
        
        # Implement a process that sends a get request to the link 
        # and returns the resulting dictionary.
        try:
            response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
            response.raise_for_status()
            exchange_rates = response.json().get('rates', {})
            return exchange_rates
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None
        
    
    def exchange_currency(self, currency_from, currency_to, amount):
        

        # implement a process that transfers the specified amount from currency `currency_from` 
        # to currency `currency_to` and, if positive, returns the amount in the new currency
        # with a positive outcome, the record of history looks like this 
        # history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        # self.write_to_history(history_message)
        
        # in case of a negative outcome, the history entry looks like this
        # - if currency_from or currency_to is specified incorrectly
        # - if amount is not a number
        # history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
        # self.write_to_history(history_message)
        try:
            amount = float(amount)
        except ValueError:
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return "Invalid amount entered. Please enter a numeric value."

        exchange_rates = self.get_exchange_rates()
        if exchange_rates is None:
            return "Failed to fetch exchange rates."

        currency_from = currency_from.upper()
        currency_to = currency_to.upper()

        if currency_from not in exchange_rates or currency_to not in exchange_rates:
            history_message = HistoryMessages.exchange("failure", amount, None, currency_from, currency_to)
            self.write_to_history(history_message)
            return f"Invalid currency code. Available currencies: {', '.join(exchange_rates.keys())}"

        conversion_rate = exchange_rates[currency_to] / exchange_rates[currency_from]
        converted_amount = amount * conversion_rate
        history_message = HistoryMessages.exchange("success", amount, converted_amount, currency_from, currency_to)
        self.write_to_history(history_message)
        return converted_amount
        