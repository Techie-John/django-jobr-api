
# Django User Management API (DJANGO-JOBR-API)

This is a Django REST Framework project that provides a User Management API, allowing users to register, log in, update their details, and delete their accounts. The API also includes Swagger documentation for easy interaction.

## Features

- User registration
- User login
- Update user details
- Delete user account
- API documentation using Swagger

## Technologies Used

- Python
- Django
- Django REST Framework
- drf-yasg (for Swagger documentation)

## Getting Started

### Prerequisites

- **Python 3.12**
- **pip** installed (commonly included with Python)
- **pipenv** installed

### Installing Pipenv

If you don't have `pipenv` installed, you can install it using pip:

```bash
pip install pipenv
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LYTE-studios/django-jobr-api.git
   cd django-jobr-api
   ```

2. Install the required packages using `pipenv`:

   ```bash
   pipenv install
   ```

   This command will read the existing `Pipfile` and install Django, Django REST Framework, and drf-yasg as specified.

3. Activate the Pipenv shell:

   ```bash
   pipenv shell
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for accessing admin features):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### 1. User Registration

- **POST** `/api/accounts/register/`
  
**Request Body:**

```json
{
    "username": "newuser",
    "email": "new@example.com",
    "password": "newpassword"
}
```

**Response:**

- **201 Created** on successful registration, returning the user details.

![Register API](https://awesomescreenshot.s3.amazonaws.com/image/2631307/51764602-f86ecdbe2f913812bc5b4e92a075727a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20241126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241126T185608Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=a93ace125ccba11312b7f0f4025fc221852c2de957471b37deb43a2f93b74993)
### 2. User Login

- **POST** `/api/accounts/login/`
  
**Request Body:**

```json
{
    "username": "testuser",
    "password": "securepassword"
}
```
**Response:**

- **200 OK** on successful login with a message.
![Login API](https://awesomescreenshot.s3.amazonaws.com/image/2631307/51764682-ae8fecb59cc85cbc980be220c40f3dd9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20241126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241126T185950Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=4fb1ad0b6943f34e44faa45077f5aae0da4455622cd2d938af8f103547454cd0)


### 3. Employee Registration
- **Endpoint**: `/register/employee/`
- **Method**: `POST`

#### Request Body
```json
{
    "date_of_birth": "YYYY-MM-DD",
    "gender": "string", // (male, female, other)
    "phone_number": "string",
    "city_name": "string",
    "biography": "string",
    "username": "string",
    "email": "string",
    "password": "string"
}
```

- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "success": true,
        "message": "Employee registered successfully."
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "non_field_errors": ["Invalid data."],
        "username": ["This field may not be blank."],
        "email": ["This field may not be blank."],
        "password": ["This field may not be blank."]
    }
    ```

### 4. Employer Registration
- **Endpoint**: `/register/employer/`
- **Method**: `POST`

#### Request Body
```json
{
    "vat_number": "string",
    "company_name": "string",
    "street_name": "string",
    "house_number": "string",
    "city": "string",
    "postal_code": "string",
    "coordinates": {"latitude": 12.34, "longitude": 56.78},
    "website": "url",
    "biography": "string",
    "username": "string",
    "email": "sample@gmail.com",
    "password": "string"
}
```

- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "success": true,
        "message": "Employer registered successfully."
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "non_field_errors": ["Invalid data."],
        "username": ["This field may not be blank."],
        "email": ["This field may not be blank."],
        "password": ["This field may not be blank."]
    }
    ```

### 5. Admin Registration
- **Endpoint**: `/register/admin/`
- **Method**: `POST`

#### Request Body
```json
{
    "full_name": "string",
    "username": "string",
    "email": "string",
    "password": "string"
}
```

- **Response**:
  - **Success (201 Created)**:
    ```json
    {
        "success": true,
        "message": "Admin registered successfully."
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
        "non_field_errors": ["Invalid data."],
        "username": ["This field may not be blank."],
        "email": ["This field may not be blank."],
        "password": ["This field may not be blank."]
    }
    ```
    
## Swagger Documentation

Swagger documentation is available at the following URL:

```
http://127.0.0.1:8000/swagger/
```

This documentation allows you to test the API endpoints interactively.

![swagger page](https://awesomescreenshot.s3.amazonaws.com/image/2631307/51764357-627f731745c2aade5422fb2509929c4a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20241126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241126T184901Z&X-Amz-Expires=28800&X-Amz-SignedHeaders=host&X-Amz-Signature=b8cb7812edc7a2fed5df663d5d96097be9e8057102349d18d97d02d8df4c37e9)

## Running Tests

To run the tests for the application, use the following command:

```bash
python manage.py test accounts
```