# Inowas Datadropper Service

With this service you can store text-based data un a Server, which will be stored, returning the hash of the content.

you can retrieve the data by making a GET-Request to the service.

## Store Data (with [httpie](https://httpie.org/))

```
http --json POST <url> http --json --verbose POST 'https://datadropper.inowas.com' data='{["timeStamp": 1, "value": 10]}'

POST / HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 47
Content-Type: application/json
Host: <url>
User-Agent: HTTPie/1.0.3

{
    "data": "{[\"timeStamp\": 1, \"value\": 10]}"
}

HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Content-Length: 61
Content-Type: application/json
Date: Fri, 25 Oct 2019 10:44:06 GMT
Server: Werkzeug/0.14.1 Python/3.6.7

{
    "filename": "3ae9b195bae56f39e2a9a758cfe83c0e9848bb91.json"
}
```


## Retrieve Data (with [httpie](https://httpie.org/))

```
http --json --verbose GET 'https://<url>/3ae9b195bae56f39e2a9a758cfe83c0e9848bb91.json'
GET /3ae9b195bae56f39e2a9a758cfe83c0e9848bb91.json HTTP/1.1
Accept: application/json, */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Type: application/json
Host: <url>
User-Agent: HTTPie/1.0.3



HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Content-Length: 47
Content-Type: application/json
Date: Fri, 25 Oct 2019 10:47:21 GMT
Server: Werkzeug/0.14.1 Python/3.6.7

{
    "data": "{[\"timeStamp\": 1, \"value\": 10]}"
}

```