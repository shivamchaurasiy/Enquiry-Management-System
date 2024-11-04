# Enquiry Management System

This Enquiry Management System is a web application developed using Python, Django, and Bootstrap. It allows efficient handling of user inquiries by providing separate sections for users and administrators, each with specific functionalities.


## Features

#### User Section : 
- User Registration & Login: Allows users to create an account and log in to access the dashboard.
- Dashboard Access: Displays user details and an option to submit new inquiries.
- Inquiry Submission: Users can submit inquiries which are stored in the EnquiryDatabase.
- Logout: Allows users to log out and return to the home page.

#### User Section : 

- Admin Registration & Login: Enables administrators to register and log in.
- Inquiry Management Dashboard: Admins can view all submitted inquiries in a tabular format.
- Inquiry Viewing: Admins can see the details of each inquiry, assisting in customer support or sales follow-up.
- Logout: Allows admins to securely log out and return to the home page.




## Data Flow

The application consists of three primary databases:

- UserDatabase: Stores user information for login and registration.
- AdminDatabase: Stores admin information to manage access to the admin dashboard.
- EnquiryDatabase: Stores all user inquiries for future reference and management.

## Technology Stack

- Backend: Python, Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite


## Usage

- User Flow: Users can register, log in, and submit inquiries via the dashboard. They can view their submitted inquiries and log out when done.
- Admin Flow: Admins can log in, view all inquiries in a tabular format, and log out upon completion.

## Future Enhancements

- Add email notifications for new inquiries.
- Integrate search and filter options for inquiries.
- Add export functionality for inquiry data.