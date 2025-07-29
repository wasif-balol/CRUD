# 🛠️ CRUD – Django Practice App

> A Python and Django-based practice application to demonstrate the four fundamental database operations:  
> **Create**, **Retrieve**, **Update**, and **Delete** using class-based views and Jinja templating.

---

## 🚀 Features

- 🔁 Fully functional CRUD operations
- 🧱 Built with **Django** backend and **Jinja templates** on the frontend
- 🧩 Uses **Class-Based Views (CBVs)** for clean separation of logic
- 📋 Implements Django’s `ListView` for efficient data retrieval
- 📝 Simple and clean user interface to interact with database records

---

## 🧰 Requirements

- Python: `3.5` – `3.8`
- Django (version specified in `requirements.txt`)
- Recommended: Use a **Python virtual environment**

---

## 💻 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/wasif-balol/CRUD.git

# 2. Navigate to the project directory
cd CRUDApplication

# 3. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate       # 📌 On Windows: venv\Scripts\activate

# 4. Install project dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver
