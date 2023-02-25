'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit B Take-home Assignment
Script 2
'''

#Printing a well formatted invoice

smallPrice = 9.20
mediumPrice = 8.52
largePrice = 7.98

smalls = input("enter number of small boxes: ")
mediums = input("enter number of medium boxes: ")
larges = input("enter number of large boxes: ")

total_small_price = float(smalls) * smallPrice
total_medium_price = float(mediums) * mediumPrice
total_large_price = float(larges) * largePrice

total_total = total_small_price + total_medium_price + total_large_price

size, qty, cost_per_box, totals = "SIZE", "QTY", "COST PER BOX", "TOTALS"


print(f"{size:8}{qty: >5}{cost_per_box: >16}{totals: >10}")

print(f"{'Small':8}{smalls:>5}{smallPrice:>16.2f}{total_small_price:>10.2f}")
print(f"{'Medium':8}{mediums:>5}{mediumPrice:>16.2f}{total_medium_price:>10.2f}")
print(f"{'Large':8}{larges:>5}{largePrice:>16.2f}{total_large_price:>10.2f}")
print(f"{'TOTAL':8}{total_total:>31.2f}")

'''
Execution Results:
enter number of small boxes: 10
enter number of medium boxes: 9
enter number of large boxes: 8
SIZE      QTY    COST PER BOX    TOTALS
Small      10            9.20     92.00
Medium      9            8.52     76.68
Large       8            7.98     63.84
TOTAL                            232.52

enter number of small boxes: 5
enter number of medium boxes: 10
enter number of large boxes: 15
SIZE      QTY    COST PER BOX    TOTALS
Small       5            9.20     46.00
Medium     10            8.52     85.20
Large      15            7.98    119.70
TOTAL                            250.90
'''