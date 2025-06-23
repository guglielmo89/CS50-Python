x = input("what's x? ")
y = input("what's y? ")

z = float(x) + float(y)     # possible also int / float conversion

# round to the nearest integer with number of digits
q = round(z, 2)

print(f"{z:,}") #group like 1,000

print(f"{z:.2f}") #two digit precision
