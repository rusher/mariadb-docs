# Orchestration

## Orchestration Endpoints

### Full Pipeline

```
POST /orchestrate/pipeline
```

**Purpose**: Executes the complete RAG pipeline in a single request: document ingestion, chunking, retrieval, and generation.

**Request body**:
```json
{
  "file_paths": ["/path/to/document1.pdf", "/path/to/document2.docx"],
  "query": "What are the key features?",
  "chunking_config": {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "chunking_strategy": "recursive"
  },
  "retrieval_config": {
    "top_k": 5
  },
  "generation_config": {
    "llm_provider": "openai",
    "llm_model": "gpt-4",
    "temperature": 0.25,
    "max_tokens": 1000
  },
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Response**:
```json
{
  "documents": [
    {"id": 42, "filename": "document1.pdf", "status": "completed"},
    {"id": 43, "filename": "document2.docx", "status": "completed"}
  ],
  "chunks_created": 25,
  "retrieval_results": [
    {"chunk_id": 101, "similarity_score": 0.92, "content": "..."}
  ],
  "generated_response": "The key features of MariaDB Data Bridge include...",
  "total_processing_time_ms": 15000,
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Usage Example**: Use this endpoint for a complete end-to-end workflow when you have new documents and want to immediately query them. This is particularly useful for integration with other systems or for batch processing.

```bash
curl -X POST "http://localhost:8000/orchestrate/pipeline" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"file_paths": ["/path/to/document1.pdf", "/path/to/document2.docx"], "query": "What are the key features?", "authorized_users": ["user1@example.com"]}'
```
