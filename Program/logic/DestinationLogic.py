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

    #Search functions
    def search_destination_by_country(self,string):
        match = []
        for country in self.all_destinations():
            if Destination.country == string:
                match.append(country)
        return self.no_match_found(match)

    def search_destination_by_airport(self,string):
        match = []
        for airport in self.all_destinations():
            if Destination.airport == string:
                match.append(airport)
        return self.no_match_found(match)

    def search_destination_by_opening_time(self,string):
        match = []
        for opening_time in self.all_destinations():
            if Destination.opening_time == string:
                match.append(opening_time)
        return self.no_match_found(match)

    def search_destination_by_closing_time(self,string):
        match = []
        for closing_time in self.all_destinations():
            if Destination.closing_time == string:
                match.append(closing_time)
        return self.no_match_found(match)

    def search_destination_by_main_contact(self,string):
        match = []
        for main_contact in self.all_destinations():
            if Destination.main_contact == string:
                match.append(main_contact)
        return self.no_match_found(match)

    def search_destination_by_state(self,string):
        match = []
        for state in self.all_destinations():
            if Destination.state == string:
                match.append(state)
        return self.no_match_found(match) 
      

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
 