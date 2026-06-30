# ---------------- Q104: Quiz application ----------------
print("\n--- Q104: Quiz application (simulated answers) ---")
questions = [
    ("Capital of India?", "b) Delhi", "b"),
    ("Language for ML?", "c) Python", "c"),
    ("CPU stands for?", "c) Central Processing Unit", "c"),
]
user_answers = ["b", "c", "a"]   # simulated answers
score = 0
for (q, correct_text, ans), user in zip(questions, user_answers):
    print(f"Q: {q}  Your answer: {user}")
    if user == ans:
        print("  Correct!")
        score += 1
    else:
        print(f"  Wrong! Correct answer: {correct_text}")
print(f"Final Score: {score}/{len(questions)}")