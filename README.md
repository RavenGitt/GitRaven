RESTful API using Python & MySQL
This repository contains a sample implementation of a RESTful API using Python and MySQL. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on a MySQL database using HTTP requests.

Prerequisites
Before running this application, ensure that you have the following installed:

Python (version 3.6 or higher)
MySQL Server
Flask (Python web framework)
Flask-RESTful (extension for building REST APIs)
MySQL Connector (Python library for connecting to MySQL)
Getting Started
1. Clone the repository:
    git clone <repository-url>
2. Create a virtual environment (optional but recommended):
    "python3 -m venv env
    source env/bin/activate"
3. Install the required dependencies:
    "pip install -r requirements.txt"
4. Configure the MySQL connection:
    Open config.py and update the MySQL database credentials according to your setup.
5. Create the necessary database tables:
    Run the following command in your terminal:
        "python create_tables.py"
6. Start the server:
    Run the following command:
        "python app.py"
The server will start running on http://localhost:5000.

API Endpoints
The API provides the following endpoints:

GET /users: Retrieve a list of all users.
GET /users/<id>: Retrieve details of a specific user.
POST /users: Create a new user.
PUT /users/<id>: Update details of a specific user.
DELETE /users/<id>: Delete a specific user.
Replace <id> with the user ID when making requests to the corresponding endpoints.

Request and Response Examples
GET /users
    Request:
        GET /users
Response:
        HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
]

GET /users/<id>
Request:
        GET /users/1
Response:
        HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}

POST /users
Request:
        POST /users
Content-Type: application/json

{
  "name": "Alice Brown",
  "email": "alice.brown@example.com"
}

Response:
    HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 3,
  "name": "Alice Brown",
  "email": "alice.brown@example.com"
}
PUT /users/<id>
Request:
        PUT /users/3
Content-Type: application/json

{
  "name": "Alice Green"
}
Response:
        HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 3,
  "name": "Alice Green",
  "email": "alice.brown@example.com"
}
DELETE /users/<id>
Request:
   DELETE /users/3
Response:
        HTTP/1.1 204 No Content
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

License
This project is licensed under the MIT License.
