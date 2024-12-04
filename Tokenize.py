import random
import re
from collections import defaultdict

def tokenize_text(text):
    """Tokenizes text into words while preserving punctuation."""
    return re.findall(r"[\w']+|[.,!?;]", text)

def build_word_graph(tokens):
    """Builds a word graph from a list of tokens."""
    word_graph = defaultdict(dict)
    prev_word = None
    for token in tokens:
        if prev_word is not None:
            if token in word_graph[prev_word]:
                word_graph[prev_word][token] += 1
            else:
                word_graph[prev_word][token] = 1
        prev_word = token
    # Convert counts to probabilities
    for word, next_words in word_graph.items():
        total_count = sum(next_words.values())
        for next_word, count in next_words.items():
            word_graph[word][next_word] = count / total_count
    return word_graph

def generate_sentence(word_graph, start_word=None):
    """Generates a sentence using the word graph."""
    if start_word is None:
        current_word = random.choice(list(word_graph.keys()))
    else:
        current_word = start_word
    sentence = [current_word]
    while current_word != '.':
        next_words = list(word_graph[current_word].keys())
        probabilities = list(word_graph[current_word].values())
        current_word = random.choices(next_words, probabilities)[0]
        sentence.append(current_word)
    return ' '.join(sentence)

# Example usage
text = "This is a sample text. It contains punctuation, such as commas, periods, and question marks."
tokens = tokenize_text(text)
word_graph = build_word_graph(tokens)
print("Generated sentence:", generate_sentence(word_graph))
