import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from GPT_Model.TransformerBlock import GPT

# Include the classes you defined before (MultiHeadAttention, TransformerBlock, PositionalEncoding, GPT)
# Add the definitions of these classes here...

# Set up the device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Sample text data
data = "This is a sample text for training the GPT model. It should be much larger in practice."
# Tokenization and vocabulary creation
tokenized_data = data.split()  # Basic tokenization by splitting on spaces
vocab = set(tokenized_data)  # Unique words
word_to_idx = {word: idx for idx, word in enumerate(vocab)}  # Mapping from words to indices
idx_to_word = {idx: word for word, idx in word_to_idx.items()}  # Reverse mapping

# Convert text to numerical indices
data_indices = [word_to_idx[word] for word in tokenized_data]


def create_batches(data, seq_length, batch_size):
    for i in range(0, len(data) - seq_length, batch_size):
        x = data[i:i + seq_length]
        y = data[i + 1:i + seq_length + 1]
        yield torch.tensor(x).to(device), torch.tensor(y).to(device)


seq_length = 5  # Length of each input sequence
batch_size = 2  # Number of sequences per batch


vocab_size = len(vocab)  # Size of your vocabulary
embed_size = 512         # Size of the embedding vector
num_layers = 6           # Number of Transformer blocks
heads = 8                # Number of attention heads
forward_expansion = 4    # Expansion factor in the feedforward layer
dropout = 0.1            # Dropout rate
max_length = seq_length  # Maximum sequence length

model = GPT(
    vocab_size=vocab_size,
    embed_size=embed_size,
    num_layers=num_layers,
    heads=heads,
    device=device,
    forward_expansion=forward_expansion,
    dropout=dropout,
    max_length=max_length
).to(device)

# modelV1.py

from GPT_Model.TransformerBlock import GPT  # Trying to import GPT

# Sample data and other code here
data_indices = [...]  # Your data
seq_length = 5
batch_size = 2
word_to_idx = {...}   # Your vocabulary mapping
idx_to_word = {...}   # Reverse mapping
