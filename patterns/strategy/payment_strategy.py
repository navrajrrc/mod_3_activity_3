"""This module defines the PaymentStrategy class."""

__author__ = "Navraj singh"
__version__ = ""

from abc import ABC, abstractmethod 
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PaymentStrategy(ABC):
    """
    
    """
    @abstractmethod
    def process_payment(self, account, payee, amount) -> str:
        """
        This will process a payment from the given account
        Account: Billing account
        Payee: payee
        amount: float
        Returns: String
        """
        pass 
