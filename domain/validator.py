from domain.entities import Participanti
from domain.entities import Evenimente
from repository.eventRepository import EventRepository
from repository.participantiRepository import ParticipantiRepository


class ParticipantValidator:
    @staticmethod
    def validare_participant(participant):
        """
        valideaza un participant nou si semnaleaza o eroare in cazul in care acesta nu e valid
        in: participant - participanti
        """
        erori = ''
        if participant.get_person_id() == '':
            erori += ' Id neintrodus;'
        if participant.get_nume() == '':
            erori += ' Nume neintrodus;'
        if participant.get_adresa() == '':
            erori += ' Adresa neintrodusa;'
        if erori != '':
            raise ValueError(erori)
        else:
            return True

    @staticmethod
    def validare_id(id):
        """
        valideaza daca un id e corect
        """
        erori = ''
        if id == '':
            erori += ' Id neintrodus;'
        if erori != '':
            raise ValueError(erori)
        else:
            return True


class EventValidator:
    @staticmethod
    def validare_event(event):
        """
        valideaza un eveniment nou si semnaleaza o eroare in cazul in care acesta nu e valid
        in: event - evenimente
        """
        erori = ''
        if event.get_id() == '':
            erori += ' Id neintrodus;'
        if event.get_data() == '':
            erori += ' Data neintrodusa;'
        if event.get_timp() == '':
            erori += ' Ora neintrodusa;'
        if event.get_descriere() == '':
            erori += ' Descriere neintrodusa;'
        if erori != '':
            raise ValueError(erori)
        else:
            return True

    @staticmethod
    def validare_id(id):
        """
        valideaza daca un id e corect
        """
        erori = ''
        if id == '':
            erori += ' Id neintrodus;'
        if erori != '':
            raise ValueError(erori)
        else:
            return True


class ValidatorInscriere:
    @staticmethod
    def validare_inscriere(id_event, id_participant, eventRepository, participantiRepository):
        erori = ''
        if eventRepository.find_repository(id_event) == 0:
            erori += 'Nu exista nici unu eveniment cu acest id.'
        if participantiRepository.find_repository(id_participant) == 0:
            erori += 'Nu exista nici un participant cu acest id.'
        if erori != '':
            raise ValueError(erori)
        else:
            return True
