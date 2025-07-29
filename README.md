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

## How to run Aurora as a whole on local machine

Visit other repos to learn how to un the fe, be, and db.

Run db first, then be, then fe.

Enjoy.

## API Endpoints



😙 😙 😙
