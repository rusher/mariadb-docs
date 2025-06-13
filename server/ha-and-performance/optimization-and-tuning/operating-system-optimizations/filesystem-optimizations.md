# Filesystem Optimizations

## Which filesystem is best?

The filesystem is not the most important aspect of MariaDB performance. Far more important are available RAM, drive speed, the system variable settings (see [Hardware Optimization](../hardware-optimization.md) and [System Variables](../system-variables/)).

Optimizing the filesystem can however in some cases make a noticeable difference. Currently, the best Linux filesystems are generally regarded as ext4, XFS and Btrfs. They are all included in the mainline Linux kernel, and are widely supported and available on most Linux distributions. Red Hat though regards Brtfs as a technology preview, not yet ready for production systems.

The following theoretical file size and filesystem size limits apply to the three filesystems:

| ext4                | XFS  | Brtfs |
| ------------------- | ---- | ----- |
|                     | ext4 | XFS   |
| Max file size       | 16TB | 8EB   |
| Max filesystem size | 1 EB | 8EB   |

Each has unique characteristics that are worth understanding to get the most from.

## Disabling access time

It's unlikely you'll need to record file access time on a database server, and mounting your filesystem with this disabled can give an easy improvement in performance. To do so, use the `noatime` option.

If you want to keep access time for [log files](../../../server-management/server-monitoring-logs/) or other system files, these can be stored on a separate drive.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
