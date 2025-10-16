# Access Control

## Access Control Endpoints

### Update Document Access

```
PUT /documents/{document_id}/access
```

**Purpose**: Updates the list of users who have access to a specific document.

**Request body**:
```json
{
  "authorized_users": ["user1@example.com", "user2@example.com", "user3@example.com"]
}
```

**Response**:
```json
{
  "document_id": 42,
  "authorized_users": ["user1@example.com", "user2@example.com", "user3@example.com"],
  "updated_at": "2025-08-25T12:45:30.123Z"
}
```

**Usage Example**: Use this endpoint to control which users can access specific documents.

```bash
curl -X PUT "http://localhost:8000/documents/42/access" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"authorized_users": ["user1@example.com", "user2@example.com"]}'
```

### Get Document Access List

```
GET /documents/{document_id}/access
```

**Purpose**: Retrieves the list of users who have access to a specific document.

**Response**:
```json
{
  "document_id": 42,
  "authorized_users": ["user1@example.com", "user2@example.com", "user3@example.com"],
  "created_by": "admin@example.com",
  "created_at": "2025-08-20T10:15:30.123Z",
  "updated_at": "2025-08-25T12:45:30.123Z"
}
```

**Usage Example**: Use this endpoint to check which users have access to a specific document.

```bash
curl "http://localhost:8000/documents/42/access" \
  -H "Authorization: Bearer YOUR_TOKEN"
```
