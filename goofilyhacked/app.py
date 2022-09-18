# importing Flask and other modules
from flask import Flask, request, render_template

import pyautogui
import webbrowser as web
import time
import pandas as pd

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():        
    return render_template("index.html")

@app.route('/whatsapp', methods =["GET", "POST"])
def whatsappSpammer():
    if request.method == "POST":
        
        num = request.form.get("num",type=int)
        contact=request.form.get("contact")
        message = request.form.get('message')
        message=message.split()

        web.open("https://web.whatsapp.com/send?phone="+contact)
        print(message)
        time.sleep(5)
        for i in range(0,num):
            for j in range(len(message)):
                for ch in message[j]:
                    pyautogui.press(ch)
                pyautogui.press(" ")
                pyautogui.press("enter")
       
    return render_template("index.html")

@app.route('/screen', methods =["GET", "POST"])
def screenSpammer():
    if request.method == "POST":
        
        num = request.form.get("num",type=int)
        message = request.form.get('message',type)
      
        total_breaks = num
        break_count = 0
        while(break_count < total_breaks):
            time.sleep(2)
            web.open(message)
            break_count = break_count + 1

    return render_template("index.html")

if __name__=='__main__':
    app.run()
