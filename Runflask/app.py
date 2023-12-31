from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import random

app = Flask(__name__)

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'project66',
}
app = Flask(__name__)



def get_db_connection():
    return mysql.connector.connect(**config)



@app.route('/')
def index():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # เราใช้คำสั่ง SQL เพื่อดึงข้อมูลทั้งหมดจากตาราง menu
        select_query = "SELECT * FROM menu_staple"
        cursor.execute(select_query)
        all_rows = cursor.fetchall()

        # สุ่มเมนูและเลือกให้มีจำนวนเมนูตามที่คุณต้องการ (ในที่นี้คือ 6) โดยไม่ซ้ำกัน
        random_rows = random.sample(all_rows, 6)

        return render_template('index.html', rows=random_rows)

    except mysql.connector.Error as e:
        return f"Error: {e}"

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/nameofmenu')
def nameofmenu():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # เราใช้คำสั่ง SQL เพื่อดึงข้อมูลทั้งหมดจากตาราง menu
        select_query = "SELECT * FROM menu_staple"
        cursor.execute(select_query)
        all_rows = cursor.fetchall()

        return render_template('nameofmenu.html', rows=all_rows)

    except mysql.connector.Error as e:
        return f"Error: {e}"

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/รายการสมุนไพร')
def รายการสมุนไพร():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # เราใช้คำสั่ง SQL เพื่อดึงข้อมูลทั้งหมดจากตาราง menu
        select_query = "SELECT * FROM staple_list"
        cursor.execute(select_query)
        all_rows = cursor.fetchall()

        return render_template('รายการสมุนไพร.html', rows=all_rows)

    except mysql.connector.Error as e:
        return f"Error: {e}"

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


# @app.route('/รายการสมุนไพร')
# def รายการสมุนไพร():
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()

#         sort = request.args.get('sort', 'list_id')
#         order = request.args.get('order', 'asc')
#         page = int(request.args.get('page', 1))  # รับค่า 'page' จาก URL parameter
#         per_page = 25  # จำนวนรายการต่อหน้า

#         offset = (page - 1) * per_page

#         select_query = f"SELECT * FROM staple_list ORDER BY {sort} {order} LIMIT %s OFFSET %s"
#         cursor.execute(select_query, (per_page, offset))
#         rows = cursor.fetchall()

#         cursor.execute("SELECT COUNT(*) FROM staple_list")
#         total_rows = cursor.fetchone()[0]

#         num_pages = (total_rows + per_page - 1) // per_page

#         return render_template('รายการสมุนไพร.html', rows=rows, page=page, num_pages=num_pages, sort=sort, order=order)

#     except mysql.connector.Error as e:
#         return f"Error: {e}"

#     finally:
#         if 'connection' in locals() and connection.is_connected():
#             cursor.close()
#             connection.close()

#search 
# @app.route('/searchstaple', methods=['GET'])
# def search_staple():
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()

#         search_query = request.args.get('search')
#         if search_query:
#             # Modify the SELECT query to include a WHERE clause for searching
#             select_query = "SELECT * FROM staple_list WHERE staple_name LIKE %s OR advantage LIKE %s"
#             cursor.execute(select_query, ('%' + search_query + '%', '%' + search_query + '%'))
#         else:
#             # If no search query provided, retrieve all records
#             select_query = "SELECT * FROM staple_list"
#             cursor.execute(select_query)

#         rows = cursor.fetchall()

#         return render_template('staple_menu.html', rows=rows)

#     except mysql.connector.Error as e:
#         return f"Error: {e}"

#     finally:
#         if 'connection' in locals() and connection.is_connected():
#             cursor.close()
#             connection.close()

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/nameofmenu')
# def nameofmenu():
#     return render_template('nameofmenu.html')


@app.route('/menupad')
def menupad():
    return render_template('menupad.html')


@app.route('/menuyum')
def menuyum():
    return render_template('menuyum.html')


@app.route('/menuRoasted')
def menuRoasted():
    return render_template('menuRoasted.html')


@app.route('/menutod')
def menutod():
    return render_template('menutod.html')


@app.route('/menuSteamed')
def menuSteamed():
    return render_template('menuSteamed.html')


@app.route('/menuphla')
def menuphla():
    return render_template('menuphla.html')


@app.route('/menugrill')
def menugrill():
    return render_template('menugrill.html')


@app.route('/menumixed')
def menumixed():
    return render_template('menumixed.html')


@app.route('/menutom')
def menutom():
    return render_template('menutom.html')


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/รายการสมุนไพร')
# def รายการสมุนไพร():
#     return render_template('รายการสมุนไพร.html')


@app.route('/กระชาย')
def กระชาย():
    return render_template('กระชาย.html')


@app.route('/กระเทียม')
def กระเทียม():
    return render_template('กระเทียม.html')


@app.route('/กะเพรา')
def กะเพรา():
    return render_template('กะเพรา.html')


@app.route('/กะหล่ำม่วง')
def กะหล่ำม่วง():
    return render_template('กะหล่ำม่วง.html')


