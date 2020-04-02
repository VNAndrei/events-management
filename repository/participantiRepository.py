"""
Created on Nov 18, 2018

@author: Andrei
"""

from domain.entities import Participanti


class ParticipantiRepository:
    def __init__(self):
        self.__elements = []
        self.__size = 0

    def add_repository(self, element):
        """
        adauga un element nou in lista daca nu exista un element cu acelasi id
        """
        if len(self.__elements) == 0:
            self.__elements.append(element)
            self.__size += 1
        else:
            for i in range(0, len(self.__elements)):
                if element.get_person_id() == self.__elements[i].get_person_id():
                    raise ValueError('element existent')

            self.__elements.append(element)
            self.__size += 1

    def delete_repository(self, id):
        """
        sterge un element din lista
        """
        if (len(self.__elements) != 0):
            for i in range(0, len(self.__elements)):
                if self.__elements[i].get_person_id() == id:
                    self.__elements.remove(self.__elements[i])
                    self.__size -= 1
                    return

    def find_repository(self, id):
        """
        cauta un element nou in lista cu acelasi id ca cel dat. daca acesta exista se returneaza daca nu se returneaza 0
        """
        if len(self.__elements) != 0:
            for i in range(0, len(self.__elements)):
                if self.__elements[i].get_person_id() == id:
                    return self.__elements[i]
            return 0

    def update_repository(self, id, element):
        """
        actualizeaza un element din lista cu acelasi id ca si cel dat
        """

        if len(self.__elements) != 0:
            for i in range(0, len(self.__elements)):
                if self.__elements[i].get_person_id() == element.get_person_id():
                    raise ValueError("exista un element cu idul acesta")
            for i in range(0, len(self.__elements)):
                if self.__elements[i].get_person_id() == id:
                    self.__elements[i].set_person_id(element.get_person_id())
                    self.__elements[i].set_nume(element.get_nume())
                    self.__elements[i].set_adresa(element.get_adresa())

    def get_all_list(self):
        """
        """
        lista_participanti = []
        for i in range(0, len(self.__elements)):
            lista_participanti.append(self.__elements[i].get_all())

        return lista_participanti

    def get_size(self):
        return self.__size
