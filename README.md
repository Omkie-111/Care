# Repository Name

**GitHub Repository Name:** Care

## Description

This GitHub repository contains the source code for a Django web application called "Care App." The Care App is a healthcare management system that allows users to book appointments, learn about available facilities, contact the healthcare team, and view information about the team members.

## Installation

To run the Care App locally, follow the steps below:

1. Clone the repository to your local machine: git clone https://github.com/Omkie-111/Care.git
2. Change into the project directory: cd django-care-app
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment:

- For Windows:

  ```
  venv\Scripts\activate
  ```

- For macOS/Linux:

  ```
  source venv/bin/activate
  ```
5. Install the dependencies: pip install -r requirements.txt
6. Create a `.env` file in the root directory and provide the necessary environment variables: EMAIL_HOST_USER=<your_email_host_user>
7. Run the database migrations: python manage.py migrate
8. Start the development server: python manage.py runserver
9. Access the Care App in your web browser at `http://localhost:8000/`.

## Configuration

The Care App requires certain configurations to function properly. The configuration settings can be found in the Django project's `settings.py` file. Below are the important configuration variables:

- `EMAIL_HOST_USER`: The email address used to send appointment-related emails.

## Usage

The Care App provides the following views and functionalities:

### Home View

- URL: `/`
- Description: Renders the homepage of the Care App.
- Function: `home(request)`

### About View

- URL: `/about/`
- Description: Renders the About page of the Care App.
- Function: `about(request)`

### Facilities View

- URL: `/facilities/`
- Description: Renders the Facilities page of the Care App.
- Function: `facilities(request)`

### Team View

- URL: `/team/`
- Description: Renders the Team page of the Care App and displays information about the team members.
- Function: `team(request)`

### Appointment View

- URL: `/appoint/`
- Description: Allows users to book an appointment by filling out a form. Sends an email confirmation to the user.
- Function: `appoint(request)`
- Method: POST
- Form Fields:
- `first_name`: First name of the user.
- `last_name`: Last name of the user.
- `email`: Email address of the user.
- `dateTime`: Date and time of the appointment.
- `phone`: Phone number of the user.
- `depart`: ID of the selected department.
- `doctor`: ID of the selected doctor.
- On successful submission of the form, the user receives an email confirmation, and a success message is displayed.

### Contact View

- URL: `/contact/`
- Description: Allows users to send a contact request by filling out a form.
- Function: `contact(request)`
- Method: POST
- Form Fields:
- `name`: Name of the user.
- `email`: Email address of the user.
- `subject`: Subject of the contact request.
- `phone`: Phone number of the user.
- `message`: Message content of the contact request.
- On successful submission of the form, a success message is displayed.

### Get Details View

- URL: `/get_details/`
- Description: Returns a JSON response containing the list of doctors based on the selected department.
- Function: `get_details(request)`
- Method: GET
- Query Parameter: `depart_id` - ID of the selected department.
- Renders the `doctor_dropdown_list_options.html` template with the retrieved list of doctors.

## Dependencies

The Care App relies on the following dependencies:

- Django: A high-level Python web framework.
- Django Templated Email: A Django app for sending templated emails.
- Django Widget Tweaks: A Django app for adding simple template filters for Django forms.
- Django Crispy Forms: A Django app that helps you create beautiful forms easily and without re-inventing the wheel.
- Django Environment Variables: A Django app for loading environment variables from a file.
- Gunicorn: A Python WSGI HTTP Server for UNIX.
- Whitenoise: A Django app for serving static files efficiently.
- Psycopg2: A PostgreSQL adapter for Python.

## File Structure

The important files and directories in the repository are as follows:

- `manage.py`: The Django project's management script.
- `care/`: The Django project directory.
- `settings.py`: The project's settings file.
- `urls.py`: The project's URL configuration.
- `wsgi.py`: The WSGI application entry point.
- `app/`: The Django app directory.
- `views.py`: Contains the views and their corresponding functions.
- `forms.py`: Contains the forms used in the app.
- `models.py`: Contains the database models used in the app.
- `templates/`: Contains the HTML templates used for rendering the views.
- `static/`: Contains static files such as CSS, JavaScript, and images.

## Contributing

If you want to contribute to the Care App, you can follow the steps below:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes.
4. Make the desired changes and commit them.
5. Push the changes to your forked repository.
6. Create a pull request on the original repository to submit your changes for review.

## License

The Care App is released under the [MIT License](LICENSE).

## Credits

The Care App is developed and maintained by Om Pchauli.












