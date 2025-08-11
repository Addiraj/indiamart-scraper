# IndiaMart Scraper API

A FastAPI-based service for extracting real-time business data from IndiaMart.

## Features

- **Real-time data extraction** from IndiaMart
- **RESTful API** with FastAPI
- **CORS enabled** for web applications
- **Health check endpoint**
- **Pagination support**
- **Error handling**

## API Endpoints

### POST /search
Search for businesses on IndiaMart

**Request Body:**
```json
{
  "query": "jewellery",
  "city": "Mumbai",
  "pages": 1
}
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "name": "Rajesh Jewellers Pvt Ltd",
      "title_url": "https://...",
      "phone_number": "8045387947"
    }
  ],
  "total_results": 15,
  "message": "Successfully found 15 businesses"
}
```

### GET /health
Health check endpoint

### GET /
API information and available endpoints

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

3. Access the API at `http://localhost:8000`
4. View API docs at `http://localhost:8000/docs`

## Railway Deployment

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the configuration
3. Deploy and get your service URL

## Usage Example

```bash
curl -X POST "https://your-railway-url.railway.app/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "jewellery",
    "city": "Mumbai",
    "pages": 1
  }'
```

## Environment Variables

- `PORT`: Server port (automatically set by Railway)

## Tech Stack

- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI server
- **Requests**: HTTP library for IndiaMart API calls
- **Pydantic**: Data validation and serialization
