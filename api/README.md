# Traffic Infraction Registration System

This project is a system for registering traffic infractions, built with FastAPI and SQLAlchemy. It allows administrators to manage records of people, vehicles, and officers, as well as providing an API for police officers to record traffic infractions.


## Features

- **Manage records for**:
    - Person: Name and email.
    - Vehicle: License plate, brand and color, related to a person.
    - Officer: Name, unique plate number and role. The latter can be OFFICER or ADMIN

- **Authentication**: Uses JWT tokens for secure access to the API. An admin officer is created with badge number `12345` and password `password1`.

- **Documentation**: API documentation is available at `http://localhost:8000/docs` via Swagger.

## Project Structure

- **application**: Contains use cases and interfaces.
- **infrastructure**: Handles database configurations, models, and repository implementations.
- **domain**: Contains repository interfaces and entity definitions.
- **presentation**: Includes the main application entry point, routes, and request/response models.
- **utils**: Contains utility functions including JWT token creation and validation.

## Requirements

- Python 3.11
* Docker (optional for containerized execution)

## Installation

#### Using virtual environment

- Navigate to the `/api` directory.
- Create and activate a virtual environment:

```bash
  python -m venv venv
```

- Activate the virtual environment for Windows:

```bash
  .\venv\Scripts\activate
```

- For macOS/Linux

```bash
  source venv/bin/activate
```

- Install the required dependencies:

```bash
  pip install -r requirements.txt
```

- Upgrade the database to the latest migration:

```bash
  alembic upgrade head
```

- Run the application:

```bash
  uvicorn src.presentation.api.main:app --reload
```

#### Using Docker

- Navigate to the `/api` directory.
- Build the Docker image:

```bash
  docker build -t n5_api .
```

- Run the Docker container:

```bash
  docker run -d -p 8000:8000 n5_api
```

#### Using Docker Compose

- From the root directory
- Build and start the services:

```bash
  docker-compose up --build -d api
```

## Authors

- [@joaquinzuazo](https://gitlab.com/jzuazo1)
