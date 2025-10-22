# API Reference

MariaDB AI RAG exposes a comprehensive RESTful API for programmatic interaction with the system. All API endpoints require authentication except for the login endpoint.

## Authentication Endpoints

### Login

```
POST /token
```

**Purpose**: Authenticates a user and provides a JWT token for subsequent API calls.

**Request body**:

```json
{
  "username": "user@example.com",
  "password": "secure_password"
}
```

**Response**:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Usage Example**: Authentication should be performed before any other API calls. The returned JWT token must be included in the Authorization header of subsequent requests:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Document Management Endpoints

### Upload Documents

```
POST /documents/ingest
```

**Purpose**: Uploads and processes one or more documents for ingestion into the system. Documents are processed asynchronously in the background.

**Request**: `multipart/form-data` with one or more file attachments

**Request Parameters**:

* `files`: One or more files to upload (required)

**Response**:

```json
{
  "message": "2 documents have been queued for ingestion.",
  "documents": [
    {
      "id": 42,
      "source": "/uploaded_files/example1.pdf",
      "filename": "example1.pdf",
      "status": "pending",
      "content": null,
      "error_message": null,
      "created_at": "2025-10-20T12:00:00.123456",
      "updated_at": null
    },
    {
      "id": 43,
      "source": "/uploaded_files/example2.docx",
      "filename": "example2.docx",
      "status": "pending",
      "content": null,
      "error_message": null,
      "created_at": "2025-10-20T12:00:00.234567",
      "updated_at": null
    }
  ]
}
```

**Status Values**:

* `pending`: Document is queued for processing
* `completed`: Document has been successfully processed
* `failed`: Document processing failed (check `error_message`)

**Usage Example**: Upload one or more documents for ingestion.

```bash
# Upload single document
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document.pdf"

# Upload multiple documents
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document1.pdf" \
  -F "files=@/path/to/document2.docx"
```

**Note**: The endpoint accepts both single and multiple files. Documents are processed asynchronously, so the initial status will be `pending`. Use the document ID to check processing status later.

### List Documents

```
GET /documents
```

**Purpose**: Retrieves a paginated list of all documents uploaded by the authenticated user.

**Parameters**:

* `skip` (optional): Number of records to skip for pagination (default: 0)
* `limit` (optional): Maximum number of records to return (default: 100)

**Response**:

```json
{
  "documents": [
    {
      "id": 42,
      "filename": "example.pdf",
      "content_type": "application/pdf",
      "size": 1048576,
      "status": "completed",
      "created_at": "2025-08-25T11:42:00.123456",
      "updated_at": "2025-08-25T11:43:30.123456",
      "chunk_count": 15
    },
    {...}
  ],
  "total_count": 42,
  "page": 1,
  "pages": 5
}
```

**Usage Example**: Use this endpoint to monitor all documents in the system, check their processing status, or select documents for further operations.

```bash
curl "http://localhost:8000/documents?skip=0&limit=10" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Retrieve Document

```
GET /documents/{document_id}
```

**Purpose**: Retrieves detailed information about a specific document.

**Response**:

```json
{
  "id": 42,
  "filename": "example.pdf",
  "content_type": "application/pdf",
  "size": 1048576,
  "status": "completed",
  "created_at": "2025-08-25T11:42:00.123456",
  "updated_at": "2025-08-25T11:43:30.123456",
  "chunk_count": 15,
  "metadata": {
    "page_count": 10,
    "author": "John Doe",
    "creation_date": "2025-08-20"
  }
}
```

**Usage Example**: Use this endpoint to check the status of a specific document or retrieve its metadata.

```bash
curl "http://localhost:8000/documents/42" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Delete Documents

```
DELETE /documents
```

**Purpose**: Deletes multiple documents and their associated chunks and vector embeddings.

**Request body**:

```json
{
  "document_ids": [42, 43, 44]
}
```

**Response**:

```json
{
  "deleted_count": 3,
  "status": "success"
}
```

**Usage Example**: Use this endpoint to remove documents that are no longer needed, freeing up storage space and improving search performance.

```bash
curl -X DELETE "http://localhost:8000/documents" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_ids": [42, 43, 44]}'
```

## Chunking Endpoints

### Chunk Documents (Batch)

```
POST /chunk
```

**Purpose**: Processes multiple documents into chunks and creates vector embeddings for semantic search. Documents are processed asynchronously in the background.

**Request body**:

```json
{
  "document_ids": [42, 43, 44],
  "chunking_method": "recursive",
  "chunk_size": 512,
  "chunk_overlap": 128,
  "threshold": 0.8
}
```

**Chunking Methods**:

* `recursive`: Recursive text splitting (default)
* `sentence`: Sentence-based chunking
* `token`: Token-based chunking
* `semantic`: Semantic similarity-based chunking (requires `threshold`)

**Response**:

```json
{
  "message": "Chunking task scheduled for 3 documents",
  "queued_documents": [42, 43, 44],
  "status": "success"
}
```

**Usage Example**: Use this endpoint after document ingestion to prepare documents for semantic search. The chunking process divides documents into semantically meaningful segments and creates vector embeddings.

