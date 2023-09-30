import re

# Read the file
with open('example-text.txt', 'r') as file:
    text = file.read()

# 1. Extract list of all words.
all_words = re.findall(r'\b\w+\b', text)
print("All Words:", all_words)
# 2. Extract list of all words starting with a capital letter.
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
print("Capital Words:", capital_words)
# 3. Extract list of all words of length 5.
five_letter_words = re.findall(r'\b\w{5}\b', text)
print("Five-Letter Words:", five_letter_words)
# 4. Extract list of all words inside double quotes.
quoted_words = re.findall(r'"([^"]+)"', text)
print("Quoted Words:", quoted_words)
# 5. Extract list of all vowels.
vowels = re.findall(r'[aeiouAEIOU]', text)
print("Vowels:", vowels)
# 6. Extract list of 3 letter words ending with letter ‘e’.
three_letter_e_words = re.findall(r'\b\w{3}e\b', text)
print("Three-Letter Words Ending with 'e':", three_letter_e_words)
# 7. Extract list of all words starting and ending with letter ‘b’.
b_words = re.findall(r'\b[bB]\w*[bB]\b', text)
print("Words Starting and Ending with 'b':", b_words)
# 8. Remove all the punctuation marks from the text.
text_without_punctuation = re.sub(r'[^\w\s]', '', text)
print("Text without Punctuation:", text_without_punctuation)
# 9. Replace all words ending 'n't' to their full form 'not'.
text_with_full_form = re.sub(r'\b(\w+)n\'t\b', r'\1 not', text)
print("Text with Full Form of 'n't':", text_with_full_form)
# 10. Replace all the new lines with a single space.
text_single_space = re.sub(r'\n', ' ', text)
print("Text with New Lines Replaced:", text_single_space)
