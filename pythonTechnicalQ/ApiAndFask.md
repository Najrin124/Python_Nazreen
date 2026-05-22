introduction to apis and flask

understand what api is
understand how abckedna nd frontend communicates
install flask in vs code
create our first flask server
create our first api
test api in brwoser and postman
understand routes, request, response and json - javascript object notation



restaurant - full stack application
front end - menu and waiter(this is what customer sees)
backend - kitchen(where actual work happens)
database - storage room/fridge

backend devlopment handles

login
registration
saving data
fetching data
calcualtions
authentication
api's

API - application programming interface

it act as mediator between 2 systems

flask - light weight python framework used to build 

APIs
websites
backend services



why flask

simple
light weight
python based
flexible


local host - your own computer act as a server

route - means url path

/ - home page
/about - about
/contact - contact page

json - javascrupt object notation - its like a dictionary format

http methods

get - fetch data
post - send data
put - update data
patch - patches the data 
delete - delete dataa

postman - api testing tool

day 2

understand http methods - get, post, put, patch, delete
dynamic routes
url parameters - means giving dynamic value sin url - we can pass the variable as parameters in url from the fucntion
query parameters - used for search, filtering, pagination , sorting, etc
request object - it contains client data, which is used for query paarameetrs, forms data, json body, headers, files, etc
get apis
post apis
json request body - data sent from client to backend
sending data from postman
json request and response
status codes

200 - success
201 - created
400 - bad request
404 - not found
500 - server error





---- - 1. What is an API?

Answer:
API (Application Programming Interface) allows different applications to communicate with each other.

Example:

Frontend sends request to backend API
Backend returns JSON response

Example:

{
  "name": "John",
  "age": 25
}
2. What is REST API?

Answer:
REST API follows REST principles using HTTP methods.

Main methods:

GET → Fetch data
POST → Create data
PUT → Update full data
PATCH → Partial update
DELETE → Remove data
3. Difference between GET and POST?
GET	POST
Fetch data	Send/Create data
Data in URL	Data in body
Less secure	More secure
Cacheable	Not cacheable
4. What is Flask?

Answer:
Flask is a lightweight Python web framework used for:

APIs
Web applications
Backend services

Example:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

app.run()
5. Why Flask instead of Django?

Answer:

Flask:

Lightweight
Flexible
Easy for APIs
Small projects

Django:

Full-featured
Built-in admin
Large applications

Interview Tip:

“I prefer Flask for microservices and REST APIs because it is simple and customizable.”

6. What is Routing in Flask?

Answer:
Routing maps URL to function.

Example:

@app.route("/users")
def users():
    return "Users List"
7. How to create API in Flask?

Answer:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({
        "users": ["A", "B"]
    })

app.run(debug=True)
8. What is jsonify()?

Answer:
jsonify() converts Python dictionary into JSON response.

Example:

return jsonify({"name": "John"})
9. What are HTTP Status Codes?

Important codes interviewer asks:

Code	Meaning
200	Success
201	Created
400	Bad Request
401	Unauthorized
404	Not Found
500	Internal Server Error

Example:

return jsonify({"msg": "Created"}), 201
10. What is request object in Flask?

Answer:
Used to get client data.

Example:

from flask import request

data = request.json
name = data["name"]
11. Difference between PUT and PATCH?

Answer:

PUT:

Updates entire resource

PATCH:

Updates partial resource

Example:

PATCH /user/1
{
  "name": "Ram"
}
12. How to connect database in Flask?

Answer:
Mostly using:

SQLite
MySQL
PostgreSQL

With:

SQLAlchemy ORM

Example:

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
13. What is ORM?

Answer:
ORM (Object Relational Mapping) converts database tables into Python classes.

Popular ORM:

SQLAlchemy
14. What is Flask Blueprints?

Answer:
Blueprints help organize large Flask applications into modules.

Example:

from flask import Blueprint

user_bp = Blueprint("user", __name__)
15. What is CORS?

Answer:
CORS allows frontend and backend on different domains to communicate.

Example:
Frontend:

localhost:3000

Backend:

localhost:5000

Install:

pip install flask-cors

Example:

from flask_cors import CORS
CORS(app)
16. What is Authentication?

Answer:
Authentication verifies user identity.

