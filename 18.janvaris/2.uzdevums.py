#Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila.

import csv

bim_bam ="2.uzdevums.csv"
try:
    with open(bim_bam, "r") as bums:
        lasa = csv.lasa(bums)
        for row in lasa:
            if len (row)>=2:
    
        
             print(row[1])
        else:
                print("Failā nav otrā rindiņa!")
except FileNotFoundError:
    print(f"Faila {bim_bam} nav atrasts.")
except Exception as e:
    print(f"Kļūda: {e}")
