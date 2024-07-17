import tkinter as tk
from tkinter import ttk

def submit_data():
    print("Data Submitted")

def create_window():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Data Entry Form")
    root.geometry("500x400")

    # Tạo khung thông tin người dùng
    user_info_frame = ttk.LabelFrame(root, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Các trường nhập trong khung thông tin người dùng
    tk.Label(user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(user_info_frame).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(user_info_frame, text="Last Name").grid(row=0, column=2, padx=5, pady=5)
    tk.Entry(user_info_frame).grid(row=0, column=3, padx=5, pady=5)

    tk.Label(user_info_frame, text="Title").grid(row=0, column=4, padx=5, pady=5)
    ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Ms.", "Dr."]).grid(row=0, column=5, padx=5, pady=5)

    tk.Label(user_info_frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
    tk.Spinbox(user_info_frame, from_=0, to=100).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(user_info_frame, text="Nationality").grid(row=1, column=2, padx=5, pady=5)
    tk.Entry(user_info_frame).grid(row=1, column=3, padx=5, pady=5)

    # Tạo khung trạng thái đăng ký
    registration_frame = ttk.LabelFrame(root, text="Registration Status")
    registration_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    tk.Checkbutton(registration_frame, text="Currently Registered").grid(row=0, column=0, padx=5, pady=5, sticky="w")

    tk.Label(registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5)
    tk.Spinbox(registration_frame, from_=0, to=50).grid(row=0, column=2, padx=5, pady=5)

    tk.Label(registration_frame, text="# Semesters").grid(row=1, column=1, padx=5, pady=5)
    tk.Spinbox(registration_frame, from_=0, to=10).grid(row=1, column=2, padx=5, pady=5)

    # Tạo khung điều khoản và điều kiện
    terms_frame = ttk.LabelFrame(root, text="Terms & Conditions")
    terms_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    tk.Checkbutton(terms_frame, text="I accept the terms and conditions.").grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Tạo nút gửi dữ liệu
    submit_button = tk.Button(root, text="Enter data", command=submit_data)
    submit_button.grid(row=3, column=0, padx=20, pady=10)

    root.mainloop()

create_window()