import mysql.connector
import qr
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------- BACKEND (UNCHANGED) -----------------
conn_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    password="26Ta1296##",
    database="more_supermarket"
)
cur_obj = conn_obj.cursor()

def data_entry_customer(c_name, c_address, cust_ph_no):
    sql = "INSERT INTO customer (c_name, c_address, ph_no) VALUES(%s, %s, %s)"
    data = (c_name, c_address, cust_ph_no)
    try:
        cur_obj.execute(sql, data)
        conn_obj.commit()
    except mysql.connector.Error as err:
        print("Details should be entered correctly", err)
        conn_obj.rollback()

def data_retrieve_customer(cust_ph_no):
    query = f"select * from customer where ph_no={cust_ph_no};"
    try:
        cur_obj.execute(query)
        result1 = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result1

def data_entry_product(p_name, p_price, p_stock):
    sql="INSERT INTO product_details (p_name, p_price, p_stock) VALUES (%s, %s, %s)"
    data=(p_name,p_price,p_stock)
    try:
        cur_obj.execute(sql,data)
        conn_obj.commit()
    except mysql.connector.Error as err:
        print("Details should be entered correctly",err)
        conn_obj.rollback()

def data_retrieve_product(p_id):
    query=f"select * from product_details where p_id={p_id}"
    try:
        cur_obj.execute(query)
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as err:
        print("Details should be entered correctly",err)
        conn_obj.rollback()
    return result

def data_entry_bill_details(bill_id,product_id,product_name,product_quantity):
    sql="insert into bill_details (bill_id, product_id, product_name, product_quantity) values (%s, %s, %s, %s)"
    data=(bill_id,product_id,product_name,product_quantity)
    try:
        cur_obj.execute(sql,data)
        conn_obj.commit()
    except mysql.connector.Error as err:
        print("Details should be entered correctly",err)
        conn_obj.rollback()

def data_entry_analytics_table(customer_id, customer_name, total_bill_amount):
    sql="insert into analytics_table (customer_id,customer_name, total_bill_amount) values (%s,%s, %s)"
    data=(customer_id,customer_name,total_bill_amount)
    try:
        cur_obj.execute(sql,data)
        conn_obj.commit()
    except mysql.connector.Error as err:
        print("Details should be entered correctly",err)
        conn_obj.rollback()

def data_retrieve_analytics_table():
    query="select bill_id from analytics_table where bill_timestamp=(select max(bill_timestamp) from analytics_table)"
    try:
        cur_obj.execute(query)
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data:", e)
        conn_obj.rollback()
    return result

def data_retrieve_login(user_id):
    query=f"select * from login where userid='{user_id}'"
    try:
        cur_obj.execute(query)
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as err:
        print("Details should be entered correctly",err)
        conn_obj.rollback()
    return result

# ----------------- FRONTEND (Tkinter) -----------------
root = tk.Tk()
root.title("Supermarket Billing System")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

# --------------- LOGIN SCREEN ----------------
def login_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)
    tk.Label(root, text="User ID:", bg="#f0f0f0").pack()
    user_entry = tk.Entry(root, width=30)
    user_entry.pack()

    tk.Label(root, text="Password:", bg="#f0f0f0").pack()
    pass_entry = tk.Entry(root, width=30, show="*")
    pass_entry.pack()

    def do_login():
        user_id = user_entry.get().strip()
        p_word = pass_entry.get().strip()
        login_details_db = data_retrieve_login(user_id)

        if login_details_db and login_details_db[-1] == p_word:
            messagebox.showinfo("Success", "Access Granted")
            main_menu()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    tk.Button(root, text="Login", command=do_login, bg="black", fg="white").pack(pady=15)

# --------------- MAIN MENU ----------------
def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Main Menu", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)
    tk.Button(root, text="Billing", width=20, command=billing_screen).pack(pady=10)
    tk.Button(root, text="Product Entry", width=20, command=product_entry_screen).pack(pady=10)

