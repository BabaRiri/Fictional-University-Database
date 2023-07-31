import sqlite3
import queries
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

dept_q = queries.dept_list()
cursor.execute(dept_q)
departments = cursor.fetchall()

advisors_q = queries.advisor_list()
advisors = cursor.fetchall()

def result_func(res):
    
    root = tk.Tk()
    root.title("Result")
    wind_w = 100
    wind_h = 50
    scr_w = root.winfo_screenwidth()
    scr_h = root.winfo_screenheight()
    x = (scr_w / 2) - (wind_w / 2)
    y = (scr_h / 2) - (wind_h / 2)
    root.geometry(f'{wind_w}x{wind_h}+{int(x)-100}+{int(y)}')
    root.minsize(400, 100)
    root.maxsize(400, 100)

    if res == 1:
        result = "Operation succesful!"
    else:
        result = "INVALID INPUT"

    msg = tk.Label(root, text=result, fg="white", font=("Arial", 15, "bold"))
    if res == 1:
        root.configure(bg="green")
        msg.configure(bg="green")
    else:
        root.configure(bg="#D90429")
        msg.configure(bg="#D90429")
    msg.place(x=200, y=50, anchor="center")

    root.mainloop()

def exit_func(root):
    root.destroy()
    welcome_window()

def exit_btn(root):
    # Create an exit button
    exit_btn = tk.Button(root, text="EXIT", fg="white", bg="#D90429", relief=tk.FLAT, command=lambda: exit_func(root))
    exit_btn.configure(width=10, height=2)
    exit_btn.place(x=500, y=640, anchor="s")

