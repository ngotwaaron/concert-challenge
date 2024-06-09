class Band:
    def __init__(self, name, hometown):
        self._name = None
        self._hometown = None
        self.name = name
        self.hometown = hometown
        self._concert_list = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        if self._hometown is not None:
            raise AttributeError("Hometown is immutable")
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Hometown must be a non-empty string")
        self._hometown = value

    
    def concerts(self):
        return self._concert_list
        

    def venues(self):
        return [concert.venue for concert in self._concert_list]
        
        

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self._concert_list.append(concert)
        return concert
    
        

    def all_introductions(self):
     return [f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}" for concert in self._concert_list]


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Date must be a non-empty string")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise TypeError("Band must be of type Band")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise TypeError("Venue must be of type Venue")
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city
        

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
        pass


class Venue:
    def __init__(self, name: str, city: str):
        self._name = None
        self._city = None
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("City must be a non-empty string")
        self._city = value

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))