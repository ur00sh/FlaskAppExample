#importovanje potrebnih modula
from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

#definisanje aplikacije
app = Flask(__name__, template_folder='') #uneti direktorijum gde se nalaze templates za flask

#definisanje metode koja vodi na pocetnu stranicu
@app.route('/')
def main():
    return render_template('index.html')

#definisanje metode koja vodi na stranicu za prijavu
@app.route('/signup')
def signup():
    return render_template('signup.html')


#definisanje POST metode
@app.route('/api/signup', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    
    if len(data) == 0:
        conn.commit()
        return json.dumps({'message':'Korisnik je uspesno prijavljen!'})
    else:
        return json.dumps({'error':str(data[0])})
    
    #proverava tacnost unetih podataka
    if _name and _email and _password:
        return json.dumps({'html':'<span>Sva polja su popunjena dobro!</span>'})
    else:
        return json.dumps({'html':'<span>Popunite potrebna polja!</span>'})

#konfiguracija mysql-a
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '' #uneti sifru od MySql-a
app.config['MYSQL_DATABASE_DB'] = 'FlaskApp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#ostvarivanje veze sa mysql bazom
conn = mysql.connect()
cursor = conn.cursor()

#hash lozinka 
_hashed_password = generate_password_hash (_password)

cursor.callproc('sp_createUser',(_name, _email, _hashed_password))
data = cursor.fetchall()

if __name__ == "__main__":
    app.run()
