# E-Commerce Chatbot Application

## Overview
This project is a Django-based e-commerce platform integrated with an AI-driven chatbot. It provides features like user authentication, dynamic product listing, detailed product views, and an interactive chatbot for user assistance. The application is designed to offer a seamless user experience while showcasing the integration of web technologies with AI. 🌟🌟🌟

---

## Features

### User Authentication
- Secure user registration, login, and logout functionalities. 🔒🔒🔒
- Built using Django's authentication system. 🛠️🛠️🛠️

### Chatbot Integration
- AI-powered chatbot using ChatterBot. 🤖🤖🤖
- Responds to predefined user queries with fallback mechanisms for unknown inputs. 💬💬💬

### Product Management
- Dynamic listing of products stored in the database. 🛍️🛍️🛍️
- Individual product detail views. 📄📄📄

### Frontend Design
- Responsive and user-friendly interface designed with Bootstrap. 🎨🎨🎨

---

## Technology Stack

| **Category**            | **Technology/Framework**                          |
|-------------------------|---------------------------------------------------|
| **Backend Framework**   | Django (Python)                                   |
| **Frontend Framework**  | HTML, CSS, Bootstrap                              |
| **Database**            | SQLite                                            |
| **Chatbot Framework**   | ChatterBot                                        |
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
   pip install chatterbot==1.0.5 chatterbot_corpus
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
       └── js/
           └── data.json
   ```

4. **Database Setup**: 💾💾💾
   - Configure the database in `settings.py` (SQLite by default).
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Load Chatbot Training Data**: 📊📊📊
   - Ensure `static/js/data.json` contains:
     ```json
     {
         "listToTrain": [
             ["Hi", "Hello! How can I assist you?"],
             ["Bye", "Goodbye! Have a great day!"]
         ]
     }
     ```

6. **Static Files**: 📂📂📂
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

4. **Interact with Chatbot**: 💬💬💬
   - Send queries via `/get_response` with the `userMessage` query parameter.

5. **Product Views**: 🛍️🛍️🛍️
   - Access product listing at `/`.
   - View specific product details at `/show/<id>`.

6. **Logout**: ❌❌❌
   - Log out via `/logout`.

---

## Sample Data
### Chatbot Training Data (`data.json`)
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

## License
This project is licensed under the MIT License. See the `LICENSE` file for details. 📜📜📜

---

## Contact
For any inquiries, please contact: 📧📧📧
- **Name**: [Your Name]
- **Email**: [Your Email]
- **LinkedIn**: [Your LinkedIn Profile]

