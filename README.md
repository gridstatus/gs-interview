# Installation

* Copy `.env.template` to `.env` and fill in the values

## Backend

### Install python

* Install the version of python in `.python-version` file using the method of your choice

### Install poetry

* https://python-poetry.org/docs/
* Depends on os and your preferred way of installing tools

### Install python packages using poetry

* Installs packages from `pyproject.toml` (`poetry.lock` is generated automatically)

```bash
poetry config virtualenvs.in-project true
poetry install --all-extras
```

## Frontend

### Install node

* Install the version of node in `.nvmrc` file using the method of your choice

### Install npm

* https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
* Depends on os and your preferred way of installing tools

### Install node packages

* Installs packages from `package.json` (`package-lock.json` is generated automatically)

```bash
npm install
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
poetry run uvicorn backend.main.main:app --port 8000 --reload
```

* Go to http://localhost:8001 to view the root of the backend
* Assuming the database connection is correct, you can go to the following to see table data
  * http://localhost:8001/data?table_name=caiso_fuel_mix
  * http://localhost:8001/data?table_name=ercot_load_forecast
