from flask import request, render_template, flash, redirect, url_for
from flask_mail import Message
from flask_login import logout_user
from forms import ContactForm
from flask_login import login_required
from datetime import datetime, timedelta
import secrets
from forms import RegistrationForm, LoginForm
from flask_login import login_user
from app import app, mail, db  # Ensure you're importing mail and db correctly
from models import User  # Import the User model to interact with the database
from forms import ForgotPasswordForm  # Ensure you have this form defined

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()  # Create an instance of your forgot password form

    if form.validate_on_submit():  # Validate form submission
        email = form.email.data  # Get the email from the form
        
        # Check if the user exists
        user = User.query.filter_by(email=email).first()  # Ensure the user exists
        if user:
            # Generate a token and set expiration
            token = secrets.token_urlsafe()
            expiration = datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour

            # Store token and expiration in database associated with the user
            user.reset_token = token  # Assuming you have a column for reset tokens
            user.token_expiration = expiration  # And for expiration
            db.session.commit()  # Commit the changes

            # Send email with reset link
            reset_link = url_for('reset_password', token=token, _external=True)
            msg = Message('Password Reset Request', recipients=[email])
            msg.body = f'Please click the following link to reset your password: {reset_link}'
            mail.send(msg)

            flash('A password reset link has been sent to your email.')
            return redirect(url_for('login'))
        else:
            flash('No account found with that email address.')  # Handle case where user does not exist

    return render_template('forgot_password.html', form=form)  # Pass the form to the template

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'POST':
        new_password = request.form['new_password']
        # Verify the token and expiration
        # Example: user = db.verify_reset_token(token)
        # if user is None: return 'Invalid or expired token'

        # Update the user's password in the database
        # Example: db.update_password(user.id, new_password)
        
        flash('Your password has been updated!')
        return redirect(url_for('login'))
    
    return render_template('reset_password.html', token=token)

@app.route('/')
def index():
    marketers = User.query.filter_by(is_marketer=True).all()
    return render_template('index.html', marketers=marketers)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check for existing username or email
        existing_user = User.query.filter((User.username == form.username.data) | 
                                           (User.email == form.email.data)).first()
        if existing_user:
            flash('Username or email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))

        # Create new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.is_marketer = form.is_marketer.data
        
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/logout')
def logout():
    logout_user()  # This logs the user out
    flash('You have been logged out.', 'info')  # Optionally, provide feedback
    return redirect(url_for('login'))  # Redirect to the login page or home

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('profile', user_id=user.id))
        else:
            flash('Login unsuccessful. Please check your email and password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()  # Instantiate the form

    # Check if the form is submitted and validated
    if form.validate_on_submit():
        # Handle form submission (e.g., send email or save the message)
        pass  # Add your submission logic here

    # Render the template with the form
    return render_template('contact.html', form=form)

@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    
    if user.is_digital_marketer:
        # Fetch additional data for digital marketers
        videos = Video.query.filter_by(user_id=user_id).all()
        images = Image.query.filter_by(user_id=user_id).all()
        return render_template('profile.html', user=user, videos=videos, images=images)
    else:
        # Fetch digital marketers for clients
        digital_marketers = User.query.filter_by(is_digital_marketer=True).all()
        return render_template('profile.html', user=user, digital_marketers=digital_marketers)

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

