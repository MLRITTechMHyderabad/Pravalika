def process_data(data, index):
    try:
        data = [int(item) for item in data] 
        result = data[index] / data[index]  
        return result
    except ZeroDivisionError:
        return "Error: Division by zero."
    except ValueError:
        return "Error: Invalid value in data (could not convert to int)."
    except IndexError:
        return "Error: Index out of range."
    except Exception as e:
        return f"Unexpected error: {e}"
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 2)) 
print(process_data(["10", "abc", "30"], 1)) 
print(process_data([10, 20], 5))
