#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Gabriel Santos IS-211 10/31/2020
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




