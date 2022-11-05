from die import Die

# Create a D6.
die_1 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    result = die_1.roll()
    results.append(result)

print(results)