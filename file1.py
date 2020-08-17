import os

def yazdir(): 
    with open("d.txt","w") as f:
        f.writelines(["furkan \n","eray\n","Ömer\n","frkn123 \n","ery893243 \n","f32pw862 \n","ffesj\n","sfjbsfsef\n","7y84395 \n","89765^+' \n"]) 
        
yazdir()   

def okuma():
    if os.path.isfile("d.txt"):
        with open("d.txt","r") as yazdir:
            return yazdir.read()

print(okuma())        



