import tiktoken # type: ignore

enc = tiktoken.get_encoding("cl100k_base")   # OpenAI tokenizer

def split_text(text: str, max_tokens: int = 1000):
    words, chunk, length = text.split(), [], 0
    for w in words:
        w_tokens = len(enc.encode(w))
        if length + w_tokens > max_tokens:
            yield " ".join(chunk)
            chunk, length = [], 0
        chunk.append(w)
        length += w_tokens
    if chunk:
        yield " ".join(chunk)
