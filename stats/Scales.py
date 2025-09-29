def detect_scale(data):
    try:
        # Try converting all values to float
        numeric_data = [float(x) for x in data]
        is_numeric = True
    except:
        is_numeric = False

    if not is_numeric:
        return "Nominal"

    unique_vals = sorted(set(numeric_data))

    # Ratio scale: all values >= 0 and has a meaningful zero
    if min(numeric_data) == 0 or all(x >= 0 for x in numeric_data):
        if len(unique_vals) > 10:
            return "Ratio"
        else:
            return "Ordinal"

    # Interval scale: contains negative values, but still numeric
    if min(numeric_data) < 0:
        return "Interval"

    # Fallback
    return "Ordinal"

user_input = input("Enter values separated by commas: ")
data = user_input.split(",")  # split into list

result = detect_scale(data)
print("Detected scale:", result)