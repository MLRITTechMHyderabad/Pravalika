dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = dict1.copy()  # Start with a copy of dict1

for key, value in dict2.items():
    if key in merged:
        # If key exists, make sure values are in a list
        if isinstance(merged[key], list):
            merged[key].append(value)
        else:
            merged[key] = [merged[key], value]
    else:
        merged[key] = value

print(merged)
