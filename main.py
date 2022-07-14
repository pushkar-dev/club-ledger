import re
import secrets
from flask import Flask, render_template, request
from dotenv import load_dotenv
from os import getenv

load_dotenv()
app=Flask(__name__)

SECRET_KEY = (getenv('SECRET_KEY'))
print(SECRET_KEY)

app.secret_key=SECRET_KEY # load some secret key from env

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('home.html')
    else :
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)



