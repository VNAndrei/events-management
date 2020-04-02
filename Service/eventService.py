"""
Created on Nov 18, 2018

@author: Andrei
"""
from domain.entities import Evenimente, Participanti
from repository.eventRepository import EventRepository
from domain.validator import EventValidator
from string import ascii_lowercase
from random import choice
import string
import random


class EventService:
    def __init__(self, eventRepository, eVal):
        self.repository = eventRepository
        self.validator = eVal

    def addEvent(self, id, data, timp, descriere):
        """
        adauga un eveniment nou daca acesta este valid si nu mai este deja introdus
        """
        event = Evenimente(id, data, timp, descriere)
        if self.validator.validare_event(event):
            self.repository.add_repository(event)
            return event

    def deleteEvent(self, id):
        """
        sterge un participant
        """
        if self.validator.validare_id(id):
            self.repository.delete_repository(id)

    def updateEvent(self, id, id_nou, data, timp, descriere):
        """
        actualizeaza un eveniment dupa idul dat
        """
        event = Evenimente(id_nou, data, timp, descriere)
        if self.validator.validare_event(event):
            self.repository.update_repository(id, event)
            return event

    def findEvent(self, chestie):
        """
        """
        rezultat = []
        for verifica in self.repository.get_all_list():
            if chestie in verifica:
                rezultat.append(verifica)
        if rezultat == []:
            raise ValueError('nu exista nici un participant care sa corespunda cautarii')
        return rezultat

    def addRandom(self):

        sir = string
        id = random.randint(1, 25)
        data = random.randint(1, 31)
        timp = random.randint(1, 24)
        descriere = []

        for i in range(0, 15):
            descriere.append(random.choice(sir.ascii_lowercase))

        self.addEvent(str(id), str(data), str(timp), "".join(descriere))

    def printEvent(self):

        if self.repository.get_all_list() == []:
            return ["nu exista evenimente"]
        else:
            return self.repository.get_all_list()
