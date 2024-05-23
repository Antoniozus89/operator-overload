class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType




firstBuilding = Building(10, 'simpleBuilding')
secondBuilding = Building(10, 'simpleBuilding')

print(firstBuilding == secondBuilding)
