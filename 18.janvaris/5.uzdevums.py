#Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas. Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu


faila_nosaukums = "lietotajs.txt"

try:
    lietot_vards = input("Ievadi savu vārdu: ")
    with open(faila_nosaukums, 'w') as file:
        file.write(lietot_vards)
    print(f"Vārds '{lietot_vards}' veiksmīgi ierakstīts failā {faila_nosaukums}.")
except FileNotFoundError as a:
    print(f"Fails nav pieejams: {a}")
except Exception as a:
    print(f"Kļūda: {a}")