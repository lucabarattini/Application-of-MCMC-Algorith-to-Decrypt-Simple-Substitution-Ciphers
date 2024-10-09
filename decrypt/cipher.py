import string
import random
from operator import itemgetter
from decrypt import loadfile as lf

def create_original_cipher(plaintext_filepath, encrypted_filepath):

    """
    Create an estimated mapping between encrypted letters and
    plaintext letters by comparing the frequencies in the
    reference corpus and cipher text.
    
    Parameters
    ----------
    plaintext_filepath : str
        the filepath of the reference corpus
    encrypted_filepath : str 
        the filepath of the cipher text that need to be decrypted
    """

    sample_plaintext = lf._readfile(plaintext_filepath)
    encrypted_text = lf._readfile(encrypted_filepath)
    
    def _count_letter_frequencies(text):

        """
        Create a dictionary of letters A-Z and count the frequency
        of each in the supplied text. it return a list sorted by frequency.

        Parameters
        ----------
        text : str
            the text used to perform the frequency analysis on
        """

        frequencies = {}

        for asciicode in range(65, 91):
            frequencies[chr(asciicode)] = 0

        for letter in text:
            asciicode = ord(letter.upper())
            if asciicode >= 65 and asciicode <= 90:
                frequencies[chr(asciicode)] += 1

        sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

        return sorted_by_frequency
    
    sample_plaintext_frequencies = _count_letter_frequencies(sample_plaintext)
    encrypted_text_frequencies = _count_letter_frequencies(encrypted_text)

    decryption_dict = {}
    for i in range(0, 26):
        decryption_dict[encrypted_text_frequencies[i][0]] = sample_plaintext_frequencies[i][0].lower()

    sorted_dict = {key: decryption_dict[key] for key in sorted(decryption_dict)}
    cipher = ''.join(sorted_dict.values())

    return cipher

def generate_cipher(cipher=None):
    '''
    This function generate a proposed cipher from a given cipher by swapping two letters randomly choosen.
    If no cipher is passed the function first generate a random cipher and then swap two random letters.
    Parameters
    ----------
    cipher : str
        a 26 character-long string 
    '''
    if cipher is None:
        # Generate a random cipher of 26 lowercase letters
        cipher = ''.join(random.sample(string.ascii_lowercase, 26))
    
    pos1 = random.randint(0, len(list(cipher))-1)
    pos2 = random.randint(0, len(list(cipher))-1)
    if pos1 == pos2:
        return generate_cipher(cipher)
    else:
        cipher = list(cipher)
        pos1_alpha = cipher[pos1]
        pos2_alpha = cipher[pos2]
        cipher[pos1] = pos2_alpha
        cipher[pos2] = pos1_alpha
        return "".join(cipher)

def apply_cipher(text, cipher):
    '''
    this function apply the given cipher to a given text

    Parameters
    ----------
    text : str
        The text to which the cipher is applied
    cipher : str
        a 26 character-long string used to encrypt/decrypt the text
    '''
    alphabet = string.ascii_lowercase
    reverse_cipher_dict = {cipher[i]: alphabet[i] for i in range(len(alphabet))}

    # Function to decrypt each character
    def decrypt_char(char):
        if char.isalpha():  # Check if the character is a letter
            # Decrypt and preserve the case (upper/lower)
            decrypted_char = reverse_cipher_dict[char.lower()]
            return decrypted_char.upper() if char