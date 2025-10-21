---
icon: maximize
---

# Performance & Troubleshooting

This section provides guidance on optimizing the MariaDB AI RAG system and resolving common issues.

## Documentation in This Section

### [Performance Tuning](performance-tuning.md)
Optimize your RAG deployment for better performance:
- Database connection pooling
- Batch processing configuration
- Embedding batch sizes
- Caching strategies
- Query optimization
- Resource allocation

### [Troubleshooting](troubleshooting.md)
Solutions for common issues:
- Connection problems
- Authentication errors
- Document ingestion failures
- Chunking issues
- Retrieval performance problems
- Generation errors
- Service startup issues

## Performance Optimization Tips

### Database Performance
- Use appropriate connection pool sizes (default: 10)
- Enable MariaDB query cache
- Optimize vector index configuration
- Monitor slow queries

### API Performance
- Configure batch sizes based on available memory
- Use async operations for large document sets
- Enable response caching where appropriate
- Monitor API response times

### Embedding Performance
- Batch embedding operations (default: 32)
- Use GPU acceleration if available
- Choose appropriate embedding models for your use case
- Cache frequently used embeddings

## Common Issues Quick Reference

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Connection timeout | Database not accessible | Check DB_HOST and DB_PORT settings |
| Authentication failed | Invalid credentials | Verify JWT_SECRET and user credentials |
| Document ingestion slow | Large files, small batch size | Increase EMBEDDING_BATCH_SIZE |
| Out of memory | Batch size too large | Reduce batch sizes in configuration |
| Service won't start | Port already in use | Check if another service is using the port |

## Getting Help

If you encounter issues not covered in this documentation:

1. Check the [Troubleshooting Guide](troubleshooting.md) for detailed solutions
2. Review the service logs for error messages
3. Verify your [Configuration](../getting-started/configuration.md) settings
4. Consult the [API Reference](../api-reference/README.md) for endpoint-specific issues

