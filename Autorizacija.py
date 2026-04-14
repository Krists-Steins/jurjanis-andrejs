username = "Juris85"
password = "ZiemasRits2024"

def izvaditIzveles():
    print("\n⌐⌐  1 » Pievienot jaunu piezīmi  ⌐⌐")
    print("⌐⌐  2 » Izdzēst piezīmi  ⌐⌐")
    print("⌐⌐  3 » Izvadīt piezīmes  ⌐⌐")
    print("⌐⌐  4 » Meklēt piezīmi pēc nosaukuma  ⌐⌐")
    print("⌐⌐  5 » Grupēt piezīmes pēc kategorijām  ⌐⌐")
    print("⌐⌐  0 » Iziet no programmas  ⌐⌐")


def rah():
    print("⌐---¬ Autentifikācija ⌐---¬")
    lietotajs = input("⌐---¬ Lietotājvārds: ")
    parole = input("⌐---¬ Parole: ")

    if lietotajs == username and parole == password:
        piezimes = []
        choice = -1

        print("\nSveiki,", username + "! Izvēlaties darbību!")

        while choice != 0:
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
                        print("Kļūda: visi lauki ir obligāti!\n")
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
                    print("\nPiezīmes:")
                    for i, p in enumerate(piezimes):
                        print(f"{i}: {p['nosaukums']}")

                    apstiprinajums = input(" »» Vai dzēst piezīmi? (Y/N): ").lower()

                    if apstiprinajums == "y":
                        indeks = input(" »» Ievadi piezīmes indeksu: ")

                        if indeks.isdigit():
                            indeks = int(indeks)
                            if 0 <= indeks < len(piezimes):
                                piezimes.pop(indeks)
                                print("Piezīme izdzēsta.")
                            else:
                                print("Nepareizs indekss!")
                        else:
                            print("Jāievada skaitlis!")
                    else:
                        print("Dzēšana atcelta.")
                else:
                    print("Nav piezīmju.")

            elif choice == 3:
                if piezimes:
                    for i, p in enumerate(piezimes):
                        print(f"\n{i}. Nosaukums: {p['nosaukums']}")
                        print(f"   Kategorija: {p['kategorija']}")
                        print(f"   Saturs: {p['saturs']}")
                else:
                    print("Nav nevienas piezīmes.")

            elif choice == 4:
                if not piezimes:
                    print("Nav nevienas piezīmes.")
                    continue

                meklesana = input(" »» Ievadiet nosaukumu: ").lower()

                atrastas = []
                for p in piezimes:
                    if meklesana in p["nosaukums"].lower():
                        atrastas.append(p)

                if atrastas:
                    print("\nAtrastās piezīmes:")
                    for p in atrastas:
                        print(f"\nNosaukums: {p['nosaukums']}")
                        print(f"Saturs: {p['saturs']}")
                        print(f"Kategorija: {p['kategorija']}")
                else:
                    print("Nekas netika atrasts.")

            elif choice == 5:
                if not piezimes:
                    print("Nav nevienas piezīmes.")
                    continue

                grupetas = {}

                for p in piezimes:
                    kat = p["kategorija"]
                    if kat not in grupetas:
                        grupetas[kat] = []
                    grupetas[kat].append(p)

                for kat, saraksts in grupetas.items():
                    print(f"\nKategorija: {kat}")
                    print("-" * 30)
                    for p in saraksts:
                        print(f"Nosaukums: {p['nosaukums']}")
                        print(f"Saturs: {p['saturs']}")
                        print()

            elif choice == 0:
                print("Programma beidzas.")

            else:
                print("Nepareiza izvēle!")

    else:
        print("Piekļuve aizliegta: nav autorizācijas.")


if __name__ == "__main__":
    rah()