#Run after only connect with the internet


from flask import Flask, render_template, request, url_for, redirect
import mysql.connector


app = Flask(__name__, template_folder='templates', static_folder='static')


db = mysql.connector.connect(
    host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
    user='uhrezqffmnurete8',
    password='jkLDZ4qhUOsvYN2JZ6OX',
    port=3306
)
curs = db.cursor(dictionary=True)
curs.execute("create database if not exists bvjy0fief8tnbddoxry8")
curs.execute("use bvjy0fief8tnbddoxry8")


@app.route('/')
def home():

    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )
    curs = db.cursor()
    curs3 = db.cursor()

    curs2 = db.cursor()
    curs.execute("create table if not exists details(id INT AUTO_INCREMENT primary key,Name varchar(20),Price int,Author varchar(20),Description text,Language text,Category text)")

    return render_template('index.html')


@app.route('/submit', methods=["POST", "GET"])
def submit():
    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )
    curs = db.cursor(dictionary=True)
    curs.execute("use bvjy0fief8tnbddoxry8")
    search_input = request.form.get('ser')
    query = f"SELECT * FROM details WHERE Name LIKE '%{search_input}%' or Author like '%{search_input}%' or Description like '%{search_input}%' or Language like '%{search_input}%' or Category like '%{search_input}%'"
    curs.execute(query)
    details = curs.fetchall()
    return render_template('search.html', details=details)


@app.route('/products/')
def products():
    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )
    curs = db.cursor(dictionary=True)
    curs.execute("use bvjy0fief8tnbddoxry8")
    curs.execute("SELECT * from details")
    details = curs.fetchall()
    return render_template('products.html', details=details)


@app.route('/product_details/home', methods=["POST", "GET"])
def product_details_ret():
    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )
    curs.execute("use bvjy0fief8tnbddoxry8")
    return redirect(url_for("home"))


@app.route('/product_details/', methods=["POST", "GET"])
def product_details():
    category = request.args.get('prod_name')
    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )
    cursor = db.cursor()
    cursor.execute("use bvjy0fief8tnbddoxry8")
    sql = "SELECT * from details"
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        if result[1] == category:
            product_details = result
            Name = product_details[1]
            Price = product_details[2]
            Author = product_details[3]
            Description = product_details[4]
            Language = product_details[5]
            Category = product_details[6]
        else:
            db = mysql.connector.connect(
                host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
                user='uhrezqffmnurete8',
                password='jkLDZ4qhUOsvYN2JZ6OX',
                port=3306,
                database='bvjy0fief8tnbddoxry8')
            cursor = db.cursor()
            cursor.execute("use bvjy0fief8tnbddoxry8")

    print(product_details)
    db.close()

    return render_template('product_details.html', Name=Name, Price=Price, Author=Author, Description=Description, Language=Language, Category=Category)


@app.route("/Addproduct", methods=["POST", "GET"])
def Addproduct():
    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )

    curs = db.cursor()
    Name = request.form.get('Name')
    Price = request.form.get('Price')
    Author = request.form.get('Author')
    Description = request.form.get('Description')
    Language = request.form.get('Language')
    Category = request.form.get('Category')

    if Name and Price and Author and Description and Language and Category != 'NULL':
        sql = "insert into details(Name,Price,Author,Description,Language,Category) values(%s,%s,%s,%s,%s,%s)"
        val = (Name, Price, Author, Description, Language, Category)

        curs.execute("create database if not exists bvjy0fief8tnbddoxry8")
        curs.execute("use bvjy0fief8tnbddoxry8")
        curs.execute(sql, val)
        db.commit()
        curs.close()
        db.close()
        return redirect(url_for("home"))
    return render_template('Addproduct.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    return render_template('contact.html')


@app.route('/price', methods=["POST", "GET"])
def price():
    db = mysql.connector.connect(
        host='bvjy0fief8tnbddoxry8-mysql.services.clever-cloud.com',
        user='uhrezqffmnurete8',
        password='jkLDZ4qhUOsvYN2JZ6OX',
        port=3306,
        database='bvjy0fief8tnbddoxry8'
    )
    curs = db.cursor(dictionary=True)
    curs.execute("SELECT * from details order by Price")
    details = curs.fetchall()
    return render_template('price.html', details=details)


if __name__ == '__main__':
    app.run(debug=True)