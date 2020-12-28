#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import code as x 

x.create("dummyname",25)

x.create("src",70,3600) 

x.read("dummyname")

x.read("src")

x.create("dummyname",50)

x.modify("dummyname",55)
 
x.delete("dummyname")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
