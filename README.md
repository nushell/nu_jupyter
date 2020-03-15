# Jupyter Notebook support for Nushell

This is a very(!) experimental kernel for Jupyter for running Nushell. It currently requires 0.11.1 or later.

To install and run the kernel:

```
> cd nu_jupyter
nu_jupyter> jupyter kernelspec install ../nu_jupyter --user
nu_jupyter> jupyter lab
```

Limitations:

* This currently is limited to single line commands to Nu. We'd like to lift this limitation in the future.
