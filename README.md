## Install pyenv

* Depends on os and your preferred way of installing tools

## Install python using pyenv

```bash
pyenv install
pyenv rehash
```

## Install poetry

* Depends on os and your preferred way of installing tools

## Install python packages using poetry

```bash
poetry config virtualenvs.in-project true
poetry install --all-extras
```

## Install nvm

* Depends on os and your preferred way of installing tools

## Install node

```bash
nvm install
nvm use
```

## Install npm

* Depends on os and your preferred way of installing tools

## Install node packages

```bash
npm install
```


## Running App

### Frontend

```bash
npm run start
```

### Backend

```bash
poetry run uvicorn backend.main.main:app --port 8000 --reload
```
