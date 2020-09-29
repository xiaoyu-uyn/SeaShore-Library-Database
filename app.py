from init import *
from modules.homePage import home_page
from modules.signIn import sign_in
from modules.signUp import sign_up
from modules.resources import res
from modules.bookStorage import sto
from multiprocessing.pool import ThreadPool
app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(sign_in)
app.register_blueprint(sign_up)
app.register_blueprint(res)
app.register_blueprint(sto)

from flask import Flask, render_template, request, json, redirect, session, blueprints
from flaskext.mysql import MySQL
from flask.blueprints import Blueprint
import re
# html.escape() can be used to avoid XSS, but because of current bootstrap,
# it is not convinient to show on original characters on html files

# Customized functions in modules


app.secret_key = 'seashore-library-secrete-key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signUp.html')

@app.route('/newRequest')
def newRequest():
    # with book_storage_id
    # if(isBorrowed) -> [waiting list page]:'you will be notified once the book returned', button 'confirm'
    #                           -> request (status = 'W')

    # form
    # start_time, stop_time -> 'confirm'[LINK](bill) -> newBill
    return render_template('signUp.html')

@app.route('/newBill')
def newBill():
    # calculate amount
    # store bill in db 

    # show amount
    # 'pay'[LINKE] -> receipt
    return render_template('signUp.html')

@app.route('/receipt')
def receipt():
    # store receipt in db

    # show receipt
    return render_template('signUp.html')

@app.route('/changeProfile')
def changeProfile():

    return render_template('signUp.html')

@app.route('/showRooms')
def showRooms():
    # show all rooms 'floor', 'postition' -> 
    return render_template('signUp.html')


# log out current user
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


""" Waiting List Logic:
        Once a book returned, assume returned book re_book_sto_id

        select requests
        where book_sto_id = re_book_sto_id, status = W
        order by last_edit_time
"""
"""
    select date, beforeNoon
    where room_id = room1, date, beforeNoon
    reservations:
    input: currentdate- 9.22
            reservations: date, beforeNoon
            
    dates = [9.22,]
    beforeNoons = [1,]

    df = day_different(9.22,dates[0])   0
    x = (int)!beforeNoons[0]            0

    A[0,0,0,1,0,0]
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
