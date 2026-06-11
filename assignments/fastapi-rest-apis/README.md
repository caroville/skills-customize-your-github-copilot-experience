# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. Practice defining endpoints, handling request data with Pydantic models, and using path and query parameters.

## 📝 Tasks

### 🛠️ Set up a FastAPI Application

#### Description
Create a FastAPI application and run it locally with Uvicorn.

#### Requirements
Completed project should:

- Create a `FastAPI` app instance in `starter-code.py`
- Define a root route at `/` that returns a JSON welcome message
- Include a comment showing how to run the app with `uvicorn`

### 🛠️ Create Endpoints and Response Models

#### Description
Add API routes that return item data and accept new item requests.

#### Requirements
Completed project should:

- Define a Pydantic `Item` model with `id`, `name`, `description`, `price`, and `in_stock` fields
- Create a `GET /items/{item_id}` route that returns item details by ID
- Create a `POST /items` route that accepts an `Item` and returns the created item

### 🛠️ Use Query Parameters and Filtering

#### Description
Implement query parameters to search and filter items.

#### Requirements
Completed project should:

- Add a `GET /items` route that returns a list of items
- Accept optional query parameters such as `q` or `available`
- Use query parameters to filter the item list before returning results

### 🛠️ Add Documentation and Test the API

#### Description
Verify the API works and explore the automatic OpenAPI docs.

#### Requirements
Completed project should:

- Run the app locally and open the Swagger UI at `/docs`
- Confirm that the API returns JSON responses for each endpoint
- Keep comments or instructions in `starter-code.py` for how to test the routes
