# E-Sign Portal

E-Sign Portal is a Django-based web application where users can register their complaints, petitions, and issues, similar to iPetitions. The platform allows the public to easily raise awareness on different causes by signing petitions and gathering public support.

## Features

- **User Registration:** Users can sign up and create an account to post petitions or sign existing ones.
- **Create Petitions:** Authenticated users can create petitions, complete with a title, description, and relevant details.
- **Sign Petitions:** Users can sign petitions to show their support.
- **List of Petitions:** View a list of all current petitions on the homepage.
- **Search Petitions:** Search for petitions by title or description.
- **Responsive Design:** The site is fully responsive and mobile-friendly.

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- SQLite (or any other database you prefer)

## Setup

### 1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/esign-portal.git
   cd esign-portal
   ```

### 2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

### 3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### 4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### 5. Set up the database:

   ```bash
   python manage.py migrate
   ```

### 6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

### 7. Run the development server:

   ```bash
   python manage.py runserver
   ```

### 8. Open your browser and go to:

   ```
   http://127.0.0.1:8000
   ```
