# Flask SQLAlchemy

A Contacts app

## Technologies

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/) for dependency and virtual environment management
- postgresql (but yuo can use another one)

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:dapt4/flask-SQLAlchemy-app.git
cd flask-SQLAlchemy-app
```

### 2. Install Poetry (if not already installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

You can also follow the official guide: https://python-poetry.org/docs/#installation

### 3. Install dependencies

```bash
poetry install
```

### 4. Create the `.env` file

Create a `.env` file at the root of the project with the following content:

```
SECRET_KEY=your_secret_key
DB_URL=postgresql://user:password@localhost:5432/your_database
```

These environment variables are required for security configuration and database connection.

### 5. Activate the virtual environment

```bash
poetry shell
```

## Project Structure

```
flask-SQLAlchemy-app
├── app.py
├── LICENSE
├── models
│   ├── contacts.py
│   └── __pycache__
├── poetry.lock
├── __pycache__
│   └── app.cpython-311.pyc
├── pyproject.toml
├── README.md
├── requirements.txt
├── routes
│   ├── contacts.py
│   └── __pycache__
├── run.sh
├── session.nvim
├── templates
│   ├── about.html
│   ├── index.html
│   ├── layout.html
│   └── update.html
└── utils
    ├── db.py
    └── __pycache__
```

## run the app
```bash
sh run.sh

```

## Useful commands

- Add a dependency:
  ```bash
  poetry add package-name
  ```

- Add a development dependency:
  ```bash
  poetry add --dev package-name
  ```

- Run a script:
  ```bash
  poetry run python path/to/script.py
  ```

## License

M.I.T. License
