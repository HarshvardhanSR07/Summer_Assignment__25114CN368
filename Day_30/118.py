# ---------------- Q118: Mini Library System ----------------
print("\n--- Q118: Mini Library System ---")

book_ids = ["B1", "B2"]
book_titles = ["Python 101", "DSA Guide"]

member_ids = ["M1"]
member_names = ["Rahul"]

# Issue record (parallel lists instead of dictionary)
issued_book_ids = ["B1"]
issued_to_members = ["M1"]

print("Books Status:")

for i in range(len(book_ids)):
    status = "Available"

    for j in range(len(issued_book_ids)):
        if book_ids[i] == issued_book_ids[j]:
            status = "Issued to " + issued_to_members[j]
            break

    print(book_titles[i] + ":", status)