"""This module defines the PenaltyStrategy class."""

__author__ = "NAVRAJ SINGH"
__version__ = ""

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PenaltyStrategy(PaymentStrategy):
    def process_payment(self, account:BillingAccount, payee: Payee, amount:float) -> str:
        """
        This will process a payment with a penality 
        Account: Billing account
        Payee: payee
        amount:float
        return str
        """
        account.deduct_balance(payee,amount)
        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            account.add_balance(payee, 10.00)
            balance = account.get_balance(payee)
            return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${balance:.2f}."
