# 🚀 Two-Tier Task Manager Application

A simple **Two-Tier Web Application** built using **Flask and MySQL**, containerized with **Docker** and orchestrated using **Docker Compose**.

This project demonstrates basic **DevOps practices** including containerization, service networking, environment variables, and persistent storage.

---

# 🏗️ Architecture

User → Flask Web Application → MySQL Database

## 📁 Project Structure

```
two-tier-task-app/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── db/
│   └── init.sql
│
├── docker-compose.yml
├── Dockerfile
├── .gitignore
└── README.md
```

# ⚙️ Technologies Used

- Python (Flask)
- MySQL
- Docker
- Docker Compose
- Linux
- Git & GitHub

---

# 🐳 Features

- Two-tier architecture
- Containerized application
- MySQL database persistence
- Docker networking between services
- Environment variable configuration

---

# ▶️ How to Run the Project

Clone the repository

```bash
git clone https://github.com/yashgondaliy/two-tier-task-app.git
cd two-tier-task-app
```
Run the code
```
git compose up -d
git compose down
