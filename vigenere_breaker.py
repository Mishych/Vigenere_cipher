from collections import Counter


def find_key_length(file, alphabet):
    # Find all occurrences of trigrams in the text and determine the distances between them
    trigrams = {}
    ciphertext = ""
    
    with open(file, 'r', encoding='utf-8') as output_file:
        for line in output_file:
            for letter in line:
                letter = letter.lower()
                if letter in alphabet:
                    ciphertext += letter
                
    for i in range(len(ciphertext) - 2):
        trigram = ciphertext[i:i+3]
        if trigram not in trigrams:
            trigrams[trigram] = []
        trigrams[trigram].append(i)
   
    # Find all possible distances between occurrences of each trigram
    distances = []
    n = 0
    for trigram, positions in trigrams.items():
        if len(positions) > 2:
            distances.append([])
            for i in range(len(positions) - 1):
                distance = positions[i+1] - positions[0]
                distances[n].append(distance)
            n += 1
            
    return distances


def find_gcd(numbers):
    # Function to find the greatest common divisor for two numbers
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Find the greatest common divisor for the first two numbers
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result


def column_entry(key, file, alphabet):
    """
    Divides the ciphertext into columns and returns them in table form.
    """
    table = [[] for _ in range(key)]
    n = 0
    
    with open(file, 'r', encoding='utf-8') as output_file:
        for line in output_file:
            for letter in line:
                letter = letter.lower()  # Convert to lowercase
                if letter in alphabet:
                    table[n % key].append(letter)
                    n += 1
    print(len(table))
    return table


def find_most_common_letters(key, table):
    """
    Finds the most common letters in each column of the ciphertext.
    """
    most_common_letters = []
    for letters_list in table:
        letter_counter = Counter(letters_list)
        most_common = letter_counter.most_common(6)
        most_common_letters.append(most_common)
    return most_common_letters


def decrypt_table(alphabet, most_common_letters):
    """
    Decrypts the table of letters of the keyword.
    """
    key_length = len(most_common_letters)
    decr_table = [[] for _ in range(key_length)]
    if alphabet == "abcdefghijklmnopqrstuvwxyz":
        popular_letter = 4
    elif alphabet == "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя":
        popular_letter = 15 
        
    
    for col, common_letters in enumerate(most_common_letters):
        for letter, _ in common_letters:
            index = (alphabet.index(letter) - popular_letter) % len(alphabet)
            decr_table[col].append(alphabet[index])
    return decr_table


def print_results(most_common_letters, decrypted_table):
    """
    Prints the results.
    """
    print("\nMost frequently occurring letters in each column of the ciphertext:")
    for i, common_letters in enumerate(most_common_letters, start=1):
        print(f"List {i}: {common_letters}")

    print("\nDetermination of keyword letters:")   
    for col, letters in enumerate(decrypted_table):
        print(f"Col {col + 1}: {letters}")
        

def friedman_index(text):
    """
    Computes the index of coincidence of the text.
    """
    text_length = len(text)
    letter_freq = Counter(text)
    
    index = sum(n * (n - 1) for n in letter_freq.values()) / (text_length * (text_length - 1))
    
    return index

def find_vigenere_key_length(file, alphabet):
    """
    Finds the length of the Vigenere cipher key using the Friedman method.
    """
    ciphertext = ""
    
    with open(file, 'r', encoding='utf-8') as output_file:
        for line in output_file:
            for letter in line:
                letter = letter.lower()
                if letter in alphabet:
                    ciphertext += letter
    
    max_key_length = 15  # Maximum possible key length
    
    index_values = []
    for key_length in range(1, max_key_length + 1):
        chunks = [ciphertext[i::key_length] for i in range(key_length)]
        avg_index = sum(friedman_index(chunk) for chunk in chunks) / key_length
        index_values.append((key_length, avg_index))
    
    # Find the key length with the highest index of coincidence
    most_likely_key_length = max(index_values, key=lambda x: x[1])[0]
    
    return most_likely_key_length


def main():
    
    alphabet_eng = "abcdefghijklmnopqrstuvwxyz"
    alphabet_ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    file = 'encrypted_output_2.txt'
    
    while True:
        choice_lang = input("Choose the language (eng/укр): ")
        if choice_lang == 'eng':
            alphabet = alphabet_eng
            break
        elif choice_lang == 'укр':
            alphabet = alphabet_ukr
            break
        else:
            print("Incorrect data! Please try again!")
      
    key_lengths = find_key_length(file, alphabet)
    gcd_values = []
    
    for i in key_lengths:
        gcd = find_gcd(i)
        if gcd not in gcd_values:
            gcd_values.append(gcd)
            
    print("Possible keys using the Kasiski method:")
    print(", ".join(map(str, gcd_values)))
    
    print('Using the Friedman method:')
    print(find_vigenere_key_length(file, alphabet))
    
    key = int(input("Enter one of the possible keys from the list --> "))

    table = column_entry(key, file, alphabet)
    most_common_letters = find_most_common_letters(key, table)
    decrypted_table = decrypt_table(alphabet, most_common_letters)

    print_results(most_common_letters, decrypted_table)

if __name__ == "__main__":
    main()
