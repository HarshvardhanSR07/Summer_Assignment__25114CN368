# ---------------- Q116: Inventory Management System ----------------
print("\n--- Q116: Inventory Management System ---")

codes = ["I1", "I2"]
names = ["Notebook", "Pen"]
qty = [50, 5]
price = [40.0, 10.0]

print("Inventory:")

for i in range(len(codes)):
    value = qty[i] * price[i]
    print("Code:", codes[i])
    print("Name:", names[i])
    print("Quantity:", qty[i])
    print("Price: Rs", price[i])
    print("Value: Rs", value)
    print()

# Low stock check
threshold = 10

print("Low Stock Items (<= ", threshold, "):")

for i in range(len(qty)):
    if qty[i] <= threshold:
        print(names[i])