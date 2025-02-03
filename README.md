

User Data API - Bulk Data Insertion
===================================
This project aims to create a Django RestFramework API for inserting user data from a .csv file into a database with validation checks. The API validates various fields like email, age, username, and password to ensure that the data being inserted is accurate and meets the required criteria.

![image](https://github.com/user-attachments/assets/a27dbf05-e093-4acf-953b-7fd686c8bb2c)




Features
========
Bulk Data Insertion: Allows users to upload a .csv file containing user data and inserts it into the database.

Validation Checks:
==================

* Email: Checks if the email already exists in the database.
* Email Format: Ensures the email is in a valid format.
* Age: The age must be between 0 and 120.
* Required Fields: Ensures that all columns in the .csv file are filled.
* Username: The username must be between 6 and 120 characters.
* Password: The password must be between 8 and 25 characters.
  
Requirements
============
To run this project, make sure you have the following installed:

* Python 3.x
* Django
* Django REST Framework (DRF)
* PostgreSql (for handling Database)
* Other dependencies (see requirements.txt)

Database Schema
==========
The application contains two tables:

* user_profile_tbl (User Profile Table)
  This table stores general user information.

| Column Name      | Data Type       | Constraints        | Description |
|-----------------|---------------|-------------------|-------------|
| id              | Integer (Auto) | Primary Key       | Unique identifier for each user profile. |
| first_name      | CharField (100) | Required         | First name of the user. |
| last_name       | CharField (100) | Required         | Last name of the user. |
| age            | Integer        | Required, 0-120  | Age of the user. |
| email          | EmailField     | Required, Unique | User's email address. |
| is_active      | BooleanField   | Default: True    | Whether the user profile is active. |
| created_at     | DateTimeField  | Auto timestamp   | The time when the user profile was created. |



* user_tbl (User Authentication Table)

   This table stores authentication-related information, linking users to their profiles.

  

| Column Name      | Data Type       | Constraints        | Description |
|-----------------|---------------|-------------------|-------------|
| id              | Integer (Auto) | Primary Key       | Unique identifier for each user. |
| username      | CharField (50) | Required         | Username for authentication. |
| password       | CharField (50) | Required         | User's password. |
| user_profile_id | ForeignKey        | One-to-One  | Relation	Links to user_profile_tbl. |


Setup
=====
1. Clone the repository
  Clone the project to your local machine:
     bash Copy Edit

        git clone <repository-url>
        cd <project-directory>

3. Create a virtual environment
   
  It’s highly recommended to create a virtual environment for this project:

    python3 -m venv venv
  On Linux & Mac, use
  
    source venv/bin/activate 
    
  On Windows, use 
  
     venv\Scripts\activate
     
3. Install dependencies

Install the required dependencies using pip:

        pip install -r requirements.txt
        
4. Create .env file
Create a .env file in the root of the project to manage sensitive environment variables (like your Django settings). Add the following to the .env file:

        DEBUG=True
        SECRET_KEY=your-secret-key
        DATABASE_URL=your-database-url
Make sure to replace your-secret-key and your-database-url with the appropriate values.

5. Apply migrations
Run the following command to apply migrations:

        python manage.py migrate
6. Start the development server
Run the development server:

        python manage.py runserver

The API will be available at http://localhost:8000.

API Endpoints:
============  
    POST /api/v1/upload/
    
Upload a .csv file to insert user data into the database.

Request Body:
-------------

The .csv file should contain the following columns:

* first_name: First name of the user
* last_name: Last name of the user
* age: Age of the user
* email: Email of the user (must be unique)
* username: Username (must be between 6 and 120 characters)
* password: Password (must be between 8 and 25 characters)

Example CSV file:

    first_name,last_name,age,email,username,password
    John,Doe,25,john.doe@example.com,johndoe,password123
    Jane,Doe,30,jane.doe@example.com,janedoe,password123
    
Response:
=========
  200 OK: The data was successfully inserted into the database.
  400 Bad Request: Validation errors (e.g., email already exists, invalid data, etc.).
  
Validation Rules
=================

Email: Must be unique.
Must follow a valid email format.
Age:Must be between 0 and 120.
Username:Must be between 6 and 120 characters.
Password:Must be between 8 and 25 characters.


Required Fields:
All fields (first_name, last_name, age, email, username, password) must be filled.


Sample Data
You can find a sample data.csv file in the sample_data/ directory. You can upload this file to test the API functionality.

Sample Data.csv:
=============
    first_name,last_name,age,email,username,password
    Alice,Smith,29,alice.smith@example.com,alicesmith,securepassword
    Bob,Johnson,35,bob.johnson@example.com,bobjohnson,anotherpassword
    Charlie,Lee,23,charlie.lee@example.com,charlielee,password1234

Testing the API
=============
You can test the API using Postman or any other API testing tool:

URL: 

    http://localhost:8000/api/v1/upload/

Method: POST

Body: Choose the file from your local machine and upload the .csv file.

Example .env File

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://your-database-url
Make sure to replace the placeholder values with your actual data. The DATABASE_URL can be any supported database URL (e.g., PostgreSQL, MySQL, etc.).

Truncate incase of wrong data inserted
===================================
    TRUNCATE TABLE user_tbl RESTART IDENTITY CASCADE;
    TRUNCATE TABLE user_profile_tbl RESTART IDENTITY CASCADE;

.env contains
==============
    DATABASE_URL=postgres://your-database-url  
    SECRET_KEY=django-insecure-de8
    DEBUG=True # Set to False in production
    ALLOWED_HOSTS = localhost,127.0.0.1

License
===========

This project is licensed under the MIT License - see the LICENSE file for details.
