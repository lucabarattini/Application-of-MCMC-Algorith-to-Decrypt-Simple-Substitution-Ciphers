import re
from collections import Counter
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def build_bigram_model(corpus_file):
    with open(corpus_file, 'r', encoding='utf-8') as file:
        text = file.read().upper()
    text = re.sub(r'[^A-Z]', '', text)
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    bigram_counts = Counter(bigrams)
    total_bigrams = sum(bigram_counts.values())
    bigram_frequencies = {bigram: count/total_bigrams for bigram, count in bigram_counts.items()}
    return bigram_frequencies

def score_text(decrypted_text, bigram_frequencies):
    text = decrypted_text.upper()
    text = re.sub(r'[^A-Z]', '', text)
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    bigram_counts = Counter(bigrams)
    score = 0
    for bigram, count in bigram_counts.items():
        if bigram in bigram_frequencies:
            score += bigram_frequencies[bigram] * count
    return score


def gpt_score(text):
    # Load pre-trained model and tokenizer
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    inputs = tokenizer.encode(text, return_tensors='pt')
    outputs = model(inputs, labels=inputs)
    loss = outputs.loss.item()

    return -loss  # Lower loss indicates better score