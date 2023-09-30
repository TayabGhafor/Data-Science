import re

# Reading the file
with open('example-text.txt', 'r') as file:
    text = file.read()

# 1. Extracting list of all words.
words = re.findall(r'\b\w+\b', text)

# 2. Extracting list of all words starting with a capital letter.
capital_words = re.findall(r'\b[A-Z]\w*\b', text)

# 3. Extracting list of all words of length 5.
five_letter_words = re.findall(r'\b\w{5}\b', text)

# 4. Extracting list of all words inside double quotes.
quoted_words = re.findall(r'"([^"]*)"', text)

# 5. Extracting list of all vowels.
vowels = re.findall(r'[aeiouAEIOU]', text)

# 6. Extracting list of 3 letter words ending with letter ‘e’.
three_letter_e_words = re.findall(r'\b\w{3}e\b', text)

# 7. Extracting list of all words starting and ending with letter ‘b’.
b_words = re.findall(r'\b[bB]\w*[bB]\b', text)

# 8. Removing all punctuation marks from text.
text_without_punctuation = re.sub(r'[^\w\s]', '', text)

# 9. Replacing all words ending ‘n't’ to their full form ‘not’.
text_replaced_not = re.sub(r'\b(\w+)n\'t\b', r'\1 not', text)

# 10. Replacing all new lines with single-space.
text_single_space = re.sub(r'\n', ' ', text)

# Printing the results
print("1. All Words:", words)
print("2. Capital Words:", capital_words)
print("3. Five Letter Words:", five_letter_words)
print("4. Quoted Words:", quoted_words)
print("5. Vowels:", vowels)
print("6. Three Letter Words Ending with 'e':", three_letter_e_words)
print("7. Words Starting and Ending with 'b':", b_words)
print("8. Text without Punctuation:\n", text_without_punctuation)
print("9. Text with 'not' Replaced:", text_replaced_not)
print("10. Text with New Lines Replaced by Spaces:\n", text_single_space)
