# E-Commerce Chatbot Application

## Overview
This repository contains a Django-based web application with basic authentication features (register, login, and logout) and product management functionalities. The application also integrates Botpress, a conversational AI platform, for enhanced user interaction capabilities. 🌟🌟🌟

### Features
- **Authentication**: User registration, login, and logout functionalities.
- **Product Management**: Display a list of products and individual product details.
- **Botpress Integration**: Enhance user experience by providing chatbot functionalities powered by Botpress.

---

## Technology Stack

| **Category**            | **Technology/Framework**                          |
|-------------------------|---------------------------------------------------|
| **Backend Framework**   | Django (Python)                                   |
| **Frontend Framework**  | HTML, CSS, Bootstrap                              |
| **Database**            | SQLite                                            |
| **Chatbot Framework**   | BotPress                                        |
| **User Authentication** | Django Authentication System                      |
| **Styling**             | Bootstrap                                         |
| **API**                 | Django REST Framework (JsonResponse)              |

---

## Project Setup

### Prerequisites
- Python 3.8 or higher. 🐍🐍🐍
- Pip package manager. 📦📦📦

### Installation Steps

1. **Clone the Repository**: 🌐🌐🌐
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies**: 🛠️🛠️🛠️
   ```bash
   pip install django
   ```

3. **Project Structure**: 🗂️🗂️🗂️
   Ensure the following directory layout:
   ```
   MyApp/
   ├── models.py
   ├── views.py
   ├── templates/
   │   ├── index.html
   │   ├── show.html
   │   └── auth/
   │       └── register.html
   │       └── login.html
   └── static/
   ```
   
4. **Database Setup**: 💾💾💾
   - Configure the database in `settings.py` (SQLite by default).
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Static Files**: 📂📂📂
   - Collect static files:
     ```bash
     python manage.py collectstatic
     ```

---

## Execution Instructions

1. **Start the Development Server**: 🚀🚀🚀
   ```bash
   python manage.py runserver
   ```

2. **Access the Application**: 🌐🌐🌐
   Open a browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

3. **Authentication**: 🔑🔑🔑
   - Register at `/register` to create an account.
   - Log in at `/login`.

4. **Product Views**: 🛍️🛍️🛍️
   - Access product listing at `/`.
   - View specific product details at `/show/<id>`.

5. **Logout**: ❌❌❌
   - Log out via `/logout`.

---

## Sample Data
### Chatbot Training Data
```json
{
    "listToTrain": [
        ["Hi", "Hello! How can I assist you?"],
        ["Bye", "Goodbye! Have a great day!"],
        ["What is your name?", "I am your chatbot assistant."]
    ]
}
```

---

## Future Enhancements

1. **Enhanced Chatbot Training**: 🤖🤖🤖
   - Incorporate larger, diverse datasets for better accuracy.

2. **Security Improvements**: 🔐🔐🔐
   - Re-enable CSRF protection and implement HTTPS for production.

3. **Scalability**: 📈📈📈
   - Transition to a production-grade database like PostgreSQL.

4. **UI Enhancements**: 🎨🎨🎨
   - Use AJAX for dynamic chatbot responses.

5. **Deployment**: ☁️☁️☁️
   - Deploy on cloud platforms (e.g., AWS, Heroku) with CI/CD pipelines.

---

## Contact
For any inquiries, please contact: 📧📧📧
- **Name**: Shashant
- **Email**: shashantyashu2004@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/shashant-yashu-383718338?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app 

