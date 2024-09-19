# EStory

This repository is home to the EStory app: A tool designed for museums to keep track of all their objects, but also that let their visitors consult everything that is available for them to see.

### What is available now
- Authentication system 
- Creating and editing objects

### Roadmap
#### Soon
- Listing and creating object operations
- Listing and creating object loans
#### In the future
- A vision of the objects by the visitors
- A visual tool to organize collections and easily being able to move objects to and from storage
- A map editing system to have a visual way of seeing which objects are in which room

## Installation

- Clone the repo
- Change the database settings in `settings.py` with the informations of your database
- Install the necessary python modules `pip install -r requirements.txt`
- Launch the server`python manage.py runserver 0.0.0.0:8000`
- Run the necessary migrations to create the database tables `python manage.py migrate`

## Tech Stack
This application uses Django 5 as well as Vue.js 3, alongside multiple Javascript libraries used for the UI (complete list coming soon).
