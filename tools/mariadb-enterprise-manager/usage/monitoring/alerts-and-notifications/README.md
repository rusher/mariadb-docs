# Alerts and notifications

This is an advanced draft\
Created by Stefan Hinz, last modified by Tauseef Khan on Oct 13, 2025

MariaDB Enterprise Manager provides a powerful and flexible alerting system, built on the capabilities of the integrated **Grafana Alerting** engine. It allows you to proactively monitor your entire database fleet, define custom rules for potential issues, and receive notifications through various channels to ensure you can respond quickly.

{% hint style="info" %}
This page is an advanced draft.
{% endhint %}

### How It Works: The Alerting Flow

The alerting process in MariaDB Enterprise Manager follows a clear, four-step flow from detection to notification.

{% stepper %}
{% step %}
### Alert Rule is Defined

An alert rule contains a query (what to measure, e.g., disk usage), a condition (the threshold, e.g., `> 90%`), and labels for routing (e.g., `type = server disk`).
{% endstep %}

{% step %}
### Instances are Evaluated

Grafana periodically runs the query against your monitored targets. It creates an **Alert Instance** for each distinct entity (e.g., one for Server 01, one for Server 02, etc.).
{% endstep %}

{% step %}
### An Instance "Fires"

If the condition is met for a specific instance (e.g., Server 01's disk usage is over 90%), that instance enters a "firing" state.
{% endstep %}

{% step %}
### Notifications are Sent

The firing alert is routed through a **Notification Policy**. The policy matches the alert's labels (e.g., `type = server disk`) and sends a notification to the configured **Contact Point** (such as Email, Slack, or PagerDuty).
{% endstep %}
{% endstepper %}

### Key Alerting Concepts

To configure alerting effectively, it's helpful to understand these core concepts from Grafana:

* **Alert Rules**: An alert rule is the combination of a data query and a threshold condition. This is the core of your alert, defining what you want to measure and when it should be considered a problem.
* **Alert Instances**: A single alert rule can generate multiple **Alert Instances**. For example, one rule to check CPU usage will create a separate instance for each server it monitors, allowing you to see the individual status of every server.
* **Contact Points**: This is _where_ notifications are sent. You can configure contact points for various destinations, such as email addresses, Slack channels, PagerDuty, or a generic webhook.
* **Notification Policies**: This is the "brain" of the routing system. Notification policies use labels to determine which firing alerts should be sent to which contact points. This allows you to, for example, send database-related alerts to the DBA team and OS-related alerts to the SRE team.
* **Silences and Mute Timings**: These features allow you to temporarily pause notifications without stopping the alert rules themselves. **Silences** are for one-off events like a planned maintenance window, while **Mute Timings** can be used for recurring periods, such as nights and weekends.

{% hint style="info" %}
For a deep dive into advanced topics like custom message templating, alert grouping, and more complex routing, see the official Grafana documentation:\
https://grafana.com/docs/grafana/latest/alerting/fundamentals/
{% endhint %}

## Attachments

Images attached to the original document:

\
\
\
\
\
\


(Note: image filenames and attachment paths are preserved from the source.)
