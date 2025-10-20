# Orchestration

## Overview

The orchestration module provides high-level endpoints that coordinate multiple steps of the RAG (Retrieval Augmented Generation) workflow. These endpoints simplify integration by handling complex workflows in a single request.

## Orchestration Endpoints

### Ingestion Orchestration

```
POST /orchestrate/ingestion
```

**Purpose**: Orchestrates the complete ingestion workflow: document upload, processing, and chunking.

**Request body**:
```json
{
  "file_paths": ["/path/to/document1.pdf", "/path/to/document2.docx"],
  "chunking_config": {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "chunking_strategy": "recursive",
    "metadata_fields": ["title", "author", "date"]
  },
  "wait_for_completion": true,
  "timeout_seconds": 300
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
  "processing_time_ms": 15000
}
```

**Usage Example**: Use this endpoint when you need to ingest documents and prepare them for retrieval.

```bash
curl -X POST "http://localhost:8000/orchestrate/ingestion" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"file_paths": ["/path/to/document1.pdf", "/path/to/document2.docx"], "wait_for_completion": true}'
```

### Generation Orchestration

```
POST /orchestrate/generation
```

**Purpose**: Orchestrates the generation workflow: retrieval and text generation.

**Request body**:
```json
{
  "query": "What are the key features?",
  "retrieval_config": {
    "top_k": 5,
    "filter": {
      "document_ids": [42, 43],
      "metadata_filter": {"author": "John Doe"}
    }
  },
  "generation_config": {
    "llm_provider": "openai",
    "llm_model": "gpt-4",
    "temperature": 0.25,
    "max_tokens": 1000,
    "system_prompt": "You are a helpful assistant."
  }
}
```

**Response**:
```json
{
  "retrieval_results": [
    {"chunk_id": 101, "similarity_score": 0.92, "content": "...", "metadata": {"title": "Features Document"}}
  ],
  "generated_response": "The key features include...",
  "processing_time_ms": 2500
}
```

**Usage Example**: Use this endpoint when you want to query existing documents.

```bash
curl -X POST "http://localhost:8000/orchestrate/generation" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the key features?", "retrieval_config": {"top_k": 5}}'
```

### Streaming Generation Orchestration

```
POST /orchestrate/generation/stream
```

**Purpose**: Same as the generation endpoint but returns the response as a stream.

**Request body**: Same as the generation endpoint.

**Response**: Server-sent events stream with the generated text.

**Usage Example**: Use this endpoint for real-time user interfaces.

```bash
curl -X POST "http://localhost:8000/orchestrate/generation/stream" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the key features?", "retrieval_config": {"top_k": 5}}'
```

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
  "wait_for_completion": true,
  "timeout_seconds": 300
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
  "generated_response": "The key features include...",
  "total_processing_time_ms": 15000
}
```

**Usage Example**: Use this endpoint for a complete end-to-end workflow when you have new documents and want to immediately query them.

```bash
curl -X POST "http://localhost:8000/orchestrate/pipeline" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"file_paths": ["/path/to/document1.pdf"], "query": "What are the key features?"}'
```
