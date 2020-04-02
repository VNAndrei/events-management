"""
Created on Dec 17, 2018

@author: Andrei
"""
from domain.entities import *


class FileEvent:
    def __init__(self, fisier):
        self.__numeFisier = fisier
        self.__size = 0

    def incarca_din_fisier(self):
        returneaza = []
        with open(self.__numeFisier, 'r') as fisier:
            for linie in fisier:
                linie = linie.strip().split(' ')
                returneaza.append(self.creeaza_event(linie))
        return returneaza

    def creeaza_event(self, atribute):
        event = Evenimente(atribute[0], atribute[1], atribute[2], atribute[3])
        return event

    def scrie_fisier(self, lista_date):
        with open(self.__numeFisier, 'w') as fisier:
            for i in lista_date:
                fisier.write(i.get_all())
                fisier.write('\n')

    def add_repository(self, element):
        """
        adauga un element nou in lista daca nu exista un element cu acelasi id
        """
        lista_date = self.incarca_din_fisier()
        if len(lista_date) == 0:
            lista_date.append(element)
            self.__size += 1
            self.scrie_fisier(lista_date)
        else:
            for i in range(0, len(lista_date)):
                if element.get_id() == lista_date[i].get_id():
                    raise ValueError('element existent')

            lista_date.append(element)
            self.__size += 1
            self.scrie_fisier(lista_date)

    def delete_repository(self, id):
        """
        sterge un element din lista
        """
        lista_date = self.incarca_din_fisier()
        if len(lista_date) != 0:
            for i in range(0, len(lista_date)):
                if lista_date[i].get_id() == id:
                    lista_date.remove(lista_date[i])
                    self.__size -= 1
                    self.scrie_fisier(lista_date)
                    return

    def find_repository(self, id):
        """
        cauta un element nou in lista cu acelasi id ca cel dat. daca acesta exista se returneaza daca nu se returneaza 0
        """
        lista_date = self.incarca_din_fisier()
        if len(lista_date) != 0:
            for i in range(0, len(lista_date)):
                if lista_date[i].get_id() == id:
                    return lista_date[i]
            return 0

    def update_repository(self, id, element):
        """
        actualizeaza un element din lista cu acelasi id ca si cel dat
        """
        lista_date = self.incarca_din_fisier()
        if len(lista_date) != 0:
            for i in range(0, len(lista_date)):
                if lista_date[i].get_id() == element.get_id():
                    raise ValueError("exista un element cu idul acesta")
            for i in range(0, len(lista_date)):
                if lista_date[i].get_id() == id:
                    lista_date[i].set_id(element.get_id())
                    lista_date[i].set_data(element.get_data())
                    lista_date[i].set_timp(element.get_timp())
                    lista_date[i].set_descriere(element.get_descriere())
            self.scrie_fisier(lista_date)

    def get_all_list(self):
        """
        returneaza toata lista de evenimente
        """
        lista_date = self.incarca_din_fisier()
        lista_events = []
        for i in range(0, len(lista_date)):
            lista_events.append(lista_date[i].get_all())

        return lista_events

    def get_size(self):
        return self.__size


class FileParticipanti:
    def __init__(self, fisier):
        self.__numeFisier = fisier
        self.__size = 0

    def incarca_din_fisier(self):
        returneaza = []
        with open(self.__numeFisier, 'r') as fisier:
            for linie in fisier:
                linie = linie.strip().split(' ')
                returneaza.append(self.creeaza_participant(linie))
        return returneaza

    def creeaza_participant(self, atribute):
        participant = Participanti(atribute[0], atribute[1], atribute[2])
        return participant

    def scrie_fisier(self, lista_date):
        with open(self.__numeFisier, 'w') as fisier:
            for i in lista_date:
                fisier.write(i.get_all())
                fisier.write('\n')

    def add_repository(self, element):
        """
        adauga un element nou in lista daca nu exista un element cu acelasi id
        """
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) == 0):
            lista_date.append(element)
            self.__size += 1
            self.scrie_fisier(lista_date)
        else:
            for i in range(0, len(lista_date)):
                if element.get_person_id() == lista_date[i].get_person_id():
                    raise ValueError('element existent')

            lista_date.append(element)
            self.__size += 1
            self.scrie_fisier(lista_date)

    def delete_repository(self, id):
        """
        sterge un element din lista
        """
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) != 0):
            for i in range(0, len(lista_date)):
                if lista_date[i].get_person_id() == id:
                    lista_date.remove(lista_date[i])
                    self.__size -= 1
                    self.scrie_fisier(lista_date)
                    return

    def find_repository(self, id):
        """
        cauta un element nou in lista cu acelasi id ca cel dat. daca acesta exista se returneaza daca nu se returneaza 0
        """
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) != 0):
            for i in range(0, len(lista_date)):
                if lista_date[i].get_person_id() == id:
                    return lista_date[i]
            return 0

    def update_repository(self, id, element):
        """
        actualizeaza un element din lista cu acelasi id ca si cel dat
        """
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) != 0):
            for i in range(0, len(lista_date)):
                if lista_date[i].get_person_id() == element.get_person_id():
                    raise ValueError("exista un element cu idul acesta")
            for i in range(0, len(lista_date)):
                if lista_date[i].get_person_id() == id:
                    lista_date[i].set_person_id(element.get_person_id())
                    lista_date[i].set_nume(element.get_nume())
                    lista_date[i].set_adresa(element.get_adresa())
            self.scrie_fisier(lista_date)

    def get_all_list(self):
        lista_date = self.incarca_din_fisier()
        lista_participanti = []
        for i in range(0, len(lista_date)):
            lista_participanti.append(lista_date[i].get_all())

        return lista_participanti

    def get_size(self):
        return self.__size


