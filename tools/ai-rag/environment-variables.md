# Environment Variables

MariaDB Data Bridge uses environment variables for configuration. These can be set in a `.env` file in the installation directory.

## Required Environment Variables

```
# Database Configuration (Required)
DB_HOST=localhost
DB_PORT=3306
DB_USER=databridge
DB_PASSWORD=your_secure_password
DB_NAME=databridge

# Server Configuration (Required)
HOST=0.0.0.0
PORT=8000

# Embedding Configuration (Required)
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small

# API Keys (Set based on your embedding/LLM provider)
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
VOYAGE_API_KEY=your_voyage_api_key
COHERE_API_KEY=your_cohere_api_key
```

## Security Configuration

### Authentication

MariaDB Data Bridge implements JWT-based authentication. Configure the following parameters in your `.env` file:

```
SECRET_KEY=your_secure_random_string
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

For production environments, it is strongly recommended to use a properly generated secure random string for the `SECRET_KEY`.

### API Key Management

External service API keys should be securely stored in the `.env` file. In production environments, consider using a secure vault solution or environment variable management system.
