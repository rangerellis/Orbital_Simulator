from datetime import datetime

class Time_Return:
    '''
    This class handles determining the current date and time and processing it into a useful form for planetary
    simulations
    '''
    def __init__(self):

        self.day = 0
        self.month = 0
        self.year = 0
        self.hour = 0
        self.minute = 0
        self.second = 0

        self.adjusted_year = 0

    def get(self):

        current = datetime.now()
        self.day = current.day
        self.month = current.month
        self.year = current.year
        self.hour = current.hour
        self.minute = current.minute
        self.second = current.second

        speed_factor = 60.0*60.0*24.0*30.0

        adjusted_second = speed_factor * self.second/60.0
        adjusted_minute = (self.minute + adjusted_second)/60.0
        adjusted_hour = (self.hour + adjusted_minute)/24.0
        adjusted_day = (self.day + adjusted_hour)/30.0
        adjusted_month = (self.month + adjusted_day)/12.0
        self.adjusted_year = self.year - 2000.0 + adjusted_month

        print("Adjusted Year: ", self.adjusted_year)

        # print("Date/Time: ", current)

        # return self.year, self.month, self.day, self.hour, self.minute, self.second

