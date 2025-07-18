# Error 3030: Slave worker has stopped after at least one previous worker encountered an error when sl

| Error Code | SQLSTATE | Error                                            | Description                                                                                                                                                                                                                                                                                                                  |
| ---------- | -------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3030       |          | ER\_SLAVE\_WORKER\_STOPPED\_PREVIOUS\_THD\_ERROR | Slave worker has stopped after at least one previous worker encountered an error when slave-preserve-commit-order was enabled. To preserve commit order, the last transaction executed by this thread has not been committed. When restarting the slave after fixing any failed threads, you should fix this worker as well. |

## Possible Causes and Solutions

{% hint style="success" %}
This article doesn't currently contain any content. [You can help!](../../../../../about/readme/contributing-documentation.md)
{% endhint %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
