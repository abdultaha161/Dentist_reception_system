# 🦷 Dentist Reception System

## This is a small, begineers-level, Command line interface based project which simulate a basic reception system. 

## Introduction 
This project is python-based dentist reception system which can be used for a small dentist practice to manage patient and their appointment.It stores all the data in JSON file for easy and non-complicated handling. It has the following key features:


- Adding and viewing of patient records
- Booking of appointments with time conflict checks
- Issuing a unique ID for every patient and appointment
- Viewing appointment schedule by date
- Cancel existing appointments
- Saving a data in readable JSON file without using any external database system.
- Also includes simple unit tests using Python’s `unittest`
- Ruff linter to make the code look more presentable 
- Using __init.py files to mark directories as python packages

## Project Structure 

Dentist_reception_system/
├── data/                # this folder Stores data in JSON files
│ ├── appointments.json
│ └── patients.json
│
├── source_code/         # this folder has all the logical code which are used in this project
│ ├── __init__.py        # this files make this whole as a package 
│ ├── appointment.py     # contains class Appointment which is used to book appointment
│ ├── patients.py        # contains class Patients which is used to enter patients data
│ ├── registry.py        # it is used to save the appointment and patients data in JSON file
│ └── menu.py            # it contains all the main body of logical code,input and output functions 
│
├── tests/               # this folder has unittest 
│ ├── __init__.py
│ └── test_dentist_system.py    # this file class and functions to perform unit tests
│
├── main.py              # use to run the whole pogram 
└── README.md            # contains all the information about this project 


## Installation and usage Instructions 

### Requirements 
- Python 3.10 or above 
- No externam liberaries are required to run the project. 

### Steps to run the program 

- Bash
- Copy 
- Download 

### drop open the project directory 
locate the main.py file in the project directory and run the program. While running the project for the first time, the app will auto create the appointment.json and patients.json file in the data folder if they already don't exist. 

### Runnig a unittest
drop open the tests folder and there a test_dentist_system.py file is located. This file contains the 3 simple unittest which test the system for patient addition, appointment booking and appointment cancellation. 

Alternatively one can also run a unittest using a pytest tests/ command.

### Sample Workflow 

Once the program is run, following menu will appear. 

1. Add patient  
2. View current patients  
3. Book Appointment  
4. View Schedule  
5. Cancel Appointment  
6. Exit  

user can choose from this menu by selecting between option 1-6.
Option 1 will add the new patient to the system
Option 2 will help the user to view the current patients 
With option 3, one can book an appointment for the patient 
Option 4 is used to view the schedule of appointments for each different dates
Option 5 helps the user to cancel the appointment
And finally option 6 exits the program. 


## Limitation and Future improvement 

### Limitations 

- Command-line interface only
- No editing for existing entries
- Basic time conflict detection

### Future improvements

- Adding a search feature to search for patients record. 
- Assigning of patients to specific rooms or dentist.
- Making a web version 
- Calender visualiazation
- Email/SMS reminder 
- Adding machine learning so that we can predict the number of no shows for a patient. 

