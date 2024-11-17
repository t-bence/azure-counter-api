# azure-counter-api

A simple visitor counter implemented in Azure Functions.

To add object storage file handling to get and update the count, start from:

```
@app.blob_input(arg_name="input",
                path="visitors/count.txt",
                connection="<BLOB_CONNECTION_SETTING>")
@app.blob_output(arg_name="output",
                path="visitors/count.txt",
                connection="<BLOB_CONNECTION_SETTING>")
```