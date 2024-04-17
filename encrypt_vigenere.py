def encrypt(letter, key, alphabet):
    index = (alphabet.index(letter) + key) % len(alphabet)
    new_letter = alphabet[index]
        
    return new_letter


def get_index(letter, alphabet):
    index = alphabet.index(letter)
    return index


alphabet_eng = "abcdefghijklmnopqrstuvwxyz"
alphabet_ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

index = 0
def encrypt_vizhynr(text, alphabet, key_word, output_file):
    encrypt_text = ""

    global index
    for letter in text:
        if letter.isupper():
            letter = letter.lower()
        
        if letter not in alphabet:
            continue
        
        letter_of_key = key_word[index]
        
        index_of_key = get_index(letter_of_key, alphabet)
        encrypt_text += encrypt(letter, index_of_key, alphabet)
        index += 1
        if index >= len(key_word):
            index = 0
        
    output_file.write(encrypt_text)  


input_file_path = 'plaintext_2.txt'
output_file_path = 'encrypted_output_2.txt'

def main():
    
    while True:
        choice_leng = input("Choose the language (eng/укр): ")
        if choice_leng == 'eng':
            alphabet = alphabet_eng
            break
        elif choice_leng == 'укр':
            alphabet = alphabet_ukr
            break
        else:
            print("Incorrect data! Please try again!")
            
    try:
        key_word = str(input("Enter the key word --> "))
    except:
        raise ValueError
        
    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'a', encoding='utf-8') as output_file:
        for line in input_file:
            encrypt_vizhynr(line, alphabet, key_word, output_file)
    
if __name__ == "__main__":
    main()
    

