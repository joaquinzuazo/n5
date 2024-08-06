
# Traffic Infraction Registration System

This project is the frontend for the Traffic Infraction Registration System, built with React. It provides an administrative interface to manage records of people, vehicles, and officers, as well as allowing officers to log in and view their own records.



## Features

- **Manage records for**:
    - Person: Name and email.
    - Vehicle: License plate, brand and color, related to a person.
    - Officer: Name and a unique badge number.

- **Authentication**: Uses JWT tokens for secure access to the API. An admin officer is created with badge number `12345` and password `password1`.

## Project Structure

- **src/components**: Contains the React components for the application.
- **src/context**: Contains the authentication context.
- **src/pages**: Contains the pages for the application.

## Requirements
- Node.js
- Docker (optional for containerized execution)
## Installation

#### Using Node.js

- Navigate to the `/front` directory.
-  Install the required dependencies:

```bash
  npm install
```

- Run the application

```bash
  npm start
```

or 

```bash
  npm run dev
```

#### Using Docker

- Navigate to the /front directory.
- Build the Docker image:

```bash
  docker build -t n5_front .
```

- Run the Docker container:

```bash
  docker run -d -p 3000:80 n5_front
```

#### Using Docker Compose

- From the root directory
- Build and start the services:

```bash
  docker-compose up --build -d api
```
## Authors

- [@joaquinzuazo](https://gitlab.com/jzuazo1)