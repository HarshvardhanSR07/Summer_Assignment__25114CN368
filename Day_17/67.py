# ---------------- Q67: Intersection of arrays ----------------
print("\n--- Q67: Intersection of arrays ---")
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
intersection = sorted(set(arr1) & set(arr2))
print(f"Array1: {arr1}, Array2: {arr2}")
print(f"Intersection: {intersection}")
 