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
- **SMTP:** Mailtrap

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
- Python (>= 3.12)
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
   DB_URI_PROD=your_postgres_database_url
   SENDER_EMAIL=sender_mail_for_notification
   KEY_SECRET=your_secret_key
   RESET_PASSWORD_SALT=your_reset_password_salt
   JWT_SECRET=your_jwt_secret_key
   SMTP_PASSWORD="<smtp_password_from_mailtrap>"
   SMTP_USER="<smpt_user>"
   ```

4. **Run Database Migrations:**
   ```bash
   flask db init
   flask db migrate -m "Initial Migrations"
   flask db upgrade
   ```

5. **Start the Development Server:**
   ```bash
   hypercorn app:app --bind 127.0.0.1:5100 --reload
   ```
   The API will be available at `http://127.0.0.1:5100`.

---

## Docker Setup

1. **Build the Docker Image:**
   ```bash
   docker build . -t docker.io/<username>/<image_name>:<tag>
   ```

2. Create docker-compose.yaml on the parent directory
    ```bash
    services:
        app-service:
            image: "docker.io/<username>/<image_name>:<tag>"
            pull_policy: always
            container_name: "flask_app_container"
            environment:
            DB_URI_PROD: <URI_CONNECTION>
            SENDER_EMAIL: <email_sender>
            SMTP_PASSWORD: <smtp_password>
            SMTP_USER: <smtp_user>
            KEY_SECRET: <key_secret>
            JWT_SECRET: 'your_jwt_secret_key'
            RESET_PASSWORD_SALT: 'your_reset_password_salt'

            
            ports:
            - "5100:5000"
            volumes:
            - app_data:/app

            pull_policy: always
            networks:
            - apps_network

    volumes:
    app_data:

    networks:
    apps_network:
    ```

2. **Run the Docker Container from the Compose File:**
   ```bash
   docker-compose -f docker-compose-babycycle.yaml up -d
   ```

3. **Access the API:**
   Open `https://<your_domain>/apidocs` in your browser.

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