'''This module calculates discount after payment'''
def discount_calculator(original_price, discount_percentage):   
    """This function calculates the final price after removing discount.
    User inputs Original_price: price of item
    discount_percentage: Discount you are offering customer e.g input 35% as 0.35"""   
    final_price = original_price -(discount_percentage*original_price)
    return final_price
