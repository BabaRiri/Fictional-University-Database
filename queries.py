def create_tables():
        query = """
                CREATE TABLE IF NOT EXISTS DEPARTMENTS (
                        id varchar(4) NOT NULL,
                        name varchar(50) DEFAULT NULL PRIMARY KEY,
                        building varchar(50) DEFAULT NULL
                )

                CREATE TABLE IF NOT EXISTS STUDENTS (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name varchar(50) DEFAULT NULL,
                        last_name varchar(50) DEFAULT NULL,
                        dept_id varchar(4) NOT NULL,
                        email varchar(50) DEFAULT NULL,
                        phone varchar(50) DEFAULT NULL,
                        FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS (id) ON DELETE CASCADE ON UPDATE CASCADE
                )

                CREATE TABLE IF NOT EXISTS INSTRUCTORS (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name varchar(50) DEFAULT NULL,
                        last_name varchar(50) DEFAULT NULL,
                        dept_id varchar(4) NOT NULL,
                        email varchar(50) DEFAULT NULL,
                        phone varchar(50) DEFAULT NULL,
                        FOREIGN KEY (dept_id) REFERENCES DEPARTMENTS (id) ON DELETE CASCADE ON UPDATE CASCADE
                )

                CREATE TABLE IF NOT EXISTS ADVISORS (
                        instructor_id int(8) NOT NULL,
                        student_id int(8) PRIMARY KEY,
                        FOREIGN KEY (instructor_id) REFERENCES INSTRUCTORS (id) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (student_id) REFERENCES STUDENTS (id) ON DELETE CASCADE ON UPDATE CASCADE
                )
                """
        return query

def select_stds():
        query = """
                SELECT *
                FROM STUDENTS
                """
        return query

def add_std_q():
    query = """
                INSERT INTO STUDENTS(id, first_name, last_name, dept_name, email, phone)
                VALUES (?,?,?,?,?,?)
            """
    return query

def del_std_q():
    query = """
                DELETE FROM STUDENTS WHERE ID=?
            """
    return query

def update_std_q():
   query = """
            UPDATE STUDENTS SET first_name=?, last_name=?, dept_name=?, email=?, phone=? WHERE id=?
        """
   return query

def search_std_q():
    query = """
            SELECT * FROM STUDENTS WHERE id=?
            """
    return query

def dept_list():
    query = """
            SELECT name FROM DEPARTMENTS
            """
    return query

def current_std_q():
    query = """
            SELECT MAX(id)FROM STUDENTS
            """
    return query

def select_inst():
        query = """
                SELECT DISTINCT(INSTRUCTORS.id), INSTRUCTORS.first_name, INSTRUCTORS.last_name, INSTRUCTORS.dept_name, INSTRUCTORS.email, INSTRUCTORS.phone
                FROM INSTRUCTORS, ADVISORS
                WHERE INSTRUCTORS.id = ADVISORS.instructor_id
                """
        return query

def add_inst_q():
    query = """
                INSERT INTO INSTRUCTORS(id, first_name, last_name, dept_name, email, phone)
                VALUES (?,?,?,?,?,?)
            """
    return query

def del_inst_q():
    query = """
                DELETE FROM INSTRUCTORS WHERE ID=?
            """
    return query

def update_inst_q():
   query = """
            UPDATE INSTRUCTORS SET first_name=?, last_name=?, dept_name=?, email=?, phone=? WHERE id=?
        """
   return query

def search_inst_q():
    query = """
            SELECT instructor_id FROM ADVISORS WHERE instructor_id=?
            """
    return query

def dept_list():
    query = """
            SELECT name FROM DEPARTMENTS
            """
    return query

def current_inst_q():
    query = """
            SELECT MAX(id)FROM INSTRUCTORS
            """
    return query

def advisor_list():
    query = """
            SELECT DISTINCT instructor_id FROM ADVISORS
            """
    return query

def select_adv_t():
    query = """
                SELECT id, first_name, last_name
                FROM INSTRUCTORS
            """
    return query

def select_all_inst():
    query = """
                SELECT *
                FROM INSTRUCTORS
            """
    return query

def select_adv_t2():
    query = """
                SELECT DISTINCT(ADVISORS.instructor_id)
                FROM ADVISORS, INSTRUCTORS
                WHERE ADVISORS.instructor_id = INSTRUCTORS.id
            """
    return query

