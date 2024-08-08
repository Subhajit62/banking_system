# -*- coding: utf-8 -*-
"""banking_system.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-NnOzjK6AziYfrBoQmNPHfPtqffEfq2x
"""

from datetime import datetime

class Account:
  # """
  # Represents a bank account.

  # Attributes:
  #   account_number: The account number.
  #   owner: The account owner's name.
  #   balance: The current account balance.
  #   transactions: A list of transaction descriptions.
  #   last_updated: The timestamp of the last update.
  # """
  def __init__(self, account_number, owner):
    self.account_number = account_number
    self.owner = owner
    self.balance = 0
    self.transactions = []
    self.last_updated = datetime.now()

  def deposit(self, amount):
    """Deposits money into the account."""
    if amount > 0:
      self.balance += amount
      self.transactions.append(f"Deposited INR {amount}")
      self.last_updated = datetime.now()
      return f"INR {amount} deposited successfully"
    else:
      return "Invalid deposit amount"

  def withdraw(self, amount):
    """Withdraws money from the account."""
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      self.transactions.append(f"Withdrew INR {amount}")
      self.last_updated = datetime.now()
      return f"INR {amount} withdrawn successfully"
    elif amount <= 0:
      return "Invalid withdrawal amount"
    else:
      return "Insufficient funds"

  def get_balance(self):
    """Returns the current balance."""
    return f"Current balance: INR {self.balance}"

  def get_transactions(self):
    """Returns the list of transactions."""
    return self.transactions

  def get_last_updated(self):
    """Returns the timestamp of the last update."""
    return self.last_updated

  def print_transactions(self):
    """Prints the transactions."""
    for transaction in self.transactions:
      print(transaction)
    return "Transactions printed successfully"

class SavingsAccount(Account):
  """
  Represents a savings account with interest.

  Attributes:
    interest_rate: The annual interest rate.
  """
  def __init__(self, account_number, owner, interest_rate):
    super().__init__(account_number, owner)
    self.interest_rate = interest_rate

  def add_interest(self):
    """Adds interest to the account balance."""
    interest = self.balance * self.interest_rate
    self.balance += interest
    self.transactions.append(f"Interest Earned: INR {interest}")
    self.last_updated = datetime.now()
    return f"Interest Earned: INR {interest}"

