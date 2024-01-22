# Club Ledger 
A project to manage inventory of clubs in institutions

- Fastapi
- Alembic
- Postgres

# Setup 
To run follow the steps
1. Initaialize alembic and setup the database url, username and password in alembic.ini file
```sh 
alembic init -t async migrations
``` 
2. Run the docker container
```sh 
docker-compose up -d --build fastapi
```
3. Make migrations
```sh
docker-compose exec fastapi alembic revision --autogenerate -m "your migration mesage"
```
4. Migrate
```sh
docker-compose exec web alembic upgrade head
```
   
