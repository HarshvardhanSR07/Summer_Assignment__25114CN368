# ---------------- Q101: Number guessing game ----------------
print("\n--- Q101: Number guessing game (simulated) ---")
secret = 42
guesses = [25, 60, 45, 42]  
attempts = 0
for guess in guesses:
    attempts += 1
    if guess < secret:
        print(f"Guess {guess}: Too low!")
    elif guess > secret:
        print(f"Guess {guess}: Too high!")
    else:
        print(f"Guess {guess}: Correct! Guessed in {attempts} attempt(s).")
        break