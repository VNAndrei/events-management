class Participanti:
    def __init__(self, personID, nume, adresa):
        self.__personID = personID
        self.__nume = nume
        self.__adresa = adresa

    def get_person_id(self):
        return self.__personID

    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def get_all(self):
        return str(self.__personID) + " " + self.__nume + " " + self.__adresa

    def set_person_id(self, value):
        self.__personID = value

    def set_nume(self, value):
        self.__nume = value

    def set_adresa(self, value):
        self.__adresa = value

    personID = property(get_person_id, set_person_id, None, None)
    nume = property(get_nume, set_nume, None, None)
    adresa = property(get_adresa, set_adresa, None, None)


class Evenimente:
    def __init__(self, ID, data, timp, descriere):
        self.__ID = ID
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def get_id(self):
        return self.__ID

    def get_data(self):
        return self.__data

    def get_timp(self):
        return self.__timp

    def get_descriere(self):
        return self.__descriere

    def get_all(self):
        return (str(self.__ID) + " " + str(self.__data) + " " + str(self.__timp) + " " + self.__descriere)

    def set_id(self, value):
        self.__ID = value

    def set_data(self, value):
        self.__data = value

    def set_timp(self, value):
        self.__timp = value

    def set_descriere(self, value):
        self.__descriere = value

    ID = property(get_id, set_id, None, None)
    data = property(get_data, set_data, None, None)
    timp = property(get_timp, set_timp, None, None)
    descriere = property(get_descriere, set_descriere, None, None)


class Inscrieri:
    def __init__(self, event_id, participant):
        self.event_id = event_id
        self.participanti = []
        self.participanti.append(participant)

    def get_event_id(self):
        return self.event_id

    def get_participanti(self):
        return self.participanti

    def set_event_id(self, id):
        self.event_id = id

    def add_participant(self, participant):
        self.participanti.append(participant)

    def delete_participant(self, participant):
        self.participanti.remove(participant)
