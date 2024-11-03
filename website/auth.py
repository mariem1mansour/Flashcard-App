from flask import Blueprint, render_template, request, flash
from .models import User
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Veuillez entrer votre email et votre mot de passe.", category='error')
        else:
            # Logique d'authentification ici
            flash("Connexion réussie!", category='success')

    return render_template("login.html")

@auth.route("/logout")
def logout():
    flash("Vous avez été déconnecté avec succès.", category='success')
    return "<p>Vous êtes déconnecté.</p>"

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form.get("email") or ""
        fullname = request.form.get("fullname") or ""
        password1 = request.form.get("password1") or ""
        password2 = request.form.get("password2") or ""

        # Validation améliorée pour s'assurer que les valeurs ne soient pas None
        # if not email:
        #     flash('Veuillez entrer une adresse email.', category='error')
        # elif len(email) < 4:
        #     flash('L\'email doit contenir plus de 3 caractères.', category='error')
        # elif not fullname:
        #     flash('Veuillez entrer votre nom complet.', category='error')
        # elif len(fullname) < 2:
        #     flash('Le nom complet doit contenir au moins 2 caractères.', category='error')
        if password1 != password2:
            flash('Les mots de passe ne correspondent pas.', category="error")
        # elif len(password1) < 7:
        #     flash('Le mot de passe doit contenir au moins 7 caractères.', category='error')
        else:
           new_user = User(email=email, fullname=fullname)
           flash('Compte créé avec succès!', category='success')

    return render_template("register.html")
