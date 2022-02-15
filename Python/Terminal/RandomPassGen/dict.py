import string
import random

letter_list = list(string.ascii_letters)

lowercase_letter_list = list(string.ascii_lowercase)
uppercase_letter_list = list(string.ascii_uppercase)

digit_list = list(string.digits)

symbol_list = [
'§', '%', '=', '/', '(', ')','|', 'Ä', '€', '÷', '×', 'ä', 'đ', '[', ']', 'ł', 'Ł', '$',
'ß', '¤', '<', '>', '#', '&', '@', '{', '}', ';', ':', ',', '.', '-', '_', '˘', '~', '^']

random.shuffle(lowercase_letter_list)
random.shuffle(uppercase_letter_list)
random.shuffle(symbol_list)
random.shuffle(digit_list)
random.shuffle(letter_list)