import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt
import stock_reader


class DataMaker():
    def __init__(self):
        self.sp500 = stock_reader.StockReader("^GSPC")
        self.dji = stock_reader.StockReader("^DJI")
        self.nasdaq = stock_reader.StockReader("^IXIC")
        self.nikkei = stock_reader.StockReader("^N225")
        self.topix = stock_reader.StockReader("1305.T")
        self.bse = stock_reader.StockReader("^BSESN")
        self.hsi = stock_reader.StockReader("^HSI")
        self.csi = stock_reader.StockReader("3188.HK")
        self.ftse100 = stock_reader.StockReader("SX5E.SW")
        self.stock_list = [self.sp500, self.dji, self.nasdaq, self.nikkei, self.topix, self.bse, self.hsi, self.csi, self.ftse100]
        self.stock_name_list = ["S&P500 US","Dow Jones 30 US", "NASDAQ US", "NIKKEI225 JP", "TOPIX JP", "BSESN IN", "HSI CN", "CHI CN", "SX5E EU"]

    def stock_month_figure_maker(self):
        xlist = []
        ylist = []
        change_list = []
        # x,y軸のデータ生成
        for member in self.stock_list:
            xlist.append(member.df_month["Date"].values)
            ylist.append(member.df_month["Close"].values)
            change_list.append(member.month_change)

        # 図の枠を生成
        with plt.rc_context({'axes.edgecolor':'white', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'white'}):
            fig, axes = plt.subplots(3, 3, facecolor="#333333", edgecolor="#333333", linewidth=1, figsize=(12,8))
        one_dimension_axes = axes.ravel()
        for i, ax in enumerate(one_dimension_axes):
            # 各描画範囲の色指定
            ax.set_facecolor((1,1,1,0))
            # チャートの描画
            ax.plot(xlist[i], ylist[i], color=self.color_dicision(round(float(change_list[i]), 2)))
            # x軸目盛り回転
            # ax.tick_params(axis='x', labelrotation= 45)
            # subplotの名前
            ax.set_title(self.stock_name_list[i] +" (" + str(round(float(change_list[i]), 2)) + "%)", color="white")
        fig.suptitle("Monthly stock price change", color="white", weight=2)
        fig.autofmt_xdate(rotation=90, ha="center")
        fig.tight_layout(rect=[0,0,1,0.96])
        plt.subplots_adjust(wspace=0.4, hspace=0.7)
        plt.savefig("Monthly stock price change.png", facecolor="#333333", edgecolor="#333333")

    def stock_year_figure_maker(self):
        xlist = []
        ylist = []
        change_list = []
        # x,y軸のデータ生成
        for member in self.stock_list:
            xlist.append(member.df_year["Date"].values)
            ylist.append(member.df_year["Close"].values)
            change_list.append(member.year_change)

        # 図の枠を生成
        with plt.rc_context({'axes.edgecolor':'white', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'white'}):
            fig, axes = plt.subplots(3, 3, facecolor="#333333", edgecolor="#333333", linewidth=1, figsize=(12,8))
        one_dimension_axes = axes.ravel()
        for i, ax in enumerate(one_dimension_axes):
            # 各描画範囲の色指定
            ax.set_facecolor((1,1,1,0))
            # チャートの描画
            ax.plot(xlist[i], ylist[i], color=self.color_dicision(round(float(change_list[i]), 2)))
            # x軸目盛り回転
            # ax.tick_params(axis='x', labelrotation= 45)
            # subplotの名前
            ax.set_title(self.stock_name_list[i] +" (" + str(round(float(change_list[i]), 2)) + "%)", color="white")
        fig.suptitle("Annual stock price change", color="white", weight=2)
        fig.autofmt_xdate(rotation=90, ha="center")
        fig.tight_layout(rect=[0,0,1,0.96])
        plt.subplots_adjust(wspace=0.4, hspace=0.7)
        plt.savefig("Annual stock price change.png", facecolor="#333333", edgecolor="#333333")


    
    def color_dicision(self, change):
        if change == 0:
            color = "#f7fdf7"
        elif 0 < change and 0.25 > change:
            color = "#edfced"
        elif 0.25 < change and 0.5 > change:
            color = "#dcf8dc"
        elif 0.5 < change and 0.75 > change:
            color = "#b8f1b8"
        elif 0.75 < change and 1.0 > change:
            color = "#95ea95"
        elif 1.0 < change and 1.25 > change:
            color = "#72e272"
        elif 1.25 < change and 1.50 > change:
            color = "#4edc4e"
        elif 1.50 < change and 1.75 < change:
            color = "#2bd52b"
        elif 1.75 < change and 2.0 < change:
            color = "#23b123"
        elif 2.0 < change and 2.25 < change:
            color = "#1d8d1d"
        elif 2.25 < change:
            color = "#156a15"
        elif 0 > change and -0.25 < change:
            color = "#fceded"
        elif -0.25 > change and -0.5 < change:
            color = "#f8dcdc"
        elif -0.5> change and -0.75 < change:
            color = "#f1b8b8"
        elif -0.75 > change and -1.0 < change:
            color = "#ea9595"
        elif -1.0 > change and -1.25 < change:
            color = "#e27272"
        elif -1.25 > change and -1.5 < change:
            color = "#dc4e4e"
        elif -1.5 > change and -1.75 < change:
            color = "#d52b2b"
        elif -1.75 > change and -2.0 < change:
            color = "#b12323"
        elif -2.0 > change and -2.25 < change:
            color = "#6a1515"
        elif -2.25 > change:
            color = "#470e0e"
        else:
            color = "#ffd5d5"
        return color



# dm = DataMaker()
# dm.stock_year_figure_maker()
# dm.stock_month_figure_maker()
