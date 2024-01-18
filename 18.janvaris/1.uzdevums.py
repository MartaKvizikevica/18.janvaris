#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā).
teksts = input("Ieraksti tekstu:")
with open ("pirmais.txt", "w") as fails:
    fails.write(teksts)

    print("Teksts ir uzrakstīts!")