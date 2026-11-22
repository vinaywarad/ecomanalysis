import pandas as pd

answers = pd.read_csv("answers.csv")

print("\n========== ALL ASSESSMENT QUESTIONS ==========\n")

for _, row in answers.iterrows():
    print(f"{row['id']}: {row['question']}")

print("\nTotal questions:", len(answers))