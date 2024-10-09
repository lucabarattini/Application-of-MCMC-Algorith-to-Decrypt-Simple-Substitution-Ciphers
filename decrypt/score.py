from collections import defaultdict
import math

def compute_ngram_probabilities(text, n):
    '''
    This function return a dictionary containing the n-gram probabilities of a given text

    Parameters
    ----------
    text : str
        A reference text used to compute the n-gram probabilities that will be used in the scoring function
    n : int
        the value of in n-gram to specify what kind of n-gram we want to use in our analysis (e.g., n=2 -> bigram)
    '''
    ngrams = defaultdict(int)
    for i in range(len(text) - n + 1):
        ngram = text[i:i+n]
        ngrams[ngram] += 1

    total_ngrams = sum(ngrams.values())
    return {ngram: count / total_ngrams for ngram, count in ngrams.items()}

def log_likelihood(text, ngram_probs, n):
    '''
    This function sums together the log likelihood of each n-grams in a given text. 
    it return a score based on how likely it is to observe the given text if the current substitution cipher were correct.

    Parameters
    ----------
    text : str
        Decrypted text to be scored
    ngram_prob : dict
        The reference ngram probabilities dictionary retuned by the function "compute_ngram_probability"
    n : int
        The n in n-gram we have used to analyze and compute the probabilities in our reference text
    '''
    likelihood = 0
    for i in range(len(text) - n + 1):
        ngram = text[i:i+n]
        likelihood += math.log(ngram_probs.get(ngram, 1e-8))
    return likelihood
