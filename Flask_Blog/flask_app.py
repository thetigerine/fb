from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8e7ae45e3fe7f7f6001e08923c175a76'


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'A link and QR code will be generated for {form.customername.data}!', 'success')
        return redirect(url_for("survey"))
    return render_template('home.html', title='Register', form=form)


@app.route("/survey")
def survey():
    return render_template('survey.html', title='Survey')


if __name__ == '__main__':
    app.run(debug=True)
