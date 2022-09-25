import sqlite3 as sql
import sys

connection = sql.connect("MoviesList.db")
pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES(Title char(50), Actor char(30), Actress char(30), Director char(40),Year int(4))")
pointer.execute('INSERT INTO MOVIES (Title, Actor, Actress, Director, Year) VALUES (?,?,?,?,?)',("Enola Holmes","Henry Cavill","Millie Bobby","Harry Bradeer",2020))
pointer.execute('INSERT INTO MOVIES (Title, Actor, Actress, Director, Year) VALUES (?,?,?,?,?)',("Avengers","Robert Downey","Scarlet","Russo Brothers",2011))

while True:
    print("\n\t\t""****Movie List Database****""\n\t\t")
    print("1. Insert New Data")
    print("2. Show datasase")
    print("3. Query Selection")
    print("4. Delete")
    print("5. Exit")
    
    choice = int(input("Enter your choice (1-5): "))
    
    if choice not in range(1,6):
        print("Enter a valid choice: ")
        continue
    else:
        if choice == 1:
            title = input("Enter Movie Title:")
            actor = input("Enter Actor Name:")
            actress = input("Enter Actress Name:")
            director = input("Enter Director Name:")
            year = int(input("Enter release year:"))
            pointer.execute("INSERT INTO MOVIES (Title, Actor, Actress, Director, Year) VALUES (?,?,?,?,?)", (title, actor, actress, director,year))
            connection.commit()
            print("****Insert Successful****")
            
        elif choice == 2:
            print("\n\t\t""****Everything in the database****""\n\t\t")
            allMovies = "SELECT * FROM MOVIES"
            pointer.execute(allMovies)
            connection.commit()
            results = pointer.fetchall()
            print("Title || \t Actor || \t Actress || \t Director || \t Year")
            print("-"*100)
            for i in results:
                print(f"{i[0]} || {i[1]} ||  {i[2]} || {i[3]} || {i[4]}")
            
        elif choice == 3:
            print("How do you like Query your Database?")
            print("Available Columns:")
            moviesList = ['title','actor','actress','director','year']
            for movieData in moviesList:
                print(movieData.upper())
            
            col = input("Enter column name from the above list: ").upper()
            print(f"\n You selected {col}")
            selection = input(f"\n What {col} are you looking for?")
    
            print(f"\n\t\t****{col.capitalize()} Query****""\n\t\t")
           
            Query = f"SELECT * FROM MOVIES WHERE {col} = '{selection}'"
            pointer.execute(Query)
            connection.commit()
            results = pointer.fetchall()
            print("Title || \t Actor || \t Actress || \t Director || \t Year")
            print("-"*100)
            for i in results:
                print(f"{i[0]} || {i[1]} ||  {i[2]} || {i[3]} || {i[4]}")
        
        elif choice == 4:
            permission = input("Do you really want to delete all database?(Y/n)").lower()
            if permission.startswith('y'):
                erase = 'DELETE FROM MOVIES'
                cur = connection.cursor()
                cur.execute(erase)
                connection.commit()
                print("\nDeletion Successful\n")
            else:
                print("\nDeletion Cancelled\n")
            
        elif choice == 5:
            print("\nThank you for visiting\n")
            connection.close()
            sys.exit(0)