# SMTP server configuration

This page explains how to configure email alerting for MariaDB Enterprise Manager using Grafana's integrated alerting engine. Configure SMTP credentials and server details in the main environment file so Enterprise Manager can send alert notifications via email.

This is an advanced draft.

{% stepper %}
{% step %}
### Edit the environment file

1. Navigate to your MariaDB Enterprise Manager installation directory:

{% code title="Shell" %}
```bash
cd enterprise-manager/
```
{% endcode %}

2. Open the `.env` file in a text editor (example uses nano):

{% code title=".env (open with nano)" %}
```bash
nano .env
```
{% endcode %}

3. Add the following block of variables to the file, filling in values for your SMTP server:

{% code title=".env (SMTP settings)" %}
```env
# --- Grafana SMTP Email Settings ---
# Set to true to enable email alerting
GF_SMTP_ENABLED=true

# Your SMTP server hostname and port
GF_SMTP_HOST=smtp.example.com:587

# Credentials for your SMTP user
GF_SMTP_USER=my-email-user
GF_SMTP_PASSWORD=my-super-secret-password

# Set to true if your server uses a self-signed certificate
GF_SMTP_SKIP_VERIFY=false

# The "From" address that will appear on alert emails
GF_SMTP_FROM_ADDRESS=alerts@my-domain.com

# The display name for the sender
GF_SMTP_FROM_NAME=MariaDB Enterprise Manager
```
{% endcode %}

4. Save the file and exit the editor.
{% endstep %}

{% step %}
### Restart the Grafana service

The new settings are applied only after Grafana restarts.

From the `enterprise-manager/` directory, restart only the Grafana container so other Enterprise Manager components are not affected:

{% code title="Restart Grafana container" %}
```bash
# Take down the existing Grafana container
docker compose down grafana

# Start a new Grafana container with the updated configuration
docker compose up -d grafana
```
{% endcode %}
{% endstep %}

{% step %}
### Verify the configuration in Grafana

After Grafana restarts:

* Open the Grafana UI.
* Create a new "Contact point".
* Use the "Test" button to send a test email and confirm that SMTP settings are correct and Enterprise Manager can send alerts.
{% endstep %}
{% endstepper %}
