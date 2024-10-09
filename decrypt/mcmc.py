import random
import math
from tqdm import tqdm
from decrypt import score
from decrypt import cipher
from decrypt import loadfile as lf

def should_accept(current_score, proposed_score, temperature):
    '''
    The "should_accept" function is a function used in the MCMC that allow us to make the decision on either choosing the proposed cipher 
        or keeping the current cipher and go to the next iteration. The proposed cipher is accepted if either have an higher score than the current or,
          even if the score is lower, the accept_probability is higher than a random probability. This last step reflect the coin toss element of a MCMC. 
    
    Parameters
    ---------------
    current_score : float
    	score of the current cipher
    proposed_score : float
    	score of the proposed cipher
    temperature : float
    	used to control the exploration of the solution space. When the temperature is high the algorithm is more likely to accept changes even if they are 
        worse than the current solution. This is useful for exploring a wide range of possible solutions and avoiding getting stuck in local optima.
    '''
    if proposed_score > current_score:
        return True
    else:
        accept_probability = math.exp((proposed_score - current_score) / temperature)
        return random.random() < accept_probability

def mcmc_decrypt(num_iterations, cipher_text, corpus_text, n):
    '''
    This function implement a Markov Chain Monte Carlo algorithm to decrypt a substitution cipher. We start with a initial cipher,
     from it we generate a propose cipher by swapping two letters randomly, after that we decrypt our cipher text and score both ciphers. 
     The scores are used to decide which cipher need to be kept for the next iteration. 
     
    The function will return two txt files:
      - one txt with the final decryption
      - one txt with the final cipher 
    
    Parameters
    ---------------
    num_iterations : int
    	The number of iteration of the MCMC algorithm
    cipher_text : str
    	the path of the cipher text we want to decrypt
    corpus_text : str 
    	the path of the reference corpus used for un n-gram probability calculation
    n : int
    	is the n in n-gram, it decide how to structure our n-gram analysis (e.g., 2 : bigram or 3 : trigram, etc)
    '''
    # Build the bigram model from the corpus
    corpus = lf._readfile(corpus_text)
    n_gram_freq = score.compute_ngram_probabilities(corpus, n)

    current_cipher = cipher.create_original_cipher(corpus_text, cipher_text)
    current_decrypted_text = cipher.apply_cipher(cipher_text, current_cipher)
    current_score = score.log_likelihood(current_decrypted_text, n_gram_freq, n)
    
    initial_temperature = 1.0
    final_temperature = 0.01
    temperature = initial_temperature
    cooling_rate = 0.95

    for _ in tqdm(range(num_iterations)):
        # Generate a proposed cipher
        proposed_cipher = cipher.generate_cipher(current_cipher)

        # Decrypt the text using the proposed cipher
        proposed_decrypted_text = cipher.apply_cipher(cipher_text, proposed_cipher)
        proposed_score = score.log_likelihood(proposed_decrypted_text, n_gram_freq, n)

        # Determine if we should accept the proposed cipher
        if should_accept(current_score, proposed_score, temperature):
            current_cipher = proposed_cipher
            current_score = proposed_score

        temperature = max(final_temperature, temperature * cooling_rate)
    
    current_decryption = cipher.apply_cipher(cipher_text, current_cipher)

    f = open("final_de