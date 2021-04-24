from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import os

app = Flask(
        __name__,
        static_url_path="",
        static_folder="static",
    )

def template(title = "HELLO!", text = ""):
    now = datetime.datetime.now()
    timeString = now
    templateDate = {
        'title' : title,
        'time' : timeString,
        'text' : text
        }
    return templateDate

@app.route("/")
def initial():
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/last_watered")
def ret_last_watered():
    templateData = template(text = water.get_last_watered())
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action():
    status = water.get_status()
    message = ""
    if (status == 1):
        message = "گلدان دارای آب است"
    else:
        message = "گلدان خشک است!"

    templateData = template(text = message)
    return render_template('main.html', **templateData)

@app.route("/water")
def action2():
    water.pump_on()
    templateData = template(text = "آب داده شد!")
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_watering(toggle):
    running = False
    if toggle == "ON":
        templateData = template(text = "آبیاری اتوماتیک فعال شد!")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templateData = template(text = "قبلا فعال شده است")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.4 auto_water.py&")
    else:
        templateData = template(text = "آبیاری اتوماتیک غیر فعال شد")
        os.system("pkill -f water.py")

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)