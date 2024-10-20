## Overview

This REST API was developed with Python, FastAPI, and Pydantic(for validation and error handling) to solve the [water jug problem](https://www.geeksforgeeks.org/two-water-jug-puzzle/). It provides the ideal solution, step-by-step, as a JSON response. 

The API endpoint is "/water-jug-calculator", an HTTP POST operation. It takes a JSON as a request parameter and returns a JSON object with an array of objects, each object in the array representing a step. 

## Algorithm

A BFS algorithm is used for this calculation, it guarantees finding the optimal solution with O(n*m) time complexity, with n and m representing the jug capacities. 

## Setup

Make sure you have Python installed. 

Clone this repository and add it to your local. Then install the dependencies:
```
pip install pydantic
pip install "fastapi[standard]"
```

Then navigate to the project folder and run the app from the command line: 
```
fastapi dev main.py
```

The terminal output will provide a link to the swagger docs(in my case it was: http://localhost:8000/docs), use them to test the API endpoint using the "Try it out" button

# Request and response formats, with samples:
## Solution found
### A
```
{
  "x_capacity": 10,
  "y_capacity": 8,
  "z_amount_wanted": 2
}
```
HTTP 200 Successful Response:
```
{
  "solution": [
    {
      "step": 1,
      "bucketX": 10,
      "bucketY": 0,
      "action": "Fill bucket X"
    },
    {
      "step": 2,
      "bucketX": 2,
      "bucketY": 8,
      "action": "Transfer from bucket X to bucket Y"
    }
  ]
}
```
### B
```
{
  "x_capacity": 3,
  "y_capacity": 9,
  "z_amount_wanted": 6
}
```
HTTP 200 Successful Response:
```
{
  "solution": [
    {
      "step": 1,
      "bucketX": 0,
      "bucketY": 9,
      "action": "Fill bucket Y"
    },
    {
      "step": 2,
      "bucketX": 3,
      "bucketY": 6,
      "action": "Transfer from bucket Y to bucket X"
    }
  ]
}
```

## No solution
```
{
  "x_capacity": 3,
  "y_capacity": 9,
  "z_amount_wanted": 20
}
```
HTTP 200 Successful Response:
```
{
  "solution": "No solution..."
}
```

## Error: non-numerical input 
```
{
  "x_capacity": 3,
  "y_capacity": 9,
  "z_amount_wanted": ab
}
```
HTTP 422	Unprocessable Entity:
```
{
  "detail": [
    {
      "type": "json_invalid",
      "loc": [
        "body",
        61
      ],
      "msg": "JSON decode error",
      "input": {},
      "ctx": {
        "error": "Expecting value"
      }
    }
  ]
}
```

## Error: fractional/decimal input 
```
{
  "x_capacity": 3,
  "y_capacity": 9,
  "z_amount_wanted": 2.5
}
```
HTTP 422	Unprocessable Entity:
```
{
  "detail": [
    {
      "type": "int_from_float",
      "loc": [
        "body",
        "z_amount_wanted"
      ],
      "msg": "Input should be a valid integer, got a number with a fractional part",
      "input": 2.5
    }
  ]
}
```

## Error: non-positive input
```
{
  "x_capacity": 3,
  "y_capacity": 9,
  "z_amount_wanted": -4
}
```
HTTP 422	Unprocessable Entity:
```
{
  "detail": [
    {
      "type": "greater_than",
      "loc": [
        "body",
        "z_amount_wanted"
      ],
      "msg": "Input should be greater than 0",
      "input": -4,
      "ctx": {
        "gt": 0
      }
    }
  ]
}
```
