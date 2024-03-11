This will only work on Linux or MacOS

```bash
chmod +x setup.sh
./setup.sh




chmod +x run.sh
./run.sh
```


To test the API

```bash
curl --location '127.0.0.1:5000/process_image?image=null' \
--form 'image=@"postman-cloud:///1eedfc57-04f4-4a60-84a2-181aaf3015e7"'
```

result

```json
{
    "discounts": {},
    "items": {
        "Pep Mocha": 4.95
    },
    "taxes": {}
}
```