```bash
curl -X POST "http://localhost:8000/chunk" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "document_ids": [42, 43],
    "chunking_method": "semantic",
    "chunk_size": 512,
    "chunk_overlap": 128,
    "threshold": 0.8
  }'
```

**Note**: For semantic chunking, the `threshold` parameter controls how similar adjacent chunks should be before they are merged.

### Chunk All Documents

```
POST /chunk/all
```

**Purpose**: Processes all documents in the system into chunks. Useful for batch processing or reprocessing all documents with new chunking parameters.

**Request body**:

```json
{
  "chunking_method": "recursive",
  "chunk_size": 512,
  "chunk_overlap": 128,
  "threshold": 0.8
}
```

**Response**:

```json
{
  "message": "Chunking task scheduled for all documents",
  "queued_documents": [42, 43, 44, 45, 46],
  "status": "success"
}
```

**Usage Example**: Use this endpoint to reprocess all documents with new chunking settings.

```bash
curl -X POST "http://localhost:8000/chunk/all" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "chunking_method": "recursive",
    "chunk_size": 512,
    "chunk_overlap": 128
  }'
```

### Filter/Retrieve Chunks

```
POST /chunks/filter
```

**Purpose**: Retrieves chunks for specific documents. Use this to check if chunking has completed or to retrieve chunk data.

**Request body**:

```json
{
  "document_ids": [42, 43]
}
```

**Response**: Array of chunk objects

```json
[
  {
    "id": "uuid-string",
    "document_id": 42,
    "chunk_text": "This is the content of the first chunk...",
    "chunk_index": 0,
    "embedding": [0.123, 0.456, ...],
    "metadata": {}
  },
  {
    "id": "uuid-string-2",
    "document_id": 42,
    "chunk_text": "This is the content of the second chunk...",
    "chunk_index": 1,
    "embedding": [0.789, 0.012, ...],
    "metadata": {}
  }
]
```

**Usage Example**: Check if documents have been chunked and retrieve their chunks.

```bash
curl -X POST "http://localhost:8000/chunks/filter" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_ids": [42, 43]}'
```

## Retrieval and Search Endpoints

### Semantic Retrieval

```
POST /retrieve
```

**Purpose**: Performs semantic search to retrieve relevant document chunks based on a query using vector similarity.

**Request body**:

```json
{
  "query": "What is MariaDB AI RAG?",
  "top_k": 20,
  "document_ids": [42, 43]
}
```

**Request Parameters**:

* `query` (required): The search query
* `top_k` (optional): Number of results to return (default: 20)
* `document_ids` (optional): Filter results to specific document IDs (default: all documents)

**Response**: Array of retrieval results

```json
[
  {
    "id": "uuid-chunk-id",
    "document_id": 42,
    "content": "MariaDB AI RAG is an enterprise-grade RAG solution...",
    "metadata": {},
    "distance": 0.15
  },
  {
    "id": "uuid-chunk-id-2",
    "document_id": 43,
    "content": "Key features include document processing and semantic search...",
    "metadata": {},
    "distance": 0.23
  }
]
```

**Response Fields**:

* `id`: Unique chunk identifier
* `document_id`: ID of the source document
* `content`: The chunk text content
* `metadata`: Additional metadata about the chunk
* `distance`: Vector distance (lower = more similar)

**Usage Example**: Use this endpoint to find semantically relevant information. The system converts your query into a vector embedding and finds the most similar chunks.

```bash
curl -X POST "http://localhost:8000/retrieve" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is MariaDB AI RAG?",
    "top_k": 5,
    "document_ids": [42, 43]
  }'
```

### Full-Text Search

```
POST /search
```

**Purpose**: Performs full-text search using MariaDB's FULLTEXT index to find relevant document chunks.

**Request body**:

```json
{
  "query": "MariaDB features",
  "top_k": 10,
  "document_ids": [42, 43]
}
```

**Request Parameters**:

* `query` (required): The search query
* `top_k` (optional): Number of results to return (default: 10)
* `document_ids` (optional): Filter results to specific document IDs

**Response**: Array of search results

```json
[
  {
    "id": "uuid-chunk-id",
    "document_id": 42,
    "source": "/uploaded_files/product_overview.pdf",
    "content": "MariaDB features include vector search, full-text indexing...",
    "score": 15.5
  },
  {
    "id": "uuid-chunk-id-2",
    "document_id": 43,
    "source": "/uploaded_files/technical_docs.pdf",
    "content": "Additional MariaDB capabilities for enterprise applications...",
    "score": 12.3
  }
]
```

**Response Fields**:

* `id`: Unique chunk identifier
* `document_id`: ID of the source document
* `source`: File path of the source document
* `content`: The chunk text content
* `score`: Relevance score (higher = more relevant)

**Usage Example**: Use this endpoint for keyword-based search when you need exact term matching.

```bash
curl -X POST "http://localhost:8000/search" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "MariaDB features",
    "top_k": 10
  }'
```

### Hybrid Search

```
POST /hybrid_search
```

**Purpose**: Combines semantic search (vector similarity) and full-text search using Reciprocal Rank Fusion (RRF) for optimal results.

**Request body**:

