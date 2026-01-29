This is a backend project built with **FastAPI**. Follow the steps below to set up and run the development environment on a new machine.

## Prerequisites

- **Python 3.10** or higher.
- **Git** installed.

## Installation & Setup

Follow these steps to set up the project locally:

### 1. Preparation
Download the code to your local machine:

```bash
git clone <YOUR_REPO_URL>
cd <YOUR_FOLDER_NAME>
```

create you venv with python using the following commands:
 ```powershell
python -m venv venv
.\venv\Scripts\Activate
```
now the terminal should show at the begging of the command line the name of the venv, if so, run the next command to install fast api with all dependencies:
 ```powershell
pip install fastapi[standard]
pip install pytest
```

### 2. Running the proyect
in order to start the proyect please execute 
```powershell
fastapi dev app/main.py
```
then the database file, db.sqlite3 should be created at the root.

### 3. Running the tests
in order to run the test cases 
```powershell
pytest app/tests.py
```
then the database file, db.sqlite3 should be created at the root.

### 0. Use requirements:
remember you could use the follow command to install all dependencies with the proper version.
```powershell
pip install -r requirements.txt
```

### *. Later or missing info here:
Authentication in fast api
Architecture improvement