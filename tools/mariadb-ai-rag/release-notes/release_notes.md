# Release Notes
MariaDB AI RAG API and MCP Server 1.0 is a tech preview of tools to enable a RAG AI system using MariaDB as the vector database. The MCP Server is an extension of the existing community MCP Server with authentication as well as new RAG AI functionality.

The AI RAG API is intended to provide a simple, configurable, REST API for ingesting documents and retrieving information from them. It is also intended to be used as a building block for larger AI RAG systems. As a REST API with controls around visibility of documents and chunks, with options for full pipeline orchestration, it can make the process of of implementing a RAG system simpler than approaches that require the user to learn and implement the ingestion, chunking, and retrieval programmatically for each application of RAG separately.

We plan to do multiple releases of this tech preview to continue to improve the system and incorporate feedback from users.

## v1.0.0

### Key Features
- RAG API endpoints for document ingestion and chunking
- User and document management endpoints
- JWT authentication for API access
- Support for multiple document formats (PDF, DOCX, TXT, CSV, XLSX)
- MariaDB vector index integration for efficient document search
- Retrieval options include semantic search, hybrid search, and fulltext search
- Support for multiple retrieval and generation models (e.g. OpenAI, Cohere, etc.)
- Support for key vaults to make configuration of sensitive information easier

### Packaging
- RPM, DEB, and MSI installers for RHEL, Ubuntu, and Windows are provided

### Installation
- Using the platform's installer file (.msi, .rpm, or .deb) run the installer
- Then follow the installation instructions in the AI RAG MCP Server and AI RAG API documentation