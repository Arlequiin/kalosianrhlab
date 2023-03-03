# Flask Forum Starter
A full-featured Forum website made with Flask. This guide contains everything you need to get started with Flask, such as using a database, setting up frontend and backend and how to make them work together.

## Learn To Use Flask
With this Forum Starter, it is really easy to get started with Flask. In the next sections, I'll talk about the code in depth so that you can have all the tools you need to customize and expand your Flask Forum.

### Imports
This Repl uses a few libraries:

+ `threading` - To keep our code running 24/7
+ `os` - To get the URL of our Repl
+ `time` - Used to get the time, date, and more
+ `SequenceMatcher` - For our search function
+ `uuid` - Generate unique ids for our forums
+ `flask` - The framework of our server
+ `requests` - To ping our Repl
+ `replit db` - Database to store our data

### Getting Started
To get started, run this Repl. Replit will automatically install the libraries for you, without any hassle. To find the link to your site, simply go to the top right corner to find it.

## Understanding The Code
I have tried my best to explain the code in detail, but I don't always get everything. Feel free to ask if you are confused!

### Flask

+ `app = flask.Flask(__name__)`  
Creates a Flask application object named "app".
<br><br>
+ `@app.route`  
Decorator that specifies a path for your Flask application
<br><br>
+ `flask.render_template`  
Serves an HTML file from **templates** folder
<br><br>
+ `flask.request.args.get`  
A Flask method that gets the query string (ex ...?v=1)
<br><br>
+ `flask.request.form.get`  
A Flask method that gets input from HTML forms
<br><br>
+ `flask.redirect`  
Redirects user to a URL

### Replit DB

+ `from replit import db`   - Imports Replit DB

#### Using Replit DB:  

Replit DB is a key-value database, which means it is *almost* exactly like a Python dictionary. However, there are a few things to watch out for. 

#### Replit DB's quirks:

When you store something in Replit DB, it changes some data types.

+ `lists` - are changed to `ObservedList`
+ `dictionaries` - are changed to `ObservedDict`

You can use access the **value** attribute to get the normal data type.

Another "caveat" of using Replit DB is that the database is not shared across users. Instead, each user has their own database for each Repl which is terminated when the user logs out (Doesn't apply to "Owners" of the Repl). However, this isn't that big of an issue, especially in our case because we are using this on a server.

The final issue with Replit DB is that it can only store objects with a JSON equivalent.

#### Replit DB in action:
Using Replit DB is an extremely simple task. To create a key, simply do so as you would for a Python dictionary.

`db["your_key"] = "some_value"`

To delete a key, simply do:

`del db["your_key"]`

There are some more functionalities, but we won't get into that here.

### The HTML

While backend may be very important, our site's a blank screen without some frontend work! This section will guide you through some of the most important things for creating websites with Flask.

#### Jinja2 Template Engine:

In this code example, we only scratch the surface of what can be done using this. As I am still not very experienced with the different functionalities, I'll leave the reader to experiment and learn about this.

[Here's a helpful link.](https://jinja.palletsprojects.com/en/3.1.x/)

#### Form Inputs:

We can get input from HTML forms like this:

```
<form method="POST">
  <input name="form name" type="text">
  <input type="submit">
</form>
```
When submitted, you can access the form's contents like this:

`flask.request.form.get("form name")`

## In Conclusion

I hope this guide has been some help to you. Try to tweak the code around, as I believe that doing is the best learning!  

If you have further questions or concerns, feel free to leave a comment down below.

Cheers,

Icemaster