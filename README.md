# Blog Platform

A Django REST API backend for a blog platform with user registration, JWT authentication, post management, comments, likes, and bookmarks.

## Features

- Custom user model with extended profile fields
- JWT authentication with `djangorestframework_simplejwt`
- Create, edit, and list blog posts
- Publish and draft post status support
- Commenting and threaded replies
- Like/unlike posts and comments
- Bookmark posts
- PostgreSQL database backend

## Technology Stack

- Python 3
- Django
- Django REST Framework
- Simple JWT
- PostgreSQL
- `python-decouple` for environment configuration

## Project Structure

- `blog_platform/` - Django project configuration
- `posts/` - Post and comment functionality
- `users/` - Authentication and user registration
- `requirements.txt` - Python dependencies

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root or export environment variables so Django can connect to PostgreSQL.

Required variables:

```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Authentication

This project uses JWT authentication.

### Register

- `POST /register/`

### Login

- `POST /login/`

### Token endpoints

- `POST /api/token/`
- `POST /api/token/refresh/`

Include the access token in requests:

```http
Authorization: Bearer <access_token>
```

## API Endpoints

### User

- `POST /register/` - Register a new user
- `POST /login/` - Login and receive access/refresh tokens
- `POST /api/token/` - Obtain JWT token pair
- `POST /api/token/refresh/` - Refresh access token

### Posts

- `POST /posts/create/` - Create a new post
- `POST /posts/<post_id>/edit/` - Edit an existing post
- `GET /posts/` - List published posts
- `GET /posts/my_posts/` - List authenticated user posts

### Comments

- `POST /posts/<post_id>/comment/` - Comment on a post
- `GET /posts/<post_id>/comments/` - View comments for a post
- `POST /comments/<comment_id>/reply/` - Reply to a comment

### Likes & Bookmarks

- `POST /posts/<post_id>/like/` - Like/unlike a post
- `POST /comments/<comment_id>/like/` - Like/unlike a comment
- `POST /posts/<post_id>/bookmark/` - Add/remove bookmark for a post

## Testing

Run the test suite with:

```bash
python manage.py test
```

## Notes

- `AUTH_USER_MODEL` is set to `users.CustomUser`.
- The default database engine is PostgreSQL.
- `DEBUG` is currently enabled; disable it before production deployment.

## License

This project is provided as-is without an explicit license. Update this section if you add a license.
