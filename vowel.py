word = input("Enter the word:")
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(f"Total vowels: {count}")