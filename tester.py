'''
Created on Nov 18, 2018

@author: Andrei
'''
from domain.validator import *
from domain.entities import *
from repository.participantiRepository import ParticipantiRepository
from repository.eventRepository import EventRepository
from Service.partiService import ParticipantiService
from Service.eventService import EventService
from Service.partiService import ParticipantiService
from domain.validator import *
import unittest

class Test(unittest.TestCase):
    def run_tests(self):
      
        self.test_Validare_participant()
        self.test_Validare_event()
        self.test_creare_event()
        self.test_creare_participant()
        self.test_add_repo()
        self.test_del_repo()
        self.test_addP()
        self.test_update_repo()
        self.test_addEvent()
        self.test_delP()
        self.test_delE()
        self.test_updE()
        self.test_updP()
        
        
    def test_Validare_participant(self):
        '''
        testeaza functia validare_participant
        '''
        validator=ParticipantValidator()
        participant=Participanti('2', 'dsf', 'adresa')
        try:
            ParticipantValidator.validare_participant( participant)
            assert True
        except ValueError:
            assert False
        participant=Participanti('', 'dsf', '')
        try:
            ParticipantValidator.validare_participant(participant)
            assert False
        except ValueError:
            assert True  
             
    def test_Validare_event(self):
        '''
        testeaza functia validare_event
        '''
        valid=EventValidator()
        event=Evenimente('2', 'dsf','sdffs' ,'adresa')
        try:
            valid.validare_event( event)
            assert True
        except ValueError:
                assert False
        event=Evenimente('','', 'dsf', '')
        try:
            valid.validare_event(event)
            assert False
        except ValueError:
            assert True   
            
    def test_creare_event(self):
        '''
        testeaza functia de creare eveniment
        '''
        event=Evenimente('1','23','23:00','caritabil')
        self.asssertEqual(event.get_id(),'1')
        assert event.get_id()=='1'
        assert event.get_data()=='23'
        assert event.get_timp()=='23:00'
        assert event.get_descriere()=='caritabil'
        
    def test_creare_participant(self):
        '''
        testeaza functia de creare participant
        '''
        parti=Participanti('1','ion','23')
        assert parti.get_person_id()=='1'
        assert parti.get_nume()=='ion'
        assert parti.get_adresa()=='23'
    
    def test_add_repo(self):
        '''
        testeaza funtia add_repo
        '''
        listaP=ParticipantiRepository()
        participant=Participanti('1','das','dsad')
        listaP.add_repository(participant)
        assert listaP.get_size()==1
        try:
            listaP.add_repository(participant)
            assert listaP.get_size()==1
            assert False
        except ValueError:
            pass
        
        listaE=EventRepository()
        event=Evenimente('1','34','123','dada')
        listaE.add_repository(event)
        assert listaE.get_size()==1
        try:
            listaE.add_repository(event)
            assert listaE.get_size()==1
            assert False
        except ValueError:
            pass
    
    def test_del_repo(self):
        '''
        testeaza functia del_repo
        '''
        listaE=EventRepository()
        event=Evenimente('1','34','123','dada')
        listaE.add_repository(event)
        assert listaE.get_size()==1
        try:
            listaE.delete_repository('1')
            assert listaE.get_size()==0
            assert True
        except ValueError:
            pass    
        
        listaP=ParticipantiRepository()
        participant=Participanti('1','dada','34')
        listaP.add_repository(participant)
        assert listaP.get_size()==1
        try:
            listaP.delete_repository('1')
            assert listaP.get_size()==0
            assert True
        except ValueError:
            pass   
        
    def test_update_repo(self):
        '''
        testeaza functia update_repo si find_repo
        '''
        listaE=EventRepository()
        event=Evenimente('1','34','123','dada')
        event2=Evenimente('1','35','124','da1da')
        listaE.add_repository(event)
        assert listaE.get_size()==1
        try:
            listaE.update_repository('1',event2)
            assert listaE.get_size()==1
            event=listaE.find_repository('1')
            assert event.get_data()=='35'
            assert event.get_id()=='1'
            assert event.get_timp()=='124'
            assert event.get_descriere()=='da1da'
        except ValueError:
            pass    
        
        listaP=ParticipantiRepository()
        participant=Participanti('1','dada','123')
        participant2=Participanti('2','da1da','13')
        listaP.add_repository(participant)
        assert listaP.get_size()==1
        try:
            listaP.update_repository('1',participant2)
            assert listaP.get_size()==1
            participant=listaP.find_repository('2')
            assert participant.get_nume()=='da1da'
            assert participant.get_person_id()=='2'
            assert participant.get_adresa()=='13'
    
        except ValueError:
            pass    
        
    def test_addP(self):
        '''
        testeaza functia addP
        '''
        listaP=ParticipantiRepository()
        validator=ParticipantValidator
        x=ParticipantiService(listaP,validator)
        participant=x.addParticipant('23', 'da', 'dresa')
        assert participant.get_person_id()=='23'
        try:
            x.addParticipant('23','da','da')  
            assert False
        except ValueError:
            pass
    
    def test_addEvent(self):
        '''
        testeaza functia addP
        '''
        listaE=EventRepository()
        validator=EventValidator
        x=EventService(listaE,validator)
        event=x.addEvent('23', '23', '23','23')
        assert event.get_id()=='23'
        try:
            x.addEvent('23','da','da','32')  
            assert False
        except ValueError:
            pass    
        
    def test_delP(self):
        '''
        testeaza functia delP
        '''
        listaP=ParticipantiRepository()
        validator=ParticipantValidator
        x=ParticipantiService(listaP,validator)
        participant=x.addParticipant('23', 'da', 'dresa')
        assert participant.get_person_id()=='23'
        
        x.deleteParticipant('2')
        assert x.repository.get_size()==1
        x.deleteParticipant('23')
        assert x.repository.get_size()==0
    
    def test_delE(self):
        '''
        testeaza functia delP
        '''
        listaE=EventRepository()
        validator=EventValidator
        x=EventService(listaE,validator)
        event=x.addEvent('23', 'da', 'dresa','34')
        assert event.get_id()=='23'
        
        x.deleteEvent('2')
        assert x.repository.get_size()==1
        x.deleteEvent('23')
        assert x.repository.get_size()==0

    def test_updE(self):
        '''
        testeaza functia  updE
        '''
        listaE=EventRepository()
        validator=EventValidator
        x=EventService(listaE,validator)
        event=x.addEvent('23', 'da', 'dresa','34')
        event2=Evenimente('2','d','sd','3r')
        assert event.get_id()=='23'
        event=x.updateEvent('23','2','d','sd','3r')
        assert event.get_id()=='2'
    
    def test_updP(self):
        '''
        testeaza functia  updateParticipant
        '''
        listaP=ParticipantiRepository()
        validator=ParticipantValidator()
        x=ParticipantiService(listaP,validator)
        participant=x.addParticipant('23', 'da', 'dresa')
        participant2=Participanti('2','d','sd')
        assert participant.get_person_id()=='23'
        participant=x.updateParticipant('23','2','d','sd')
        assert participant.get_person_id()=='2'

test=Test()      
test.run_tests()       
