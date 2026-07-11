from chonkie import RecursiveChunker

chunker = RecursiveChunker()

chunks = chunker("chonkie is the goodest boi! My favorite chunking hippo hehe.")

for chunk in chunks:
    print(f"Chunk: {chunk.text}")
    print(f"Tokens: {chunk.token_count}")
