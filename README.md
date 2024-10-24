HubNet
HubNet is a platform connecting digital marketers and clients. It allows digital marketers to showcase their skills, manage projects, and interact with clients, while clients can hire marketers, view their profiles, and leave feedback. This README provides an overview of how to set up and use HubNet.

Features:
For Digital Marketers:
Profile Page: Showcase skills, years of experience, ratings, and views.
Portfolio: Upload videos and images to demonstrate past work.
Job Management: View pending jobs, accept or reject offers, mark jobs as completed, and request payment.
Self-Description: Write notes about yourself and your experience.

For Clients:
Browse Digital Marketers: View profiles and skills of digital marketers.
Project Offers: Offer and assign projects to digital marketers.
Rating and Feedback: Rate marketers after project completion and leave comments.
Payments: Pay digital marketers directly through the platform.
Previous Projects: Check previous collaborations and projects.

Getting Started
Prerequisites
Before you can run the HubNet application, make sure you have the following installed:

Python 3.9+
Flask
Flask-WTF
Flask-Login
SQLAlchemy (for database interactions)
Installation

Clone the repository:

git clone https://github.com/yourusername/hubnet.git
cd hubnet

Run the Flask application: To run the application
navigate to the repo and issue the command:

flask run

The app will be available at http://127.0.0.1:5000.


Database Models
User Model: Not yet implemented (to be added).
RegistrationForm: Handles user registration with fields for username, email, password, and a digital marketer flag.
LoginForm: Handles user login with email and password.

Routing Overview
/register: User registration page.
/login: User login page.
/profile: User profile page, which differentiates between digital marketers and clients.
/dashboard: Client dashboard to view and manage projects.
/marketer-dashboard: Digital marketer's dashboard to manage jobs, skills, and portfolio.

Customizing Profile Page
The profile page dynamically adapts to the user type:

Digital Marketers: Show portfolio, skills, pending jobs, and self-description.
Clients: View digital marketers' portfolios, offer projects, and leave feedback.
Login Redirect

Upon successful login, users are redirected to the profile page.

Contact Page Layout
The contact form is positioned beside the address for a cleaner user experience. You can modify this layout in contact.html by adjusting the CSS grid or Flexbox settings in the template.

Contributing
Feel free to submit a pull request if you'd like to contribute to HubNet. Make sure to follow the code style guidelines and write unit tests for any new features.
