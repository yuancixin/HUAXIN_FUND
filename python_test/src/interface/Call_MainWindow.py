import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface.UI_MainWindow import Ui_MainWindow
import pandas as pd
import csv 
from config.properties import SOURCE_DIR
import fetch_data.get_future_data
import fetch_data.get_stock_data
import fetch_data.get_actual_price
import fetch_data.get_research_data
import trading_strategy.future_strategy_NM


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.input_future_n.setValue(60)
        self.input_future_m.setValue(0.010)
        self.input_future_d.setValue(20)
        
        self.button_update.clicked.connect(self.update_start)
        self.button_clearlog.clicked.connect(self.clearlog)
        self.button_future_strategy.clicked.connect(self.future_strategy_start)
        
        # 重定向输出  （关键）
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
    
    def update_start(self):
        self.button_update.setEnabled(False)
        self.label_update_state.setText('数据正在更新中')
        self.Update_thread = UpdateThread(self.check_update_future, self.check_update_stock, self.check_update_actual, self.check_update_research)
        self.Update_thread.UpdateEndSignal.connect(self.update_end)
        self.Update_thread.start()
        
    def update_end(self):
        self.button_update.setEnabled(True)
        self.label_update_state.setText('数据更新完成')
        QtWidgets.QMessageBox.information(self.button_update, "提示", "数据更新完成")
        
    def clearlog(self):
        self.LogInfoBrowser.setText('')
        
    def future_strategy_start(self):
        self.button_future_strategy.setEnabled(False)
        self.Strategy_Future_Thread = StrategyFutureThread(self.check_fut_ave, self.check_fut_nm, self.input_future_n.value(), self.input_future_m.value(), self.input_future_d.value())
        self.Strategy_Future_Thread.StrategyFutureEndSignal.connect(self.future_strategy_end)
        self.Strategy_Future_Thread.start()
        
    def future_strategy_end(self):
        self.button_future_strategy.setEnabled(True)

    def outputWritten(self, text):  
        cursor = self.LogInfoBrowser.textCursor()  # 光标
        cursor.movePosition(QtGui.QTextCursor.End)  # 光标移至最后
        cursor.insertText(text)  # 插入文本
        self.LogInfoBrowser.setTextCursor(cursor)  # 使之生效
        self.LogInfoBrowser.ensureCursorVisible()  # 确保滚动文本编辑时光标是可视的。  


class StrategyFutureThread(QThread):
    StrategyFutureEndSignal = pyqtSignal()
    
    def __init__(self, check_fut_ave, check_fut_nm, input_future_n, input_future_m, input_future_d, parent=None):
        super(StrategyFutureThread, self).__init__(parent)
        self.check_fut_ave = check_fut_ave
        self.check_fut_nm = check_fut_nm
        self.input_future_n = input_future_n
        self.input_future_m = input_future_m
        self.input_future_d = input_future_d

    def run(self):
        df_source = pd.read_csv('%s/future_data.csv' % SOURCE_DIR, quoting=csv.QUOTE_NONE)
        if self.check_fut_ave.isChecked():
            trading_strategy.future_strategy_NM.get_code_near_ave(df_source, self.input_future_n, self.input_future_m, self.input_future_d)
        if self.check_fut_nm.isChecked():
            trading_strategy.future_strategy_NM.get_code_fit_strategy(df_source)  
        self.StrategyFutureEndSignal.emit()


class UpdateThread(QThread):
    UpdateEndSignal = pyqtSignal()

    def __init__(self, check_update_future, check_update_stock, check_update_actual, check_update_research, parent=None):
        super(UpdateThread, self).__init__(parent)
        self.check_update_future = check_update_future
        self.check_update_stock = check_update_stock
        self.check_update_actual = check_update_actual
        self.check_update_research = check_update_research
    
    def run(self):
        if self.check_update_future.isChecked():
            fetch_data.get_future_data.main()
        if self.check_update_stock.isChecked():   
            fetch_data.get_stock_data.main()
        if self.check_update_actual.isChecked():
            fetch_data.get_actual_price.main()
        if self.check_update_research.isChecked():
            fetch_data.get_research_data.main()
        self.UpdateEndSignal.emit()


class EmittingStream(QObject):  
        textWritten = pyqtSignal(str)  # 定义一个发送str的信号

        def write(self, text):  
            self.textWritten.emit(str(text))  


def main():
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
