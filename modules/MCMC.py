import random
import scoring_function
import cipher
import frequencyanalysis
import math

def should_accept(current_score, proposed_score, temperature):
    if proposed_score > current_score:
        return True
    else:
        accept_probability = math.exp((proposed_score - current_score) / temperature)
        return random.random() < accept_probability


def mcmc_decrypt(num_iterations, cipher_text, corpus_text, outputfile_cipher, outputfile_decryption):
    # Build the bigram model from the corpus
    bigram_frequencies = scoring_function.build_bigram_model(corpus_text)

    # Start with the initial cipher
    current_cipher = frequencyanalysis.create_original_cipher(corpus_text, cipher_text)
    current_decrypted_text = cipher.apply_cipher_on_text(cipher_text, current_cipher)
    current_score = scoring_function.score_text(current_decrypted_text, bigram_frequencies)

    initial_temperature = 1.0
    final_temperature = 0.01
    temperature = initial_temperature
    cooling_rate = 0.95

    for _ in range(num_iterations):
        # Generate a proposed cipher
        proposed_cipher = cipher.generate_cipher(current_cipher)

        # Decrypt the text using the proposed cipher
        proposed_decrypted_text = cipher.apply_cipher_on_text(cipher_text, proposed_cipher)
        proposed_score = scoring_function.score_text(proposed_decrypted_text, bigram_frequencies)

        # Determine if we should accept the proposed cipher
        if should_accept(current_score, proposed_score, temperature):
            current_cipher = proposed_cipher
            current_score = proposed_score

        temperature = max(final_temperature, temperature * cooling_rate)

    f = open(outputfile_cipher, "w")
    f.write(current_cipher)
    f.close()

    current_decryption = cipher.apply_cipher_on_text(cipher_text, current_cipher)

    f = open(outputfile_decryption, "w")
    f.write(current_decryption)
    f.close()
    
