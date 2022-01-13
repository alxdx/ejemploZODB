import persistent

class Account (persistent.Persistent):
    def __init__(self,owner):
        self.owner = owner 
        self.balance = 0.0
    def deposit(self,amount):
        self.balance += amount
    def cash(self,amount):
        self.balance -=amount
