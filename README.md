# Grid Status Interview

* This repo is used to administer technical interviews for Grid Status
* If you are interested in working at Grid Status, look for our available jobs at http://gridstatus.io/jobs

# Installation

## Backend

### Install python

* Install the version of python in `.python-version` file using the method of your choice

### Install poetry

* https://python-poetry.org/docs/
* Installation method depends on OS and your preferred way of installing tools

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
* Installation method depends on OS and your preferred way of installing tools

### Install node packages

* Installs packages from `package.json` (`package-lock.json` is generated automatically)

```bash
npm install
```

# Running App

* Copy `.env.template` to `.env` and fill in the values

## Frontend

```bash
npm run start
```

* Go to http://localhost:3000 to view the app
* Go to http://localhost:3000/data to view the data page which displays some data from the database

## Backend

```bash
poetry run uvicorn backend.main.main:app --port 8000 --reload
```

* Go to http://localhost:8000 to view the root of the backend
* Assuming the database connection is correct, you can go to the following to see table data
  * http://localhost:8000/data?table_name=caiso_fuel_mix
  * http://localhost:8000/data?table_name=nyiso_load
  * http://localhost:8000/tables to see a list of all tables

# Database

* Only tables in the `PUBLIC` schema need to be supported
* Any columns beginning with `_` are artifacts of the ETL process and should not be displayed or included in downloads

# Frontend Querying

* You will need to implement querying the backend API server from the frontend
* One option for doing so is Tanstack Query: https://tanstack.com/query/latest/docs/framework/react/examples/basic
