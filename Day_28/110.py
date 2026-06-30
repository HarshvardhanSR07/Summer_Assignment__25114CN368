# ---------------- Q110: Bank Account System ----------------
print("\n--- Q110: Bank Account System ---")

name = "Rahul Sharma"
balance = 5000.0

print("Account Holder:", name)
print("Opening Balance: Rs", balance)

# Deposit money
deposit = 1500
balance = balance + deposit
print("After depositing Rs", deposit, ": Rs", balance)

# Withdraw money
withdraw = 2000
balance = balance - withdraw
print("After withdrawing Rs", withdraw, ": Rs", balance)

# Final balance
print("Final Balance: Rs", balance)