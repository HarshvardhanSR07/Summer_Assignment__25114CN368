# ---------------- Q107: Salary management system ----------------
print("\n--- Q107: Salary management ---")
basic = 40000.0
hra = basic * 0.20
da = basic * 0.10
gross = basic + hra + da
pf = basic * 0.12
tax = gross * 0.05
net = gross - pf - tax
print(f"Basic: Rs {basic:.2f}")
print(f"HRA (20%): Rs {hra:.2f}, DA (10%): Rs {da:.2f}, Gross: Rs {gross:.2f}")
print(f"PF (12%): Rs {pf:.2f}, Tax (5%): Rs {tax:.2f}")
print(f"Net Salary: Rs {net:.2f}")