class InscriereRepository(object):
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
            id_participant = element.get_participanti()[0]
            id_event = element.get_event_id()
            for i in range(0, len(self.__elements)):
                if id_event == self.__elements[i].get_event_id():
                    lista_participanti = self.__elements[i].get_participanti()
                    if id_participant in lista_participanti:
                        raise ValueError('participant inscris deja la acest eveniment')
                    else:
                        self.__elements[i].add_participant(id_participant)
                        return
            self.__elements.append(element)
            self.__size += 1

    def delete_repository(self, id):
        """
        sterge un element din lista
        """
        if len(self.__elements) != 0:
            for i in range(0, len(self.__elements)):
                if self.__elements[i].get_event_id() == id:
                    self.__elements.remove(self.__elements[i])
                    self.__size -= 1
                    return

    def delete_participant(self, id):
        """
        """
        if len(self.__elements) != 0:
            for i in range(0, len(self.__elements)):
                lista_participanti = self.__elements[i].get_participanti()
                if id in lista_participanti:
                    self.__elements[i].delete_participant(id)

    def find_repository(self, id):
        """
        cauta un element nou in lista cu acelasi id ca cel dat. daca acesta exista se returneaza daca nu se returneaza 0
        """
        lista_evenimente = []
        if len(self.__elements) != 0:
            for i in range(0, len(self.__elements)):
                lista_participanti = self.__elements[i].get_participanti()
                if id in lista_participanti:
                    lista_evenimente.append(self.__elements[i].get_event_id())
            if lista_evenimente != []:
                return lista_evenimente
            else:
                raise ValueError("aceasta persoana nu e inscrisa la nici un eveniment")
        else:
            raise ValueError('nu exista nici o inscriere')

    def find_participanti(self, index):
        return self.__elements[index].get_participanti()

    def find_id_event(self, index):
        return self.__elements[index].get_event_id()

    def get_size(self):
        return self.__size
