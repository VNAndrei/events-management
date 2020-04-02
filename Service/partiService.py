"""
Created on Nov 18, 2018

@author: Andrei
"""
from domain.entities import Participanti
from repository.participantiRepository import ParticipantiRepository
from domain.validator import ParticipantValidator
import string
import random


class ParticipantiService:
    def __init__(self, participantRepository, participantValidator):
        self.repository = participantRepository
        self.validator = participantValidator

    def addParticipant(self, id, nume, adresa):
        """
        adauga un participant nou daca acesta este valid si nu mai este deja introdus
        """
        participant = Participanti(id, nume, adresa)

        if self.validator.validare_participant(participant):
            self.repository.add_repository(participant)
            return participant

    def deleteParticipant(self, id):
        """
        sterge un participant
        """
        if self.validator.validare_id(id):
            self.repository.delete_repository(id)

    def updateParticipant(self, id, id_nou, nume, adresa):
        """
        actualizeaza un eveniment dupa idul dat
        """
        participant = Participanti(id_nou, nume, adresa)
        if self.validator.validare_participant(participant):
            self.repository.update_repository(id, participant)
            return participant

    def findParticipant(self, chestie):
        """
        """
        rezultat = []
        for verifica in self.repository.get_all_list():
            if str(chestie) in verifica:
                rezultat.append(verifica)
        if rezultat == []:
            raise ValueError('nu exista nici un participant care sa corespunda cautarii')
        return rezultat

    def addRandom(self):
        """
        """
        sir = string
        id = random.randint(1, 25)
        nume = []
        adresa = []

        for i in range(0, 6):
            nume.append(random.choice(sir.ascii_lowercase))
            adresa.append(random.choice(sir.ascii_lowercase))

        self.addParticipant(str(id), "".join(nume), "".join(adresa))

    def printParticipanti(self):

        if self.repository.get_all_list() == []:
            return ["nu exista participanti"]
        else:
            return self.repository.get_all_list()
