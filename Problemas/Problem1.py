# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:18:28 2020

@author: Tito
"""

def getRemainingMonthlyBalance(month, balance, monthlyInterestRate, monthlyPaymentRate):
    """
    This method calculates the credit card balance after one year if a person 
    only pays the minimum monthly payment required by the credit card company each month.
    
    Parameters
    ----------
    month : Integer
        The month the balance is calculated on.
    balance : Number
        The outstanding balance on the credit card.
    monthlyInterestRate : Number
        Monthly interest rate as a decimal.
    monthlyInterestRate : Number
        Minimum monthly payment rate as a decimal.

    Returns
    -------
    The remaining balance at the end of the month, not rounded.

    """
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalanceMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    month += 1
    if month < 12:
        getRemainingMonthlyBalance(month, updatedBalanceMonth, monthlyInterestRate, monthlyPaymentRate)
    else:
        print("Remaining balance: " +str(round(updatedBalanceMonth, 2)))
        

def getRemainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    This method  calculate the credit card balance after one year if a person 
    only pays the minimum monthly payment required by the credit card company each month.
    
    Parameters
    ----------
    balance : Number
        The outstanding balance on the credit card.
    annualInterestRate : Number
        Annual interest rate as a decimal.
    monthlyInterestRate : Number
        Minimum monthly payment rate as a decimal.

    Returns
    -------
    The remaining balance at the end of the year, not rounded.

    """
    monthlyInterestRate = annualInterestRate / 12.0

    getRemainingMonthlyBalance(0, balance, monthlyInterestRate, monthlyPaymentRate)

    
getRemainingBalance(42, 0.2, 0.04)

getRemainingBalance(484, 0.2, 0.04)