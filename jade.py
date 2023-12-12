from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime
# import datetime
import calendar
from MakeMyTrip import Test
from GoIbibo import Test1
import multiprocessing

jade = Flask(__name__)

@jade.route("/results", methods=["GET", "POST"])
def results():
    source = request.args.get("source")
    destination = request.args.get("destination")
    date_ymd = request.args.get("date")
    
    a = datetime.strptime(date_ymd, "%Y-%m-%d")
    date_dmy = a.strftime("%m/%Y")
    date = a.strftime("%d")
    mon = calendar.month_name[int(date_dmy[0:2])] + ' ' + date_dmy[3:]
    # print(type(source), type(destination), type(date), type(mon))
    # date1 = datetime.strptime(date_ymd, "%d %m %Y")
    b = datetime.strptime(date_ymd, "%Y-%m-%d").weekday()
    b1 = calendar.day_name[b]
    date_pass = b1[:3]
    
    result_queue1 = multiprocessing.Queue()
    result_queue2 = multiprocessing.Queue()
    
    c1 = Test(source, destination, date, mon, date_pass, result_queue1)
    # c2 = c1.gb()
    c3 = Test1(source, destination, date, mon, date_pass, result_queue2)
    # c4 = c3.gb()
    
    process1 = multiprocessing.Process(target=c1.mmt)
    process2 = multiprocessing.Process(target=c3.gb)
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    result1 = result_queue1.get()
    result2 = result_queue2.get()
    
    # data = {"status": 200, "MakeMyTrip": result1[0], "url1": result1[1]}
    var = "₹ " + result2[0] + " per adult"
    data = {"status": 200, "MakeMyTrip": result1[0], "url1": result1[1], "GoIbibo": var, "url2": result2[1]}
    return render_template("results.html", data=data)

@jade.route("/details", methods=["GET", "POST"])
def details():
    if request.method == "POST":
        source = request.form.get("from")
        destination = request.form.get("to")
        date = request.form.get("date")
        return redirect(url_for("results", source=source, destination=destination, date=date))
    return render_template("details.html")
    
@jade.route("/")
def home():
    return render_template("homepage.html")

if __name__ == '__main__':
    jade.run(debug=True, port=5000)