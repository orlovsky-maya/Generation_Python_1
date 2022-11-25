def encrypting(text, alphabet_lower, alphabet_upper, step, number_of_characters):
    encrypt_text = ''
    for symbol_open in text:
        if str(symbol_open).isalpha():
            if str(symbol_open).islower():
                index_of_symbol_open = alphabet_lower.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open + step) % number_of_characters
                encrypt_text += alphabet_lower[index_of_symbol_encrypted]
            if str(symbol_open).isupper():
                index_of_symbol_open = alphabet_upper.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open + step) % number_of_characters
                encrypt_text += alphabet_upper[index_of_symbol_encrypted]
        else:
            encrypt_text += symbol_open
    return encrypt_text


alphabet_lower_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number_of_characters_en = 26

text_to_encrypt = input().split()
encrypted_text = []

for word_to_encrypt in text_to_encrypt:
    counter_of_letter = 0
    if word_to_encrypt.isalpha():
        encrypted_word = encrypting(word_to_encrypt, alphabet_lower_en, alphabet_upper_en, len(word_to_encrypt),
                                    number_of_characters_en)
        encrypted_text.append(encrypted_word)
    else:
        for symbol in word_to_encrypt:
            if symbol.isalpha():
                counter_of_letter += 1
        encrypted_word = encrypting(word_to_encrypt, alphabet_lower_en, alphabet_upper_en, counter_of_letter,
                                    number_of_characters_en)
        encrypted_text.append(encrypted_word)

print(*encrypted_text)
