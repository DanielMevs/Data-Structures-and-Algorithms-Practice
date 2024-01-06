class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id -> (startStation, time)
        self.totalMap = {} # (startStation, endStation) -> [totalTime, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkInTime = self.checkInMap[id]
        route = (startStation, stationName)
        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]
        self.totalMap[route][0] += t - checkInTime
        self.totalMap[route][1] += 1

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count
        
