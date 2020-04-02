"""
Created on Dec 16, 2018

@author: Andrei
"""
from repository.eventRepository import EventRepository
from repository.participantiRepository import ParticipantiRepository
from repository.inscriereRepository import InscriereRepository
from domain.entities import Evenimente, Participanti, Inscrieri


class FileToMemoryEvent(EventRepository):
    def __init__(self, fisier):
        EventRepository.__init__(self)
        self.__numeFisier = fisier
        self.incarca_din_fisier()

    def incarca_din_fisier(self):

        with open(self.__numeFisier, 'r') as fisier:
            for linie in fisier:
                linie = linie.strip().split(' ')
                EventRepository.add_repository(self, self.creeaza_event(linie))

    def creeaza_event(self, atribute):
        event = Evenimente(atribute[0], atribute[1], atribute[2], atribute[3])
        return event

    def add_repository(self, element):
        EventRepository.add_repository(self, element)
        self.adaugaLaFisier(element)

    def adauga_la_fisier(self, element):

        with open(self.__numeFisier, 'a') as fisier:
            fisier.write('\n')
            linie_noua = element.get_all()
            fisier.write(linie_noua)

    def scrie_fisier(self):
        with open(self.__numeFisier, 'w') as fisier:
            for i in self.__elements:
                fisier.write(i.get_all())
                fisier.write('\n')

    def delete_repository(self, id):
        EventRepository.delete_repository(self, id)
        self.scrie_fisier()

    def update_repository(self, id, element):
        EventRepository.update_repository(self, id, element)
        self.scrie_fisier()


class FileToMemoryParticipanti(ParticipantiRepository):
    def __init__(self, fisier):
        ParticipantiRepository.__init__(self)
        self.__numeFisier = fisier
        self.incarca_din_fisier()

    def incarca_din_fisier(self):

        with open(self.__numeFisier, 'r') as fisier:
            for linie in fisier:
                linie = linie.strip().split(' ')
                ParticipantiRepository.add_repository(self, self.creeaza_participant(linie))

    def creeaza_participant(self, atribute):
        participant = Participanti(atribute[0], atribute[1], atribute[2])
        return participant

    def add_repository(self, element):
        EventRepository.add_repository(self, element)
        self.adaugaLaFisier(element)

    def adauga_la_fisier(self, element):

        with open(self.__numeFisier, 'a') as fisier:
            fisier.write('\n')
            linie_noua = element.get_all()
            fisier.write(linie_noua)

    def scrie_fisier(self):
        with open(self.__numeFisier, 'w') as fisier:
            for i in self.__elements:
                fisier.write(i.get_all())
                fisier.write('\n')

    def delete_repository(self, id):
        EventRepository.delete_repository(self, id)
        self.scrie_fisier()

    def update_repository(self, id, element):
        EventRepository.update_repository(self, id, element)
        self.scrie_fisier()


class FileToMemoryInscriere(InscriereRepository):
    def __init__(self, fisier):
        InscriereRepository.__init__(self)
        self.__numeFisier = fisier
        self.incarca_din_fisier()

    def incarca_din_fisier(self):

        with open(self.__numeFisier, 'r') as fisier:
            for linie in fisier:
                linie = linie.strip().split(' ')

                for i in range(1, len(linie)):
                    inscriere = [linie[0], linie[i]]
                    # print(inscriere)
                    InscriereRepository.add_repository(self, self.creeaza_inscriere(inscriere))

    def creeaza_inscriere(self, atribute):
        inscriere = Inscrieri(atribute[0], atribute[1])
        return inscriere

    def add_repository(self, element):
        InscriereRepository.add_repository(self, element)
        self.adaugaLaFisier(element)

    def adauga_la_fisier(self, element):

        with open(self.__numeFisier, 'a') as fisier:
            fisier.write('\n')
            linie_noua = element.get_all()
            fisier.write(linie_noua)

    def scrie_fisier(self):
        with open(self.__numeFisier, 'w') as fisier:
            for i in self.__elements:
                fisier.write(i.get_all())
                fisier.write('\n')

    def delete_repository(self, id):
        return InscriereRepository.delete_repository(self, id)
        self.scrie_fisier()

    def delete_participant(self, id):
        InscriereRepository.delete_participant(self, id)
        self.scrie_fisier()
