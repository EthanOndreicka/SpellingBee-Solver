
def find_words_with_letters(word_list, key_letter, other_letters):
    matching_words = []

    # Iterate through each word in the list
    for word in word_list:
        # Check if the word contains the key letter, is 4 or more letters, and can be formed using the other letters
        if len(word) >= 4 and key_letter in word and all(word.count(letter) <= other_letters.count(letter) for letter in word if letter != key_letter):
            matching_words.append(word)

    return matching_words


words = []  # List to store lines

# Word list file
file_path = "./words.txt"

# Open the file
with open(file_path, 'r') as file:
    for line in file:
        # Remove leading and trailing whitespace
        clean_line = line.strip()
        words.append(clean_line)


# User input
key_letter = input("Enter the key letter that every word must contain: ").lower()
other_letters = input("Enter 6 other letters that words may or may not contain: ").lower()

#  Get result
result = find_words_with_letters(words, key_letter, other_letters)

# Print matching words
print("Words that can be formed with the given letters:")
for word in result:
    print(word)