Common methods:

JWT Token
Session Authentication
OAuth
17. What is JWT?

Answer:
JWT (JSON Web Token) is used for secure authentication.

Flow:

Login
Server generates token
Client sends token in headers

Example header:

Authorization: Bearer token
18. What is Middleware in Flask?

Answer:
Middleware processes request before response.

Example:

Logging
Authentication
Validation
19. How to handle errors in Flask?

Answer:

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404
20. What is Virtual Environment?

Answer:
Virtual environment isolates project dependencies.

Create:

python -m venv venv

Activate:

source venv/bin/activate
21. What is API Testing?

Answer:
Testing API endpoints using:

Postman
Pytest
Curl
22. Explain CRUD Operations
Operation	HTTP Method
Create	POST
Read	GET
Update	PUT/PATCH
Delete	DELETE
23. What is Flask RESTful?

Answer:
Flask-RESTful helps build REST APIs faster using classes and resources.

24. What is Dependency Injection?

Short Answer:
Passing dependencies externally instead of creating them inside class/function.

Interviewers ask this in experienced roles.

25. Explain API Security Best Practices

Answer:

Use HTTPS
JWT Authentication
Input validation
Rate limiting
Password hashing
Avoid exposing secrets
26. What interviewer checks before hiring?
They check:
1. API Fundamentals
HTTP methods
Status codes
JSON
REST concepts
2. Flask Knowledge
Routing
Request/Response
Database
Error handling
3. Practical Skills

Can you:

Build CRUD API?
Connect database?
Authenticate users?
Debug errors?
4. Communication

Can you explain concepts clearly?

5. Project Experience

Be ready to explain:

Your API project
Challenges
Deployment
Security
27. Common Coding Task in Interview

Interviewers may ask:

Build:
Login API
CRUD API
Todo API
User Management API

Example:

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    return jsonify({
        "message": "User created"
    }), 201
28. Important Advanced Questions
What is Stateless API?

Server does not store client session.

What is Idempotent Method?

Multiple identical requests give same result.

Examples:

GET
PUT
DELETE
What is Rate Limiting?

Restricts number of API requests.

What is Pagination?

Used for large datasets.

Example:

/api/users?page=1&limit=10
29. Best Answer for “Tell me about your Flask experience”

Example:

“I have built REST APIs using Flask with CRUD operations, JWT authentication, SQLAlchemy database integration, and API testing using Postman. I also handled error handling, validation, and deployment.”

30. Final Hiring Tips
To get selected:
Build 2–3 real Flask API projects
Learn JWT authentication
Practice CRUD APIs
Know HTTP status codes
Explain projects confidently
Practice coding live
Best Projects for Interview
Employee Management API
Todo API
E-commerce Backend
Authentication System
Blog API
Chat Backend API
Most Important Tools
Flask
Postman
SQLAlchemy
Docker
Git
GitHub
What is microservices, mvc
What is Microservices?

Microservices is a software architecture where a large application is divided into small independent services.

Each service:

Handles one specific functionality
Runs independently
Has its own database (sometimes)
Communicates using APIs
Simple Example

For an E-commerce Application:

Instead of one huge application:

Separate services:
User Service
Product Service
Payment Service
Order Service
Notification Service

Each service works independently.

Real Flow

Example:

User places order
Order Service creates order
Payment Service processes payment
Notification Service sends email/SMS

All communicate through APIs.

Advantages of Microservices
Benefit	Explanation
Scalability	Scale only needed service
Independent Deployment	Deploy one service without affecting others
Faster Development	Teams work separately
Better Maintenance	Smaller codebase
Fault Isolation	One service failure doesn't stop all
Disadvantages
Problem	Explanation
Complex Architecture	Hard to manage many services
Network Calls	Slower than monolithic sometimes
Deployment Complexity	Need Docker/Kubernetes often
Debugging Difficulty	Hard across multiple services
Monolithic vs Microservices
Monolithic	Microservices
Single application	Multiple small services
One codebase	Separate codebases
Hard to scale	Easy to scale
Tight coupling	Loose coupling
Example Interview Answer

“Microservices architecture breaks a large application into small independent services that communicate using APIs. It improves scalability, deployment flexibility, and maintainability.”

