# Django Course Marketplace
## Overview
This Django application is a course marketplace platform, similar to Udemy, where users can access and enroll in various courses. It provides a secure authentication system and offers features such as course uploads, prerequisites, video lessons, payments, discounts, and coupon code integration.

## Features
### Admin Course Management
Streamlined course management for admin users, allowing them to efficiently handle course details, such as prerequisites, essentials, and multiple videos.
Comprehensive categorization and administration of courses through an intuitive admin dashboard.
### Secure Authentication
Robust authentication system that ensures the security of user accounts, enabling users to confidently sign up, log in, and maintain their credentials.
Implementation of advanced authentication mechanisms to safeguard user data and transactional information.
### Course Listing and Enrollment
Engaging home screen showcasing a wide array of courses through visually appealing HTML cards, enhancing the user browsing experience.
Smooth enrollment process, enabling users to effortlessly enroll in free courses or preview paid courses before making a purchase decision.
Seamlessly adding purchased courses to the user's account upon successful payment, granting immediate access to course content.
### Secure Payment Integration
Integration of the highly secure and reliable Razorpay payment gateway, ensuring safe and seamless transactions for users.
Support for various payment methods, offering users a convenient and trustworthy checkout process for purchasing courses.
### Video Player
Custom-built media player designed to provide an immersive and user-friendly experience for playing video lectures within the application.
Seamless integration with YouTube, dynamically fetching and delivering video lectures based on user preferences and course requirements.
### Discount and Coupon Codes
User-friendly discount system that allows users to apply coupon codes during the payment process, granting them access to exclusive discounts on paid courses.
Accurate validation and application of coupon codes, ensuring transparent and fair pricing for users.


## Clone the repository:

### bash
git clone https://github.com/your-username/your-repository.git
Set up the Django environment:

### Create and activate a virtual environment.
Install the required dependencies listed in requirements.txt.
Configure the project:

### Set up the database and perform migrations using python manage.py migrate.
Update the configuration settings in settings.py, including database credentials and payment gateway details.

### Run the Django development server:

python manage.py runserver
Access the application:
Open your web browser and visit http://localhost:8000 to explore the application locally.


## License

Feel free to customize this README file to add more specific details, such as installation instructions, deployment options, or any additional features or functionalities unique to your Django application.
