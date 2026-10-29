# --- Lab 7 Self-Assessment ---

# Question 1:
# The first bug I noticed was the missing colon in the for loop.
# I spotted it by reading the code before running it, and the
# SyntaxError confirmed my suspicion. This showed me that I tend
# to notice syntax mistakes first. The debugging print statements
# helped me investigate the other errors by tracking variable values.

# Question 2:
# apply_discount(price, tier) calculates the price after applying
# a discount based on the customer's membership tier.
# It takes two inputs: the original price and the membership tier.
# Gold gets 15% off, silver gets 10%, bronze gets 5%, and other
# tiers get no discount. It returns the discounted price, not the
# tax or the final price after tax.
# A colleague could use it without reading the function's code
# if the accepted tiers and their discounts were documented.

# Question 3:
# AI Disclosure:
# I used ChatGPT to help me understand the debugging process,
# add temporary print statements, interpret error messages,
# and check my reasoning while correcting the code.
#
# Reflection:
# AI helped build my understanding because I still ran the code,
# examined the errors, and tested the fixes. I learned why
# len(sales) is 5 even though the last valid index is 4,
# and how changing a loop condition prevents an IndexError.


# --- Exercise 1: calculate_tax ---

def calculate_tax(price, rate): return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):,.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):,.2f}")


# --- Exercise 2: apply_discount ---

def apply_discount(price, tier):
    if tier == "gold":
        discount = .15
    elif tier == "silver":
         discount = .1
    elif tier == "bronze":
         discount = .05
    else:
        discount = 0
    return price * (1 - discount)

print(f"gold: ${apply_discount(200, 'gold'):,.2f}")
print(f"silver: ${apply_discount(200, 'silver'):,.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):,.2f}")
print(f"none: ${apply_discount(200, 'none'):,.2f}")

# --- Exercise 3: Compose them ---

discounted_price = apply_discount(200, 'gold')
tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax
print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4: Loop + function ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")



# --- Exercise 5: Debug First, Then Ask | Fixed broken_sales.py


sales = [120, 80, 250, 175, 90]

# Bug 1: Using = replaced the total with each new sale.
# I changed it to += to keep adding each sale to the previous total.

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2: The for loop was missing a colon, causing a SyntaxError.
# I added the colon at the end of the loop statement.

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3: The loop allowed i to equal 5, even though the last index is 4.
# I removed = from <= so the loop stops before accessing an invalid index.

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6: Scope experiment ---


x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?


# I predicted all three outputs correctly: 100, 1998, and 100. 
# Scope determines where a variable can be used.
# Even though both variables are named x, they are not the same.
# The x inside double_it() is local to that function, so changing
# it does not affect the global x outside the function.
# That's why we see those outputs.







    


