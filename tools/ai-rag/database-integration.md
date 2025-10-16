# Database Integration

## Database Integration Endpoints

### Ingest from Database Table

```
POST /documents/ingest-from-table
```

**Purpose**: Ingests data directly from a MariaDB table or view, treating it as a CSV data source. This allows for seamless integration with existing database content.

**Request body**:
```json
{
  "table_name": "customer_feedback",
  "schema_name": "databridge",
  "column_mapping": {
    "content": "feedback_text",
    "metadata": ["customer_id", "product_id", "rating", "date_submitted"],
    "id_column": "feedback_id"
  },
  "filter_condition": "rating >= 3 AND date_submitted > '2025-01-01'",
  "batch_size": 1000,
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Response**:
```json
{
  "job_id": "db_ingest_xyz123",
  "status": "processing",
  "table_name": "customer_feedback",
  "estimated_rows": 5230,
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Usage Example**: Use this endpoint to ingest structured data from your database tables or views. The system will process each row as a document, with specified columns as content and metadata.

```bash
curl -X POST "http://localhost:8000/documents/ingest-from-table" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"table_name": "customer_feedback", "schema_name": "databridge", "column_mapping": {"content": "feedback_text", "metadata": ["customer_id", "product_id", "rating", "date_submitted"], "id_column": "feedback_id"}, "authorized_users": ["user1@example.com"]}'
```

### Ingest from SQL Query

```
POST /documents/ingest-from-query
```

**Purpose**: Ingests data from the results of a custom SQL query, providing maximum flexibility for selecting and transforming data from your database.

**Request body**:
```json
{
  "sql_query": "SELECT id, title, content, author, published_date FROM articles WHERE status = 'published' AND category = 'technical'",
  "column_mapping": {
    "content": ["title", "content"],
    "metadata": ["author", "published_date"],
    "id_column": "id"
  },
  "batch_size": 500,
  "authorized_users": ["user1@example.com", "user2@example.com", "user3@example.com"]
}
```

**Response**:
```json
{
  "job_id": "query_ingest_abc456",
  "status": "processing",
  "estimated_rows": 127,
  "authorized_users": ["user1@example.com", "user2@example.com", "user3@example.com"]
}
```

**Usage Example**: Use this endpoint when you need to ingest data from complex queries or joins across multiple tables.

```bash
curl -X POST "http://localhost:8000/documents/ingest-from-query" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"sql_query": "SELECT id, title, content, author, published_date FROM articles WHERE status = \'published\'", "column_mapping": {"content": ["title", "content"], "metadata": ["author", "published_date"], "id_column": "id"}, "authorized_users": ["user1@example.com", "user2@example.com"]}'
```

### Check Database Ingestion Status

```
GET /documents/ingest-status/{job_id}
```

**Purpose**: Checks the status of a database ingestion job.

**Response**:
```json
{
  "job_id": "db_ingest_xyz123",
  "status": "completed",
  "processed_rows": 5230,
  "created_documents": 5230,
  "failed_rows": 0,
  "completion_time": "2025-08-25T12:34:56.789Z",
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Usage Example**: Use this endpoint to monitor the progress of database ingestion jobs.

```bash
curl "http://localhost:8000/documents/ingest-status/db_ingest_xyz123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```
