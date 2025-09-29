from scipy.stats import skew, kurtosis

# Step 1: Take input from user
raw_data = input("Enter ungrouped numerical data separated by commas: ")

# Step 2: Convert input string to a list of floats
try:
    data = [float(x.strip()) for x in raw_data.split(",")]
except ValueError:
    print("Invalid input! Please enter only numbers separated by commas.")
    exit()

# Step 3: Calculate skewness and kurtosis
data_skewness = skew(data)
data_kurtosis = kurtosis(data)  # By default, Fisher's definition (normal dist = 0)

# Step 4: Display results
print("\n--- Results ---")
print("Ungrouped Data:", data)

# Skewness
print(f"\nSkewness: {data_skewness:.4f}")
if data_skewness > 0:
    print("Interpretation: Positively skewed (tail on the right)")
elif data_skewness < 0:
    print("Interpretation: Negatively skewed (tail on the left)")
else:
    print("Interpretation: Symmetrical distribution")

# Kurtosis
print(f"\nKurtosis: {data_kurtosis:.4f}")
if data_kurtosis > 0:
    print("Interpretation: Leptokurtic (sharper peak than normal distribution)")
elif data_kurtosis < 0:
    print("Interpretation: Platykurtic (flatter than normal distribution)")
else:
    print("Interpretation: Mesokurtic (normal distribution)")
