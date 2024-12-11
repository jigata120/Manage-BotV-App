# vevn
- create and activate:
     ```bash
      python -m venv vevn
      source ./venv/bin/activate 
# Requirements: 
- command
    ```bash
        pip freeze > requirements.txt

# Database Setup

- The app requires initial data to function correctly. Use the following pre-configured database credentials in your `.env` file:
Follow these steps:
1. Copy the `.env` file from this Google docs to your `.env`:
   https://docs.google.com/document/d/19rYhp5h2gJuBBxF73XGrrN4ms9kQeJXCAmepEXsOYww/edit?usp=sharing
2. Apply migrations:
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
# Run server
- bash command
   ```bash
        uvicorn ChatbotManager.asgi:application --host 127.0.0.1 --port 8080 --reload
# Initial accounts:
1. Admin 
    - superuser
    - Group: Administrators
    - login credentials
      - username: admin
      - pass: admin
2. Support
   - staff
    - Group: Support
    - login credentials
      - username: support
      - pass: 123admin123
3. User
   - login credentials
     - username: user
     - pass: nonadmin

# Run tests: 
  ```bash
     python manage.py test Chatbots.tests --keepdbw