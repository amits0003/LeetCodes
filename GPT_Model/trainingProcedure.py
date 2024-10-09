import torch
import torch.optim as optim
from torch import nn

from GPT_Model.TransformerBlock import GPT

# Initialize model, optimizer, loss function, etc.
model = GPT(
    vocab_size=50257,
    embed_size=512,
    num_layers=6,
    heads=8,
    device="cuda" if torch.cuda.is_available() else "cpu",
    forward_expansion=4,
    dropout=0.1,
    max_length=512
).to("cuda")

optimizer = optim.Adam(model.parameters(), lr=3e-4)
criterion = nn.CrossEntropyLoss()


def train_step(data, target, model, optimizer):
    model.train()
    optimizer.zero_grad()

    # Mask the future tokens (causal mask)
    mask = torch.tril(torch.ones((target.size(1), target.size(1)))).to("cuda")

    output = model(data, mask)
    loss = criterion(output.view(-1, output.size(-1)), target.view(-1))
    loss.backward()
    optimizer.step()

    return loss.item()
