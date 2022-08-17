from pathlib import Path

from tokenizers import ByteLevelBPETokenizer

#paths = [str(x) for x in Path("./").glob("**/*.csv")]
paths = [str(x) for x in Path("/mnt/c/Users/iotfs/OneDrive - Universiti Malaya/dataset/Dataset_csv/unsw/nfstream/corpus/").glob("**/*.csv")]

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

# Save files to disk
tokenizer.save_model("./models/", "sampletoken")