# --------------- PRODUCT ENTRY ----------------
def product_entry_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Product Entry", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(root, text="Product Name").pack()
    name_entry = tk.Entry(root, width=30)
    name_entry.pack()
    tk.Label(root, text="Price").pack()
    price_entry = tk.Entry(root, width=30)
    price_entry.pack()
    tk.Label(root, text="Stock").pack()
    stock_entry = tk.Entry(root, width=30)
    stock_entry.pack()

    def save_product():
        p_name = name_entry.get().strip().title()
        p_price = price_entry.get().strip()
        p_stock = stock_entry.get().strip()
        data_entry_product(p_name, p_price, p_stock)
        messagebox.showinfo("Success", "Product Added Successfully")

    tk.Button(root, text="Save", command=save_product, bg="green", fg="white").pack(pady=20)

# --------------- BILLING SCREEN ----------------
def billing_screen():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Billing", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(root, text="Customer Phone Number").pack()
    ph_entry = tk.Entry(root, width=30)
    ph_entry.pack()

    def start_bill():
        cust_ph_no = ph_entry.get().strip()
        result_from_customer = data_retrieve_customer(cust_ph_no)

        if result_from_customer:
            messagebox.showinfo("Customer Found", f"{result_from_customer}")
            start_gui_billing(result_from_customer)
        else:
            messagebox.showinfo("New Customer", "Enter new customer details")
            new_customer_screen(cust_ph_no)

    tk.Button(root, text="Start Billing", command=start_bill, bg="black", fg="white").pack(pady=20)

# --------------- NEW CUSTOMER ----------------
def new_customer_screen(phone):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="New Customer", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(root, text="Name").pack()
    n_entry = tk.Entry(root, width=30)
    n_entry.pack()
    tk.Label(root, text="Address").pack()
    a_entry = tk.Entry(root, width=30)
    a_entry.pack()

    def save_new_customer():
        data_entry_customer(n_entry.get(), a_entry.get(), phone)
        result = data_retrieve_customer(phone)
        start_gui_billing(result)

    tk.Button(root, text="Save Customer", command=save_new_customer, bg="green", fg="white").pack(pady=20)

# --------------- BILLING PROCESS ----------------
def start_gui_billing(customer):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Billing", font=("Arial", 16, "bold")).pack(pady=20)

    total_bill = tk.DoubleVar(value=0)

    tk.Label(root, text="Enter GST (%)").pack()
    gst_entry = tk.Entry(root)
    gst_entry.pack()

    def scan_product():
        p_id = qr.qr_code_scanner()
        result = data_retrieve_product(p_id)
        if not result:
            messagebox.showerror("Error", "Product not found!")
            return

        p_name = result[1]
        p_price = float(result[2])

        qty_win = tk.Toplevel(root)
        qty_win.title("Quantity")
        tk.Label(qty_win, text=f"Product: {p_name}").pack(pady=10)
        qty_entry = tk.Entry(qty_win)
        qty_entry.pack()

        def add_item():
            qty = int(qty_entry.get())
            last_bill_id = data_retrieve_analytics_table()
            new_bill_id = (last_bill_id[0] + 1) if last_bill_id else 1
            data_entry_bill_details(new_bill_id, p_id, p_name, qty)
            cost = qty * p_price
            total_bill.set(total_bill.get() + cost)
            messagebox.showinfo("Added", f"Added {p_name}, Cost: {cost}")
            qty_win.destroy()

        tk.Button(qty_win, text="Add", command=add_item).pack(pady=10)

    def finalize_bill():
        try:
            gst = float(gst_entry.get())
        except:
            gst = 0
        final = total_bill.get() * (1 + gst / 100)
        data_entry_analytics_table(customer[0], customer[1], final)
        messagebox.showinfo("Final Bill", f"Total: {total_bill.get()} + GST = {final}")
        main_menu()

    tk.Button(root, text="Scan Product", command=scan_product, bg="blue", fg="white").pack(pady=20)
    tk.Button(root, text="Finish Billing", command=finalize_bill, bg="green", fg="white").pack(pady=20)

# ---------------- START APP ----------------
login_screen()
root.mainloop()
conn_obj.close()
