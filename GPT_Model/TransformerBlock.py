import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from GPT_Model.modelV1 import seq_length, batch_size, word_to_idx, idx_to_word, \
    device, create_batches
from GPT_Model.trainingProcedure import train_step, model


class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size
        self.heads = heads
        self.head_dim = embed_size // heads

        assert self.head_dim * heads == embed_size, "Embedding size needs to be divisible by heads"

        self.values = nn.Linear(self.head_dim, embed_size, bias=False)
        self.keys = nn.Linear(self.head_dim, embed_size, bias=False)
        self.queries = nn.Linear(self.head_dim, embed_size, bias=False)
        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, values, keys, query, mask):
        N = query.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        # Split the embedding into multiple heads for multi-head attention
        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = query.reshape(N, query_len, self.heads, self.head_dim)

        # Scaled dot-product attention
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))

        attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(N, query_len, self.embed_size)

        return self.fc_out(out)


class TransformerBlock(nn.Module):
    def __init__(self, embed_size, heads, dropout, forward_expansion):
        super(TransformerBlock, self).__init__()
        self.attention = MultiHeadAttention(embed_size, heads)
        self.norm1 = nn.LayerNorm(embed_size)
        self.norm2 = nn.LayerNorm(embed_size)

        self.feed_forward = nn.Sequential(
            nn.Linear(embed_size, forward_expansion * embed_size),
            nn.ReLU(),
            nn.Linear(forward_expansion * embed_size, embed_size),
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, value, key, query, mask):
        attention = self.attention(value, key, query, mask)
        x = self.dropout(self.norm1(attention + query))
        forward = self.feed_forward(x)
        out = self.dropout(self.norm2(forward + x))
        return out


class PositionalEncoding(nn.Module):
    def __init__(self, embed_size, max_len):
        super(PositionalEncoding, self).__init__()
        self.encoding = torch.zeros(max_len, embed_size)
        self.encoding.requires_grad = False

        pos = torch.arange(0, max_len).unsqueeze(1).float()
        _2i = torch.arange(0, embed_size, 2).float()

        self.encoding[:, 0::2] = torch.sin(pos / (10000 ** (_2i / embed_size)))
        self.encoding[:, 1::2] = torch.cos(pos / (10000 ** (_2i / embed_size)))

    def forward(self, x):
        return x + self.encoding[:x.size(1), :].to(x.device)


class GPT(nn.Module):
    def __init__(self, vocab_size, embed_size, num_layers, heads, device, forward_expansion, dropout, max_length):
        super(GPT, self).__init__()
        self.embed_size = embed_size
        self.device = device
        self.word_embedding = nn.Embedding(vocab_size, embed_size)
        self.position_embedding = PositionalEncoding(embed_size, max_length)

        self.layers = nn.ModuleList(
            [TransformerBlock(embed_size, heads, dropout, forward_expansion) for _ in range(num_layers)]
        )

        self.fc_out = nn.Linear(embed_size, vocab_size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask):
        N, seq_length = x.shape
        positions = torch.arange(0, seq_length).expand(N, seq_length).to(self.device)
        out = self.dropout(self.word_embedding(x) + self.position_embedding(positions))

        for layer in self.layers:
            out = layer(out, out, out, mask)

        logits = self.fc_out(out)
        return logits


optimizer = optim.Adam(model.parameters(), lr=3e-4)
criterion = nn.CrossEntropyLoss()

# Training loop
num_epochs = 10  # Number of epochs
for epoch in range(num_epochs):
    total_loss = 0
    for x, y in create_batches(data_indices, seq_length, batch_size):
        loss = train_step(x, y, model, optimizer)
        total_loss += loss

    print(f"Epoch {epoch + 1}, Loss: {total_loss / (len(data_indices) // batch_size)}")


def generate_text(model, start_text, word_to_idx, idx_to_word, num_words=50):
    model.eval()
    words = start_text.split()
    input_sequence = torch.tensor([word_to_idx[word] for word in words]).unsqueeze(0).to(device)

    for _ in range(num_words):
        with torch.no_grad():
            output = model(input_sequence, mask=None)  # Adjust mask for your implementation
            next_word_logits = output[:, -1, :]
            next_word_idx = torch.argmax(next_word_logits, dim=-1).item()
            words.append(idx_to_word[next_word_idx])
            input_sequence = torch.cat((input_sequence, torch.tensor([[next_word_idx]]).to(device)), dim=1)

    return ' '.join(words)


# Generate text
print(generate_text(model, "This is", word_to_idx, idx_to_word))


def get_data_indices():
    from GPT_Model.modelV1 import data_indices  # Moved inside function to avoid circular import
    return data_indices
