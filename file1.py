def yazdir(): 
    with open("d.txt","w") as f:
        liste = ["\nfurkan ","eray","Ömer","frkn123 ","ery893243 ",
        "f32pw862 ","ffesj","sfjbsfsef","7y84395","89765^+' "]
        for i in liste:
            f.writelines(i+"\n")
        
        for i in range(len(liste)):
            f.write(liste[i]+ "\n")  
        
yazdir()   


def okuma():
    if os.path.isfile("d.txt"):
        with open("d.txt","r") as yazdir:
            return yazdir.read()

print("Word List :", okuma())             

print("İkiside oluyor en başta yaptığımda oluyor.")
