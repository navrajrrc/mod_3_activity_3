"""This module defines the PartialPaymentStrategy class."""

__author__ = "Navraj singh"
__version__ = ""

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PartialPaymentStrategy(PaymentStrategy):

    def process_payment(self, account: BillingAccount, payee: Payee, amount:float) -> str:
        """
        This will process a partial payment from a given account
        Account: Billing account
        Payee: payee
        amount: float
        retuns str
        """
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)

        if balance <=0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."