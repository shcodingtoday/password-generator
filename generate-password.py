import random;
from english_words import get_english_words_set
import pyperclip

# using Keysmith to run apple script to run shell script to run this script
# This script copies a new password to the clipboard
# /Users/sh/DEV/password-generator/generate-password.py 
words = list(get_english_words_set(['web2'], alpha=True))
password = ""
count = 0
minLength = 8
maxLength = 12
maxWordLength = 5
while (len(password)< minLength):
    if (count > 4):
        words = list(get_english_words_set(['web2'], alpha=True))
        count =0;
    count += 1
    new = words[random.randint(0, len(words)-1)]
    if (len(new) > maxWordLength):
        continue
    if ((len(new) + len(password)) < maxLength):
        password += new
        if (len(password) < minLength):
            password += "-"
# print(password + "-X1!")
pyperclip.copy(password + "-X1!")
# pyperclip.paste()