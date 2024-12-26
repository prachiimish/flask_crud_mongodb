# CRUD Flask Application with MongoDB

This project demonstrates how to create a simple CRUD (Create, Read, Update, Delete) API with Flask and MongoDB. It uses RESTful endpoints to perform operations on a `User` resource, and MongoDB as the database to store user information.

## Prerequisites
- **Python 3.7+**: Install Python from [python.org](https://www.python.org/downloads/)
- **MongoDB**: Install MongoDB from [mongodb.com](https://www.mongodb.com/try/download/community)
- **pip**: Python's package installer (usually comes with Python)
- **Docker** (optional for containerization): Download and install from [docker.com](https://www.docker.com/products/docker-desktop)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prachiimish/flask_crud_mongodb.git
   cd flask_crud_mongodb
   ```

2. **Create and activate a virtual environment:**

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary Python packages, including `Flask`, `pymongo`, and `Flask-PyMongo`.

4. **Start MongoDB**: Ensure MongoDB is running on your local machine.

   - On macOS/Linux: 
     ```bash
     sudo service mongod start
     ```
   - On Windows, start the MongoDB service via the MongoDB Compass application or from the command line.

## Project Structure

Here's an overview of the project structure:

```
/flask_crud-mongodb
│
├── /app                  # Main application folder
│   ├── __init__.py       # Initialize the Flask app
│   ├── routes.py         # Define the REST API routes (CRUD operations)
│
├── /venv                 # Virtual environment folder (use `python -m venv venv` to create it)
│
├── Dockerfile            # Dockerfile for containerizing the application
├── docker-compose.yml    # Docker Compose file for running the app with MongoDB
├── requirements.txt      # Python dependencies (Flask, pymongo, etc.)
├── run.py                # The entry point to run the app
└── README.md             # Project documentation            
            
```

## Running the Application

1. **Run the Flask application:**

   After installing the dependencies, run the Flask app:

   ```bash
   python3 run.py
   ```

2. **Access the app**: The Flask app will be accessible at:

   ```
   http://127.0.0.1:5000
   ```

   You can access the API endpoints using Postman or any API client.

## API Endpoints

This application provides the following RESTful endpoints to interact with the `User` resource:

- **GET** `/users`:
  - Retrieve a list of all users in the database.

- **GET** `/users/<id>`:
  - Retrieve a user by their unique ID.

- **POST** `/users`:
  - Create a new user in the database.
  - Body:
    ```json
    {
      "id": "123",
      "name": "John Doe",
      "email": "john.doe@example.com",
      "password": "secure"
    }
    ```

- **PUT** `/users/<id>`:
  - Update an existing user by their unique ID.
  - Body:
    ```json
    {
      "id": "456",
      "name": "John Smith",
      "email": "john.smith@example.com",
      "password": "secure"
    }
    ```

- **DELETE** `/users/<id>`:
  - Delete a user by their unique ID.

## Testing the API

You can test the API using Postman or any REST client. Here are the steps to test:

1. **GET** `/users`: To get all users
2. **GET** `/users/<id>`: To get a user by ID
3. **POST** `/users`: To create a new user
4. **PUT** `/users/<id>`: To update a user
5. **DELETE** `/users/<id>`: To delete a user


## Docker Setup 

If you prefer to run the app in a Docker container, follow these steps:

1. **Build the Docker image**:

   ```bash
   docker build -t flask-mongodb-crud .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 5000:5000 flask-mongodb-crud
   ```

The app will be accessible at `http://127.0.0.1:5000` inside the Docker container.
