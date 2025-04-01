import collections
import string
import re

def vigenere_cipher(text, key, decrypt=False):
    alphabet = string.ascii_lowercase
    key = key.lower()
    result = []
    key_index = 0
    
    for char in text:
        if char.lower() in alphabet:
            shift = alphabet.index(key[key_index])
            if decrypt:
                shift = -shift
            new_index = (alphabet.index(char.lower()) + shift) % 26
            new_char = alphabet[new_index]
            if char.isupper():
                new_char = new_char.upper()
            result.append(new_char)
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    
    return ''.join(result)

def frequency_analysis(text):
    text = text.lower()
    letter_counts = collections.Counter(c for c in text if c in string.ascii_lowercase)
    total_letters = sum(letter_counts.values())
    frequencies = {letter: count / total_letters * 100 for letter, count in letter_counts.items()}
    return frequencies

def kasiski_examination(text):
    text = re.sub(r'[^a-z]', '', text.lower())
    sequences = collections.defaultdict(list)
    
    for i in range(len(text) - 3):
        seq = text[i:i+3]
        for j in range(i + 3, len(text) - 3):
            if text[j:j+3] == seq:
                sequences[seq].append(j - i)
    
    distances = [dist for seq in sequences for dist in sequences[seq]]
    return collections.Counter(distances)

# Крок 1: Шифрування
original_text = "Vigenere cipher is stronger than Caesar cipher.Focusing on the overall system, rather than a single goal, is one of the core themes of this book. It is also one of the deeper meanings behind the word atomic. By now, you’ve probably realized that an atomic habit refers to a tiny change. "
key = "KEY"
ciphered_text = vigenere_cipher(original_text, key)
print("Зашифрований текст:", ciphered_text)

# Крок 2: Частотний аналіз
frequencies = frequency_analysis(ciphered_text)
print("Частотний аналіз:", frequencies)

# Крок 3: Визначення довжини ключа методом Касіскі
kasiski_result = kasiski_examination(ciphered_text)
print("Метод Касіскі - ймовірні довжини ключа:", kasiski_result)

# Крок 4: Розшифрування
decrypted_text = vigenere_cipher(ciphered_text, key, decrypt=True)
print("Розшифрований текст:", decrypted_text)
