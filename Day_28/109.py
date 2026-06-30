
# ---------------- Q109: Library management system ----------------
print("\n--- Q109: Library management ---")
books = [
    {"id": "B1", "title": "Python Basics", "issued": False},
    {"id": "B2", "title": "Data Structures", "issued": True},
]
print("Books:")
for b in books:
    status = "Issued" if b["issued"] else "Available"
    print(f"  ID: {b['id']}, Title: {b['title']}, Status: {status}")
# Issue a book
target = next(b for b in books if b["id"] == "B1")
target["issued"] = True
print(f"Issued '{target['title']}' -> Status now: {'Issued' if target['issued'] else 'Available'}")