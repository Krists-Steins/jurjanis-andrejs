username = "Juris85"
password = "ZiemasRits2024"

def izvaditIzveles():
    print("⌐⌐  1 » Pievienot jaunu piezīmi  ⌐⌐")
    print("⌐⌐  2 » Izdzēst piezīmi  ⌐⌐")
    print("⌐⌐  3 » Izvadīt piezīmes  ⌐⌐")
    print("⌐⌐  0 » Iziet no programmas  ⌐⌐")

def rah():
    print("⌐---¬ Autentifikācija ⌐---¬")
    lietotajs = input("⌐---¬ Lietotājvārds: ")
    parole = input("⌐---¬ Parole: ")

    if lietotajs == username and parole == password:
        piezimes = []
        choice = -1

        while choice != 0:
            print("\nSveiki, " + username + "! Izvēlaties darbību!")
            izvaditIzveles()

            try:
                choice = int(input(" »» Ievadiet izvēli: "))
            except ValueError:
                print("Nepareiza ievade!")
                continue

            if choice == 1:
                while True:
                    nosaukums = input(" »» Ievadiet piezīmes nosaukumu: ").strip()
                    saturs = input(" »» Ievadiet piezīmes saturu: ").strip()
                    kategorija = input(" »» Ievadiet kategoriju: ").strip()

                    if not nosaukums or not saturs or not kategorija:
                        print("Kļūda: visi lauki ir obligāti! Mēģiniet vēlreiz.\n")
                    else:
                        piezime = {
                            "nosaukums": nosaukums,
                            "saturs": saturs,
                            "kategorija": kategorija
                        }
                        piezimes.append(piezime)
                        print("Piezīme pievienota!")
                        break

            elif choice == 2:
                if piezimes:
                    print("Piezīmes:")
                    for i, p in enumerate(piezimes):
                        print(f"{i}: {p}")

                    apstiprinajums = input(" » » Vai dzēst piezīmi? (Y/N): ")
                    if apstiprinajums.lower() == "y":
                        indeks = int(input(" »» Ievadi piezīmes indeksu: "))
                        if 0 <= indeks < len(piezimes):
                            piezimes.pop(indeks)
                            print("Piezīme izdzēsta.")
                        else:
                            print("Nepareizs indekss!")
                    else:
                        print("Dzēšana atcelta.")
                else:
                    print("Nav piezīmju.")

            elif choice == 3:
                if piezimes:
                    for i, p in enumerate(piezimes):
                        print(f"\n{i}. Nosaukums: {p['nosaukums']}")
                        print(f"   Saturs: {p['saturs']}")
                        print(f"   Kategorija: {p['kategorija']}")
                else:
                    print("Nav nevienas piezīmes.")
            elif choice == 0:
                print("Programma beidzas.")

            else:
                print("Nepareiza izvēle!")

    else:
        print("Piekļuve aizliegta: nav dota autorizācija.")

if __name__ == "__main__":
    rah()