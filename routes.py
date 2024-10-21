from flask import render_template, url_for, flash, redirect
from app import app, db
from forms import RegistrationForm, LoginForm, SkillForm, RatingForm
from models import User, Skill, Rating
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def index():
    marketers = User.query.filter_by(is_marketer=True).all()
    return render_template('index.html', marketers=marketers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.is_marketer = form.is_marketer.data
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)

@app.route('/hire/<int:user_id>', methods=['GET', 'POST'])
@login_required
def hire(user_id):
    form = RatingForm()
    if form.validate_on_submit():
        rating = Rating(score=form.score.data, comment=form.comment.data, user_id=user_id)
        db.session.add(rating)
        db.session.commit()
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('index'))
    return render_template('hire.html', form=form)

@app.route('/add_skill', methods=['GET', 'POST'])
@login_required
def add_skill():
    form = SkillForm()
    if form.validate_on_submit():
        skill = Skill(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(skill)
        db.session.commit()
        flash('Skill added successfully!', 'success')
        return redirect(url_for('profile', user_id=current_user.id))
    return render_template('add_skill.html', form=form)

