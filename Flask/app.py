#importovanje modula
from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL()
conn = mysql.connect()
cursor = conn.connect()
hashed_password = generate_password_hash(password)

# mysql konfiguracija
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#pozivanje procedure za kreiranje korisnika
cursor.callproc('sp_createUser',(_name,_email,_hashed_password))

data = cursor.fetchall()

if len(data) is 0:
    conn.commit()
    return json.dumps({'message':'User created successfully!'})
else:
    return json.dumps({'error':str(data[0])})

@app.route("/")
#definisanje glavne funkcije
def main():
    #renderuje html
    return render_template('index.html', template_folder = "/home/urosh/Flask/templates")

#stranica za ulogovanje
@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route('/api/signup', method=['POST'])
def signUp():
    #cita upisane podatke iz interfejsa 
    name = request.form['inputNmae']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    
    #potvrdjuje primljenje vrednosti
    if name and email and password:
        return json.dumps({'html':'<span>All fields good!</span>'})
    else:
        return json.dumps({'html':'<span>All fields false!</span>'})

if __name__ == "__main__":
    app.run()