Common Technologies Used
Flask
Docker
Kubernetes
RabbitMQ
Apache Kafka
What is MVC?

MVC stands for:

Model — View — Controller

It is a software design pattern used to organize application code.

MVC Components
1. Model

Handles:

Database
Business logic
Data operations

Example:

class User(db.Model):
    name = db.Column(db.String(50))
2. View

Handles:

UI
HTML pages
What user sees

Example:

<h1>User Profile</h1>
3. Controller

Handles:

User requests
Application logic
Connects Model and View

Example:

@app.route("/users")
def users():
    return render_template("users.html")
MVC Flow
User sends request
Controller receives request
Controller talks to Model
Model fetches data
Controller sends data to View
View displays response
Simple Real Example
Food Delivery App
Model:

Stores:

Restaurants
Orders
Users
View:

Shows:

Menu page
Order page
Controller:

Processes:

Order requests
Login requests
Advantages of MVC
Benefit	Explanation
Clean structure	Organized code
Easy maintenance	Separate concerns
Reusable code	Easier development
Team collaboration	Frontend/backend separate
Difference Between MVC and Microservices
MVC	Microservices
Design Pattern	Architecture Style
Organizes code inside app	Splits entire app into services
Single application structure	Distributed systems
Mostly for development structure	Mostly for scalability
Short Interview Answer

“MVC is a design pattern that separates application into Model, View, and Controller for better code organization. Microservices is an architecture where applications are divided into independent services communicating through APIs.”

### Flask Knowledge * Routing * Request/Response * Database * Error handling

...

Got it — you want a clear interview-focused explanation of these Flask core topics. These are very frequently asked in API/Flask interviews.

1. Routing in Flask
What is Routing?

Routing means mapping a URL to a function.

When a user opens a URL, Flask decides which function should run.

Example:
@app.route("/")
def home():
    return "Home Page"
@app.route("/users")
def users():
    return "Users List"
Types of Routes:
Static route: /home
Dynamic route: /user/<id>
@app.route("/user/<int:id>")
def get_user(id):
    return f"User ID: {id}"
Interview Answer:

“Routing in Flask maps URLs to Python functions using decorators like @app.route(). It helps handle different endpoints in a web application.”

2. Request / Response in Flask
What is Request?

Request = data coming from client (frontend, Postman, mobile app)

You get it using:

from flask import request
Example:
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    return {"message": "Login successful"}
Types of request data:
JSON → request.json
Form data → request.form
Query params → request.args

Example:

/search?name=ram
request.args.get("name")
What is Response?

Response is what server sends back:

JSON
String
HTML
from flask import jsonify

return jsonify({"status": "success"})
Interview Answer:

“Request is the data sent by the client to the server, and response is the data returned by the server, usually in JSON format in REST APIs.”

3. Database in Flask

Flask does not come with a built-in database system. We use external tools like:

SQLite
MySQL
PostgreSQL

Most commonly used ORM:
SQLAlchemy

Example Model:
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
Insert Data:
user = User(name="Ram")
db.session.add(user)
db.session.commit()
Interview Answer:

“Flask uses external databases and SQLAlchemy ORM to interact with databases using Python classes instead of raw SQL queries.”

4. Error Handling in Flask
What is Error Handling?

It is used to handle errors gracefully instead of crashing the app.

Example 404 Error:
@app.errorhandler(404)
def not_found(error):
    return {"error": "Page not found"}, 404
Example 500 Error:
@app.errorhandler(500)
def server_error(error):
    return {"error": "Internal server error"}, 500
Using Try-Except:
@app.route("/divide")
def divide():
    try:
        result = 10 / 0
        return str(result)
    except Exception as e:
        return {"error": str(e)}
Interview Answer:

“Error handling in Flask is used to manage exceptions and return meaningful HTTP responses instead of application crashes using error handlers like @app.errorhandler().”

🔥 Quick Revision (Very Important)
Routing → URL to function mapping
Request → data from client
Response → data from server
Database → handled using SQLAlchemy ORM
Error handling → manage exceptions using errorhandler

If you want next step, I can give:

🔥 Flask CRUD interview coding questions
🔥 JWT authentication questions
🔥 Real interview project explanation
🔥 2–3 year experience Flask interview Q&A set




















