# MariaDB AI RAG - Deployment Overview (Simplified)

## What You Have

**One Package**: `ai-nexus.deb`

**What's Inside the Package**:
- RAG API application
- MCP Server application
- Both applications bundled together

## What You Need to Deploy

### 1. The Application Package (ai-nexus.deb)
This contains your RAG API and MCP Server applications.

### 2. A Database (MariaDB)
The applications need a database to store documents and vector embeddings.

### 3. Configuration (Secret Management Mode)
You need to choose HOW to provide secrets (API keys, passwords) to the applications.

---

## Two Deployment Options

### Option A: Deploy on Ubuntu (Native) ✅ SIMPLER
**What happens**: Install the .deb package directly on Ubuntu

```
Ubuntu Server
├── MariaDB (you install separately)
├── RAG API (from .deb package)
└── MCP Server (from .deb package)
```

**Steps**:
1. Install MariaDB on Ubuntu
2. Install ai-nexus.deb on Ubuntu
3. Configure secrets (choose a mode)
4. Start services

**Guide**: `UBUNTU_DEPLOYMENT_GUIDE.md`

---

### Option B: Deploy with Docker (on Windows) 🐳
**What happens**: Package everything in Docker containers

```
Windows + Docker Desktop
├── Docker Container 1: MariaDB
└── Docker Container 2: ai-nexus.deb 
```

**Steps**:
1. Build Docker image (wraps the .deb package)
2. Start containers with docker-compose
3. Configure secrets (choose a mode)

**Guide**: `DOCKER_DEPLOYMENT_GUIDE.md`

---

## Secret Management Modes (Works with BOTH Options)

**After you deploy the application (Ubuntu or Docker), you choose ONE mode:**

### Mode 1: Standalone (Simplest) ⭐
**How it works**: Secrets stored in a plain text config file

**Config File Location**:
- Ubuntu: `/opt/rag-in-a-box/config/config.env.template`
- Docker: `config.env.secure.local`

**Example**:
```bash
GEMINI_API_KEY=your_actual_gemini_api_key_here
DB_PASSWORD=your_secure_database_password
SECRET_KEY=your_generated_secret_key_64_chars_long
```

**How to generate secure keys**:
```bash
# Generate a secure secret key (Python)
python3 -c "import secrets; print(secrets.token_urlsafe(64))"

# Or using PowerShell
[Convert]::ToBase64String((1..64 | ForEach-Object { Get-Random -Maximum 256 }))
```

**When to use**: Development, testing, single developer

---

### Mode 2: Local Vault (Production-like) 🔐
**How it works**: Secrets stored in HashiCorp Vault (running locally)

**Architecture**:
```
Your Application (RAG API + MCP Server)
    ↓ (fetches secrets at startup)
HashiCorp Vault (running locally)
    ↓ (stores)
Secrets (API keys, passwords)
```

**Config File Location**:
- Ubuntu: `/opt/rag-in-a-box/config/config.env.template`
- Docker: `config.env.vault.local`

**Example**:
```bash
VAULT_ADDR=http://127.0.0.1:8200
VAULT_TOKEN=your_vault_token
VAULT_SECRET_PATH=rag-in-a-box
# Application fetches secrets from Vault at startup
```

**When to use**: Team development, production-like testing

---

### Mode 3: 1Password (Enterprise) 🔑
**How it works**: Secrets stored in 1Password vault

**Architecture**:
```
Your Application (RAG API + MCP Server)
    ↓ (fetches secrets via 1Password CLI)
1Password CLI
    ↓ (connects to)
1Password Cloud
    ↓ (stores)
Secrets (API keys, passwords)
```

**Config File**:
```bash
GEMINI_API_KEY=op://Employee/RAG-API-Keys/gemini
DB_PASSWORD=op://Employee/RAG-Database/password
# op:// references point to 1Password items
```

**When to use**: Enterprise with 1Password subscription

---

### Mode 4: HCP Vault (Production Cloud) ☁️
**How it works**: Secrets stored in HashiCorp Cloud Platform

**Architecture**:
```
Your Application (RAG API + MCP Server)
    ↓ (fetches secrets at startup)
HCP Vault (cloud service)
    ↓ (stores)
Secrets (API keys, passwords)
```

**When to use**: Production cloud deployments

---

## Complete Deployment Flow

### Scenario 1: Ubuntu Native + Standalone Mode

