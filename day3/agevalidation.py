
customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

apply_discount = lambda customer: customer.update({"total_purchase": customer["total_purchase"] * 0.90}) if 18 <= customer["age"] <= 25 else customer.update({"total_purchase": customer["total_purchase"] * 0.95}) if 26 <= customer["age"] <= 40 else customer
list(map(apply_discount, customers))
print(customers)
