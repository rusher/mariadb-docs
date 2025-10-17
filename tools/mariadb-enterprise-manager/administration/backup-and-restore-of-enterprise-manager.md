# Backup & Restore of Enterprise Manager

Note: This is about backing up Enterprise Manager (EM), not the databases.

## Backing up Enterprise Manager Server

{% stepper %}

{% step %}
## Stop the Enterprise Manager
1. Go to the Enterprise Manager installation directory
2. Run `docker compose stop` to stop the Enterprise Manager
{% endstep %}

{% step %}
## Create a directory for backups

{% code title="Create the `backups` directory" %}
```bash
mkdir backups
```
{% endcode %}
{% endstep %}


{% step %}
## Take a backup of all the volumes

{% code title="Back up all volumes" %}
```bash
docker run --rm --volumes-from enterprise-manager-grafana -v $(pwd)/backups/:/backups/ alpine:latest tar -czf /backups/grafana-backup.tar.gz /var/lib/grafana/
docker run --rm --volumes-from enterprise-manager-prometheus -v $(pwd)/backups/:/backups/ alpine:latest tar -czf /backups/prometheus-backup.tar.gz /prometheus/
docker run --rm --volumes-from enterprise-manager-supermax -v $(pwd)/backups/:/backups/ alpine:latest tar -czf /backups/supermax-backup.tar.gz /var/lib/supermax/
```
{% endcode %}

The `backups` directory now contains the data from the Enterprise Manager.
{% endstep %}

{% endstepper %}

## Restoring Enterprise Manager Server

Instruction to restore Enterprise Manager server
