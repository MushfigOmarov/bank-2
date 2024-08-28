import json
from FileManager import FileManager
from HistoryMessages import HistoryMessages


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.file_manager = FileManager()
        self.hist_file_path = "hist.json"

    def write_to_history(self, hist_dict):
        #         with open(self.hist_file_path, 'w') as hist_file:
        #             hist_file.write(json.dumps(hist_dict) + '\n')
        self.file_manager.add_to_json(hist_dict, self.hist_file_path)

    def deposit(self, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                #                  history_message = HistoryMessages.deposit("failure", amount, self.balance)
                status = "failure"
                print("Invalid amount for deposit!")
            else:
                self.balance += amount
#                 history_message = HistoryMessages.deposit("success", amount, self.balance)
#                 self.write_to_history(history_message)
                status = "success"
        except ValueError:
            print("Invalid input for deposit!")
            status = "failure"

        history_message = HistoryMessages.deposit(status, amount, self.balance)
        self.write_to_history(history_message)
#        history_message = HistoryMessages.deposit("failure", amount, self.balance)

#         self.write_to_history(history_message)
#         return history_message

    def debit(self, amount):
        try:
            amount = int(amount)
#             if amount <= 0 or amount > self.balance:
#                 history_message = HistoryMessages.debit("failure", amount, self.balance)
            if self.balance < amount:
                status = "failure"
                print("Invalid amount for debit!")
            else:
                self.balance -= amount
#                 history_message = HistoryMessages.debit("success", amount, self.balance)
#                 self.write_to_history(history_message)
                status = "success"
        except ValueError:
            print("Invalid input for debit!")
            status = "failure"
        history_message = HistoryMessages.debit(
            "failure", amount, self.balance)
        self.write_to_history(history_message)
#         return history_message

    def get_balance(self):
        return self.balance

#     def dict_to_string(self, dict):
#         if dict["operation_type"] != "exchange":
#             return f'type: {dict["operation_type"]} status: {dict["status"]} amount: {dict["amount_of_deposit"]} balance: {dict["total_balance"]}'
#         else:
#             return f'type: {dict["operation_type"]} status: {dict["status"]} pre exchange amount: {dict["pre_exchange_amount"]} exchange amount: {dict["exchange_amount"]} currency from: {dict["currency_from"]} currency to: {dict["currency_to"]}'

    def get_history(self):
        history_lines = []
        with open(self.hist_file_path, 'r') as hist_file:
            for line in hist_file:
                hist_dict = json.loads(line)  # Doğru dönüşüm yapılmalı
                history_lines.append(self.dict_to_string(
                    hist_dict))  # Listeye ekleme yapılmalı
        return history_lines

    def dict_to_string(self, hist_dict):
        if hist_dict["operation_type"] != "exchange":
            return f'type: {hist_dict["operation_type"]} status: {hist_dict["status"]} amount: {hist_dict["amount_of_deposit"]} balance: {hist_dict["total_balance"]}'
        else:
            return f'type: {hist_dict["operation_type"]} status: {hist_dict["status"]} pre exchange amount: {hist_dict["pre_exchange_amount"]} exchange amount: {hist_dict["exchange_amount"]} currency from: {hist_dict["currency_from"]} currency to: {hist_dict["currency_to"]}'