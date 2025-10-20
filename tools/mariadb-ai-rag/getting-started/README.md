---
icon: rabbit
---

# Getting Started

Welcome to MariaDB AI RAG! This section will guide you through installing, configuring, and running the MariaDB AI RAG API and MCP Server.

## Documentation in This Section

### [Overview](overview.md)
Learn about the MariaDB AI RAG system architecture and components:
- System architecture
- Core modules (Ingestion, Chunking, Retrieval, Generation)
- Data flow and processing pipeline
- Integration with MariaDB vector database

### [Installation](installation.md)
Step-by-step installation instructions for all supported platforms:
- Linux (Ubuntu/Debian - .deb packages)
- Linux (RHEL/Fedora - .rpm packages)
- Windows (.msi installer)
- System requirements and prerequisites

### [Configuration](configuration.md)
Configure the RAG API and MCP Server:
- Environment variables
- Configuration file setup
- Database connection settings
- API keys and authentication
- Embedding and LLM provider configuration

### [Service Management](service-management.md)
Manage the RAG API and MCP Server services:
- Starting and stopping services
- Service status monitoring
- Log file locations
- Troubleshooting service issues

## Quick Start Guide

1. **Install the package** for your platform (see [Installation](installation.md))
2. **Configure your environment** with database credentials and API keys (see [Configuration](configuration.md))
3. **Start the services** using the service management commands
4. **Verify installation** by accessing the API health endpoint:
   ```bash
   curl http://localhost:8000/health
   ```

## Next Steps

After completing the getting started guide:
- Explore the [API Reference](../api-reference/README.md) for detailed endpoint documentation
- Learn about [Access Control](../api-reference/access-control.md) for user management
- Review [Performance Tuning](../performance-and-troubleshooting/performance-tuning.md) for optimization