```json
{
  "query": "MariaDB vector capabilities",
  "top_k": 20,
  "k": 60,
  "provider": "openai",
  "model": "text-embedding-3-small",
  "document_ids": [42, 43]
}
```

**Request Parameters**:

* `query` (required): The search query
* `top_k` (optional): Number of results to return (default: 20)
* `k` (optional): RRF parameter for rank fusion (default: 60)
* `provider` (optional): Embedding provider for semantic search
* `model` (optional): Embedding model for semantic search
* `document_ids` (optional): Filter results to specific document IDs

**Response**: Array of hybrid search results

```json
[
  {
    "id": "uuid-chunk-id",
    "document_id": 42,
    "source": "/uploaded_files/product_overview.pdf",
    "content": "MariaDB vector capabilities enable semantic search...",
    "metadata": {},
    "distance": 0.18,
    "score": 14.2
  },
  {
    "id": "uuid-chunk-id-2",
    "document_id": 43,
    "source": "/uploaded_files/technical_docs.pdf",
    "content": "Vector indexing in MariaDB provides fast similarity search...",
    "metadata": {},
    "distance": 0.25,
    "score": 11.8
  }
]
```

**Response Fields**:

* `id`: Unique chunk identifier
* `document_id`: ID of the source document
* `source`: File path of the source document
* `content`: The chunk text content
* `metadata`: Additional metadata about the chunk
* `distance`: Vector distance from semantic search (lower = more similar)
* `score`: Full-text relevance score (higher = more relevant)

**Usage Example**: Use this endpoint for the best of both worlds - combining semantic understanding with keyword matching.

```bash
curl -X POST "http://localhost:8000/hybrid_search" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "MariaDB vector capabilities",
    "top_k": 10,
    "k": 60
  }'
```

### Generate Text

```
POST /generate
```

**Purpose**: Generates a response to a query using a language model and the provided context chunks.

**Request body**:

```json
{
  "query": "Explain MariaDB AI RAG features",
  "chunks": [
    "MariaDB AI RAG is an enterprise-grade RAG solution that integrates with MariaDB...",
    "Key features include document processing, semantic search, and AI-powered responses..."
  ],
  "llm_provider": "openai",
  "llm_model": "gpt-4",
  "temperature": 0.7,
  "top_p": 0.9,
  "max_tokens": 1000
}
```

**Request Parameters**:

* `query` (required): The user's question or prompt
* `chunks` (required): Array of context chunks to use for generation
* `llm_provider` (optional): LLM provider - `openai`, `anthropic`, `gemini`, `cohere`, `ollama`, `azure`, `bedrock`
* `llm_model` (optional): Specific model to use (e.g., `gpt-4`, `claude-3-opus`)
* `temperature` (optional): Controls randomness (0.0-2.0, default: 0.7)
* `top_p` (optional): Nucleus sampling parameter (0.0-1.0, default: 0.9)
* `max_tokens` (optional): Maximum tokens to generate (1-8192, default: 1000)

**Response**:

```json
{
  "response": "MariaDB AI RAG is an enterprise-grade Retrieval-Augmented Generation (RAG) solution that seamlessly integrates with MariaDB. Its key features include..."
}
```

**Usage Example**: Use this endpoint after retrieving relevant chunks to generate a coherent response based on the information in those chunks.

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain MariaDB AI RAG features",
    "chunks": ["chunk1", "chunk2"],
    "llm_provider": "openai",
    "llm_model": "gpt-4",
    "temperature": 0.7
  }'
```

### Asynchronous Generation

```
POST /generate-async
```

**Purpose**: Generates a response asynchronously, useful for long-running generation tasks.

**Request body**: Same as `/generate`

**Response**: Same as `/generate`

**Usage Example**: Use this endpoint for generation tasks that may take longer to complete.

```bash
curl -X POST "http://localhost:8000/generate-async" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Provide a detailed analysis",
    "chunks": ["chunk1", "chunk2"],
    "llm_provider": "openai",
    "llm_model": "gpt-4"
  }'
```

### Streaming Generation

```
POST /generate-stream
```

**Purpose**: Generates a response with streaming output (Server-Sent Events), allowing for real-time display of results as tokens are generated.

**Request body**: Same as `/generate`

**Response**: Server-Sent Events (SSE) stream with the following event types:

```json
// Start event
{"type": "start", "provider": "openai", "model": "gpt-4"}

// Token events (streamed as generated)
{"type": "token", "content": "MariaDB", "chunk_index": 1}
{"type": "token", "content": " Data", "chunk_index": 2}
{"type": "token", "content": " Bridge", "chunk_index": 3}

// Completion event
{"type": "complete", "duration": 2.5, "chunks_streamed": 150}

// Error event (if error occurs)
{"type": "error", "message": "Error description"}
```

**Usage Example**: Use this endpoint for a better user experience when generating longer responses, as it allows displaying partial results as they become available.

```bash
curl -X POST "http://localhost:8000/generate-stream" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain MariaDB AI RAG features",
    "chunks": ["chunk1", "chunk2"],
    "llm_provider": "openai",
    "llm_model": "gpt-4"
  }'
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
