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

    def stock_year_figure_maker(self):

        # 3*3の図の枠を生成
        fig = plt.figure(facecolor="#3c3c3c", edgecolor="#3c3c3c", linewidth=2, figsize=(12,8))
        ax1 = fig.add_subplot(3, 3, 1)
        ax2 = fig.add_subplot(3, 3, 2)
        ax3 = fig.add_subplot(3, 3, 3)
        ax4 = fig.add_subplot(3, 3, 4)
        ax5 = fig.add_subplot(3, 3, 5)
        ax6 = fig.add_subplot(3, 3, 6)
        ax7 = fig.add_subplot(3, 3, 7)
        ax8 = fig.add_subplot(3, 3, 8)
        ax9 = fig.add_subplot(3, 3, 9)
        # 各描画範囲の色指定
        ax1.set_facecolor((1,1,1,0))
        ax2.set_facecolor((1,1,1,0))
        ax3.set_facecolor((1,1,1,0))
        ax4.set_facecolor((1,1,1,0))
        ax5.set_facecolor((1,1,1,0))
        ax6.set_facecolor((1,1,1,0))
        ax7.set_facecolor((1,1,1,0))
        ax8.set_facecolor((1,1,1,0))
        ax9.set_facecolor((1,1,1,0))

        # 描画データ成形
        x1 = self.sp500.df_year["Date"].values
        y1 = self.sp500.df_year["Close"].values
        x2 = self.dji.df_year["Date"].values
        y2 = self.dji.df_year["Close"].values
        x3 = self.nasdaq.df_year["Date"].values
        y3 = self.nasdaq.df_year["Close"].values
        x4 = self.nikkei.df_year["Date"].values
        y4 = self.nikkei.df_year["Close"].values
        x5 = self.topix.df_year["Date"].values
        y5 = self.topix.df_year["Close"].values
        x6 = self.bse.df_year["Date"].values
        y6 = self.bse.df_year["Close"].values
        x7 = self.hsi.df_year["Date"].values
        y7 = self.hsi.df_year["Close"].values
        x8 = self.csi.df_year["Date"].values
        y8 = self.csi.df_year["Close"].values
        x9 = self.ftse100.df_year["Date"].values
        y9 = self.ftse100.df_year["Close"].values

        # チャートの描画
        ax1.plot(x1, y1, color=self.color_dicision(round(float(self.sp500.year_change), 2)), label="sp500")
        ax2.plot(x2, y2, color=self.color_dicision(round(float(self.dji.year_change), 2)), label="Dow30")
        ax3.plot(x3, y3, color=self.color_dicision(round(float(self.nasdaq.year_change), 2)), label="Nasdaq")
        ax4.plot(x4, y4, color=self.color_dicision(round(float(self.nikkei.year_change), 2)), label="Nikkei225")
        ax5.plot(x5, y5, color=self.color_dicision(round(float(self.topix.year_change), 2)), label="TOPIX")
        ax6.plot(x6, y6, color=self.color_dicision(round(float(self.bse.year_change), 2)), label="BSESN")
        ax7.plot(x7, y7, color=self.color_dicision(round(float(self.hsi.year_change), 2)), label="HSI")
        ax8.plot(x8, y8, color=self.color_dicision(round(float(self.csi.year_change), 2)), label="CSI")
        ax9.plot(x9, y9, color=self.color_dicision(round(float(self.ftse100.year_change), 2)), label="FTSE")

        # x軸目盛り回転
        ax1.tick_params(axis='x', labelrotation= 45)
        ax2.tick_params(axis='x', labelrotation= 45)
        ax3.tick_params(axis='x', labelrotation= 45)
        ax4.tick_params(axis='x', labelrotation= 45)
        ax5.tick_params(axis='x', labelrotation= 45)
        ax6.tick_params(axis='x', labelrotation= 45)
        ax7.tick_params(axis='x', labelrotation= 45)
        ax8.tick_params(axis='x', labelrotation= 45)
        ax9.tick_params(axis='x', labelrotation= 45)

        # subplotの名前
        ax1.set_title("S&P500 (" + str(round(float(self.sp500.year_change), 2)) + "%)")
        ax2.set_title("Dow Jones 30 (" + str(round(float(self.dji.year_change), 2)) + "%)")
        ax3.set_title("NASDAQ (" + str(round(float(self.nasdaq.year_change), 2)) + "%)")
        ax4.set_title("NIKKEI225 (" + str(round(float(self.nikkei.year_change), 2)) + "%)")
        ax5.set_title("TOPIX (" + str(round(float(self.topix.year_change), 2)) + "%)")
        ax6.set_title("BSESN (" + str(round(float(self.bse.year_change), 2)) + "%)")
        ax7.set_title("HSI (" + str(round(float(self.hsi.year_change), 2)) + "%)")
        ax8.set_title("CHI (" + str(round(float(self.csi.year_change), 2)) + "%)")
        ax9.set_title("SX5E (" + str(round(float(self.ftse100.year_change), 2)) + "%)")


        # 表の表示
        fig.suptitle("Annual stock price change")
        fig.tight_layout(rect=[0,0,1,0.96])
        plt.subplots_adjust(wspace=0.4, hspace=0.6)
        plt.savefig("Annual stock price change.png", facecolor="#3c3c3c", edgecolor="#3c3c3c")
    
    

    def stock_month_figure_maker(self):

        # 3*3の図の枠を生成
        fig = plt.figure(facecolor="#3c3c3c", edgecolor="#3c3c3c", linewidth=2, figsize=(12,8))
        ax1 = fig.add_subplot(3, 3, 1)
        ax2 = fig.add_subplot(3, 3, 2)
        ax3 = fig.add_subplot(3, 3, 3)
        ax4 = fig.add_subplot(3, 3, 4)
        ax5 = fig.add_subplot(3, 3, 5)
        ax6 = fig.add_subplot(3, 3, 6)
        ax7 = fig.add_subplot(3, 3, 7)
        ax8 = fig.add_subplot(3, 3, 8)
        ax9 = fig.add_subplot(3, 3, 9)
        # 各描画範囲の色指定
        ax1.set_facecolor((1,1,1,0))
        ax2.set_facecolor((1,1,1,0))
        ax3.set_facecolor((1,1,1,0))
        ax4.set_facecolor((1,1,1,0))
        ax5.set_facecolor((1,1,1,0))
        ax6.set_facecolor((1,1,1,0))
        ax7.set_facecolor((1,1,1,0))
        ax8.set_facecolor((1,1,1,0))
        ax9.set_facecolor((1,1,1,0))

        # 描画データ成形
        x1 = self.sp500.df_month["Date"].values
        y1 = self.sp500.df_month["Close"].values
        x2 = self.dji.df_month["Date"].values
        y2 = self.dji.df_month["Close"].values
        x3 = self.nasdaq.df_month["Date"].values
        y3 = self.nasdaq.df_month["Close"].values
        x4 = self.nikkei.df_month["Date"].values
        y4 = self.nikkei.df_month["Close"].values
        x5 = self.topix.df_month["Date"].values
        y5 = self.topix.df_month["Close"].values
        x6 = self.bse.df_month["Date"].values
        y6 = self.bse.df_month["Close"].values
        x7 = self.hsi.df_month["Date"].values
        y7 = self.hsi.df_month["Close"].values
        x8 = self.csi.df_month["Date"].values
        y8 = self.csi.df_month["Close"].values
        x9 = self.ftse100.df_month["Date"].values
        y9 = self.ftse100.df_month["Close"].values

        # チャートの描画
        ax1.plot(x1, y1, color=self.color_dicision(round(float(self.sp500.month_change), 2)), label="sp500")
        ax2.plot(x2, y2, color=self.color_dicision(round(float(self.dji.month_change), 2)), label="Dow30")
        ax3.plot(x3, y3, color=self.color_dicision(round(float(self.nasdaq.month_change), 2)), label="Nasdaq")
        ax4.plot(x4, y4, color=self.color_dicision(round(float(self.nikkei.month_change), 2)), label="Nikkei225")
        ax5.plot(x5, y5, color=self.color_dicision(round(float(self.topix.month_change), 2)), label="TOPIX")
        ax6.plot(x6, y6, color=self.color_dicision(round(float(self.bse.month_change), 2)), label="BSESN")
        ax7.plot(x7, y7, color=self.color_dicision(round(float(self.hsi.month_change), 2)), label="HSI")
        ax8.plot(x8, y8, color=self.color_dicision(round(float(self.csi.month_change), 2)), label="CSI")
        ax9.plot(x9, y9, color=self.color_dicision(round(float(self.ftse100.month_change), 2)), label="FTSE")

        # x軸目盛り回転
        ax1.tick_params(axis='x', labelrotation= 45)
        ax2.tick_params(axis='x', labelrotation= 45)
        ax3.tick_params(axis='x', labelrotation= 45)
        ax4.tick_params(axis='x', labelrotation= 45)
        ax5.tick_params(axis='x', labelrotation= 45)
        ax6.tick_params(axis='x', labelrotation= 45)
        ax7.tick_params(axis='x', labelrotation= 45)
        ax8.tick_params(axis='x', labelrotation= 45)
        ax9.tick_params(axis='x', labelrotation= 45)

        # subplotの名前
        ax1.set_title("S&P500 (" + str(round(float(self.sp500.month_change), 2)) + "%)")
        ax2.set_title("Dow Jones 30 (" + str(round(float(self.dji.month_change), 2)) + "%)")
        ax3.set_title("NASDAQ (" + str(round(float(self.nasdaq.month_change), 2)) + "%)")
        ax4.set_title("NIKKEI225 (" + str(round(float(self.nikkei.month_change), 2)) + "%)")
        ax5.set_title("TOPIX (" + str(round(float(self.topix.month_change), 2)) + "%)")
        ax6.set_title("BSESN (" + str(round(float(self.bse.month_change), 2)) + "%)")
        ax7.set_title("HSI (" + str(round(float(self.hsi.month_change), 2)) + "%)")
        ax8.set_title("CHI (" + str(round(float(self.csi.month_change), 2)) + "%)")
        ax9.set_title("SX5E (" + str(round(float(self.ftse100.month_change), 2)) + "%)")

        # 表の表示
        fig.suptitle("Monthly stock price change")
        fig.tight_layout(rect=[0,0,1,0.96])
        plt.subplots_adjust(wspace=0.4, hspace=0.7)
        plt.savefig("Monthly stock price change.png", facecolor="#3c3c3c", edgecolor="#3c3c3c")

    
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



dm = DataMaker()
dm.stock_year_figure_maker()
dm.stock_month_figure_maker()











    # vix = stock_reader.StockReader("^VIX")
    # oil = stock_reader.StockReader("CL=F")
    # gold = stock_reader.StockReader("GC=F")
    
    




# test
# dji = StockReader("^DJI")
# print(dji.year_change)
