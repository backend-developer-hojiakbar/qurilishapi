# Adolat AI Backend API

This is the backend API for the Adolat AI legal assistant application. It provides authentication, user management, device management, and case data storage functionalities.

## Technologies Used

- Django 4.2
- Django REST Framework
- SQLite (default database, can be changed to PostgreSQL)
- JWT Authentication
- CORS Headers

## Setup Instructions

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/auth/token/` - Obtain JWT tokens
- `POST /api/auth/token/refresh/` - Refresh JWT tokens

### Users

- `POST /api/users/login/` - Login with token
- `POST /api/users/logout/` - Logout
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/update/` - Update user profile
- `GET /api/users/devices/` - List user devices
- `POST /api/users/devices/register/` - Register a new device
- `DELETE /api/users/devices/remove/<device_id>/` - Remove a device

### Cases

- `GET /api/cases/` - List all cases for the authenticated user
- `POST /api/cases/create/` - Create a new case
- `GET /api/cases/<case_id>/` - Get details of a specific case
- `PUT /api/cases/<case_id>/update/` - Update a specific case
- `DELETE /api/cases/<case_id>/delete/` - Delete a specific case

#### Case Files
- `POST /api/cases/<case_id>/files/add/` - Add a file to a case

#### Case Participants
- `POST /api/cases/<case_id>/participants/add/` - Add a participant to a case

#### Tasks
- `POST /api/cases/<case_id>/tasks/add/` - Add a task to a case
- `PUT /api/cases/<case_id>/tasks/<task_id>/update/` - Update a task

#### Timeline Events
- `POST /api/cases/<case_id>/timeline/add/` - Add a timeline event to a case

#### Evidence Items
- `POST /api/cases/<case_id>/evidence/add/` - Add evidence to a case

#### Billing Entries
- `POST /api/cases/<case_id>/billing/add/` - Add a billing entry to a case

#### Notes
- `POST /api/cases/<case_id>/notes/add/` - Add a note to a case

## Device Limit

Each user can register a maximum of 2 devices. When a user tries to register a third device, they will receive an error message.

## Authentication

All API endpoints (except login) require JWT authentication. Include the access token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Models

The backend includes the following models:

1. **User** - Custom user model with phone number and full name
2. **Device** - Tracks user devices with a limit of 2 per user
3. **Case** - Main case model with all case-related data
4. **CaseFile** - Files associated with cases
5. **CaseParticipant** - Participants in cases
6. **Task** - Tasks related to cases
7. **TimelineEvent** - Timeline events for cases
8. **EvidenceItem** - Evidence items for cases
9. **BillingEntry** - Billing entries for cases
10. **Note** - Notes for cases
11. **KnowledgeBaseSection** - Knowledge base sections for cases
12. **RiskMatrixEntry** - Risk matrix entries for cases
13. **DebateResult** - Debate results for cases

## Admin Interface

The Django admin interface is available at `/admin/` for managing users, cases, and other data.