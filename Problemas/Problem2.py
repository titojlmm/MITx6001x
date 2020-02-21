# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:18:28 2020

@author: Tito
"""

def getFixesMonthlyPayment(month, balancemensual, monthlyInterestRate, minimumFixedMonthlyPayment):
    """
    This method  calculate the credit card balance after one month if a person 
    only pays the minimum monthly payment required by the credit card company each month.
    
    Parameters
    ----------
    month : Integer
        The month the balance is calculated on.
    balance : Number
        The outstanding balance on the credit card.
    monthlyInterestRate : Number
        Monthly interest rate as a decimal.
    minimumFixedMonthlyPayment: Integer (10x)
        The minimum monthly payment required by the credit card company each month

    Returns
    -------
    The remaining balance at the end of the month, not rounded.

    """
    monthlyUnpaidBalance = balancemensual - minimumFixedMonthlyPayment
    updatedBalanceMonth = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    month += 1
    if month < 12:
        getFixesMonthlyPayment(month, updatedBalanceMonth, monthlyInterestRate, minimumFixedMonthlyPayment)
    else:
        if updatedBalanceMonth > 0:
            getFixesMonthlyPayment(0, balance, monthlyInterestRate, minimumFixedMonthlyPayment + 10)
        else:
            print("Lowest Payment: " +str(minimumFixedMonthlyPayment))
        

def getFixesMonthlyPaymentYear(balancetotal, annualInterestRate):
    """
    This method calculates the minimum fixed monthly payment needed
    in order pay off a credit card balance within 12 months.
    The monthly payment must be a multiple of $10 and is the same for all months.
    
    Prints out one line: the lowest monthly payment that will pay off all debt in under 1 year.

    
    Parameters
    ----------
    balance : Number
        The outstanding balance on the credit card.
    annualInterestRate : Number
        Annual interest rate as a decimal.

    Returns
    -------
    NONE

    """
    monthlyInterestRate = annualInterestRate / 12.0

    getFixesMonthlyPayment(0, balancetotal, monthlyInterestRate, 10)

balance = 3329
annualInterestRate = 0.2   
getFixesMonthlyPaymentYear(balance, annualInterestRate)
