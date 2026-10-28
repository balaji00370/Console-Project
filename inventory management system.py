import mysql.connector


# ---------------- CONNECT TO DATABASE ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Balaji_@007",
        database="inventorymanage"
    )


# ---------------- ADD RECORD ----------------
def addrec():
    db = connect_db()
    c = db.cursor()

    name = input("Enter item name: ")
    p = float(input("Enter MRP of item: "))
    id1 = int(input("Enter item ID: "))
    lrd = input("Enter item last restocking date (yyyy-mm-dd): ")
    q = int(input("Enter quantity of item as per last restocking date: "))

    query = """
        INSERT INTO item
        (ID, Name, Product_price, Quantity, Last_restocking_date)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (id1, name, p, q, lrd)

    c.execute(query, values)
    db.commit()

    print("Record added successfully.")

    c.close()
    db.close()


# ---------------- UPDATE RECORD ----------------
def updaterec():
    db = connect_db()
    c = db.cursor()

    print("\nID**********NAME**********PRICE**********QUANTITY**********LASTDATE_OF_RESTOCKING**********")

    c.execute("SELECT * FROM item")
    rows = c.fetchall()

    for i in rows:
        for m in i:
            print(m, end="**********")
        print()

    print()

    toedit = int(input("Enter item ID of record to edit: "))

    print("a - Edit name")
    print("b - Edit price")
    print("c - Edit item ID")
    print("d - Edit last restocking date")
    print("e - Edit stock quantity")

    z = input("Enter a-e: ")

    if z == 'a':
        n = input("Enter new name: ")

        query = "UPDATE item SET Name = %s WHERE ID = %s"
        c.execute(query, (n, toedit))

    elif z == 'b':
        n = float(input("Enter new price: "))

        query = "UPDATE item SET Product_price = %s WHERE ID = %s"
        c.execute(query, (n, toedit))

    elif z == 'c':
        n = int(input("Enter new ID: "))

        query = "UPDATE item SET ID = %s WHERE ID = %s"
        c.execute(query, (n, toedit))

    elif z == 'd':
        n = input("Enter new last restocking date (yyyy-mm-dd): ")

        query = "UPDATE item SET Last_restocking_date = %s WHERE ID = %s"
        c.execute(query, (n, toedit))

    elif z == 'e':
        n = int(input("Enter new quantity: "))

        query = "UPDATE item SET Quantity = %s WHERE ID = %s"
        c.execute(query, (n, toedit))

    else:
        print("Invalid choice.")
        c.close()
        db.close()
        return

    db.commit()

    if c.rowcount > 0:
        print("Record updated successfully.")
    else:
        print("No record found with that ID.")

    c.close()
    db.close()


# ---------------- DELETE RECORD ----------------
def delrec():
    db = connect_db()
    c = db.cursor()

    print("\nID**********NAME**********PRICE**********QUANTITY**********LASTDATE_OF_RESTOCKING**********")

    c.execute("SELECT * FROM item")
    rows = c.fetchall()

    for i in rows:
        for m in i:
            print(m, end="**********")
        print()

    print()

    todel = int(input("Enter item ID of record to delete: "))

    query = "DELETE FROM item WHERE ID = %s"
    c.execute(query, (todel,))

    db.commit()

    if c.rowcount > 0:
        print("Record deleted successfully.")
    else:
        print("No record found with that ID.")

    c.close()
    db.close()


# ---------------- SHOW ALL RECORDS ----------------
def showallrecs():
    db = connect_db()
    c = db.cursor()

    print("\nID**********NAME**********PRICE**********QUANTITY**********LASTDATE_OF_RESTOCKING**********")

    c.execute("SELECT * FROM item")
    rows = c.fetchall()

    if len(rows) == 0:
        print("No records found.")

    for i in rows:
        for m in i:
            print(m, end="**********")
        print()

    print()

    c.close()
    db.close()


# ---------------- MAIN MENU ----------------
choice = 1

while choice != 0:

    print("\n************************************")
    print("1 - Add an item")
    print("2 - Remove an item")
    print("3 - Edit specifics of an item")
    print("4 - Show all items")
    print("5 - Help: See all commands again")
    print("0 - Quit")
    print("************************************")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        addrec()

    elif choice == 2:
        delrec()

    elif choice == 3:
        updaterec()

    elif choice == 4:
        showallrecs()

    elif choice == 5:
        print("\n1 - Add an item")
        print("2 - Remove an item")
        print("3 - Edit specifics of an item")
        print("4 - Show all items")
        print("5 - Help")
        print("0 - Quit")

    elif choice == 0:
        print("Program ended.")

    else:
        print("Invalid choice. Please try again.")