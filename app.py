from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Message sent successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

