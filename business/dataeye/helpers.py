from math import radians, cos, sin, asin, sqrt


class RequestDataDistance:
    def __init__(self, req_lat, req_long) -> None:
        self.lat = req_lat
        self.long = req_long

    def get_distance_in_km(self, lat, long):
        # convert decimal degrees to radians
        lat1, long1, lat2, long2 = map(radians, [self.lat, self.long, lat, long])

        # haversine formula
        dlon = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers is 6371
        km = 6371 * c
        return km
