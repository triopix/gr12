"""

Exercise 3.1 

The cover price of a book is $24.95, but bookstores get a 40 percent discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy. Calculate the total
wholesale costs for 60 copies.

"""

# price in $
cover_price = 24.95

# as percentage
discount = 40

# initial shipping cost in $
shipping_cost = 3

# recurring shipping cost after initial
recurring_shipping_cost = 0.75

# number of book copies
number_of_copies = 60


def calculate_wholesale_cost(cv_price, disc, init_shipping_cst, reccur_shipping_cst, copies):
    
    # discounted cost
    cost_after_disc = cv_price - (cv_price * (disc / 100))
    
    # total cost
    total_cost = cost_after_disc + init_shipping_cst + (reccur_shipping_cst * (copies-1))
    
    return total_cost


test = calculate_wholesale_cost(cover_price, discount, shipping_cost, recurring_shipping_cost, number_of_copies)

print(f"Your total wholesale cost is: {test}")