def admin_window(root):
    # Destroy the welcome window
    root.destroy()

    # Create a new window for the admin
    admin_root = tk.Tk()
    wind_w = 1000
    wind_h = 650
    scr_w = admin_root.winfo_screenwidth()
    scr_h = admin_root.winfo_screenheight()
    x = (scr_w / 2) - (wind_w / 2)
    y = (scr_h / 2) - (wind_h / 2)
    admin_root.geometry(f'{wind_w}x{wind_h}+{int(x)}+{int(y)-30}')
    admin_root.configure(bg="#EDF2F4")
    admin_root.title("DB ADMINSTRATOR")

    # Create frames for the content of the window
    students_frame = tk.Frame(admin_root, width=1000, height=600, bg="#F8F9F9")
    students_frame.place(x=500,y=650, anchor="s")
    instructors_frame = tk.Frame(admin_root, width=1000, height=600, bg="#F8F9F9")
    instructors_frame.place(x=500,y=650, anchor="s")
    advisors_frame = tk.Frame(admin_root, width=1000, height=600, bg="#F8F9F9")
    advisors_frame.place(x=500,y=650, anchor="s")

    def create_top_frame():
        # Create a frame at the top of the window for the user buttons 
        top_frame = tk.Frame(admin_root, width=1000, height=50, bg="#2B2D42")
        top_frame.place(x=500, y=0, anchor="n")

        top_label = tk.Label(top_frame, text="ADMIN USER", font=("Arial", 15, "bold"), fg="white", bg="#2B2D42")
        top_label.place(x=900, y=25, anchor="c")

        #Change the colour of buttons when clicked
        def colour_change(x):
            if x == 1:
                button.configure(bg="#EDF2F4", fg="#2B2D42")
                button1.configure(bg="#8D99AE", fg="white")
                button2.configure(bg="#8D99AE", fg="white")
                student_function()

            if x == 2:
                button.configure(bg="#8D99AE", fg="white")
                button1.configure(bg="#EDF2F4", fg="#2B2D42")
                button2.configure(bg="#8D99AE", fg="white")
                instructor_function()

            if x == 3:
                button.configure(bg="#8D99AE", fg="white")
                button1.configure(bg="#8D99AE", fg="white")
                button2.configure(bg="#EDF2F4", fg="#2B2D42")
                advisor_function()


        # Create the buttons for the top frame to select a user type
        button = tk.Button(top_frame, text="Students", bg="#EDF2F4", fg="#2B2D42", width=20, height=3, relief=tk.FLAT, command=lambda: colour_change(1))
        button.place(x=140, y=25, anchor="center")

        button1 = tk.Button(top_frame, text="Instructors", bg="#8D99AE", fg="white", width=20, height=3, relief=tk.FLAT, command=lambda: colour_change(2))
        button1.place(x=300, y=25, anchor="center")

        button2 = tk.Button(top_frame, text="Advisors", bg="#8D99AE", fg="white", width=20, height=3, relief=tk.FLAT, command=lambda: colour_change(3))
        button2.place(x=460, y=25, anchor="center")

    #Student frame
    def student_function():

        data_frame = tk.Frame(admin_root, width=1000, height=600, bg="#EDF2F4")
        data_frame.place(x=500, y=45, anchor="n")

        # Create the treeview widget and add it to the data frame
        treeview = ttk.Treeview(data_frame, height=14)
        # Add columns to the treeview
        treeview["columns"] = ("ID","first_name", "last_name", "dept", "email", "phone")

        # Set the column names
        treeview.column("#0", width=0, minwidth=0, anchor="center")
        treeview.column("ID", width=100, minwidth=100, anchor="w")
        treeview.column("first_name", width=150, minwidth=100, anchor="w")
        treeview.column("last_name", width=200, minwidth=100, anchor="w")
        treeview.column("dept", width=200, minwidth=100, anchor="w")
        treeview.column("email", width=200, minwidth=100, anchor="w")
        treeview.column("phone", width=100, minwidth=100, anchor="w")

        treeview.heading("#0", text="")
        treeview.heading("ID", text="ID")
        treeview.heading("first_name", text="First Name")
        treeview.heading("last_name", text="Last Name")
        treeview.heading("dept", text="Department")
        treeview.heading("email", text="Email Address")
        treeview.heading("phone", text="Phone Number")

        treeview.tag_configure('stripe', background='#E6E6E6')

        query = queries.select_stds()
        cursor.execute(query)
        data = cursor.fetchall()

        # Add the data to the treeview 
        for row in data:
            treeview.insert("", "0", text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        for i, item in enumerate(treeview.get_children()):
            if i % 2 == 0 and not treeview.tag_has('stripe', item):
                treeview.item(item, tags=('stripe',))

        # Pack the treeview to show it in the window
        treeview.place(x=500, y=100, anchor="n")

        def select_row(item_id):
            # Convert the item ID to an integer index
            index = treeview.index(item_id)
            
            # Scroll the Treeview to bring the selected item into view
            treeview.yview(index)

        def search_student(entry_ID):
            # Get the search value from the entry widget
            std_id = entry_ID.get()
            try:
                std_id = int(std_id)
            except ValueError:
                print("Error: Invalid integer representation")

            print("Search Function")
            print("ID:", std_id)

            # Execute a SELECT query to retrieve the matching student data
            query = queries.search_std_q()
            data = (std_id,)
            cursor.execute(query, data)
            result = cursor.fetchone()

            if result is not None:
                # Clear any existing highlights in the Treeview widget
                treeview.selection_remove(treeview.selection())
                print("Looking for student")
                # Find the item in the Treeview widget and highlight it
                for i in treeview.get_children():
                    item = treeview.item(i)
                    
                    if item['values'][0] == std_id:
                        treeview.selection_set(i)
                        treeview.focus(i)
                        select_row(i)
                        break
                    else:
                        print(f'Comparing {item["values"][0]} with {std_id}')
            else:
                result_func(0)

        def add_student(entry_ID, entry_first_name, entry_last_name, entry_dept, entry_email, entry_phone):
            # Get the values from the entry widgets
            std_id = entry_ID.get()
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            dept = entry_dept.get()
            email = entry_email.get()
            phone = entry_phone.get()
            print(departments)
            print(dept)

            if len(dept) == 0 or dept not in [d[0] for d in departments]:
                print('The value is empty or not in the departments')
                result_func(0)
                return
            
            if len(first_name) == 0:
                result_func(0)
                return
            
            if len(last_name) == 0:
                result_func(0)
                return

            # Insert the new student data into the database using an INSERT query
            query = queries.add_std_q()
            data = (std_id, first_name, last_name, dept, email, phone)
            try:
                cursor.execute(query, data)
                conn.commit()
                state = 1

                # Clear the entry widgets if they exist
                if entry_ID.winfo_exists():
                    entry_ID.delete(0, "end")
                if entry_first_name.winfo_exists():
                    entry_first_name.delete(0, "end")
                if entry_last_name.winfo_exists():
                    entry_last_name.delete(0, "end")
                if entry_dept.winfo_exists():
                    entry_dept.delete(0, "end")
                if entry_email.winfo_exists():
                    entry_email.delete(0, "end")
                if entry_phone.winfo_exists():
                    entry_phone.delete(0, "end")

            except sqlite3.IntegrityError as e:
                state = 0
                print(e)

            # Update the Treeview widget
            for widget in data_frame.winfo_children():
                widget.destroy()
            student_function()

            # Display a message indicating the success or failure of the operation
            result_func(state)

        def del_std():
            index = treeview.focus()
            print(index)

            if index is None:
                result_func(0)
                return

            item = treeview.item(index)
            print(item)

            if item is None:
                result_func(0)
                return
            values = item['values']

            if values:
                pk = values[0]
                query = queries.del_std_q()
                data = (pk,)
                try:
                    cursor.execute(query, data)
                    treeview.delete(index)
                    conn.commit()
                    result_func(1)
                except sqlite3.IntegrityError as e:
                    result_func(0)
                    print(e)

            return

        def update_student(entry_ID, entry_first_name, entry_last_name, entry_dept, entry_email, entry_phone):
            # Get the values from the entry widgets
            std_id = entry_ID.get()
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            dept = entry_dept.get()
            email = entry_email.get()
            phone = entry_phone.get()

            if len(dept) == 0 or dept not in [d[0] for d in departments]:
                print('The value is empty or not in the departments')
                result_func(0)
                return
            
            if len(first_name) == 0:
                result_func(0)
                return
            
            if len(last_name) == 0:
                result_func(0)
                return

            # Update the student data in the database using an UPDATE query
            query = queries.update_std_q()
            data = (first_name, last_name, dept, email, phone, std_id)
            try:
                cursor.execute(query, data)
                conn.commit()
                state = 1

                # Clear the entry widgets if they exist
                if entry_ID.winfo_exists():
                    entry_ID.delete(0, "end")
                if entry_first_name.winfo_exists():
                    entry_first_name.delete(0, "end")
                if entry_last_name.winfo_exists():
                    entry_last_name.delete(0, "end")
                if entry_dept.winfo_exists():
                    entry_dept.delete(0, "end")
                if entry_email.winfo_exists():
                    entry_email.delete(0, "end")
                if entry_phone.winfo_exists():
                    entry_phone.delete(0, "end")

            except sqlite3.IntegrityError as e:
                state = 0
                print(e)

            # Update the Treeview widget
            for widget in data_frame.winfo_children():
                widget.destroy()
            student_function()

            # Display a message indicating the success or failure of the operation
            result_func(state)

        search_query = tk.StringVar()
        search_entry = tk.Entry(data_frame, textvariable=search_query, font=("Helvetica", 12), width=300)
        search_entry.insert(0, "Student ID")
        search_entry.config(fg="gray", font=("Arial", 12))

        def clear_placeholder(event):
            # Delete the placeholder text if it is present
            if search_entry.get() == "Student ID":
                search_entry.delete(0, "end")

        search_entry.bind("<Button-1>", clear_placeholder)

        search_entry.configure(width=30)
        search_entry.place(x=560, y=58, anchor="ne")

        search_button = tk.Button(data_frame, text="Search", bg="#2B2D42", fg="white", width=20, height=1, relief=tk.FLAT, command= lambda: search_student(search_entry))
        search_button.place(x=570, y=55, anchor="nw")
        
        search_sign = tk.Label(data_frame, text="SEARCH STUDENTS:", bg="#EDF2F4", fg="#2B2D42", font=("bold", 20))
        search_sign.place(x=500, y=30, anchor="center")

        # Create and place a labels and entry forms
        id_label = tk.Label(data_frame, text="ID:", font=("Helvetica", 12), bg="#EDF2F4")
        id_label.place(x=150, y=430, anchor="e")
        id_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        id_entry.place(x=150, y=430, anchor="w")
        query = queries.current_std_q()
        cursor.execute(query)
        data = cursor.fetchone()
        value = data[0]
        id_entry.insert(0, f'{value+1}')
        id_entry.config(fg="black", font=("Arial", 12))
    

        first_name_label = tk.Label(data_frame, text="First Name:", font=("Helvetica", 12), bg="#EDF2F4")
        first_name_label.place(x=450, y=430, anchor="e")
        first_name_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        first_name_entry.place(x=450, y=430, anchor="w")

        last_name_label = tk.Label(data_frame, text="Last Name:", font=("Helvetica", 12), bg="#EDF2F4")
        last_name_label.place(x=750, y=430, anchor="e")
        last_name_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        last_name_entry.place(x=750, y=430, anchor="w")

        dept_label = tk.Label(data_frame, text="Department:", font=("Helvetica", 12), bg="#EDF2F4")
        dept_label.place(x=150, y=470, anchor="e")
        dept_entry = ttk.Combobox(data_frame, values=departments, font=("Helvetica", 12), width=18)
        dept_entry.place(x=150, y=470, anchor="w")

        email_label = tk.Label(data_frame, text="Email:", font=("Helvetica", 12), bg="#EDF2F4")
        email_label.place(x=450, y=470, anchor="e")
        email_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        email_entry.place(x=450, y=470, anchor="w")

        phone_label = tk.Label(data_frame, text="Phone:", font=("Helvetica", 12), bg="#EDF2F4")
        phone_label.place(x=750, y=470, anchor="e")
        phone_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        phone_entry.place(x=750, y=470, anchor="w")

        def show_selected_row(event):
            # Get the selected item's values
            index = treeview.focus()
            item = treeview.item(index)
            id_val = item['values'][0]
            first_name_val = item['values'][1]
            last_name_val = item['values'][2]
            dept_val = item['values'][3]
            email_val = item['values'][4]
            phone_val = item['values'][5]

            # Clear the Entry widgets
            id_entry.delete(0, "end")
            first_name_entry.delete(0, "end")
            last_name_entry.delete(0, "end")
            dept_entry.delete(0, "end")
            email_entry.delete(0, "end")
            phone_entry.delete(0, "end")

            # Insert the values into the Entry widgets
            id_entry.insert(0, id_val)
            first_name_entry.insert(0, first_name_val)
            last_name_entry.insert(0, last_name_val)
            dept_entry.insert(0, dept_val)
            email_entry.insert(0, email_val)
            phone_entry.insert(0, phone_val)

        treeview.bind("<ButtonRelease-1>", show_selected_row)

        add_btn = tk.Button(data_frame, text="ADD", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: add_student(id_entry, first_name_entry, last_name_entry, dept_entry, email_entry, phone_entry))
        add_btn.configure(width=15, height=2)
        add_btn.place(x=420, y=520, anchor="e")

        update_btn = tk.Button(data_frame, text="UPDATE", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: update_student(id_entry, first_name_entry, last_name_entry, dept_entry, email_entry, phone_entry))
        update_btn.configure(width=15, height=2)
        update_btn.place(x=500, y=520, anchor="center")

        delete_btn = tk.Button(data_frame, text="DELETE", fg="white", bg="#2B2D42", relief=tk.FLAT, command=del_std)
        delete_btn.configure(width=15, height=2)
        delete_btn.place(x=580, y=520, anchor="w")

        exit_btn(admin_root)
        return

    #Instructor frame
    def instructor_function():
        data_frame = tk.Frame(admin_root, width=1000, height=600, bg="#EDF2F4")
        data_frame.place(x=500, y=45, anchor="n")

        # Create the treeview widget and add it to the data frame
        treeview = ttk.Treeview(data_frame, height=14)
        # Add columns to the treeview
        treeview["columns"] = ("ID","first_name", "last_name", "dept", "email", "phone")

        # Set the column names
        treeview.column("#0", width=0, minwidth=0, anchor="center")
        treeview.column("ID", width=100, minwidth=100, anchor="w")
        treeview.column("first_name", width=150, minwidth=100, anchor="w")
        treeview.column("last_name", width=200, minwidth=100, anchor="w")
        treeview.column("dept", width=200, minwidth=100, anchor="w")
        treeview.column("email", width=200, minwidth=100, anchor="w")
        treeview.column("phone", width=100, minwidth=100, anchor="w")

        treeview.heading("#0", text="")
        treeview.heading("ID", text="ID")
        treeview.heading("first_name", text="First Name")
        treeview.heading("last_name", text="Last Name")
        treeview.heading("dept", text="Department")
        treeview.heading("email", text="Email Address")
        treeview.heading("phone", text="Phone Number")

        treeview.tag_configure('stripe', background='#E6E6E6')

        query = queries.select_all_inst()
        cursor.execute(query)
        data = cursor.fetchall()

        # Add the data to the treeview 
        for row in data:
            treeview.insert("", "0", text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        for i, item in enumerate(treeview.get_children()):
            if i % 2 == 0 and not treeview.tag_has('stripe', item):
                treeview.item(item, tags=('stripe',))

        # Pack the treeview to show it in the window
        treeview.place(x=500, y=100, anchor="n")

        def select_row(item_id):
            # Convert the item ID to an integer index
            index = treeview.index(item_id)
            
            # Scroll the Treeview to bring the selected item into view
            treeview.yview(index)


        def search_instructor(entry_ID):
            # Get the search value from the entry widget
            inst_id = entry_ID.get()
            try:
                inst_id = int(inst_id)
            except ValueError:
                print("Error: Invalid integer representation")

            print("Search Function")
            print("ID:", inst_id)

            # Execute a SELECT query to retrieve the matching student data
            query = queries.search_inst_q()
            data = (inst_id,)
            cursor.execute(query, data)
            result = cursor.fetchone()

            if result is not None:
                # Clear any existing highlights in the Treeview widget
                treeview.selection_remove(treeview.selection())
                print("Looking for student")
                # Find the item in the Treeview widget and highlight it
                for i in treeview.get_children():
                    item = treeview.item(i)
                    
                    if item['values'][0] == inst_id:
                        treeview.selection_set(i)
                        treeview.focus(i)
                        select_row(i)
                        break
                    else:
                        print(f'Comparing {item["values"][0]} with {inst_id}')
            else:
                result_func(0)

        def add_instructor(entry_ID, entry_first_name, entry_last_name, entry_dept, entry_email, entry_phone):
            # Get the values from the entry widgets
            inst_id = entry_ID.get()
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            dept = entry_dept.get()
            email = entry_email.get()
            phone = entry_phone.get()
            print(departments)
            print(dept)

            if len(dept) == 0 or dept not in [d[0] for d in departments]:
                print('The value is empty or not in the departments')
                result_func(0)
                return
            
            if len(first_name) == 0:
                result_func(0)
                return
            
            if len(last_name) == 0:
                result_func(0)
                return

            # Insert the new student data into the database using an INSERT query
            query = queries.add_inst_q()
            data = (inst_id, first_name, last_name, dept, email, phone)
            try:
                cursor.execute(query, data)
                conn.commit()
                state = 1

                # Clear the entry widgets if they exist
                if entry_ID.winfo_exists():
                    entry_ID.delete(0, "end")
                if entry_first_name.winfo_exists():
                    entry_first_name.delete(0, "end")
                if entry_last_name.winfo_exists():
                    entry_last_name.delete(0, "end")
                if entry_dept.winfo_exists():
                    entry_dept.delete(0, "end")
                if entry_email.winfo_exists():
                    entry_email.delete(0, "end")
                if entry_phone.winfo_exists():
                    entry_phone.delete(0, "end")

            except sqlite3.IntegrityError as e:
                state = 0
                print(e)

            # Update the Treeview widget
            for widget in data_frame.winfo_children():
                widget.destroy()
            instructor_function()

            # Display a message indicating the success or failure of the operation
            result_func(state)

        def del_inst():
            index = treeview.focus()
            item = treeview.item(index)
            values = item['values']
            print(values)
        
            pk = values[0]
            query = queries.del_inst_q()
            data = (pk,)
            try:
                cursor.execute(query, data)
                treeview.delete(index)
                conn.commit()

                # Delete all references to the instructor in the ADVISORS table
                query = """DELETE FROM ADVISORS WHERE instructor_id=?"""
                cursor.execute(query, data)
                conn.commit()
                result_func(1)
            except sqlite3.IntegrityError as e:
                result_func(0)
                print(e)

            return

        def update_instructor(entry_ID, entry_first_name, entry_last_name, entry_dept, entry_email, entry_phone):
            # Get the values from the entry widgets
            inst_id = entry_ID.get()
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            dept = entry_dept.get()
            email = entry_email.get()
            phone = entry_phone.get()

            if len(dept) == 0 or dept not in [d[0] for d in departments]:
                print('The value is empty or not in the departments')
                result_func(0)
                return
            
            if len(first_name) == 0:
                result_func(0)
                return
            
            if len(last_name) == 0:
                result_func(0)
                return

            # Update the student data in the database using an UPDATE query
            query = queries.update_inst_q()
            data = (first_name, last_name, dept, email, phone, inst_id)
            try:
                cursor.execute(query, data)
                conn.commit()
                state = 1

                # Clear the entry widgets if they exist
                if entry_ID.winfo_exists():
                    entry_ID.delete(0, "end")
                if entry_first_name.winfo_exists():
                    entry_first_name.delete(0, "end")
                if entry_last_name.winfo_exists():
                    entry_last_name.delete(0, "end")
                if entry_dept.winfo_exists():
                    entry_dept.delete(0, "end")
                if entry_email.winfo_exists():
                    entry_email.delete(0, "end")
                if entry_phone.winfo_exists():
                    entry_phone.delete(0, "end")

            except sqlite3.IntegrityError as e:
                state = 0
                print(e)

            # Update the Treeview widget
            for widget in data_frame.winfo_children():
                widget.destroy()
            instructor_function()

            # Display a message indicating the success or failure of the operation
            result_func(state)

        search_query = tk.StringVar()
        search_entry = tk.Entry(data_frame, textvariable=search_query, font=("Helvetica", 12), width=300)
        search_entry.insert(0, "Instructor ID")
        search_entry.config(fg="gray", font=("Arial", 12))

        def clear_placeholder(event):
            # Delete the placeholder text if it is present
            if search_entry.get() == "Instructor ID":
                search_entry.delete(0, "end")

        search_entry.bind("<Button-1>", clear_placeholder)

        search_entry.configure(width=30)
        search_entry.place(x=560, y=58, anchor="ne")

        search_button = tk.Button(data_frame, text="Search", bg="#2B2D42", fg="white", width=20, height=1, relief=tk.FLAT, command= lambda: search_instructor(search_entry))
        search_button.place(x=570, y=55, anchor="nw")
        
        search_sign = tk.Label(data_frame, text="SEARCH INSTRUCTORS:", bg="#EDF2F4", fg="#2B2D42", font=("bold", 20))
        search_sign.place(x=500, y=30, anchor="center")

        # Create and place a labels and entry forms
        id_label = tk.Label(data_frame, text="ID:", font=("Helvetica", 12), bg="#EDF2F4")
        id_label.place(x=150, y=430, anchor="e")
        id_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        id_entry.place(x=150, y=430, anchor="w")
        query = queries.current_inst_q()
        cursor.execute(query)
        data = cursor.fetchone()
        value = data[0]
        id_entry.insert(0, f'{value+1}')
        id_entry.config(fg="black", font=("Arial", 12))
    

        first_name_label = tk.Label(data_frame, text="First Name:", font=("Helvetica", 12), bg="#EDF2F4")
        first_name_label.place(x=450, y=430, anchor="e")
        first_name_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        first_name_entry.place(x=450, y=430, anchor="w")

        last_name_label = tk.Label(data_frame, text="Last Name:", font=("Helvetica", 12), bg="#EDF2F4")
        last_name_label.place(x=750, y=430, anchor="e")
        last_name_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        last_name_entry.place(x=750, y=430, anchor="w")

        dept_label = tk.Label(data_frame, text="Department:", font=("Helvetica", 12), bg="#EDF2F4")
        dept_label.place(x=150, y=470, anchor="e")
        dept_entry = ttk.Combobox(data_frame, values=departments, font=("Helvetica", 12), width=18)
        dept_entry.place(x=150, y=470, anchor="w")

        email_label = tk.Label(data_frame, text="Email:", font=("Helvetica", 12), bg="#EDF2F4")
        email_label.place(x=450, y=470, anchor="e")
        email_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        email_entry.place(x=450, y=470, anchor="w")

        phone_label = tk.Label(data_frame, text="Phone:", font=("Helvetica", 12), bg="#EDF2F4")
        phone_label.place(x=750, y=470, anchor="e")
        phone_entry = tk.Entry(data_frame, font=("Helvetica", 12), width=20)
        phone_entry.place(x=750, y=470, anchor="w")

        def show_selected_row(event):
            # Get the selected item's values
            index = treeview.focus()
            item = treeview.item(index)
            id_val = item['values'][0]
            first_name_val = item['values'][1]
            last_name_val = item['values'][2]
            dept_val = item['values'][3]
            email_val = item['values'][4]
            phone_val = item['values'][5]

            # Clear the Entry widgets
            id_entry.delete(0, "end")
            first_name_entry.delete(0, "end")
            last_name_entry.delete(0, "end")
            dept_entry.delete(0, "end")
            email_entry.delete(0, "end")
            phone_entry.delete(0, "end")

            # Insert the values into the Entry widgets
            id_entry.insert(0, id_val)
            first_name_entry.insert(0, first_name_val)
            last_name_entry.insert(0, last_name_val)
            dept_entry.insert(0, dept_val)
            email_entry.insert(0, email_val)
            phone_entry.insert(0, phone_val)

        treeview.bind("<ButtonRelease-1>", show_selected_row)

        add_btn = tk.Button(data_frame, text="ADD", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: add_instructor(id_entry, first_name_entry, last_name_entry, dept_entry, email_entry, phone_entry))
        add_btn.configure(width=15, height=2)
        add_btn.place(x=420, y=520, anchor="e")

        update_btn = tk.Button(data_frame, text="UPDATE", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: update_instructor(id_entry, first_name_entry, last_name_entry, dept_entry, email_entry, phone_entry))
        update_btn.configure(width=15, height=2)
        update_btn.place(x=500, y=520, anchor="center")

        delete_btn = tk.Button(data_frame, text="DELETE", fg="white", bg="#2B2D42", relief=tk.FLAT, command=del_inst)
        delete_btn.configure(width=15, height=2)
        delete_btn.place(x=580, y=520, anchor="w")

        exit_btn(admin_root)
        return

    #Advisor frame
    def advisor_function():
        data_frame = tk.Frame(admin_root, width=1000, height=600, bg="#EDF2F4")
        data_frame.place(x=500, y=45, anchor="n")

        sign = tk.Label(data_frame, text="ADVISOR PORTAL", bg="#EDF2F4", fg="#2B2D42", font=("bold", 20))
        sign.place(x=500, y=30, anchor="center")

        # Create the treeview widget and add it to the data frame
        treeview = ttk.Treeview(data_frame, height=6)
        # Add columns to the treeview
        treeview["columns"] = ("ID", "first_name", "last_name", "dept", "email", "phone")

        # Set the column names
        treeview.column("#0", width=100, minwidth=100, anchor="center")
        treeview.column("ID", width=0, minwidth=0, anchor="w")
        treeview.column("first_name", width=150, minwidth=100, anchor="w")
        treeview.column("last_name", width=200, minwidth=100, anchor="w")
        treeview.column("dept", width=200, minwidth=100, anchor="w")
        treeview.column("email", width=200, minwidth=100, anchor="w")
        treeview.column("phone", width=100, minwidth=100, anchor="w")

        treeview.heading("#0", text="ID")
        treeview.heading("ID", text="")
        treeview.heading("first_name", text="First Name")
        treeview.heading("last_name", text="Last Name")
        treeview.heading("dept", text="Department")
        treeview.heading("email", text="Email Address")
        treeview.heading("phone", text="Phone Number")

        treeview.tag_configure('stripe', background='#E6E6E6')

        query = queries.select_inst()
        cursor.execute(query)
        data = cursor.fetchall()

        # Add the data to the treeview 
        for row in data:
            treeview.insert("", "0", text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        def add_children(parent):
            # Create a new cursor for the query
            cursor = conn.cursor()
            # Get the ID of the parent row
            parent_id = treeview.item(parent)['text']

            # Query the children for the parent row from the database
            query = """ SELECT DISTINCT s.id, s.first_name, s.last_name, s.dept_name, s.email, s.phone
                        FROM STUDENTS s
                        JOIN ADVISORS a ON s.id = a.student_id
                        JOIN INSTRUCTORS i ON a.instructor_id = ?
                    """
            cursor.execute(query, (parent_id,))
            data = cursor.fetchall()

            # Add the children to the treeview
            for row in data:
                # Use the values from the child row that match the columns in the treeview
                child = treeview.insert(parent, "end", text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5]), open=True)
                # Recursively add the children for the current child
                add_children(child)
            # Close the cursor after executing the query
            cursor.close
        
        # Iterate over the rows in the treeview and add their children
        for parent in treeview.get_children():
            add_children(parent)

        for i, item in enumerate(treeview.get_children()):
            if treeview.get_children(item):  # check if the item has children
                if not treeview.tag_has('stripe', item):
                    treeview.item(item, tags=('stripe',))

        # Pack the treeview to show it in the window
        treeview.place(x=500, y=60, anchor="n")


        #instructor management


        def search_instructor(entry_ID):
            # Get the search value from the entry widget
            inst_id = entry_ID.get()

            try:
                inst_id = int(inst_id)
            except ValueError:
                print("Error: Invalid integer representation")

            print("Search Function")
            print("ID:", inst_id)

            def select_row(item_id):
                # Convert the item ID to an integer index
                index = treeview2.index(item_id)
                
                # Scroll the Treeview to bring the selected item into view
                treeview2.yview(index)

            # Execute a SELECT query to retrieve the matching student data
            #query = queries.select_adv_t2()
            query = f"""
                SELECT DISTINCT(ADVISORS.instructor_id)
                FROM ADVISORS, INSTRUCTORS
                WHERE ADVISORS.instructor_id = '{inst_id}'
            """
            cursor.execute(query)
            result = cursor.fetchone()

            if result is not None:
                # Clear any existing highlights in the Treeview widget
                treeview2.selection_remove(treeview2.selection())
                print("Looking for instructor")
                # Find the item in the Treeview widget and highlight it
                for i in treeview2.get_children():
                    item = treeview2.item(i)
                    
                    if item['values'][0] == inst_id:
                        treeview2.selection_set(i)
                        treeview2.focus(i)
                        select_row(i)
                        break
                    else:
                        print(f'Comparing {item["values"][0]} with {inst_id}')
            else:
                result_func(0)

        def search_student(entry_ID):
            # Get the search value from the entry widget
            id = entry_ID.get()
            try:
                id = int(id)
            except ValueError:
                print("Error: Invalid integer representation")

            print("Search Function")
            print("ID:", id)

            def select_row3(item_id):
                # Convert the item ID to an integer index
                index = treeview3.index(item_id)
                
                # Scroll the Treeview to bring the selected item into view
                treeview3.yview(index)

            # Execute a SELECT query to retrieve the matching student data
            #query = queries.select_adv_t2()
            query = f"""
                    SELECT id
                    FROM STUDENTS
                    WHERE id = '{id}'
                """
            cursor.execute(query)
            result = cursor.fetchone()

            if result is not None:
                # Clear any existing highlights in the Treeview widget
                treeview3.selection_remove(treeview3.selection())
                print("Looking for student")
                # Find the item in the Treeview widget and highlight it
                for i in treeview3.get_children():
                    item = treeview3.item(i)
                        
                    if item['values'][0] == id:
                        treeview3.selection_set(i)
                        treeview3.focus(i)
                        select_row3(i)
                        break
                    else:
                        print(f'Comparing {item["values"][0]} with {id}')
            else:
                result_func(0)

        search_query = tk.StringVar()
        search_entry = tk.Entry(data_frame, textvariable=search_query, font=("Helvetica", 12), width=300)
        search_entry.insert(0, "Instructor ID")
        search_entry.config(fg="gray", font=("Arial", 12))
        
        def clear_placeholder(event):
            # Delete the placeholder text if it is present
            if search_entry.get() == "Instructor ID":
                search_entry.delete(0, "end")

        search_entry.bind("<Button-1>", clear_placeholder)
        search_entry.configure(width=20)
        search_entry.place(x=310, y=258, anchor="ne")

        search_sign = tk.Label(data_frame, text="SELECT INSTRUCTOR", bg="#EDF2F4", fg="#2B2D42", font=("bold", 14))
        search_sign.place(x=295, y=235, anchor="center")

        search_button = tk.Button(data_frame, text="Search", bg="#2B2D42", fg="white", width=20, height=1, relief=tk.FLAT, command= lambda: search_instructor(search_entry))
        search_button.place(x=320, y=255, anchor="nw")

        # Create the treeview widget and add it to the data frame
        treeview2 = ttk.Treeview(data_frame, height=6)
        # Add columns to the treeview
        treeview2["columns"] = ("ID", "first_name", "last_name")

        # Set the column names
        treeview2.column("#0", width=100, minwidth=100, anchor="center")
        treeview2.column("ID", width=0, minwidth=0, anchor="w")
        treeview2.column("first_name", width=120, minwidth=100, anchor="w")
        treeview2.column("last_name", width=120, minwidth=100, anchor="w")

        treeview2.heading("#0", text="ID")
        treeview2.heading("ID", text="")
        treeview2.heading("first_name", text="Last Name")
        treeview2.heading("last_name", text="Last Name")

        query = queries.select_adv_t()
        cursor.execute(query)
        data = cursor.fetchall()

        # Add the data to the treeview 
        for row in data:
            treeview2.insert("", "0", text=row[0], values=(row[0], row[1], row[2]))

        # Pack the treeview to show it in the window
        treeview2.place(x=300, y=290, anchor="n")

        search_query2 = tk.StringVar()
        search_entry2 = tk.Entry(data_frame, textvariable=search_query2, font=("Helvetica", 12), width=300)
        search_entry2.insert(0, "Student ID")
        search_entry2.config(fg="gray", font=("Arial", 12))
        
        def clear_placeholder2(event):
            # Delete the placeholder text if it is present
            if search_entry2.get() == "Student ID":
                search_entry2.delete(0, "end")

        search_entry2.bind("<Button-1>", clear_placeholder2)
        search_entry2.configure(width=20)
        search_entry2.place(x=710, y=258, anchor="ne")

        search_sign = tk.Label(data_frame, text="SELECT STUDENT", bg="#EDF2F4", fg="#2B2D42", font=("bold", 14))
        search_sign.place(x=695, y=235, anchor="center")

        search_button = tk.Button(data_frame, text="Search", bg="#2B2D42", fg="white", width=20, height=1, relief=tk.FLAT, command= lambda: search_student(search_entry2))
        search_button.place(x=720, y=255, anchor="nw")

        # Create the treeview widget and add it to the data frame
        treeview3 = ttk.Treeview(data_frame, height=6)
        # Add columns to the treeview
        treeview3["columns"] = ("ID", "first_name", "last_name")

        # Set the column names
        treeview3.column("#0", width=100, minwidth=100, anchor="center")
        treeview3.column("ID", width=0, minwidth=0, anchor="w")
        treeview3.column("first_name", width=120, minwidth=100, anchor="w")
        treeview3.column("last_name", width=120, minwidth=100, anchor="w")

        treeview3.heading("#0", text="ID")
        treeview3.heading("ID", text="")
        treeview3.heading("first_name", text="Last Name")
        treeview3.heading("last_name", text="Last Name")

        query = queries.select_std_t()
        cursor.execute(query)
        data = cursor.fetchall()

        # Add the data to the treeview 
        for row in data:
            treeview3.insert("", "0", text=row[0], values=(row[0], row[1], row[2]))

        # Pack the treeview to show it in the window
        treeview3.place(x=700, y=290, anchor="n")


        def add_advisor():
            i_id = treeview2.focus()
            id_a = treeview2.item(i_id, 'values')

            s_id = treeview3.focus()
            id_b = treeview3.item(s_id, 'values')

            if id_a and id_b:
                # Get the item identifier for the selected item in treeview2
                item_i_id = treeview2.selection()[0]

                # Get the values for the selected item in treeview2
                values_i = treeview2.item(item_i_id, "values")
                instructor_id = int(values_i[0])

                # Get the item identifier for the selected item in treeview3
                item_s_id = treeview3.selection()[0]

                # Get the values for the selected item in treeview3
                values_s = treeview3.item(item_s_id, "values")
                student_id = int(values_s[0])

                query = """ INSERT INTO ADVISORS (instructor_id, student_id) VALUES(?, ?)"""
                cursor.execute(query, (instructor_id, student_id))

                # Commit the changes to the database
                conn.commit()
                result_func(1)
                
            else:
                print("Ddnt get it")
                result_func(0)

            advisor_function()
            return

        def del_advisor():
            index = treeview2.focus()
            item = treeview2.item(index)
            values = item['values']

            if values:
                pk = values[0]
                data = (pk,)
                try:
                    # Delete all references to the instructor in the ADVISORS table
                    query = """DELETE FROM ADVISORS WHERE instructor_id=?"""
                    cursor.execute(query, data)
                    conn.commit()
                    result_func(1)
                except sqlite3.IntegrityError as e:
                    result_func(0)
                    print(e)
            else:
                print("Ddnt get it")
                result_func(0)

            return
  
        def rm_advisor():
            index = treeview3.focus()
            item = treeview3.item(index)
            values = item['values']

            if values:
                pk = values[0]
                data = (pk,)
                print(data)
                try:
                    # Delete all references to the instructor in the ADVISORS table
                    query = """DELETE FROM ADVISORS WHERE student_id=?"""
                    cursor.execute(query, data)
                    print("query ran")
                    conn.commit()
                    result_func(1)
                except sqlite3.IntegrityError as e:
                    result_func(0)
                    print(e)
            else:
                print("Ddnt get it")
                result_func(0)

            return

        #BOTTONS
        add_adv = tk.Button(data_frame, text="ADD ADVISOR", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: add_advisor())
        add_adv.configure(width=40, height=2)
        add_adv.place(x=155, y=450, anchor="nw")

        del_adv = tk.Button(data_frame, text="DELETE ADVISOR", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: del_advisor())
        del_adv.configure(width=40, height=2)
        del_adv.place(x=155, y=500, anchor="nw")

        ass_adv = tk.Button(data_frame, text="ASSIGN ADVISOR", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: add_advisor())
        ass_adv.configure(width=40, height=2)
        ass_adv.place(x=555, y=450, anchor="nw")

        rm_adv = tk.Button(data_frame, text="REMOVE ADVISOR", fg="white", bg="#2B2D42", relief=tk.FLAT, command=lambda: rm_advisor())
        rm_adv.configure(width=40, height=2)
        rm_adv.place(x=555, y=500, anchor="nw")

        exit_btn(admin_root)
        return

    create_top_frame()
    student_function()
    exit_btn(admin_root)
    admin_root.mainloop()

def welcome_window():
    #Create the welcome window and specify its attributes
    root = tk.Tk()
    wind_w = 300
    wind_h = 300
    scr_w = root.winfo_screenwidth()
    scr_h = root.winfo_screenheight()
    x = (scr_w / 2) - (wind_w / 2)
    y = (scr_h / 2) - (wind_h / 2)
    root.geometry(f'{wind_w}x{wind_h}+{int(x)}+{int(y)-30}')
    root.minsize(300, 300)
    root.maxsize(300, 300)
    root.title("Welcome")
    root.configure(bg="#2B2D42")

    welc_l = tk.Label(root, text="WELCOME", fg="white", bg="#2B2D42", font=("Arial", 22, "bold"))
    welc_l.place(x=150, y=50, anchor="center")

    info_l = tk.Label(root, text=" This a Lab Assignment for:\nCOMP343 \n(Database Management Systems)\nPrepared by:\nSeward Richard Mupereri\n(20140175)\nSubmitted to:\nDr. Ferhun Yorgancıoğlu",  fg="white", bg="#2B2D42")
    info_l.place(x=150, y=130, anchor="center")
    
   # Create three buttons for different user types
    a_btn = tk.Button(root, text="LOG IN", fg="white", bg="#D90429", font=("Arial", 12, "bold"), relief=tk.FLAT, command=lambda: admin_window(root))
    a_btn.configure(width=20, height=2)
    a_btn.place(x=150, y=230, anchor="center")

    root.mainloop()

welcome_window()

conn.close()