```
Step 1: Install MariaDB on Ubuntu
    ↓
Step 2: Install ai-nexus.deb on Ubuntu
    ↓
Step# 3. Edit /opt/rag-in-a-box/config/config.env.template
        Put secrets directly in file (Standalone mode)
        GEMINI_API_KEY=your_actual_api_key
        DB_PASSWORD=your_secure_password
    ↓
Step 4: Start services in their own terminals by running:
        /opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
        CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server
    ↓
Step 5: Application reads secrets from config file
    ↓
✅ Done! Application running with Standalone mode
```

---

### Scenario 2: Ubuntu Native + Vault Mode

```
Step 1: Install MariaDB on Ubuntu
    ↓
Step 2: Install HashiCorp Vault on Ubuntu
    ↓
Step# 3. Store secrets in Vault
        vault kv put secret/rag-in-a-box \
          GEMINI_API_KEY="your_api_key" \
          DB_PASSWORD="your_password"
    ↓
Step 4: Install ai-nexus.deb on Ubuntu
    ↓
Step 5: Edit /opt/rag-in-a-box/config/config.env.template
        Configure Vault connection (NOT the secrets themselves)
        VAULT_ADDR=http://127.0.0.1:8200
        VAULT_TOKEN=your_vault_root_token
    ↓
Step 6: Start services in their own terminals by running:
        /opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
        CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server
    ↓
Step 7: Application connects to Vault and fetches secrets
    ↓
✅ Done! Application running with Vault mode
```

---

### Scenario 3: Docker + Standalone Mode

```
Step 1: Build Docker image (wraps ai-nexus.deb)
        docker build -t ai-nexus-image .
    ↓
Step# 2. Edit config.env.secure.local
        Put secrets directly in file (Standalone mode)
        GEMINI_API_KEY=your_actual_api_key
        DB_PASSWORD=your_secure_password
    ↓
Step 3: Start containers
        docker-compose up -d
        (Starts MariaDB container + ai-nexus container)
    ↓
Step 4: Application reads secrets from config file
    ↓
✅ Done! Application running with Standalone mode
```

---

### Scenario 4: Docker + Vault Mode

```
Step 1: Build Docker image (wraps ai-nexus.deb)
        docker build -t ai-nexus-image .
    ↓
Step 2: Start Vault container
        docker-compose -f Localvault/docker-compose.vault.yml up -d
    ↓
Step# 3. Store secrets in Vault
        docker exec vault vault kv put secret/rag-in-a-box \
          GEMINI_API_KEY="your_api_key" \
          DB_PASSWORD="your_password"
    ↓
Step 4: Edit config.env.vault.local
        Configure Vault connection
        VAULT_ADDR=http://rag-vault:8200
        VAULT_TOKEN=your_vault_token
    ↓
Step 5: Start containers with Vault config
        docker-compose --env-file config.env.vault.local up -d
    ↓
Step 6: Application connects to Vault and fetches secrets
    ↓
✅ Done! Application running with Vault mode
```

---

## Key Points to Understand

### 1. The Package is the Same
The `ai-nexus.deb` package is identical regardless of:
- Where you deploy it (Ubuntu or Docker)
- Which secret mode you use (Standalone, Vault, 1Password, HCP)

### 2. Deployment Location is Independent of Secret Mode
You can use ANY secret mode with ANY deployment location:
- Ubuntu + Standalone ✅
- Ubuntu + Vault ✅
- Ubuntu + 1Password ✅
- Docker + Standalone ✅
- Docker + Vault ✅
- Docker + 1Password ✅

### 3. The Application Decides at Startup
When RAG API and MCP Server start, they:
1. Read the config file
2. Check which mode is configured
3. Fetch secrets accordingly:
   - Standalone: Read from config file directly
   - Vault: Connect to Vault and fetch
   - 1Password: Use 1Password CLI to fetch
   - HCP: Connect to HCP Vault and fetch

---

## Which Guide to Use?

### I want to deploy on Ubuntu (no Docker)
→ Use: **`UBUNTU_DEPLOYMENT_GUIDE.md`**

**Then choose secret mode:**
- Standalone: Edit `/opt/rag-in-a-box/config/config.env.template` with actual secrets
- Vault: Install Vault, store secrets, configure Vault connection in config
- 1Password: Install 1Password CLI, configure 1Password references in config

---

### I want to deploy with Docker (on Windows)
→ Use: **`DOCKER_DEPLOYMENT_GUIDE.md`**

**Then choose secret mode:**
- Standalone: Edit `config.env.secure.local` with actual secrets
- Vault: Run Vault container, store secrets, use `config.env.vault.local`
- 1Password: Install 1Password CLI, use `config.env.1password.employee`

