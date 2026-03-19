from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime, timedelta

# ================= DATABASE CONNECTION =================
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="RAHUL123",  # CHANGE THIS
        database="gym_management"
    )

# ================= AUTO EXPIRY UPDATE =================
def update_expiry_status():
    con = connect_db()
    cur = con.cursor()
    today = datetime.now().date()

    cur.execute("""
        UPDATE members
        SET status='Expired'
        WHERE expiry_date < %s
    """, (today,))

    cur.execute("""
        UPDATE members
        SET status='Active'
        WHERE expiry_date >= %s
    """, (today,))

    con.commit()
    con.close()

# ================= MAIN WINDOW =================
root = Tk()
root.title("Gym Member Management System - Pro Version")
root.geometry("1250x720")
root.config(bg="white")

title = Label(root, text="Gym Management System (Professional)",
              font=("Arial", 22, "bold"),
              bg="black", fg="white")
title.pack(fill=X)

# ================= VARIABLES =================
name_var = StringVar()
phone_var = StringVar()
email_var = StringVar()
gender_var = StringVar()
age_var = StringVar()
plan_var = StringVar()
selected_member_id = None

# ================= DASHBOARD =================
def load_dashboard():
    update_expiry_status()

    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM members")
    total_members = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM members WHERE status='Active'")
    active_members = cur.fetchone()[0]

    cur.execute("SELECT IFNULL(SUM(amount),0) FROM payments")
    total_revenue = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM attendance WHERE attendance_date=%s",
                (datetime.now().date(),))
    today_attendance = cur.fetchone()[0]

    lbl_total.config(text=f"Total Members: {total_members}")
    lbl_active.config(text=f"Active Members: {active_members}")
    lbl_revenue.config(text=f"Total Revenue: ₹{total_revenue}")
    lbl_attendance.config(text=f"Today Attendance: {today_attendance}")

    con.close()

dashboard_frame = Frame(root, bg="#ecf0f1", height=80)
dashboard_frame.pack(fill=X)

lbl_total = Label(dashboard_frame, font=("Arial", 12, "bold"), bg="#ecf0f1")
lbl_total.pack(side=LEFT, padx=20)

lbl_active = Label(dashboard_frame, font=("Arial", 12, "bold"), bg="#ecf0f1")
lbl_active.pack(side=LEFT, padx=20)

lbl_revenue = Label(dashboard_frame, font=("Arial", 12, "bold"), bg="#ecf0f1")
lbl_revenue.pack(side=LEFT, padx=20)

lbl_attendance = Label(dashboard_frame, font=("Arial", 12, "bold"), bg="#ecf0f1")
lbl_attendance.pack(side=LEFT, padx=20)

# ================= MEMBER FORM =================
frame = Frame(root, bd=4, relief=RIDGE, bg="white")
frame.place(x=20, y=150, width=400, height=500)

Label(frame, text="Member Form",
      font=("Arial", 15, "bold"), bg="white").grid(row=0, columnspan=2, pady=10)

Label(frame, text="Full Name").grid(row=1, column=0)
Entry(frame, textvariable=name_var).grid(row=1, column=1)

Label(frame, text="Phone").grid(row=2, column=0)
Entry(frame, textvariable=phone_var).grid(row=2, column=1)

Label(frame, text="Email").grid(row=3, column=0)
Entry(frame, textvariable=email_var).grid(row=3, column=1)

Label(frame, text="Gender").grid(row=4, column=0)
ttk.Combobox(frame, textvariable=gender_var,
             values=["Male", "Female"]).grid(row=4, column=1)

Label(frame, text="Age").grid(row=5, column=0)
Entry(frame, textvariable=age_var).grid(row=5, column=1)

Label(frame, text="Plan").grid(row=6, column=0)
plan_combo = ttk.Combobox(frame, textvariable=plan_var)
plan_combo.grid(row=6, column=1)

# ================= LOAD PLANS =================
def load_plans():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT plan_name FROM plans")
    plan_combo['values'] = [row[0] for row in cur.fetchall()]
    con.close()

load_plans()

