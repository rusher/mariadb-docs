# Enterprise-Grade Authentication

A cornerstone of the Enterprise edition is its ability to integrate with centralized secret managers, eliminating the need for static credentials stored in `.env` files. The server dynamically fetches database credentials and API keys at startup, ensuring a secure and compliant operational posture.

### HashiCorp Vault Integration

The server can authenticate with a HashiCorp Vault instance using a specified role to retrieve MariaDB credentials and other secrets. This integration is compatible with both self-hosted Vault servers and the HashiCorp Cloud Platform (HCP).

### 1Password Integration

The server provides a mechanism to integrate with 1Password Secrets, allowing it to securely retrieve database credentials and other sensitive information at runtime.
