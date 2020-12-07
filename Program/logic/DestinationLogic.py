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

    #Returns a list of destination types
    def destination_types(self):
        '''Returns a list of destination types'''
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.destination_type not in retList:
                retList.append(destination.destination_type)
        return self.no_match_found(retList)

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
 