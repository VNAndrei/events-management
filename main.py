"""
Created on Nov 12, 2018

@author: Andrei
"""
from ui.console import Consola
from repository.participantiRepository import ParticipantiRepository
from repository.eventRepository import EventRepository
from repository.inscriereRepository import InscriereRepository
from domain.validator import EventValidator, ParticipantValidator, ValidatorInscriere
from Service.eventService import EventService
from Service.partiService import ParticipantiService
from Service.inscriereService import InscriereService
from repository.fileToMemory import *
from repository.FileRepository import *

listaEvent = EventRepository()
listaEvent2 = FileToMemoryEvent('data/evenimente.txt')
listaEvent3 = FileEvent('data/evenimente.txt')

listaParticipanti = ParticipantiRepository()
listaParticipanti2 = FileToMemoryParticipanti('data/participanti.txt')
listaParticipanti3 = FileParticipanti('data/participanti.txt')

listaInscriere = InscriereRepository()
listaInscriere2 = FileToMemoryInscriere('data/inscrieri.txt')
listaInscriere3 = FileInscrieri('data/inscrieri.txt')

validatorEvent = EventValidator()
validatorParticipanti = ParticipantValidator()
validatorInscriere = ValidatorInscriere()
serviceEvent = EventService(listaEvent3, validatorEvent)
serviceParti = ParticipantiService(listaParticipanti3, validatorParticipanti)
serviceInscrisi = InscriereService(listaEvent3, listaParticipanti3, listaInscriere3, validatorInscriere)
console = Consola(serviceParti, serviceEvent, serviceInscrisi)
console.run()
