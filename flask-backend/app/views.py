from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Client ,Blog, About, Services, Contact, Experience
from app.forms import ContactForm # type: ignore
from sqlalchemy.exc import IntegrityError

@app.route("/")
def index():
    experience_data = Experience.query.all()
    blogs_data = Blog.query.all()
    abouts_data = About.query.all()
    servis_data = Services.query.all()
    return render_template("index.html", blogs=blogs_data, about=abouts_data, servis=servis_data)


@app.route("/category")
def category():
    blogs_data = Blog.query.all()
    return render_template("category.html", blogs=blogs_data)


@app.route("/about")
def about():
    abouts_data = About.query.all()
    return render_template("about.html", about=abouts_data)


@app.route("/client")
def client():
    clients_data = Client.query.all()
    return render_template("client.html", clients=clients_data)


def add_contact(name, phonenumber, email, message):
    try:
        new_contact = Contact(name=name, phonenumber=phonenumber, email=email, metin=message)
        db.session.add(new_contact)
        db.session.commit()
        flash('Talebiniz alınmıştır. Teşekkür ederiz!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('Bu isim veya telefon numarası zaten kayıtlıdır. Lütfen farklı bir isim veya telefon numarası deneyin.', 'error')
    except Exception as e:
        db.session.rollback()
        flash('Bir hata oluştu. Lütfen daha sonra tekrar deneyin.', 'error')
    finally:
        db.session.close()

@app.route("/work1")
def work1():
    servis_data = Services.query.all()
    return render_template("work1.html")

@app.route("/experience")
def experience():
    experience_data = Experience.query.all()
    return render_template("experience.html")

@app.route("/about1")
def about1():
    return render_template("about1.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        add_contact(form.name.data, form.phonenumber.data, form.email.data, form.message.data)
        flash('Talebiniz alınmıştır. Teşekkür ederiz!', 'success')
        return redirect(url_for('contact'))  # Başarı sayfasına yönlendirme

    return render_template("contact.html", form=form)

@app.route('/login_with_facebook')
def login_with_facebook():
    # Facebook'un kendi giriş sayfasının URL'sini belirtin
    facebook_login_url = "https://www.facebook.com/login.php"

    # Kullanıcıyı Facebook giriş sayfasına yönlendirin
    return redirect(facebook_login_url)

# Instagram için OAuth 2.0 Redirect URL
instagram_redirect_url = "https://www.instagram.com/accounts/login/"

# LinkedIn için OAuth 2.0 Redirect URL
linkedin_redirect_url = "https://www.linkedin.com/login/"

@app.route('/login_with_instagram')
def login_with_instagram():
    # Kullanıcıyı Instagram giriş sayfasına yönlendirin
    return redirect(instagram_redirect_url)

@app.route('/login_with_linkedin')
def login_with_linkedin():
    # Kullanıcıyı LinkedIn giriş sayfasına yönlendirin
    return redirect(linkedin_redirect_url)

twitter_redirect_url = "https://twitter.com/i/flow/login"

@app.route('/login_with_twitter')
def login_with_twitter():
    # Kullanıcıyı Twitter giriş sayfasına yönlendirin
    return redirect(twitter_redirect_url)

@app.route("/login")
def login():
    return render_template("login.html")
