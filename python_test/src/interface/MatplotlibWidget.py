import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MyFigure(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def show_strategy_difference(self, name, x, y):
        self.axes = self.fig.add_subplot(111)
        self.fig.suptitle('%s基差图' % name)
        self.axes.plot(x, y)
        self.axes.grid(True)
        
    def show_strategy_nm(self, code1, code2, N, x, y11, y12, y21, y22, y31, y32):
        self.axes1 = self.fig.add_subplot(311)
        self.fig.suptitle('%s and %s (N=%s)' % (code1, code2, N))
        self.axes1.plot(x, y11, label='difference')
        self.axes1.plot(x, y12, label='ave_difference')
        self.axes1.legend(loc='upper left')
        self.axes1.grid(True)
        self.axes2 = self.fig.add_subplot(312)
        self.axes2.plot(x, y21, label='oi1')
        self.axes2.plot(x, y22, label='oi2')
        self.axes2.legend(loc='upper left')
        self.axes2.grid(True)
        self.axes3 = self.fig.add_subplot(313)
        self.axes3.plot(x, y31, label='vol1')
        self.axes3.plot(x, y32, label='vol2')
        self.axes3.legend(loc='upper left')
        self.axes3.grid(True)


class MatplotlibWidget(QWidget):

    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()
        
    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyFigure(self, width=50, height=40, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)
        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.mpl.show_strategy_difference('a', [1, 2, 3], [2, 3, 4])
    ui.show()
    sys.exit(app.exec_())
        
