# Active Context

Current focus:

- User authentication system with custom User model
- JWT authentication with updated endpoints under /api/auth/
- Email-based authentication (instead of username-based)
- User registration and profile management
- Ensuring user data security and password validation
- Organizing all authentication endpoints under a common prefix (/api/auth/)
- Implementing and refining prompt CRUD endpoints
- Ensuring file-backed storage is robust and error-tolerant
- Enforcing authentication and permissions for API actions
- Adding pagination to list endpoints
- Improving error handling and input validation
- Swagger (drf-spectacular) API documentation endpoints added and documented
- Refactored PromptSerializer to fix DRF field errors
- Fixed /clone endpoint to not require a request body

Recent changes:

- Implemented custom User model with email-based authentication
- Created user registration endpoint (/api/auth/register/)
- Implemented user profile endpoint (/api/auth/me/) for retrieving and updating profile
- Moved JWT authentication endpoints:
  - /api/token/ → /api/auth/login/
  - /api/token/refresh/ → /api/auth/token/refresh/
  - /api/token/verify/ → /api/auth/token/verify/
- Fixed JWT authentication flows to work with email-based login
- Created accounts app for user management functionality
- Added comprehensive JWT authentication test suite
- Added prompt cloning endpoint
- Integrated IsAuthenticatedOrReadOnly permissions
- Improved file read/write logic for markdown content
- Integrated drf-spectacular for OpenAPI/Swagger docs
- Refactored PromptSerializer to use write-only/read-only fields for content
- /clone endpoint now works with empty or no request body

Next steps:

- Add comprehensive tests for user authentication
- Add/expand automated tests for the clone endpoint (especially POST with empty body)
- Update OpenAPI/Swagger documentation to clarify that /clone does not require a request body
- Review other endpoints for similar UX/API consistency
- Consider implementing email verification for new accounts
- Add password reset functionality
- Implement token blacklist for enhanced security
- Add rate limiting for authentication endpoints
- Consider adding social authentication options
- Add account management features (password change, account deletion)
- Add more tests (unit and integration)
- Document required environment variables
- Plan for advanced features (e.g., prompt versioning, search)
- Monitor token usage and adjust expiration times if needed
