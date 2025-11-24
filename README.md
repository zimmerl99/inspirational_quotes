# Quote Microservice Help

**Endpoint:** GET /quotes

## Example Request
```python
# request from the url and port that you are running the api from
response = requests.get("http://127.0.0.1:8001/quotes")

if response.status_code == 200:
    data = response.json()
    quote_string = data['data']
    print(quote_string)
```

## Example Response
```json
{
    "data": "The only way to do great work is to love what you do. - Steve Jobs"
}
```

## Response Fields

- `data`: String containing an inspirational quote

## Notes

- Returns a random inspirational quote on each request
- No request body required
- Simple GET endpoint with no parameters
