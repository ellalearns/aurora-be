# Aurora (Back-End)

Aurora is the ultimate productivity app for procastinators. It allows users to set a daily target, and they have to hit a minimum of the daily target for the day to be a success.

This is Aurora's backend server, open to power users who want to request the API instead of run it in the mobile app.

Uncover how to authenticate your session, access daily tasks, and return other details.

Welcome, Sailor!

## Tech Stack

- Python: Main programming language used in server
- Flask: A Python server framework for developing quick prototype APIs
- MySQL: DBMS for storing and modifying user data
- Pymysql: A Python library acting as a DB connector
- JWT: Used for authenticating users

## Quick Start - How to run locally

- Step 1: Clone Git Repo

```bash
git clone https://github.com/ellalearns/aurora-be.git
```

- Step 2: Access the aurora-be directory

```bash
cd aurora-be
```

- Step 3: (Optional) Create and Activate a Virtual env
```bash
python3 -m venv aurora
source ./aurora/bin/activate
```

- Step 4: (Optional) Activate testenv to test fast
```bash
mv .testenv .env
source .env
```

- Step 5: Install required packages and the aurora-be directory as a package

```bash
pip install -r requirements.txt
pip install .
rm -rf build
```

- Step 6: Set up local https with mkcert since the API only accepts secure requests

```bash
sudo apt install libnss3-tools
sudo apt install mkcert
mkcert -install
mkcert localhost
```

- Step 7: Run the API 😊

```bash
python3 ./api/v1/app.py
```

If everything went according to plan, you should the following JSON response at the root route:

**Response**
```bash
{
  "greeting": "welcome, sailor :)"
}
```

## How to run Aurora as a whole on local machine

Visit other repos to learn how to un the fe, be, and db.

Run db first, then be, then fe.

Enjoy.

## API Endpoints

Aurora's public API allows users to authenticate their sessions, create and edit tasks, modify user details, and modify the daily target. 

Before you begin, here is the main URL for a local host:
```bash
https://``127.0.0.1:5000
```

### User Details

You can request a user's details as long as you send a valid token as a session cookie.

**Request**
```bash
GET /user/
```
**Valid Response**
```bash
{ "user": {
        "id": xxx
        "username": xxx,
        "email": "email@sample.com",
        "daily_target": 3,
        "max_major": 2,
        "current_major": 0,
        "tasks": [],
        "reports": [],
        "targets": []
      }
  }
```
**Possible Errors**
```bash
{ "msg": "incorrect token" }
```

### Authentication

You can create a new user, sign in, and sign out via the pulic API.

#### Sign Up

Send a POST request containing a JSON body detailing the new user's email, new password, and new username. 

**Request**

```bash
curl https://127.0.0.1:5000/auth/sign-up/
-H "Content-Type: application/json"
-X POST
```

**Request body**
```bash
{
  "email": "email@sample.com",
  "password": "newpassword",
  "username": "myUsername"
}
```

**Valid Response**
```bash
{
  "new_user_id": "newid",
  "new_user_username": "newusername"
}
```

**Possible Errors**
```bash
{ "msg": "email not valid" }
```
```bash
{ "msg": "invalid password" }
```
```bash
{ "msg": "username not present" }
```

## To be continued...

😙 😙 😙
