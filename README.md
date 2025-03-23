# 🛍️ Tech Market Backend

This project is a **backend API** built using **Django & Django Rest Framework (DRF)** to enable users to buy and sell technology products securely. It provides authentication, permissions, and user management features.

## 📌 About the Project

The backend API enables users to:
- 🛒 List, update, and delete their own technology products
- 🔑 Register, authenticate, and manage their profiles securely
- 🔍 Browse products added by other users
- 🛡️ Restrict access based on API key authentication

## 🚀 Technologies Used

- **Python** – Core programming language
- **Django** – Web framework for building robust applications
- **Django Rest Framework (DRF)** – For API development
- **SQLite** – Database for storing user and product information
- **Docker & Nginx** – For containerization and deployment

## 🔧 Installation & Setup

Follow these steps to set up and run the backend locally:

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/aykhanko/API-E-Commerce-DB-Sqlite.git
```

### 2️⃣ Navigate to the project directory:
```bash
cd API-E-Commerce-DB-Sqlite
```

### 3️⃣ Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 4️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 5️⃣ Apply migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```
Then visit: [http://localhost:8000](http://localhost:8000)

## 🔥 Key Features

- **Authentication & Security**: Uses token-based authentication
- **Permissions**: Only authenticated users can manage their own products and profiles
- **Product Listings**: Users can browse and view all available products
- **Profile Management**: Each user has their own profile for selling products

## 🌍 Deployment

The backend API is **Dockerized and deployed using Nginx** on a **free hosting platform**.
