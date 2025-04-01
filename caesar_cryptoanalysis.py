import collections
import string

def caesar_cipher(text, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(table)

def frequency_analysis(text):
    text = text.lower()
    letter_counts = collections.Counter(c for c in text if c in string.ascii_lowercase)
    total_letters = sum(letter_counts.values())
    frequencies = {letter: count / total_letters * 100 for letter, count in letter_counts.items()}
    return frequencies

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Крок 1: Шифрування тексту
original_text = "The quick brown fox jumps over the lazy dog."
shift_value = 3
ciphered_text = caesar_cipher(original_text, shift_value)
print("Зашифрований текст:", ciphered_text)

# Крок 2: Частотний аналіз
frequencies = frequency_analysis(ciphered_text)
print("Частотний аналіз:", frequencies)

# Крок 3: Розшифрування
for shift in range(1, 26):
    decrypted_text = caesar_decipher(ciphered_text, shift)
    print(f"Зсув {shift}: {decrypted_text}")