from flask import Flask
from threading import Thread
import os
import random

app = Flask("")

@app.route("/")
def main():
  file = os.listdir("./cogs")
  file = file[1:]
  file = random.choice(file)
  with open(f"./cogs/{file}","r") as r:
    p = r.readlines()
    k = ""
    for x in p:
      k+=f"<pre>{x}</pre>"
      
    return k

def run():
  app.run(host="0.0.0.0",port="8080")

def keep_alive():
  Thread(target=run).start()