class FileInscrieri:

    def __init__(self, fisier):
        self.__numeFisier = fisier
        self.__size = 0

    def incarca_din_fisier(self):
        returneaza = []

        with open(self.__numeFisier, 'r') as fisier:
            for linie in fisier:
                linie = linie.strip().split(' ')
                inscriere = Inscrieri(linie[0], linie[1])
                for i in range(2, len(linie)):
                    inscriere.add_participant(linie[i])
                returneaza.append(inscriere)
        return returneaza

    def scrie_fisier(self, lista_date):
        with open(self.__numeFisier, 'w') as fisier:
            for i in lista_date:
                fisier.write(i.get_all())
                fisier.write('\n')

    def add_repository(self, element):
        """
        adauga un element nou in lista daca nu exista un element cu acelasi id
        """
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) == 0):
            lista_date.append(element)
            self.__size += 1
            self.scrie_fisier(lista_date)
        else:
            id_participant = element.get_participanti()[0]
            id_event = element.get_event_id()
            for i in range(0, len(lista_date)):
                if id_event == lista_date[i].get_event_id():
                    lista_participanti = lista_date[i].get_participanti()
                    if id_participant in lista_participanti:
                        raise ValueError('participant inscris deja la acest eveniment')
                    else:
                        lista_date[i].add_participant(id_participant)
                        self.scrie_fisier(lista_date)
                        return
            lista_date.append(element)
            self.__size += 1
            self.scrie_fisier(lista_date)

    def delete_repository(self, id):
        """
        sterge un element din lista
        """
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) != 0):
            for i in range(0, len(lista_date)):
                if lista_date[i].get_event_id() == id:
                    lista_date.remove(lista_date[i])
                    self.__size -= 1
                    self.scrie_fisier(lista_date)
                    return

    def delete_participant(self, id):
        '''
        '''
        lista_date = self.incarca_din_fisier()
        if (len(lista_date) != 0):
            for i in range(0, len(lista_date)):
                lista_participanti = lista_date[i].get_participanti()
                if id in lista_participanti:
                    lista_date[i].delete_participant(id)
                    self.scrie_fisier(lista_date)

    def find_repository(self, id):
        """
        cauta un element nou in lista cu acelasi id ca cel dat. daca acesta exista se returneaza daca nu se returneaza 0
        """
        lista_date = self.incarca_din_fisier()
        lista_evenimente = []
        if len(lista_date) != 0:
            for i in range(0, len(lista_date)):
                lista_participanti = lista_date[i].get_participanti()
                if id in lista_participanti:
                    lista_evenimente.append(lista_date[i].get_event_id())
            if lista_evenimente != []:
                return lista_evenimente
            else:
                raise ValueError("aceasta persoana nu e inscrisa la nici un eveniment")
        else:
            raise ValueError('nu exista nici o inscriere')

    def find_participanti(self, index):
        lista_date = self.incarca_din_fisier()
        return lista_date[index].get_participanti()

    def find_id_event(self, index):
        lista_date = self.incarca_din_fisier()
        return lista_date[index].get_event_id()

    def get_size(self):
        lungime = len(self.incarca_din_fisier())
        return lungime
