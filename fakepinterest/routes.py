from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormCriarConta, FormLogin



@app.route("/", methods=['GET', 'POST'])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)



@app.route("/criarconta", methods=['GET', 'POST'])
def criarconta():
    formcriarconta = FormCriarConta()
    return  render_template("criarconta.html", form=formcriarconta)



@login_required
@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
