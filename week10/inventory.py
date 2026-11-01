# Reflection 1:
# I was surprised that Python lets me access items from the end of a list
# using negative indices and select multiple items at once with slicing.
# I expected that I would need a separate loop to do those things.

# Reflection 2:
# During my real estate case competition, I worked with property rents
# and financial assumptions while evaluating a development project.
# A Python list could have helped me compare rents, calculate averages,
# and identify the highest and lowest values without repeatedly
# checking the data manually in Excel.


# Exercise 1 - Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2 - Index practice

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3 - Slicing

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4 - Modify

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5 - Tuple comparison

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed. They are useful for keeping coordinates fixed.")
print(coords)

# Exercise 6 - Average of a list of sales

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

best = max(sales)
worst = min(sales)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Best: {best}")
print(f"Worst: {worst}")

# Exercise 7 - Accumulator pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print(prices)
print(discounted)

# Exercise 8 - Filter by threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print(len(high_sales))
print(f"{sum(high_sales) / len(high_sales):.2f}")