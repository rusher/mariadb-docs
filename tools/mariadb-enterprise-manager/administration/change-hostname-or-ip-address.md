# Change hostname or IP address

To set the hostname or IP address for an existing MariaDB Enterprise Management instance, follow these instructions. Changing the hostname or IP address is useful if your server's IP changed or if you need to switch from an IP address to a public DNS name.

{% stepper %}
{% step %}
### Connect to your server

SSH into the server where your Enterprise Manager is running:

{% code title="# Connect via SSH" %}
```bash
ssh user@your-server-ip
```
{% endcode %}
{% endstep %}

{% step %}
### Navigate to the directory

Change into the `enterprise-manager` directory, where your Docker Compose files are located:

{% code title="# Change directory" %}
```bash
cd enterprise-manager
```
{% endcode %}
{% endstep %}

{% step %}
### Edit the `.env` file

Open the environment file with a text editor (for example `nano`):

{% code title="# Open .env" %}
```bash
nano .env
```
{% endcode %}

Find the line that begins with `MEMA_HOSTNAME=` and update it with the new hostname or IP address. Example:

{% code title="# .env example" %}
```env
MEMA_HOSTNAME=your.new.hostname.or.ip
```
{% endcode %}
{% endstep %}

{% step %}
### Save the file

Save the file and exit the editor
{% endstep %}

{% step %}
### Restart the services

Restart the MEM services so the new environment variable takes effect. The `--force-recreate` flag ensures the containers are rebuilt using the updated environment variables:

{% code title="# Restart services" %}
```bash
docker compose up -d --force-recreate
```
{% endcode %}

After the restart, your Enterprise Manager will be accessible at the new hostname or IP address.
{% endstep %}
{% endstepper %}
