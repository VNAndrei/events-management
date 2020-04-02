from domain.entities import Inscrieri, Participanti
from domain.entities import Evenimente
from Service.sortari import *


class InscriereService:

    def __init__(self, listaE, listaP, listaI, inscriereVlaidator):
        self.eventRepository = listaE
        self.participantiRepository = listaP
        self.inscriereRepository = listaI
        self.inscriereValidator = inscriereVlaidator

    def inscriere(self, id_event, id_participant):
        """
        """
        if self.inscriereValidator.validare_inscriere(id_event, id_participant, self.eventRepository,
                                                      self.participantiRepository):
            inscriere = Inscrieri(id_event, id_participant)
            self.inscriereRepository.add_repository(inscriere)

    def recursiv(self, lista_iduri):
        if len(lista_iduri) == 1:
            return [self.eventRepository.find_repository(lista_iduri[0])]
        return [self.eventRepository.find_repository(lista_iduri[0])] + self.recursiv(lista_iduri[1:])

    def lista_participare_dupa_descriere(self, id):
        """
        """

        lista_evenimente = []
        lista_iduri = self.inscriereRepository.find_repository(id)
        if lista_iduri != []:
            for i in range(0, len(lista_iduri)):
                lista_evenimente = self.recursiv(lista_iduri)
                # .append(self.eventRepository.find_repository(lista_iduri[i]))

            lista_evenimente = sorted(lista_evenimente, key=lambda element: element.get_descriere(), reverse=False)
            lista_string = []
            for i in range(0, len(lista_evenimente)):
                lista_string.append(lista_evenimente[i].get_all())
            return lista_string

    def lista_participare_dupa_timp(self, id):
        """
        """
        lista_iduri = []
        lista_evenimente = []
        lista_iduri = self.inscriereRepository.find_repository(id)
        if lista_iduri != []:
            for i in range(0, len(lista_iduri)):
                lista_evenimente.append(self.eventRepository.find_repository(lista_iduri[i]))

            lista_evenimente = sorted(lista_evenimente, key=lambda element: int(element.get_timp()), reverse=False)
            lista_string = []
            for i in range(0, len(lista_evenimente)):
                lista_string.append(lista_evenimente[i].get_all())
            return lista_string

    def delete_inscris(self, id):
        """
        """
        self.inscriereRepository.delete_participant(id)

    def delete_event(self, id):
        """
        """

        self.inscriereRepository.delete_repository(id)

    def lista_participare_dupa_data(self, id):
        """
        """
        lista_iduri = []
        lista_evenimente = []
        lista_iduri = self.inscriereRepository.find_repository(id)
        if lista_iduri != []:
            for i in range(0, len(lista_iduri)):
                lista_evenimente.append(self.eventRepository.find_repository(lista_iduri[i]))

            lista_evenimente = selection_sort(lista_evenimente, key=lambda element: int(element.get_data()),
                                              invers=False)
            lista_string = []
            for i in range(0, len(lista_evenimente)):
                lista_string.append(lista_evenimente[i].get_all())
            return lista_string

    def persoane_max_evenimente(self):
        """
        """
        if self.inscriereRepository.get_size() != 0:
            participari = {}
            inscrieri = self.get_inscrieri()
            for i in inscrieri:
                lista_participanti = i[1]
                for j in lista_participanti:
                    if j in participari:
                        participari[j] += 1
                    else:
                        participari[j] = 1

            participari = sorted(participari.items(), key=lambda element: element[1], reverse=True)

            return participari[0]
        else:
            raise ValueError('nu exista inscrieri')

    def event_max_participanti(self):
        """
        """
        participari = self.get_inscrieri()
        rezultat = []

        participari = shaker_sort(participari, key=lambda event: len(event[1]), invers=True)
        for i in range(0, int(len(participari) * 0.2) + 1):
            rezultat.append([participari[i][0], len(participari[i][1])])
        return rezultat

    def get_inscrieri(self):
        rezultat = []
        if self.inscriereRepository.get_size() == 0:
            raise ValueError('nu exista nici o inscriere')
        for i in range(0, self.inscriereRepository.get_size()):
            rezultat.append([self.inscriereRepository.find_id_event(i), self.inscriereRepository.find_participanti(i)])
        return rezultat