---

## Quick Decision Tree

```
Do you have Ubuntu system?
├─ Yes → Deploy natively on Ubuntu
│         Guide: UBUNTU_DEPLOYMENT_GUIDE.md
│         
│         Choose secret mode:
│         ├─ Simple testing? → Standalone
│         ├─ Team development? → Local Vault
│         ├─ Have 1Password? → 1Password
│         └─ Production cloud? → HCP Vault
│
└─ No (Windows/Mac) → Deploy with Docker
          Guide: DOCKER_DEPLOYMENT_GUIDE.md
          
          Choose secret mode:
          ├─ Simple testing? → Standalone
          ├─ Team development? → Local Vault (Docker)
          ├─ Have 1Password? → 1Password
          └─ Production cloud? → HCP Vault
```

---

## Example: Complete Ubuntu Deployment (Standalone)

```bash
# 1. Install database
sudo apt install -y mariadb-server
sudo mysql_secure_installation

# 2. Create database
sudo mariadb -u root -p
CREATE DATABASE kb_chunks;
EXIT;

# 3. Install application
sudo apt install -y ./ai-nexus.deb

# 4. Configure (Standalone mode - secrets in file)
cp /opt/rag-in-a-box/config/config.env.template /path/to/config.env
nano /path/to/config.env

# Add these lines:
GEMINI_API_KEY=your_actual_gemini_api_key_here
DB_PASSWORD=your_secure_database_password
SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three
JWT_SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three
MCP_AUTH_SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three

# 5. Start services in their own terminals:
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server

# 6. Verify
curl http://localhost:8000/health

# ✅ Done! Running in Standalone mode
```

---

## Example: Complete Ubuntu Deployment (Vault)

```bash
# 1. Install database
sudo apt install -y mariadb-server
sudo mysql_secure_installation
sudo mariadb -u root -p -e "CREATE DATABASE kb_chunks;"

# 2. Install Vault
wget https://releases.hashicorp.com/vault/1.15.0/vault_1.15.0_linux_amd64.zip
unzip vault_1.15.0_linux_amd64.zip
sudo mv vault /usr/local/bin/

# 3. Start Vault
vault server -dev &
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# 4. Store secrets in Vault
vault kv put secret/rag-in-a-box \
  GEMINI_API_KEY="your_actual_gemini_api_key" \
  DB_PASSWORD="your_secure_database_password" \
  SECRET_KEY="your_generated_secret_key"

# 5. Install application
sudo apt install -y ./ai-nexus.deb

# 6. Configure (Vault mode - connection info only)
cp /opt/rag-in-a-box/config/config.env.template /path/to/config.env
nano /path/to/config.env

# Add these lines:
VAULT_ADDR=http://127.0.0.1:8200
VAULT_TOKEN=your_vault_root_token
VAULT_SECRET_PATH=rag-in-a-box
VAULT_MOUNT_POINT=secret

# 7. Start services in their own terminals:
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server

# 8. Verify
curl http://localhost:8000/health

# ✅ Done! Running in Vault mode
# Application fetched secrets from Vault at startup
```

---

## Summary

**One Package** (`ai-nexus.deb`) contains RAG API + MCP Server

**Two Deployment Options**:
1. Ubuntu Native (install .deb directly)
2. Docker (wrap .deb in container)

**Four Secret Modes** (choose one):
1. Standalone (secrets in config file)
2. Local Vault (secrets in local Vault)
3. 1Password (secrets in 1Password)
4. HCP Vault (secrets in cloud Vault)

**The application is the same - only the deployment location and secret source change.**

---

## Which Documentation to Read?

| Your Situation | Read This |
|----------------|-----------|
| Have Ubuntu, want simplest setup | `UBUNTU_DEPLOYMENT_GUIDE.md` (Standalone section) |
| Have Ubuntu, want Vault | `UBUNTU_DEPLOYMENT_GUIDE.md` + Vault setup |
| Have Windows, want Docker | `DOCKER_DEPLOYMENT_GUIDE.md` (Standalone section) |
| Have Windows, want Docker + Vault | `DOCKER_DEPLOYMENT_GUIDE.md` (Vault section) |
| Need to understand architecture | `TECHNICAL_ARCHITECTURE.md` |
| Need step-by-step checklist | `DEPLOYMENT_CHECKLIST.md` |

---

**Is this clearer now?** The key insight is:
- **Same package** everywhere
- **Choose where** to deploy (Ubuntu or Docker)
- **Choose how** to manage secrets (Standalone/Vault/1Password/HCP)
