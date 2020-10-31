#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Gabriel Santos IS-211 10/17/2020
import sqlite3 as lite
import sys

con = lite.connect('pets.db')

with con:

    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS person;")
    cursor.execute("DROP TABLE IF EXISTS pet;")
    cursor.execute("DROP TABLE IF EXISTS person_pet;")
    
    cursor.execute("CREATE TABLE person (id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,age INTEGER);")
    cursor.execute("CREATE TABLE pet (id INTEGER PRIMARY KEY,name TEXT,breed TEXT,age INTEGER,dead INTEGER);")
    cursor.execute("CREATE TABLE person_pet (person_id INTEGER,pet_id INTEGER);")
    
    cursor.execute("INSERT INTO person VALUES(1,'James','Smith',41)")
    cursor.execute("INSERT INTO person VALUES(2,'Diana','Greene',23)")
    cursor.execute("INSERT INTO person VALUES(3,'Sara','White',27)")
    cursor.execute("INSERT INTO person VALUES(4,'William','Gibson',23)")
    
    cursor.execute("INSERT INTO pet VALUES(1,'Rusty','Dalmation',4,1)")
    cursor.execute("INSERT INTO pet VALUES(2,'Bella','Alaskan Malmute',3,0)")
    cursor.execute("INSERT INTO pet VALUES(3,'Max','Cocker Spaniel',1,0)")
    cursor.execute("INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0)")
    cursor.execute("INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0)")
    cursor.execute("INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1)")
    
    cursor.execute("INSERT INTO person_pet VALUES(1,1)")
    cursor.execute("INSERT INTO person_pet VALUES(1,2)")
    cursor.execute("INSERT INTO person_pet VALUES(2,3)")
    cursor.execute("INSERT INTO person_pet VALUES(2,4)")
    cursor.execute("INSERT INTO person_pet VALUES(3,5)")
    cursor.execute("INSERT INTO person_pet VALUES(4,6)")


# In[19]:


cursor.execute("SELECT * FROM person")
cursor.fetchall()


# In[20]:


cursor.execute("SELECT * FROM pet")
cursor.fetchall()


# In[21]:


cursor.execute("SELECT * FROM person_pet")
cursor.fetchall()


# In[24]:


def print_names():
    conn = lite.connect('pets.db')
    answer = input("ID Number? Press '-1' to exit \n")
    while answer != '-1':
        with con:
            try:
                cursor = conn.cursor()
                per_data = cursor.execute("SELECT first_name,last_name,age FROM person WHERE person.id=?",[answer])
                per_rows = per_data.fetchone()
                
                pet_data = cursor.execute("SELECT pet.name,pet.breed,pet.age,pet.dead FROM pet INNER JOIN person_pet ON person_pet.pet_id=pet.id INNER JOIN person ON person.id=person_pet.person_id WHERE person.id=?",[answer])
                pet_rows = pet_data.fetchall()
                
                if(per_rows==None):
                    print("That user doesn't exist, try again")
                    answer = input("ID Number? Press '-1' to exit \n")
                
                else:
                    
                    print("{} {} who is {} years old".format(per_rows[0],per_rows[1],per_rows[2]))
                    
                    for pet_pos in pet_rows:
                                if pet_pos[3] == 1:
                                    w = 'owned'
                                    w2 = 'was'
                                else:
                                    w = 'owns'
                                    w2= 'is'
                                
                                print("{} {}, a {} that {} {} years old".format(w,pet_pos[0],pet_pos[1],w2,pet_pos[2]))
                    answer = input("What ID are you looking for? Enter '-1' to exit \n")
                    
            except lite.Error as err:
                print("Error: {}".format(err))
                sys.exit()
    conn.close()

if __name__ == '__main__':
    print_names()


# In[ ]:




