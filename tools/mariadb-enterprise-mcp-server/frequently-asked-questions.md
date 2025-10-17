# Frequently Asked Questions

<details>

<summary><strong>Where do you get MCP Server from and what are the installation requirements?</strong></summary>

The MCP Server can be launched individually or as part of the RAG-in-a-box system. It is distributed as pre-compiled binaries that can run on various operating systems, including:

* Windows
* RHEL (Red Hat Enterprise Linux)
* Ubuntu

</details>

<details>

<summary><strong>Is MCP Server a command-line tool, or does it have a GUI?</strong></summary>

The MCP Server is a network service that runs as an HTTP server; it does not have a graphical user interface (GUI) or a direct command-line interface (CLI) for tools. It's designed to be a backend service that is:

* Accessed programmatically via the Model Context Protocol.
* Integrated into AI assistants and clients like Claude Desktop, Cursor, or Windsurf.

You interact with the server by configuring a client application to communicate with it. For example, here is how you might configure a client like Windsurf:

{% code overflow="wrap" %}
```json
{
  "mcpServers": {
    "rag-mcp": {
      "serverUrl": "http://localhost:8002/mcp",
      "headers": {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xyz.abc"
      }
    }
  }
}
```
{% endcode %}

</details>

<details>

<summary><strong>How do you configure the MCP Server and connect it to MariaDB?</strong></summary>

The MCP Server does not include its own database. It acts as a client and requires a connection to an external, pre-existing MariaDB server.

The system components are connected as follows:

```
MCP Server (Port 8002) ---------> MariaDB Server (Port 3306)
                         (connects via MySQL protocol)
```

Configuration is managed through environment files where you specify the connection details for your MariaDB instance.

</details>

<details>

<summary><strong>How are tools like <code>list_databases</code> executed?</strong></summary>

Tools are not typed into a command line. Instead, they are executed programmatically by a Large Language Model (LLM) in response to a user's query in natural language.

The process works like this:

1. A user asks a question in an integrated client (e.g., "Can you show me what databases are available?").
2. The LLM interprets the request and determines that the `list_databases` tool is needed.
3. The LLM calls the `list_databases` tool by sending a JSON-RPC request to the MCP Server.
4. The MCP Server executes the tool against the connected MariaDB database.
5. The results are sent back to the LLM, which formats them into a natural language response for the user.

</details>

<details>

<summary><strong>What are the JSON snippets in the documentation for?</strong></summary>

The JSON snippets shown in the documentation are examples of the "behind-the-scenes" communication between a client, the LLM, and the MCP Server. They are not meant to be copied and pasted into a CLI but serve to illustrate how the protocol functions.

</details>

<details>

<summary></summary>

Token management is a critical part of the system's security, handled primarily by the RAG API.

**Token Generation**

The process involves two main steps:

**/User Registration**

```
graph TD
    A[User] -->|Sends Email & Password| B(POST /register)
    B --> C[Hash Password with bcrypt]
    C --> D[Store User in Database]
```

**Step 2: User Login & Token Generation**



```
graph TD
    A[User] -->|Sends Credentials| B(POST /token)
    B --> C[Verify Credentials in DB]
    C --> D[Determine User Roles]
    D --> E[Generate JWT Token]
    E --> F[Return Token to User]
```

**Token Usage**

Once a client has a JWT, it includes it in the `Authorization` header of every request to the MCP Server. The server then validates the token before processing the request.

```
sequenceDiagram
    participant Client
    participant MCP Server
    participant RAG API
    participant Database

    Client->>MCP Server: Tool Call + JWT Token
    
    Note over MCP Server: 1. Extract Token<br/>2. Verify JWT Signature
    
    MCP Server->>Database: 3. Validate User in DB
    Database-->>MCP Server: User Record
    
    Note over MCP Server: (If RAG tool is called)
    MCP Server->>RAG API: 4. Forward Request + Token
    Note over RAG API: 5. Verify Token Again
    RAG API-->>MCP Server: Processed Result
    
    MCP Server-->>Client: Response
```

**Key Security Measures**

* **Signature Verification**: Prevents token tampering.
* **Expiration Check**: Tokens have a limited lifetime (e.g., 30 minutes).
* **Database Validation**: Ensures the user associated with the token still exists and is active.
* **Issuer/Audience Validation**: Prevents a token from one system from being used on another.
* **Not-Before Check**: Prevents a token from being used before it is valid.

</details>

Token management is a critical part of the system's security, handled primarily by the RAG API.

**Token Generation**

The process involves two main steps:

**Step 1: User Registration**

```
graph TD
    A[User] -->|Sends Email & Password| B(POST /register)
    B --> C[Hash Password with bcrypt]
    C --> D[Store User in Database]
```

**Step 2: User Login & Token Generation**

```
graph TD
    A[User] -->|Sends Credentials| B(POST /token)
    B --> C[Verify Credentials in DB]
    C --> D[Determine User Roles]
    D --> E[Generate JWT Token]
    E --> F[Return Token to User]
```

**Token Usage**

Once a client has a JWT, it includes it in the `Authorization` header of every request to the MCP Server. The server then validates the token before processing the request.

```
sequenceDiagram
    participant Client
    participant MCP Server
    participant RAG API
    participant Database

    Client->>MCP Server: Tool Call + JWT Token
    
    Note over MCP Server: 1. Extract Token<br/>2. Verify JWT Signature
    
    MCP Server->>Database: 3. Validate User in DB
    Database-->>MCP Server: User Record
    
    Note over MCP Server: (If RAG tool is called)
    MCP Server->>RAG API: 4. Forward Request + Token
    Note over RAG API: 5. Verify Token Again
    RAG API-->>MCP Server: Processed Result
    
    MCP Server-->>Client: Response
```

**Key Security Measures**

* **Signature Verification**: Prevents token tampering.
* **Expiration Check**: Tokens have a limited lifetime (e.g., 30 minutes).
* **Database Validation**: Ensures the user associated with the token still exists and is active.
* **Issuer/Audience Validation**: Prevents a token from one system from being used on another.
* **Not-Before Check**: Prevents a token from being used before it is valid.
