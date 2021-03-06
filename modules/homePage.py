from init import *
from init.pattern import check_pattern

home_page = Blueprint('home_page', __name__)


@home_page.route('/customerHome')
def customerHome():
    if session.get('user'):
        cid = session.get('user')
        print("customer id: ", cid)

        conn = mysql.connect()
        cursor = conn.cursor()

        # customers: customer_id, customer_username, customer_firstname, customer_lastname, customer_password, timestamp

        # get customer's information
        sql = "select customer_id, customer_username, customer_firstname, customer_lastname from customers where customer_id = %s"
        val = cid
        cursor.execute(sql, val)
        data = cursor.fetchall()
        user_info = {"User Name": data[0][1], "First Name": data[0][2], "Last Name": data[0][3]}

        # get customer's requests
        sql = "select a.request_id, book_name, a.book_sto_id, request_status, request_start, request_stop, datediff(request_stop, curdate()) " \
              "from requests a join books_storage b join books c where a.customer_id = %s and " \
              "a.book_sto_id = b.book_sto_id and b.book_id = c.book_id"
        val = cid
        cursor.execute(sql, val)
        req_cols = (("ID", "Book Name", "Book Storage ID", "Status", "Start", "Stop", "Overdue", "Receipt", "Operation"))
        requests = cursor.fetchall()

        # get customer's reservations
        sql = "select a.reservation_id, reservation_date, room_id from reservations as a, rooms_has_reservations as b " \
              "where a.customer_id = %s and a.reservation_id = b.reservation_id; "
        val = cid
        cursor.execute(sql, val)
        reservations = cursor.fetchall()
        res_cols = ("ID", "Date", "Room")

        conn.commit()
        cursor.close()
        conn.close()
        print(requests)
        print(reservations)

        return render_template('customerHome.html', user_info=user_info, requests=requests, req_cols=req_cols, reservations=reservations, res_cols=res_cols)
    else:
        return redirect('/signIn')
