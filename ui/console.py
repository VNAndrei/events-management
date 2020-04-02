from builtins import str


class Consola:
    def __init__(self, serviceParticipanti, serviceEvent, serviceInscriere):
        self.serviceParticipanti = serviceParticipanti
        self.serviceEvent = serviceEvent
        self.serviceInscriere = serviceInscriere

    def ui_print_menu(self):
        print("""
        1. Adauga
            a) persoana
            b) eveniment
        2. Sterge
            a) persoana
            b) eveniment
        3. Modifica
            a) persoana
            b) eveniment
        4. Inscrie persoane la eveniment
        5. Rapoarte
            a) Lista de evenimente la care participa o persoana ordonat alfabetic dupa descriere
            b) Lista de evenimente la care participa o persoana ordonat alfabetic dupa data
            c) Persoane participante la cele mai multe evenimente
            d) Primele 20% evenimente cu cei mai multi participanti
            *e) Lista de evenimente la care participa o persoana ordonat alfabetic dupa timp
        6. Tipareste
            a) persoane
            b) evenimente
        7. Populeaza aleator
            a) persoane
            b) evenimente
        8.Cauta
            a) persoana
            b) eveniment
        9. Tipareste inscrieri
        10. Exit
        
        """)

    def ui_print_lista(self, lista):

        if len(lista) <= 1:
            print(lista[0])
        else:
            print(lista[0])
            self.ui_print_lista(lista[1:])

    def run(self):

        while True:
            self.ui_print_menu()
            comanda = input("Introduceti comanda:")
            if comanda == '10':
                return
            elif comanda == '7b':
                try:
                    self.serviceEvent.addRandom()
                except ValueError as erori:
                    print(erori)
            elif comanda == '7a':
                try:
                    self.serviceParticipanti.addRandom()
                except ValueError as erori:
                    print(erori)
            elif comanda == '1a':
                try:
                    self.serviceParticipanti.addParticipant(input("introduceti id:"), input("introduceti nume:"),
                                                            input("introduceti adresa:"))
                except ValueError as erori:
                    print(erori)
            elif comanda == '1b':
                try:
                    self.serviceEvent.addEvent(input("introduceti id:"), input("introduceti data:"),
                                               input("introduceti timp:"), input("introduceti descriere:"))
                except ValueError as erori:
                    print(erori)
            elif comanda == '2a':
                try:
                    participant_sters = input("introduceti id:")
                    self.serviceParticipanti.deleteParticipant(participant_sters)
                    self.serviceInscriere.delete_inscris(participant_sters)
                except ValueError as erori:
                    if erori != 'nu exista nici o inscriere':
                        print(erori)
            elif comanda == '2b':
                try:
                    event_sters = input("introduceti id:")
                    self.serviceEvent.deleteEvent(event_sters)
                    self.serviceInscriere.delete_event(event_sters)
                except ValueError as erori:
                    if erori != 'nu exista nici o inscriere':
                        print(erori)
            elif comanda == '6a':
                self.ui_print_lista(self.serviceParticipanti.printParticipanti())
            elif comanda == '6b':
                self.ui_print_lista(self.serviceEvent.printEvent())
            elif comanda == '3a':
                try:
                    self.serviceParticipanti.updateParticipant(
                        input('introduceti id-ul participantului pe care doriti sa-l modificati: '),
                        input('introduceti id: '), input("introduceti nume:"), input("introduceti adresa:"))
                except ValueError as erori:
                    print(erori)
            elif comanda == '3b':
                try:
                    self.serviceEvent.updateEvent(
                        input('introduceti id-ul evenimentului pe care doriti sa-l modificati: '),
                        input("introduceti id:"), input("introduceti data:"), input("introduceti timp:"),
                        input("introduceti descriere:"))
                except ValueError as erori:
                    print(erori)
            elif comanda == '4':
                try:
                    self.serviceInscriere.inscriere(input('Introduceti id-ul evenimentului:'),
                                                    input('Introduceti id-ul participantului: '))
                except ValueError as erori:
                    print(erori)
            elif comanda == '5a':
                try:
                    self.ui_print_lista(
                        self.serviceInscriere.lista_participare_dupa_descriere(input('introduceti id: ')))
                except ValueError as erori:
                    print(erori)
            elif comanda == '5b':
                self.ui_print_lista(self.serviceInscriere.lista_participare_dupa_data(input('introduceti id: ')))
            elif comanda == '5c':
                try:
                    de_printat = self.serviceInscriere.persoane_max_evenimente()

                    self.ui_print_lista(self.serviceParticipanti.findParticipant(de_printat[0]))
                except ValueError as erori:
                    print(erori)
            elif comanda == '5d':
                try:
                    de_printat = self.serviceInscriere.event_max_participanti()
                    for i in range(0, len(de_printat)):
                        print(self.serviceEvent.findEvent(de_printat[i][0])[0] + "nr participanti:" + str(
                            de_printat[i][1]))
                except ValueError as erori:
                    print(erori)

            elif comanda == '5e':
                try:
                    self.ui_print_lista(self.serviceInscriere.lista_participare_dupa_timp(input('introduceti id: ')))
                except ValueError as erori:
                    print(erori)

            elif comanda == '8a':
                try:
                    self.ui_print_lista(self.serviceParticipanti.findParticipant(input("introduceti cautarea: ")))
                except ValueError as erori:
                    print(erori)
            elif comanda == '8b':

                try:
                    self.ui_print_lista(self.serviceEvent.findEvent(input("introduceti cautarea: ")))
                except ValueError as erori:
                    print(erori)
            elif comanda == '9':
                try:
                    self.ui_print_lista(self.serviceInscriere.get_inscrieri())
                except ValueError as erori:
                    print(erori)
            else:
                print("\nComanda invalida\n")
