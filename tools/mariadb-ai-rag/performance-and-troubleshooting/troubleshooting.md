# Troubleshooting

## Common Issues

### Service Won't Start

* Check if another process is using the configured port
* Verify database connection settings
* Ensure environment variables are properly set
* Check for errors in the log files

### Document Ingestion Fails

* Verify file format is supported (see Appendix for supported formats)
* Check file size limits (default is 10MB per file)
* Ensure sufficient disk space
* Verify file permissions

### Vector Search Returns Poor Results

* Verify document chunking configuration (try adjusting chunk size and overlap)
* Check embedding model configuration (consider using a more powerful model)
* Ensure documents were properly ingested and chunked
* Try reindexing vectors if you've changed embedding models

## Log Files

Log files are located in the following directories:

* API logs: `logs/api.log`
* Ingestion logs: `logs/ingestion.log`
* Chunking logs: `logs/chunking.log`
* Error logs: `logs/error.log`

## Diagnostic Steps

1.  Check service status:

    ```bash
    systemctl status mariadb-data-bridge
    ```
2.  View recent logs:

    ```bash
    tail -n 100 logs/error.log
    ```
3.  Verify API accessibility:

    ```bash
    curl http://localhost:8000/health
    ```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
