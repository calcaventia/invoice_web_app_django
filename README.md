#Quick Invoice

Quick Invoice is a an invoice management system that enables small business owners to generate invoices and send them to their clients.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

##Technologies Used

List of technologies and frameworks used in the project:
  - Django
  - Python
  - Vue

##Installation

1. Install or update Python and Django.

2. Clone the repository:

    ```bash
    git clone https://github.com/calcaventia/invoice_web_app_django.git
    ```

3. Navigate to the project directory:

    ```bash
    cd invoice_web_app_django
    ```

4. Set up virtual environment:

  For Windows:
    ```bash
    - python -m venv venv
    ```
  For macOS/Linux:
    ```bash
    - python3 -m venv venv
    ```
  
5. Activate virtual environment:

  For Windows:
    ```bash
    - venv\Scripts\activate
    ```
  For macOS/Linux:
    ```bash
    - venv\bin\activate
    ```

6. Install dependencies:

    ```bash
        pip install -r requirements.txt
    ```
 
7. Run the Django server:

    ```bash
    python manage.py runserver
    ```

##Usage

-Once the server is running, access the application in your web browser at `http://localhost:8000`.
-To access the Django admin interface, go to http://localhost:8001/admin in your web browser. Create a superuser account if needed.