def search_adv_q():
    query = """
            SELECT id
            FROM INSTRUCTORS
            """
    return query

def select_std_t():
    query = """
            SELECT id, first_name, last_name
            FROM STUDENTS
            """
    return query

#Creating and Populating Database
def create_tables2():
    query = """
    CREATE TABLE IF NOT EXISTS section (
        sec_id int(4),
        course_id varchar(6),
        semester varchar(8),
        year int(4),
        building varchar(20),
        room_number varchar(6),
        time_slot_id int(3),
        PRIMARY KEY (sec_id, course_id, semester, year),
        FOREIGN KEY (course_id) REFERENCES course(course_id),
        FOREIGN KEY (building) REFERENCES classroom(building),
        FOREIGN KEY (room_number) REFERENCES classroom(room_number),
        FOREIGN KEY (time_slot_id) REFERENCES time_slot(time_slot_id)
    );

    CREATE TABLE IF NOT EXISTS course (
        course_id varchar(6) NOT NULL,
        title varchar(60),
        dept_name varchar(30),
        credits numeric(4,2),
        PRIMARY KEY (course_id),
        FOREIGN KEY (dept_name) REFERENCES department(dept_name)
    );

    CREATE TABLE IF NOT EXISTS prereq (
        course_id varchar(6) NOT NULL,
        prereq_id varchar(6),
        PRIMARY KEY (course_id, prereq_id),
        FOREIGN KEY (course_id) REFERENCES course(course_id),
        FOREIGN KEY (prereq_id) REFERENCES course(course_id)
    );

    CREATE TABLE IF NOT EXISTS classroom (
        room_number varchar(6) NOT NULL,
        building varchar(20) NOT NULL,
        capacity int(4) NOT NULL,
        PRIMARY KEY (room_number, building)
    );

    CREATE TABLE IF NOT EXISTS time_slot (
        time_slot_id int(3) NOT NULL,
        day varchar(10) NOT NULL,
        start_time varchar(10) NOT NULL,
        end_time varchar(10) NOT NULL,
        PRIMARY KEY (time_slot_id, day, start_time)
    );

    CREATE TABLE IF NOT EXISTS takes (
        ID int(8) NOT NULL,
        course_id varchar(6) NOT NULL,
        sec_id int(4) NOT NULL,
        semester varchar(8) NOT NULL,
        year int(4) NOT NULL,
        grade varchar(1),
        PRIMARY KEY (ID, course_id, sec_id, semester, year),
        FOREIGN KEY (ID) REFERENCES student(ID),
        FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES section(course_id, sec_id, semester, year)
    );

    CREATE TABLE IF NOT EXISTS student (
        ID int(8) NOT NULL,
        name varchar(100) NOT NULL,
        dept_name varchar(30) NOT NULL,
        tot_cred numeric(4, 2),
        PRIMARY KEY (ID),
        FOREIGN KEY (dept_name) REFERENCES department (dept_name)
    );

    CREATE TABLE IF NOT EXISTS department (
        dept_name varchar(30) NOT NULL,
        building varchar(20),
        budget numeric(18, 2),
        PRIMARY KEY (dept_name)
    );

    CREATE TABLE IF NOT EXISTS instructor (
        ID int(8) NOT NULL,
        name varchar(100) NOT NULL,
        dept_name varchar(30) NOT NULL,
        salary numeric(8, 2) NOT NULL,
        PRIMARY KEY (ID),
        FOREIGN KEY (dept_name) REFERENCES department(dept_name)
    );

    CREATE TABLE IF NOT EXISTS teaches (
        ID int(8) NOT NULL,
        sec_id int(4),
        course_id varchar(6),
        semester varchar(8),
        year int(4),
        PRIMARY KEY (ID, sec_id, course_id, semester, year),
        FOREIGN KEY (ID) REFERENCES instructor(ID),
        FOREIGN KEY (sec_id, course_id, semester, year) REFERENCES section(sec_id, course_id, semester, year)
    );

    CREATE TABLE IF NOT EXISTS advisor (
        s_id int(8) NOT NULL,
        i_id int(8) NOT NULL,
        PRIMARY KEY (s_id),
        FOREIGN KEY (s_id) REFERENCES student(ID),
        FOREIGN KEY (i_id) REFERENCES instructor(ID)
    )
    """
    return query