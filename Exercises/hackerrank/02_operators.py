# from decimal import Decimal

mealCost = float(input())
# tipPercent = float(input())
# taxPercent = float(input())

# mealCost = 12.00
tip = mealCost * 20 / 100
tax = mealCost * 8 / 100
print(float(tip))
print(float(tax))

totalCost = mealCost + tip + tax
print(totalCost)
print(round(totalCost))
