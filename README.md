# 🏋️ Gym Member Management System

A professional **Gym Member Management System** developed using **Python, Tkinter, and MySQL**. This desktop application helps gym owners efficiently manage members, membership plans, payments, attendance, and membership status through an intuitive graphical interface.

---

## 📌 Features

### 👤 Member Management
- Add new gym members
- Update existing member information
- Delete member records
- View all registered members
- Automatic form reset after operations

### 💳 Membership Plans
- Assign membership plans
- Store plan details in MySQL
- Manage multiple membership types

### 💰 Payment Management
- Record member payments
- Calculate total revenue
- Maintain payment history

### 📅 Attendance Management
- Mark daily attendance
- Track today's attendance
- Store attendance records in the database

### 📊 Dashboard
- Total registered members
- Active members count
- Total revenue generated
- Today's attendance summary

### ⏳ Automatic Membership Expiry
- Automatically checks membership expiry dates
- Updates expired memberships
- Keeps active membership status up-to-date

### 🗄️ Database Management
- MySQL database integration
- Secure CRUD operations
- Organized relational database structure

---

# 🛠️ Technologies Used

- Python 3.x
- Tkinter
- ttk (Tkinter Widgets)
- MySQL
- MySQL Connector Python
- Datetime Module

---

# 📂 Project Structure

```text
Gym_Member_Manager_py/
│
├── Gym Member Manager/
│   ├── gym_member_managment.py
│   └── gym_member_managment.sql
│
├── README.md
└── .gitignore
```

---

# ⚙️ Requirements

Install the required dependency:

```bash
pip install mysql-connector-python
```

---

# 🗃️ Database Setup

1. Install **MySQL Server**.
2. Create a database named:

```sql
gym_management
```

3. Import the SQL file:

```text
gym_member_managment.sql
```

4. Update the database credentials inside the Python file:

```python
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="gym_management"
    )
```

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/Gym_Member_Manager_py.git
```

Move into the project folder:

```bash
cd Gym_Member_Manager_py
```

Run the application:

```bash
python "Gym Member Manager/gym_member_managment.py"
```

---

# 🖥️ Application Modules

- Dashboard
- Member Registration
- Membership Plan Management
- Payment Management
- Attendance Tracking
- Membership Expiry Management

---

# 📊 Dashboard Overview

The dashboard displays:

- 👥 Total Members
- ✅ Active Members
- 💰 Total Revenue
- 📅 Today's Attendance

---

# 🚀 Future Enhancements

- User Authentication
- Admin & Staff Roles
- BMI Calculator
- Workout Plan Management
- Diet Plan Management
- Barcode / QR Code Check-In
- Membership Renewal Reminders
- Email & SMS Notifications
- PDF Receipt Generation
- Monthly Revenue Reports
- Data Backup & Restore
- Dark Mode Support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is developed for **educational and learning purposes**. You are free to use, modify, and improve it for personal or academic projects.

---

# 👨‍💻 Author

**Rahul Kulkarni**

Python Developer • Desktop Application Developer • Database Enthusiast

If you found this project helpful, consider giving it a ⭐ on GitHub.
