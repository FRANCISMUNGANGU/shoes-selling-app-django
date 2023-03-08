DJANGO : web app framework which is used to develop web apps.

HOW DJANGO WORKS :

Design Pattern : MODEL : data that app uses  VIEW : the functions working on the data that the app is using TEMPLATE (MVT) : Interface /Client Sees.

1. Request Handling : the request received by the web server : events : Django passes the request via a web server gateway interface (WSGI) for a response :
2. URL routing : Once Django receives the request , it uses a URL dispatcher (defining an action) to match the requested url to a specific function
  '' /home ''  -> function -> logic -> returns a html interface.
3. Views Functions : a view function will take a request as an object and returns a response object. View functions are used to write the business logic/ manipulations on data.
4. Model : defines the structure of our database table : Django uses a tool called object-relational-mapper , which maps database tables to python objects (classes -> blueprint)
5. Templates : Contains HTML files and placeholders for dynamic content.
6. Responses : Once a view function is executed , it returns a response object , -> this objects come in various formats -> JSON. HTML . XML
7. Administration : Django has a fully created administration interface based of the models of the projects


HOW TO INSTALL DJANGO AND GET A SET UP / RUN A PROJECT
1. Check if python is installed : python --version
2. Install Python Django : pip install django
3. Create the project structure : django-admin startproject cruddjangoexample
4. Expain the key files :
    1. Manage.py : file that is responsible for running the django project
    2. Settings.py : configurations inclusion : -> connection to a database , connection to other extra packages(pip install ...), connection to the models.
    3. urls.py : This is the file used for url routing. -> indicate our routes
5. To run a django app we use the command: python manage.py runserver
6. We create an app module : python manage.py startapp modulename(employee)

-----------------------------------------------------------------------------------------------
7. Database set up for our app : modify our db configurations in setting.py for installed apps to add our module, and database to connect to our mysql sytem.
8. Modify your models.py to include tables to create and then Run Migrations to create the tables based off the models.
   - python manage.py makemigrations
   - python manage.py migrate
9.  if mysql error : pip install mysqlclient






























