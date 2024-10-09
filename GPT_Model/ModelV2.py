import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium" or "gpt2-large" for larger models
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()


# Function to generate a response from the model
def generate_response(prompt, max_length=100):
    # Encode the prompt and convert to tensor
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text
    with torch.no_grad():
        output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)

    # Decode the generated text and return
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


# Simple loop to interact with the model
if __name__ == "__main__":
    print("Welcome to the GPT-like chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("Type your question here : ")
        if user_input.lower() == 'exit':
            break
        response = generate_response(user_input)
        print("Bot:", response)
