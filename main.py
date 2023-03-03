import threading
import os
import time
from difflib import SequenceMatcher
import uuid
import flask
import requests
from replit import db


# set up database here
if "forums" not in db:
  db["forums"] = {}
if "accounts" not in db:
  db["accounts"] = {}


# creates a flask app
app = flask.Flask(__name__)

# the root url
@app.route("/")
def home():
  # serves a webpage from templates folder
  return flask.render_template("index.html")

@app.route("/login")
def login():
  # simple login page using replit auth
  return flask.render_template("login.html")

# the forum url
@app.route("/forum")
def forums():
  try:
    # check if user is in a forum
    forum = flask.request.args.get("forum")
    
    # returns forum page
    return flask.render_template("forum.html",forum=db["forums"][forum])
  except:
    pass
  
  # if no forum, return forums "homepage"
  return flask.render_template("forums.html",forums=dict(sorted(db["forums"].items(), key=lambda item: item[1]["time"], reverse=True)))

@app.route("/forum",methods=["POST"])
def post():
  # check if user is logged in
  username = flask.request.headers.get("X-Replit-User-Name")
  
  if not username:
    # redirects to login
    return flask.redirect("/login")
  
  # gets query, url looks like:
  # .../forum?forum=(forum name)
  forum = flask.request.args.get("forum")
  
  search = flask.request.form.get("search")
  comment = flask.request.form.get("comment")
  create = flask.request.form.get("create")
  title = flask.request.form.get("title")
  desc = flask.request.form.get("desc")
  
  if search:
    # search here
    forums = db["forums"]
    for forum, data in db["forums"].items():
      forums[forum]["score"] = SequenceMatcher(None, search, data["title"]).ratio() # sort
    
    forums = dict(sorted(forums.items(), key=lambda item: item[1]["score"], reverse=True)) # sort dict
    
    # return sorted data
    return flask.render_template("forums.html",forums=forums)
  
  if comment:
    # add comment to user's current forum
    db["forums"][forum]["comments"].insert(0,{"content":comment,"user":username,"date":time.ctime()})
    
    return flask.redirect(f"/forum?forum={forum}")
  
  if create:
    return flask.render_template("create.html")
  
  if title and desc: # means they are creating a forum
    id = str(uuid.uuid4()) # generate id for forum
    
    # save to db
    db["forums"][id] = {"title":title,"desc":desc,"date":" ".join(time.ctime().split()[:3]),"time":time.time(),"op":username,"comments":[]}
    
    # reload their page
    return flask.redirect(f"/forum?forum={id}")
  
  # if no forms were filled, reload
  return flask.redirect("/forum")

@app.route("/youtube")
def youtube():
  return flask.render_template("youtube.html")

@app.route("/discord")
def discord():
  return flask.render_template("discord.html")

@app.route("/tutos")
def tutos():
  return flask.render_template("tutos.html")

@app.route("/tutos/part-1-decomp")
def tutos_decomp_1():
  return flask.render_template("tutos/part-1-decomp.html")
  
@app.route("/profile")
def profile():
  username = flask.request.headers.get("X-Replit-User-Name")
  
  if not username:
    return flask.redirect("/login")
  else:
    return flask.redirect("/") # you can add to this!


def ping():
  # ping this site every 600 seconds to keep it on
  while True:
    time.sleep(600)
    try:
      requests.get(f'https://{os.environ["REPL_SLUG"]}.{os.environ["REPL_OWNER"]}.repl.co')
    except Exception as e:
      print(e)


keep_alive = threading.Thread(target=ping)
# terminate sub thread when main thread stops
keep_alive.daemon = True

# start the thread
keep_alive.start()

# starts the server
app.run("0.0.0.0")
