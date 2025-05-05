# System Patterns

## API Authentication & Authorization

- JWT-based authentication using djangorestframework-simplejwt
- Two-token system: access token (short-lived) and refresh token (long-lived)
- Token-based endpoints follow REST conventions
- Protected endpoints require valid JWT in Authorization header
- Token refresh mechanism for maintaining sessions
- Token verification endpoint for validating tokens
- Email-based user authentication with custom User model
- User registration and profile management endpoints

## User Management

- Custom User model extending Django's AbstractUser
- Email as the primary identifier (instead of username)
- User registration with email, password, and optional profile fields
- Profile management (view/update) for authenticated users
- Password validation using Django's built-in validators
- JWT tokens generated upon registration and login

## API Design

- Django REST Framework (DRF) for API endpoints
- ModelViewSet pattern for prompt CRUD
- File-backed storage: prompt content is saved as markdown files on disk, with file paths tracked in the database
- Serializers handle validation and data transformation
- Permissions enforced using DRF's IsAuthenticatedOrReadOnly
- Custom actions (e.g., prompt cloning) implemented via @action decorator

## Security Patterns

- JWT tokens signed with HS256 algorithm
- Refresh tokens can be blacklisted after rotation
- Access tokens expire frequently (60 minutes)
- Defensive coding for file I/O and user input
- Environment variables used for secrets and configuration
- Token verification before processing protected requests
- Password hashing using Django's default PBKDF2 algorithm
- Password validation to enforce security standards
