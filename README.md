# Installation

* Copy `.env.template` to `.env` and fill in the values

## Backend

### Install pyenv

* https://github.com/pyenv/pyenv
* Depends on os and your preferred way of installing tools

### Install python using pyenv

* Installs the version of python in `.python-version` file

```bash
pyenv install
pyenv rehash
```

### Install poetry

* https://python-poetry.org/docs/
* Depends on os and your preferred way of installing tools

### Install python packages using poetry

* Installs packages from `pyproject.toml` (`poetry.lock` is generated automatically)

```bash
poetry config virtualenvs.in-project true
poetry install --all-extras
```

### Install pre-commit hooks

```bash
poetry run pre-commit install
```

## Frontend

### Install nvm

* https://github.com/nvm-sh/nvm
* Depends on os and your preferred way of installing tools

### Install node

* Installs the version of node in `.nvmrc` file

```bash
nvm install
nvm use
```

### Install npm

* https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
* Depends on os and your preferred way of installing tools

### Install node packages

* Installs packages from `package.json` (`package-lock.json` is generated automatically)

```bash
npm install
```

### Install frontend pre-commit hooks

```bash
npm run dev-prepare
```

# Running App

## Frontend

```bash
npm run start
```

* Go to http://localhost:3000 to view the app

## Backend

* If you change the `--port` flag, you will need to update the `VITE_API_HOST` in the `.env` file

```bash
poetry run uvicorn backend.main.main:app --port 8001 --reload
```

* Go to http://localhost:8001 to view the root of the backend
* Assuming the database connection is correct, you can go to the following to see table data
  * http://localhost:8001/data?table_name=caiso_fuel_mix
  * http://localhost:8001/data?table_name=ercot_load_forecast
