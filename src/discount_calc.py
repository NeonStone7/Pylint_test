import pandas as pd

def discount_calculator(Original_price, discount_percentage):
    """This function calculates the final price after removing discount.
    User inputs Original_price: price of item
    discount_percentage: Discount you are offering customer e.g input 35% as 0.35"""
    Final_price = Original_price - (discount_percentage * Original_price)
    return Final_price
