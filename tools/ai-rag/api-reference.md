# API Reference

MariaDB Data Bridge exposes a comprehensive RESTful API for programmatic interaction with the system. All API endpoints require authentication except for the login endpoint.

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

### Upload Document

```
POST /documents/ingest
```

**Purpose**: Uploads and processes a single document for ingestion into the system.

**Request**: `multipart/form-data` with file attachment

**Response**:
```json
{
  "id": 42,
  "filename": "example.pdf",
  "content_type": "application/pdf",
  "size": 1048576,
  "status": "processing",
  "created_at": "2025-08-25T11:42:00.123456"
}
```

**Usage Example**: Use this endpoint to upload individual documents. The document will be processed asynchronously, and its content will be extracted and prepared for chunking.

```bash
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@/path/to/document.pdf"
```

### Upload Multiple Documents

```
POST /documents/ingest-multiple
```

**Purpose**: Uploads and processes multiple documents in a single request.

**Request**: `multipart/form-data` with multiple file attachments

**Response**:
```json
{
  "documents": [
    {
      "id": 42,
      "filename": "example1.pdf",
      "status": "processing"
    },
    {
      "id": 43,
      "filename": "example2.docx",
      "status": "processing"
    }
  ],
  "total_count": 2
}
```

**Usage Example**: Use this endpoint when you need to upload multiple documents at once. This is more efficient than making separate calls for each document.

```bash
curl -X POST "http://localhost:8000/documents/ingest-multiple" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document1.pdf" \
  -F "files=@/path/to/document2.docx"
```

### List Documents

```
GET /documents
```

**Purpose**: Retrieves a paginated list of all documents uploaded by the authenticated user.

**Parameters**:
- `skip` (optional): Number of records to skip for pagination (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

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

### Chunk Document

```
POST /chunks/document
```

**Purpose**: Processes a document into chunks and creates vector embeddings for semantic search.

**Request body**:
```json
{
  "document_id": 42,
  "chunk_size": 1000,
  "chunk_overlap": 200,
  "chunking_strategy": "recursive"
}
```

**Response**:
```json
{
  "document_id": 42,
  "status": "processing",
  "task_id": "abc123def456"
}
```

**Usage Example**: Use this endpoint after document ingestion to prepare the document for semantic search. The chunking process divides the document into semantically meaningful segments and creates vector embeddings.

```bash
curl -X POST "http://localhost:8000/chunks/document" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_id": 42, "chunk_size": 1000, "chunk_overlap": 200, "chunking_strategy": "recursive"}'
```

### Chunk Multiple Documents

```
POST /chunks/batch
```

**Purpose**: Processes multiple documents into chunks in a single batch operation.

**Request body**:
```json
{
  "document_ids": [42, 43, 44],
  "chunk_size": 1000,
  "chunk_overlap": 200,
  "chunking_strategy": "recursive"
}
```

**Response**:
```json
{
  "batch_id": "batch_xyz789",
  "document_count": 3,
  "status": "processing"
}
```

**Usage Example**: Use this endpoint to process multiple documents at once, which is more efficient than individual chunking requests.

```bash
curl -X POST "http://localhost:8000/chunks/batch" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_ids": [42, 43, 44], "chunk_size": 1000, "chunk_overlap": 200, "chunking_strategy": "recursive"}'
```

## Retrieval and Generation Endpoints

### Retrieve Documents

```
POST /retrieve
```

**Purpose**: Performs semantic search to retrieve relevant document chunks based on a query.

**Request body**:
```json
{
  "query": "What is MariaDB Data Bridge?",
  "top_k": 5,
  "filter": {
    "document_ids": [42, 43]
  }
}
```

**Response**:
```json
{
  "results": [
    {
      "chunk_id": 101,
      "document_id": 42,
      "document_name": "product_overview.pdf",
      "content": "MariaDB Data Bridge is an enterprise-grade RAG solution...",
      "similarity_score": 0.92,
      "metadata": {
        "page": 1,
        "section": "Introduction"
      }
    },
    {...}
  ],
  "total_chunks_searched": 150,
  "query_time_ms": 45
}
```

**Usage Example**: Use this endpoint to find relevant information across your document collection. The system will convert your query into a vector embedding and find the most semantically similar chunks.

```bash
curl -X POST "http://localhost:8000/retrieve" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is MariaDB Data Bridge?", "top_k": 5}'
```

### Generate Text

```
POST /generate
```

**Purpose**: Generates a response to a query using a language model and the provided context chunks.

**Request body**:
```json
{
  "query": "Explain MariaDB Data Bridge features",
  "chunks": [
    "MariaDB Data Bridge is an enterprise-grade RAG solution that integrates with MariaDB...",
    "Key features include document processing, semantic search, and AI-powered responses..."
  ],
  "llm_provider": "openai",
  "llm_model": "gpt-4",
  "temperature": 0.25,
  "max_tokens": 1000
}
```

**Response**:
```json
{
  "response": "MariaDB Data Bridge is an enterprise-grade Retrieval-Augmented Generation (RAG) solution that seamlessly integrates with MariaDB. Its key features include...",
  "model_used": "openai/gpt-4",
  "tokens_used": 245,
  "generation_time_ms": 1250
}
```

**Usage Example**: Use this endpoint after retrieving relevant chunks to generate a coherent response based on the information in those chunks. This combines the retrieval and generation steps of the RAG process.

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "Explain MariaDB Data Bridge features", "chunks": ["chunk1", "chunk2"], "llm_provider": "openai", "llm_model": "gpt-4"}'
```

### Streaming Generation

```
POST /generate/stream
```

**Purpose**: Generates a response to a query with streaming output, allowing for real-time display of results.

**Request body**: Same as `/generate`

**Response**: Server-Sent Events (SSE) stream with incremental text generation

**Usage Example**: Use this endpoint for a better user experience when generating longer responses, as it allows displaying partial results as they become available.

```bash
curl -X POST "http://localhost:8000/generate/stream" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "Explain MariaDB Data Bridge features", "chunks": ["chunk1", "chunk2"], "llm_provider": "openai", "llm_model": "gpt-4"}'
```
