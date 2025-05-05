# Project Brief

This project is a Django-based backend for managing AI prompt content. It provides a RESTful API for CRUD operations on prompts, with prompt content stored in markdown files on disk. The system includes user management with email-based authentication and is designed for secure, authenticated access. It supports prompt cloning, pagination, and file-backed storage for scalability and maintainability.

Key requirements:

- User registration and authentication with email-based login
- Profile management for users
- JWT-based authentication for secure API access
- CRUD API for prompt management
- File-backed storage for prompt content (markdown)
- Authentication and authorization for sensitive actions
- Pagination for list endpoints
- Defensive coding against common security vulnerabilities
- Environment variable usage for secrets and configuration
- Extensible for future features (e.g., versioning, tagging, social auth)
