def lasit_failu(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Fails saturs:")
            print(saturs)
    except FileNotFoundError:
        print("Fails nav atrasts.")

if __name__ == "__main__":
    faila_nosaukums = input("Ievadi tekst failu ar .txt: ")
    lasit_failu(faila_nosaukums)
import csv

def lasit_csv_failu(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            lasitajs = csv.reader(fails)
            print("Ceturtās kolonnas dati:")
            for rinda in lasitajs:
                if len(rinda) >= 4:
                    print(rinda[3])  # Izdrukā ceturtās kolonnas datus
                else:
                    print("Rindā nav ceturtās kolonnas")
    except FileNotFoundError:
        print("Faila nav atrasts.")

if __name__ == "__main__":
    faila_nosaukums = input("Lūdzu, ievadiet CSV faila nosaukumu: ")
    lasit_csv_failu(faila_nosaukums)
def lasit_rindas(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 4:
                print("Trešās rindas saturs:")
                print(rindas[2])
                print("\nCeturtās rindas saturs:")
                print(rindas[3])
            else:
                print("Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print("Fails nav atrasts.")

if __name__ == "__main__":
    faila_nosaukums = input("Lūdzu, ievadiet teksta faila nosaukumu: ")
    lasit_rindas(faila_nosaukums)
def lasit_failu(nosaukums):
    try:
        with open(nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print("Fails nav atrasts.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    faila_nosaukums = input("Lūdzu, ievadiet faila nosaukumu: ")
    faila_formats = input("Lūdzu, ievadiet faila formātu (paplašinājumu): ")
    faila_nosaukums_ar_formats = faila_nosaukums + "." + faila_formats
    lasit_failu(faila_nosaukums_ar_formats)
def ierakstit_vardu_faila(vards):
    try:
        with open("lietotajs.txt", 'w') as fails:
            fails.write(vards)
        print("Vārds veiksmīgi ierakstīts failā.")
    except Exception as e:
        print("Kļūda:", e)

if __name__ == "__main__":
    vards = input("Lūdzu, ievadiet savu vārdu: ")
    ierakstit_vardu_faila(vards)
