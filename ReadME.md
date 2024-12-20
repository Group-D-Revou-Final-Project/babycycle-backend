# The Backend API for babycycle.my.id

## Overview
This repository contains the backend API for the babycycle platform, developed to manage various functionalities including user management, cart operations, transactions, and more. It is built using Python with Flask and integrates PostgreSQL (via Supabase) as the database.

---

## Deployment and Documentation
- **API Documentation:** [https://api.ahmadcloud.my.id/apidocs](https://api.ahmadcloud.my.id/apidocs)
- **Deployed Backend:** [https://api.ahmadcloud.my.id](https://api.ahmadcloud.my.id)

---

## GitHub Repository
- **Repository Link:** [https://github.com/Group-D-Revou-Final-Project/babycycle-backend.git](https://github.com/Group-D-Revou-Final-Project/babycycle-backend.git)

---

## Tech Stack
- **Programming Language:** Python
- **Framework:** Flask
- **Database:** PostgreSQL (Supabase)
- **Dependency Management:** Poetry
- **Containerization:** Docker

---

## Features
- User Authentication and Authorization (JWT based)
- Cart and Order Management
- Product CRUD Operations
- API Documentation with Swagger
- Deployment-ready with Docker

---

## Installation and Setup

### Prerequisites
- Python (>= 3.8)
- Docker
- Poetry
- PostgreSQL

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Group-D-Revou-Final-Project/babycycle-backend.git
   cd babycycle-backend
   ```

2. **Set Up Virtual Environment:**
   ```bash
   poetry install
   poetry shell
   ```

3. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and configure the following:
   ```env
   FLASK_ENV=development
   DATABASE_URL=your_postgres_database_url
   SECRET_KEY=your_secret_key
   RESET_PASSWORD_SALT=your_reset_password_salt
   ```

4. **Run Database Migrations:**
   ```bash
   flask db upgrade
   ```

5. **Start the Development Server:**
   ```bash
   flask run
   ```
   The API will be available at `http://127.0.0.1:5000`.

---

## Docker Setup

1. **Build the Docker Image:**
   ```bash
   docker build -t babycycle-backend .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 5000:5000 babycycle-backend
   ```

3. **Access the API:**
   Open `http://127.0.0.1:5000` in your browser.

---

## Testing

Run unit tests using the following command:
```bash
pytest
```

---

## API Documentation
Interactive API documentation is available at:
- [Swagger Docs](https://api.ahmadcloud.my.id/apidocs)

---

## Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature description'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For any queries or support, please contact the development team via the repository's issue tracker.

