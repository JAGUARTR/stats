from collections import Counter

# Collect from user
entries = []
print("Enter values (type 'done' when finished):")
while True:
    entry = input("Enter an item: ")
    if entry.lower() == 'done':
        break
    entries.append(entry)

# Create a frequency table
frequency_table = Counter(entries)

# Print the frequency table
print("\nFrequency Table:")
for item, frequency in frequency_table.items():
    print(f"{item}: {frequency}")
