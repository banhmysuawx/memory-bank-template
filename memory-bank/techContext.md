# Tech Context

- Python 3.x
- Django 5.x
- Django REST Framework (DRF)
- djangorestframework-simplejwt for JWT authentication
- SQLite (default, can be swapped for Postgres)
- File system for markdown storage
- Environment variables for configuration (e.g., BASE_DIR, secret keys)
- Recommended: use Docker for local development
- Dependencies managed via pip/requirements.txt

Required environment variables:

- SECRET_KEY (used for both Django and JWT signing)
- BASE_DIR
- DEBUG
- ALLOWED_HOSTS

Security:

- JWT-based authentication with access and refresh tokens
- Access tokens expire after 60 minutes
- Refresh tokens expire after 24 hours
- Never hardcode secrets; always use environment variables or a secrets manager
- Sanitize all user inputs
- Use Django's built-in protections against common vulnerabilities
- Custom User model with email-based authentication

Authentication:

- JWT (JSON Web Token) based authentication
- Email-based authentication (instead of username)
- Custom User model in accounts app
- Token endpoints:
  - POST /api/auth/login/ - Obtain token pair
  - POST /api/auth/token/refresh/ - Refresh access token
  - POST /api/auth/token/verify/ - Verify token validity
  - POST /api/auth/register/ - Register new user
  - GET/PUT /api/auth/me/ - Get/update user profile
- Protected endpoints require Bearer token in Authorization header
