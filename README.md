# Club Ledger 
A project to manage inventory of clubs in institutions

- Fastapi
- Alembic
- Postgres

# Setup 
To run follow the steps
1. setup the virtualenv, activate and installl requirements
   
2. Initaialize alembic and setup the database url, username and password in alembic.ini file
```sh 
alembic init -t async migrations
``` 
3. Run the docker container
```sh 
docker-compose up -d --build fastapi
```
4. Make migrations
```sh
alembic revision --autogenerate -m "your migration mesage"
```
5. Migrate
```sh
alembic upgrade head
```
   
