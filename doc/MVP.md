# MVP

## Function

1. Planing meetings (create, delete, update, read)
2. Planing tasks (create, delete, update, read)
3. Interface for all meetings and tasks.
4. Authorization (support 5 devices, jwt token: access and refresh)

## Models design

1. Meetings
- id (unique)
- title (name of meeting)
- description
- start_datetime
- end_datetime
- created_at
- updated_at
- reminder_datetime

2. Tasks
- id (task)
- title (name of task)
- description
- status (done, in progress, todo)
- created_at
- updated_at
- reminder_datetime

3. User
- email
- username
- password_hash
- sessions 


## Authentication

All logic must work minimal 1 seconds.

### Register

Data:
- email
- username (How call users)
- password

Need add verify email (send code)


### Login

Data
- email
- password

Return

Tokens:
- access token
- refresh token


### Update access and refresh tokens

This is update refresh and access token to services.

Important need support 5+ user device.

We save refresh token in database.

Logic

1. Get user_id in refresh token
2. Search refresh token 
3. If refresh token is valid, then create new access token and refresh token.
4. Update old refresh token in new refresh token
5. Return new tokens to user (set to Cookie)


## Technologies

1. Python (fastAI, pydantic, uvicorn)
2. Vue (frontend)
3. PostgreSQL (database)



## API (MVP)

### Login
### Logout
### Register
### Update access and refresh tokens
### Get user info

### Create meeting
### Get meeting (need meeting uid)
### Get meetings (return meetings uid's)
### Delete meeting
### Update meeting

### Create tasks
### Get task (need task uid) 
### Get tasks (return tasks uid's)
### Delete task
