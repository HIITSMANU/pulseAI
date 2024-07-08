
# PulseAI

PulseAI is a hospital management system where the patient registers himself and books a appointment of the doctor and additionally he can post blogs of his own and can comment on other's blogs. Here Doctor(Admin) can track the patient details and can change the status of appointment of the patient 
, Basically there are two users 1.**Patient(User)**,2.**Doctor(Admin)** 

**ADMIN**- Doctor logs in and accesses admin dashboard.
Doctor manages appointments and patient interactions.
Doctor publishes and manages blog posts.
Doctor reviews patient test results and assigns medications.
Doctor uses inline stack for managing patient visit records.

**USER**- Patient registers and logs in.Patient reads and comments on blogs.Patient fills out a heart disease test form.AI model predicts heart disease risk.Patient views test results and can schedule appointments.



## Features

**Admin**
- Doctor logs in and accesses admin dashboard.
- Doctor manages appointments and patient interactions.
- Doctor publishes and manages blog posts.
- Doctor reviews patient test results and assigns medications.
- Doctor uses inline stack for managing patient visit records.

**Student**
- Patient registers and logs in.
- Patient reads and comments on blogs.
- Patient fills out a heart disease test form.
- AI model predicts heart disease risk.
- Patient views test results and can schedule appointments.


## Tech Stack

**Frontend:** Html, Css, Bootstrap 

**Server:** db.sqlite3 

**Backend:** Django


## Screenshots

**Homepage**
![Screenshot 2024-07-08 141610](https://github.com/HIITSMANU/pulseAI/assets/132491372/71f491ec-5b65-4c73-8730-570d5a4f7ac2)
![Screenshot 2024-07-08 141659](https://github.com/HIITSMANU/pulseAI/assets/132491372/e0227ddf-a103-4c18-82ad-d840ef7de112)
![Screenshot 2024-07-08 141746](https://github.com/HIITSMANU/pulseAI/assets/132491372/0777e3c1-9175-47d8-b8a5-205119c1ade5)

**About**
![Screenshot 2024-07-08 141835](https://github.com/HIITSMANU/pulseAI/assets/132491372/68753b09-7dc0-46ec-b32a-fb4d1836123d)

**Blogs**
![Screenshot 2024-07-08 141932](https://github.com/HIITSMANU/pulseAI/assets/132491372/6a20b9dc-416c-4337-b35c-4097ed229322)

**SignUp**
![Screenshot 2024-07-08 142027](https://github.com/HIITSMANU/pulseAI/assets/132491372/6346e8cb-616b-4932-9bb2-840330ea68f9)

**SignIn**
![Screenshot 2024-07-08 142113](https://github.com/HIITSMANU/pulseAI/assets/132491372/ffd1f1b0-b541-4e7a-8150-3067a5b859ff)

**AI Driven Test(Heart Disease Probability Predictor)**
![Screenshot 2024-07-08 142424](https://github.com/HIITSMANU/pulseAI/assets/132491372/74820a52-5cda-49ff-b75d-19f16d0a6834)

**Book an Appointment**
![Screenshot 2024-07-08 142455](https://github.com/HIITSMANU/pulseAI/assets/132491372/8a2b16ee-5338-4973-a2a9-f02244c63d0a)

**Profile View**
![Screenshot 2024-07-08 142545](https://github.com/HIITSMANU/pulseAI/assets/132491372/af788978-fc38-470c-aebd-269dc681791d)

**After Patient Login**
![Screenshot 2024-07-08 142223](https://github.com/HIITSMANU/pulseAI/assets/132491372/068c57e2-5f8e-4420-a79b-76268868bc24)



## Running Tests

To run tests, run the following command

How to CreateVirualEnvironment(Refer to the Below Link)
```bash
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
```

How to StartProject 
```bash
  django-admin startproject projectname
```
How to CreateApp
```bash
  python manage.py startapp appname
```

Build Command 
```bash
  python manage.py -r requirements.txt
```

Run Command
```bash
  python manage.py runserver
```

To see the dependencies
```bash
  pip freeze
```

To make migrations
```bash
  python manage.py makemigrations
  python manage.py migrate
```

To make admin registration
```bash
  python manage.py createsuperuser
  enter email:
  enter password:
  re-enter password:
```






