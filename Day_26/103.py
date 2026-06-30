# ---------------- Q103: ATM simulation ----------------
print("\n--- Q103: ATM simulation (simulated transactions) ---")
balance = 10000.0
print(f"Opening balance: Rs {balance:.2f}")
deposit_amt = 2000.0
balance += deposit_amt
print(f"Deposited Rs {deposit_amt:.2f} -> Balance: Rs {balance:.2f}")
withdraw_amt = 3500.0
if withdraw_amt <= balance:
    balance -= withdraw_amt
    print(f"Withdrew Rs {withdraw_amt:.2f} -> Balance: Rs {balance:.2f}")
else:
    print("Insufficient balance!")
print(f"Final balance: Rs {balance:.2f}")