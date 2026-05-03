# 🔍 Lost & Found

A Django-based web application for reporting and discovering lost and found items. Users can post items they've lost or found, browse listings, and connect with others to reunite people with their belongings.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- Post lost or found item listings
- Browse and search items by category or location
- User authentication (register, login, logout)
- Manage your own listings
- Responsive UI

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default Django)
- **CI/CD:** GitHub Actions

---

## 📁 Project Structure

```
Lost-found/
├── .github/
│   └── workflows/        # GitHub Actions CI/CD pipelines
├── home/                 # Home app (landing page, dashboard)
├── items/                # Items app (lost/found listings logic)
├── lost_and_found/       # Core Django project settings
├── templates/            # HTML templates
├── users/                # User authentication app
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Komil-goat/Lost-found.git
   cd Lost-found
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **(Optional) Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

### Running the App

```bash
python manage.py runserver
```

Then open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📖 Usage

1. Register for an account or log in.
2. Post a **Lost** item if you've lost something, or a **Found** item if you've found something.
3. Browse listings to see if your item has been found (or claimed).
4. Contact the poster to arrange a meetup and return the item.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the [Apache-2.0 License](LICENSE).
