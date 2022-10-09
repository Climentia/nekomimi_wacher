import pandas_datareader as pdr
import time_reader


class StockReader():
    def __init__(self,stock_name):
        print(stock_name)
        self.yahoo_reader(stock_name)
        
    def yahoo_reader(self, stock_name):
        tr = time_reader.TimeReader()
        dt = tr.get_time()
        start_year = str(dt.year) + "-01-01"
        end = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day)
        if (dt.day < 3) and (dt.weekday() > 4):
            if dt.month == 1:
                start_month = str(dt.year-1) + "-" + "01-01"
            else:
                start_month = str(dt.year) + "-" + str(dt.month-1) + "-01"
        else:
            start_month = str(dt.year) + "-" + str(dt.month) + "-01"
        # start_week = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day-dt.weekday())

        self.df_year = pdr.DataReader(stock_name,"yahoo", start = start_year, end = end)
        self.df_year['Date'] = self.df_year.index
        year_head = self.df_year.iat[0,3]
        year_tail = self.df_year.iat[-1,3]
        self.year_change = (year_tail - year_head)/year_head*100
        self.df_month = self.df_year[start_month:end]
        month_head = self.df_month.iat[0,3]
        month_tail = self.df_month.iat[-1,3]
        self.month_change = (month_tail - month_head)/month_head*100
        # print(self.df_month)
        # self.df_week = self.df_year[start_week:end]
        # week_head = self.df_week.iat[0,3]
        # week_tail = self.df_week.iat[-1,3]
        # self.week_change = (week_tail - week_head)/week_head*100




# test
# dji = StockReader("^DJI")
# print(dji.year_change)

