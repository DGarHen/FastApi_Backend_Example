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
```

### 2. Running the proyect
```powershell
fastapi dev [class]
```

### note for later:
Para que "la otra persona" sepa exactamente qué versiones instalar, no basta con decirle "instala fastapi". Lo profesional es generar una lista de lo que tienes instalado tú ahora mismo.

Ejecuta este comando en tu terminal (con el `venv` activado) antes de subir tus cambios a Git:

```powershell
pip freeze > requirements.txt
```
entonces la persona podra ejecutar: 
```powershell
pip install -r requirements.txt
```