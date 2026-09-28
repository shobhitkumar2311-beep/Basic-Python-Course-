# Can we have a set with 18 (int) and '18' (str) as two different elements?

s = set()
s.add(18)  # Adding an integer
s.add('18')  # Adding a string
print("The set contains:", s)

# The output will be The set contains: {'18', 18}