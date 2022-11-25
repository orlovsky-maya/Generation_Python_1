def decryption(text_to_decrypt, alphabet_lower, alphabet_upper, step, number_of_characters):
    decrypted_text = ''
    for symbol_open in text_to_decrypt:
        if str(symbol_open).isalpha():
            if str(symbol_open).islower():
                index_of_symbol_open = alphabet_lower.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open - step) % number_of_characters
                decrypted_text += alphabet_lower[index_of_symbol_encrypted]
            if str(symbol_open).isupper():
                index_of_symbol_open = alphabet_upper.find(str(symbol_open))
                index_of_symbol_encrypted = (index_of_symbol_open - step) % number_of_characters
                decrypted_text += alphabet_upper[index_of_symbol_encrypted]
        else:
            decrypted_text += symbol_open
    return decrypted_text


alphabet_lower_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number_of_characters_en = 26

text_to_decrypt_en = input()
for shift_step in range(26):
    decrypted_text_en = decryption(text_to_decrypt_en, alphabet_lower_en, alphabet_upper_en, shift_step,
                                   number_of_characters_en)
    print(decrypted_text_en)
