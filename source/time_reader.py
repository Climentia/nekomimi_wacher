import time
import datetime

class TimeReader():
    def get_time(self):
        ut = time.time()
        self.dt = datetime.datetime.fromtimestamp(ut)
        return self.dt        

# test_code
timereader = TimeReader()
timereader.get_time()


