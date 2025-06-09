# mysql\_thread\_end

## Syntax

```c
void mysql_thread_end(void );
```

## Description

The mysql\_thread\_end() function needs to be called before a client thread ends. It will release thread specific memory, which was allocated by a previous [mysql\_thread\_init()](mysql_thread_init.md) call. Returns void.

{% hint style="info" %}
Unlike [mysql\_thread\_init()](mysql_thread_init.md) mysql\_thread\_end() will not be invoked automatically if the thread ends. To avoid memory leaks mysql\_thread\_end() must be called explicitly.
{% endhint %}

## See also

* [mysql\_thread\_init()](mysql_thread_init.md)
* [mysql\_thread\_safe()](mysql_thread_safe.md)

{% @marketo/form formid="4316" %}
