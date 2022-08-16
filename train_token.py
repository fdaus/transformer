from pathlib import Path

from tokenizers import ByteLevelBPETokenizer

paths = [str(x) for x in Path("./").glob("**/*.csv")]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
    "TLS",
    "HTTP",
    "DNS",
])

# Save files to disk
tokenizer.save_model(".", "sampletoken")