# ================= SAVE MEMBER =================
def save_member():
    global selected_member_id
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT plan_id, duration_months FROM plans WHERE plan_name=%s",
                (plan_var.get(),))
    plan = cur.fetchone()
    if not plan:
        messagebox.showerror("Error", "Select Plan")
        return

    plan_id, duration = plan
    join_date = datetime.now()
    expiry_date = join_date + timedelta(days=30*duration)

    if selected_member_id is None:
        cur.execute("""INSERT INTO members
            (full_name, phone, email, gender, age, plan_id,
             join_date, expiry_date, status)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (name_var.get(), phone_var.get(), email_var.get(),
             gender_var.get(), age_var.get(),
             plan_id, join_date, expiry_date, "Active"))
    else:
        cur.execute("""UPDATE members SET
            full_name=%s, phone=%s, email=%s,
            gender=%s, age=%s, plan_id=%s
            WHERE member_id=%s""",
            (name_var.get(), phone_var.get(), email_var.get(),
             gender_var.get(), age_var.get(),
             plan_id, selected_member_id))

    con.commit()
    con.close()
    clear_fields()
    show_members()
    load_dashboard()
    selected_member_id = None
    messagebox.showinfo("Success", "Saved Successfully")

# ================= CLEAR =================
def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    gender_var.set("")
    age_var.set("")
    plan_var.set("")

# ================= SHOW MEMBERS =================
def show_members():
    con = connect_db()
    cur = con.cursor()
    cur.execute("""SELECT m.member_id, m.full_name,
                   p.plan_name, m.expiry_date, m.status
                   FROM members m
                   JOIN plans p ON m.plan_id=p.plan_id""")
    rows = cur.fetchall()
    member_table.delete(*member_table.get_children())
    for row in rows:
        member_table.insert("", END, values=row)
    con.close()

# ================= SELECT MEMBER =================
def select_member(event):
    global selected_member_id
    selected = member_table.focus()
    data = member_table.item(selected)
    row = data['values']
    if row:
        selected_member_id = row[0]
        name_var.set(row[1])
        plan_var.set(row[2])

# ================= DELETE =================
def delete_member():
    selected = member_table.focus()
    if not selected:
        return
    member_id = member_table.item(selected)['values'][0]
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM members WHERE member_id=%s", (member_id,))
    con.commit()
    con.close()
    show_members()
    load_dashboard()

# ================= PAYMENT =================
def record_payment():
    selected = member_table.focus()
    if not selected:
        messagebox.showerror("Error", "Select Member First")
        return

    member_id = member_table.item(selected)['values'][0]

    con = connect_db()
    cur = con.cursor()
    cur.execute("""SELECT price FROM plans
                   JOIN members ON plans.plan_id=members.plan_id
                   WHERE member_id=%s""", (member_id,))
    amount = cur.fetchone()[0]

    cur.execute("INSERT INTO payments (member_id, amount, payment_date) VALUES (%s,%s,%s)",
                (member_id, amount, datetime.now()))
    con.commit()
    con.close()

    receipt = f"""
    -------- GYM PAYMENT RECEIPT --------
    Member ID : {member_id}
    Amount Paid : ₹{amount}
    Date : {datetime.now().date()}
    -------------------------------------
    """
    messagebox.showinfo("Payment Successful", receipt)
    load_dashboard()

# ================= ATTENDANCE =================
def mark_attendance():
    selected = member_table.focus()
    if not selected:
        messagebox.showerror("Error", "Select Member First")
        return

    member_id = member_table.item(selected)['values'][0]
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO attendance (member_id, attendance_date) VALUES (%s,%s)",
                (member_id, datetime.now().date()))
    con.commit()
    con.close()
    messagebox.showinfo("Success", "Attendance Marked")
    load_dashboard()

# ================= TABLE =================
table_frame = Frame(root)
table_frame.place(x=450, y=150, width=750, height=350)

member_table = ttk.Treeview(table_frame,
                            columns=("ID","Name","Plan","Expiry","Status"),
                            show="headings")

for col in ("ID","Name","Plan","Expiry","Status"):
    member_table.heading(col, text=col)

member_table.pack(fill=BOTH, expand=1)
member_table.bind("<ButtonRelease-1>", select_member)

# ================= BUTTONS =================
Button(frame, text="Save Member", bg="green", fg="white",
       command=save_member).grid(row=7, columnspan=2, pady=10)

Button(frame, text="Delete Member", bg="red", fg="white",
       command=delete_member).grid(row=8, columnspan=2, pady=5)

Button(root, text="Record Payment", bg="blue", fg="white",
       command=record_payment).place(x=500, y=530, width=200)

Button(root, text="Mark Attendance", bg="orange", fg="white",
       command=mark_attendance).place(x=750, y=530, width=200)

# ================= INIT =================
show_members()
load_dashboard()

root.mainloop()
