# Input word
word = input("Add Word : ")

# Convert each character to its ASCII value
ascii_values = [ord(char) for char in word]

# Print result
print(f"Your ASCII values for '{word}':")
print(ascii_values)