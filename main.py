from importlib.metadata import version
import tiktoken

import torch

print("TikToken version:", tiktoken.__version__)
print("PyTorch version:", torch.__version__)

# Test TikToken
encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode("Hello from Python and Docker!")

print("Tokens:", tokens)

# Test PyTorch
tensor = torch.tensor([1, 2, 3])
print("Tensor:", tensor)


print("tiktoken version:", version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

text = (
            "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
            "of someunknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})

print(integers)


print('hello')
