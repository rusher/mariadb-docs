# Performance Tuning

## Chunking Strategy Selection

The choice of chunking strategy significantly impacts retrieval quality. Available strategies include:

- **Fixed Size**: Simple character-based chunking with fixed size
- **Sentence**: Chunks based on sentence boundaries
- **Paragraph**: Chunks based on paragraph boundaries
- **Recursive**: Hierarchical chunking that preserves document structure
- **Semantic**: AI-powered chunking based on content meaning

For most use cases, the recursive strategy provides a good balance between performance and quality.
