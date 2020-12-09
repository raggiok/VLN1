from data.dataAPI import dataAPI
from models.Destinations import Destination

class DestinationLogic():
    def __init__(self):
        self.data = dataAPI()

    def create_destination(self, a_list):
        '''Creates a destination in the database'''
        destination_instance = Destination(self.data.new_destination_id, *a_list)
        
    def edit_destination(self, destination_instance):
        '''Edits a destination in the database'''
        self.data.edit_destination(destination_instance)

     #### Search Function #####  
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
            if destination.opening_time not in retList:
                retList.append(destination.opening_time)
        return retList     

    def search_destinations_by_country(self,country):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.country == country:
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_cities(self,city):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.city == city:
                retList.append(destination)
        return self.no_match_found(retList)

    def search_destinations_by_airport(self,airport):
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.airport == airport:
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
            if destination.opening_time == opening_time:
                retList.append(destination)
        return self.no_match_found(retList)          


    #### Search Function ##### 

    #Returns all information about all destinations
    def all_destinations(self):
        '''Returns all information about all destinations'''
        return self.data.get_destinations()

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list
 