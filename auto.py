# method __init__(
#     self,
#     mileage_limit,
#     number_of_months_limit,
#     last_service_mileage,
#     current_mileage,
#     last_service_date)

#     self.mileage_limit = mileage_limit
#     self.number_of_months_limit = number_of_months_limit
#     self.last_service_mileage = last_service_mileage
#     self.current_mileage = current_mileage
#     self.last_service_date = last_service_date

# method is_service_due(self)
#     if the current mileage >= the mileage at last service + the mileage limit
#         return True
#     elif today >= the date of the last service + the number of months limit
#         return True
#     else
#         return False

# method update_mileage(self, new_mileage)
#     self.current_mileage = new_mileage

# method add_trip(self, trip_mileage)
#     new_mileage = self.current_mileage + trip_mileage
#     self.current_mileage = new_mileage


import datetime


class Automobile:
    def __init__(self,
        mileage_limit,
        number_of_months_limit,
        last_service_mileage,
        current_mileage,
        last_service_date
        ):

        self.mileage_limit = mileage_limit
        self.number_of_months_limit = number_of_months_limit
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date

def is_service_due(self):
    if self.current_mileage >= (self.last_service_mileage + self.mileage_limit):
        return True
    elif datetime.now() >= self.last_service_date + self.number_of_months_limit:
        return True
    else:
        return False

def update_mileage(self, new_mileage):
    self.current_mileage = new_mileage

def add_trip(self, trip_mileage):
    new_mileage = self.current_mileage + trip_mileage
    self.current_mileage = new_mileage
