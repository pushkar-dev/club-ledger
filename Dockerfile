FROM python:3.12
workdir /
# 

# 
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
# RUN pip install --no-cache-dir --upgrade psycopg2
# RUN python -m app.db.base
# 
COPY ./app ./app
copy ./alembic ./alembic
copy ./migrations ./migrations 
copy ./alembic.ini ./alembic.ini

# RUN alembic revision --autogenerate -m "init"
# RUN alembic upgrade head

# 
CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]