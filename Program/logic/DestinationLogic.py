from data.DestinationDatabase import DestinationData

class DestinationLogic():
    def __init__(self):
        self.data = DestinationData()

    def create_destination(self, destination_instance):
        '''Creates a destination in the database'''
        return self.data.new_destination(destination_instance)
        
    def edit_destination(self, destination_instance):
        '''Edits a destination in the database'''
        return self.data.edit_destination(destination_instance)

    #Returns a list of destination types
    def destination_types(self):
        '''Returns a list of destination types'''
        destination = self.data.get_destinations()
        retList = []
        for destination in destination:
            if destination.destination_type not in retList:
                retList.append(destination.destination_type)
        return retList

    #Returns all information about all destinations
    def all_destinations(self):
        '''Returns all information about all destinations'''
        return self.data.get_destinations()

 