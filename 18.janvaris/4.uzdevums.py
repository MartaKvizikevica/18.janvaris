#Izveidot Python programmu, kur  lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.  Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas!

faila_nosaukums=input ("Ievadi faila nosaukumu!:")
faili_ns=input("Ievadi faila paplašinājumu!:")

bum_bum=f"{faila_nosaukums}.{faili_ns}"

try:
    with open(bum_bum, "r") as file:
        saturs= file.read()
    print(saturs)


except FileNotFoundError:
    print(f"Faila {bum_bum} nav atrasts.")
except Exception as e:
    print(f"Kļūda: {e}")
