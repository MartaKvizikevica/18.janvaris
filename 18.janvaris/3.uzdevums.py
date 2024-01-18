#Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu

vie_di ="tresais.txt"

try:
    with open(vie_di, "r") as file:
        rinda = file.readlines()
        if len(rinda)>=3:
            print(rinda[2])


        else:
            print("Failā nav trešā rindiņa!")
except FileNotFoundError:
    print(f"Fails {vie_di} nav atrasts.")

except Exception as a:
    print(f"Kļūda: {a}")