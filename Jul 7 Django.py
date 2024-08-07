'''DJANGO - back-end server side web framework
Is free Open source and written in python
Makes it easier to build web pages using python

DJANGO takes care of difficult stuff so that you can concentrate on building web
applications.

Django emphasizes reusability of components, referred to as DRY(Don't Repeat
Yourself)

Django comes with ready to use features like login system and CRUD operations
(Create Read Update Delete)

Django is helpful for datbase driven websites.

How does Django works?
MVT design pattern - Model View Template

Model- The data you want tp present
View- A request handler that returns the relevant template & content-based
on the request from the user
Template- A text file(like HTML file)mcontaining the layout of the web page,
with logic on how to display data


Web Architecture- Client -> requests-> Server-> response->Browser

Client & Browser - HTML, CSS, JS - Front End
Server - Python, PHP, Java, Pearl - Back End

In Django data is delivered as an Object Relational Mapping(ORM), which is a
technique designed to make it easier to work with databases.Most common way to
extract data from database is SQL.
ORM makes it easier to communicate with database,withoit having to write complex
SQL statements

Models are located in a file called models.py

View- fn or method that takes http req as arguments, imports the relevant models
and finds out what data to send to the template, and returns the final result.

Views are usually located in a file called view.py

Template- view decides what data to send to the template. Template describe how
the rsult shoudl be represented.

Django uses std HTML to describe the layout, but uses Django tags to add logic

Templates of applications in folder named templates.

URLs- Django provides a way to navigate around the different pages in a website
When a user requests a URL, Django decides which view it will send it to.
This is done in a file called urls.py

What happens ??
when Django is installed and 1st Django web application is created and browser
requests the URL, this is basically what happens:
1. Django receives the URL, cheks the urls.py file and calls the view that matches
the URL.
2. The View, located in view.py, checks for relevant models.
3. Models are imported from models.py file
4. The view then sends the data to a specified template in the template folder.
5. The template contains HTML and Django tags, and with the data it returns
finished HTML content back to browser.

FRAMEWORK
* Framework provides a Generic Structure(Base) upon which web application can be
developed
* It allows you to Focus on the application logic, rather than spending time to
create things from scratch
* Provide Security to your application, so no need for you to write security for
your application
* Since it provides Generic Structure, code maintainability become easy

Ready Made Code
* Login and Register Module
* Frameowrk provide ready made code for Login and Register
* Use Login and Register code to develop your application

Features of Django Framework
* Battery included Approach- backup approach.readily available codes
* Rapid Development
* Security- best defender against hacking attacks.security is taken care off
* Scalable- ability to work smoothly with increase in no. of users
* Admin Interface- Readymade admin interface. decides whomanages  and customise
the website.automatic Admin UI.
* REST Framework for API- Develop API for applications'''
