@app.route('/ขมิ้น')
def ขมิ้น():
    return render_template('ขมิ้น.html')


@app.route('/ข่า')
def ข่า():
    return render_template('ข่า.html')


@app.route('/ขิง')
def ขิง():
    return render_template('ขิง.html')


@app.route('/ขึ้นฉ่าย')
def ขึ้นฉ่าย():
    return render_template('ขึ้นฉ่าย.html')


@app.route('/แครอท')
def แครอท():
    return render_template('แครอท.html')


@app.route('/ตะไคร้')
def ตะไคร้():
    return render_template('ตะไคร้.html')


@app.route('/ตะไคร้ซอย')
def ตะไคร้ซอย():
    return render_template('ตะไคร้ซอย.html')


@app.route('/แตงกวา')
def แตงกวา():
    return render_template('แตงกวา.html')


@app.route('/ถั่วงอก')
def ถั่วงอก():
    return render_template('ถั่วงอก.html')


@app.route('/ถั่วฝักยาว')
def ถั่วฝักยาว():
    return render_template('ถั่วฝักยาว.html')


@app.route('/ถั่วลิสง')
def ถั่วลิสง():
    return render_template('ถั่วลิสง.html')


@app.route('/ใบชะพลู')
def ใบชะพลู():
    return render_template('ใบชะพลู.html')


@app.route('/ใบบัวบก')
def ใบบัวบก():
    return render_template('ใบบัวบก.html')


@app.route('/ใบมะกรูด')
def ใบมะกรูด():
    return render_template('ใบมะกรูด.html')


@app.route('/ใบสะระแหน่')
def ใบสาระแหน่():
    return render_template('ใบสะระแหน่.html')


@app.route('/ใบโหระพา')
def ใบโหระพา():
    return render_template('ใบโหระพา.html')


@app.route('/ผักชี')
def ผักชี():
    return render_template('ผักชี.html')


@app.route('/ผักชีซอย')
def ผักชีซอย():
    return render_template('ผักชีซอย.html')


@app.route('/ผักชีฝรั่ง')
def ผักชีฝรั่ง():
    return render_template('ผักชีฝรั่ง.html')


@app.route('/พริก')
def พริก():
    return render_template('พริก.html')


@app.route('/พริกขี้หนู')
def พริกขี้หนู():
    return render_template('พริกขี้หนู.html')


@app.route('/พริกขึ้หนูสวน')
def พริกขึ้หนูสวน():
    return render_template('พริกขึ้หนูสวน.html')


@app.route('/พริกขึ้หนูแห้ง')
def พริกขึ้หนูแห้ง():
    return render_template('พริกขึ้หนูแห้ง.html')


@app.route('/พริกจินดาแดง')
def พริกจินดาแดง():
    return render_template('พริกจินดาแดง.html')


@app.route('/พริกชี้ฟ้า')
def พริกชี้ฟ้า():
    return render_template('พริกชี้ฟ้า.html')


@app.route('/พริกชี้ฟ้าแดง')
def พริกชี้ฟ้าแดง():
    return render_template('พริกชี้ฟ้าแดง.html')


@app.route('/พริกชี้ฟ้าแดงแห้ง')
def พริกชี้ฟ้าแดงแห้ง():
    return render_template('พริกชี้ฟ้าแดงแห้ง.html')


@app.route('/พริกไทย')
def พริกไทย():
    return render_template('พริกไทย.html')


@app.route('/พริกไทยป่น')
def พริกไทยป่น():
    return render_template('พริกไทยป่น.html')


@app.route('/พริกไทยอ่อน')
def พริกไทยอ่อน():
    return render_template('พริกไทยอ่อน.html')


@app.route('/พริกสด')
def พริกสด():
    return render_template('พริกสด.html')


@app.route('/พริกแห้ง')
def พริกแห้ง():
    return render_template('พริกแห้ง.html')


@app.route('/มะกรูด')
def มะกรูด():
    return render_template('มะกรูด.html')


@app.route('/มะนาว')
def มะนาว():
    return render_template('มะนาว.html')


@app.route('/มะขาม')
def มะขาม():
    return render_template('มะขาม.html')


@app.route('/มะเขือเปราะ')
def มะเขือเปราะ():
    return render_template('มะเขือเปราะ.html')


@app.route('/มะพร้าว')
def มะพร้าว():
    return render_template('มะพร้าว.html')


@app.route('/มะม่วง')
def มะม่วง():
    return render_template('มะม่วง.html')


@app.route('/เม็ดมะม่วงหิมพานต์')
def เม็ดมะม่วงหิมพานต์():
    return render_template('เม็ดมะม่วงหิมพานต์.html')


@app.route('/รากผักชี')
def รากผักชี():
    return render_template('รากผักชี.html')


@app.route('/หอมแดง')
def หอมแดง():
    return render_template('หอมแดง.html')


if __name__ == '__main__':
    app.run(debug=True)
