from data.dataAPI import dataAPI
from models.Destinations import Destination

class DestinationLogic():
    def __init__(self):
        self.data = dataAPI()

    def create_destination(self, country, city, airport, phone_number, opening_time, closing_time, main_contact):
        '''Creates a destination in the database'''
        destination_instance = Destination(self,country, city, airport, phone_number, opening_time, closing_time, main_contact)
        return self.data.create_destination(destination_instance)

    def edit_destination(self, destination_instance):
        '''Edits a destination in the database'''
        return self.data.update_destination(destination_instance)

     #### Search Function #####  
     # the avalible functions return a 
     # list of all avalible options for 
     # the choosen parameter 
    def available_countries(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.country not in retList:
                retList.append(destination.country)
        return retList

    def available_cities(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.city not in retList:
                retList.append(destination.city)
        return retList     

    def available_airports(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.airport not in retList:
                retList.append(destination.airport)
        return retList

    def available_phone_numbers(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.phone_number not in retList:
                retList.append(destination.phone_number)
        return retList 

    def available_opening_times(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.opening_time not in retList:
                retList.append(destination.opening_time)
        return retList             

    def available_closing_times(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.closing_time not in retList:
                retList.append(destination.closing_time)
        return retList 

    def available_main_contacts(self):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.main_contact not in retList:
                retList.append(destination.main_contact)
        return retList     

    def search_destinations_by_id(self,unique_id):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.unique_id == unique_id:
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_country(self,country):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.country.lower() == country.lower():
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_cities(self,city):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.city.lower() == city.lower():
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_airport(self,airport):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.airport.lower() == airport.lower():
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_phone_number(self,phone_number):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.phone_number == phone_number:
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_opening_time(self,opening_time):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.opening_time == opening_time:
                retList.append(destination)
        return self.no_match_found(retList)        

    def search_destinations_by_closing_time(self,closing_time):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.closing_time == closing_time:
                retList.append(destination)
        return self.no_match_found(retList)  


    def search_destinations_by_main_contact(self,main_contact):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.main_contact.lower() == main_contact.lower():
                retList.append(destination)
        return self.no_match_found(retList)          


    #### Search Function ##### 

    #Returns all information about all destinations
    def all_destinations(self):
        '''Returns all information about all destinations'''
        return self.data.get_destinations()

    def delete_destination(self, ID_number):
        search = self.search_destinations_by_id(ID_number)
        if search[0] != "\n*** No match found ***\n":
            self.data.delete_destination(search[0])
            return ["\n*** Destination successfully deleted ***\n"]
        else:
            return search

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list
 