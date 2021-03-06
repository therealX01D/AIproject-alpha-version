# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ai.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 647)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEntry.setGeometry(QtCore.QRect(0, 40, 271, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TextEntry.setFont(font)
        self.TextEntry.setObjectName("TextEntry")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(279, 39, 601, 511))
        self.widget.setMouseTracking(True)
        self.widget.setObjectName("widget")
        self.Directed_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Directed_Button.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.Directed_Button.setCheckable(True)
        self.Directed_Button.setChecked(False)
        self.Directed_Button.setObjectName("Directed_Button")
        self.Physics_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Physics_Button.setGeometry(QtCore.QRect(280, 10, 101, 23))
        self.Physics_Button.setCheckable(True)
        self.Physics_Button.setChecked(True)
        self.Physics_Button.setDefault(True)
        self.Physics_Button.setObjectName("Physics_Button")
        self.UniformCostButton = QtWidgets.QPushButton(self.centralwidget)
        self.UniformCostButton.setGeometry(QtCore.QRect(20, 560, 131, 61))
        self.UniformCostButton.setObjectName("UniformCostButton")
        self.DFS_Button = QtWidgets.QPushButton(self.centralwidget)
        self.DFS_Button.setGeometry(QtCore.QRect(170, 560, 75, 61))
        self.DFS_Button.setObjectName("DFS_Button")
        self.BFSButton = QtWidgets.QPushButton(self.centralwidget)
        self.BFSButton.setGeometry(QtCore.QRect(260, 560, 75, 61))
        self.BFSButton.setObjectName("BFSButton")
        self.Start_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_line_edit.setGeometry(QtCore.QRect(740, 10, 41, 20))
        self.Start_line_edit.setObjectName("Start_line_edit")
        self.goal_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.goal_lineEdit.setGeometry(QtCore.QRect(832, 10, 41, 20))
        self.goal_lineEdit.setObjectName("goal_lineEdit")
        self.Start_label = QtWidgets.QLabel(self.centralwidget)
        self.Start_label.setGeometry(QtCore.QRect(708, 10, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Start_label.setFont(font)
        self.Start_label.setObjectName("Start_label")
        self.Goal_label = QtWidgets.QLabel(self.centralwidget)
        self.Goal_label.setGeometry(QtCore.QRect(800, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        self.Goal_label.setFont(font)
        self.Goal_label.setObjectName("Goal_label")
        self.iterative_deepening_Button = QtWidgets.QPushButton(self.centralwidget)
        self.iterative_deepening_Button.setGeometry(QtCore.QRect(360, 560, 121, 61))
        self.iterative_deepening_Button.setObjectName("iterative_deepening_Button")
        self.Lim_DFS_button = QtWidgets.QPushButton(self.centralwidget)
        self.Lim_DFS_button.setGeometry(QtCore.QRect(664, 558, 121, 61))
        self.Lim_DFS_button.setObjectName("Lim_DFS_button")
        self.Limited_dfs_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Limited_dfs_lineEdit.setGeometry(QtCore.QRect(794, 598, 81, 20))
        self.Limited_dfs_lineEdit.setObjectName("Limited_dfs_lineEdit")
        self.limit_limited_dfs_label = QtWidgets.QLabel(self.centralwidget)
        self.limit_limited_dfs_label.setGeometry(QtCore.QRect(800, 570, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.limit_limited_dfs_label.setFont(font)
        self.limit_limited_dfs_label.setObjectName("limit_limited_dfs_label")
        self.Limit_Iterative_deepening_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Limit_Iterative_deepening_line_edit.setGeometry(QtCore.QRect(570, 570, 51, 20))
        self.Limit_Iterative_deepening_line_edit.setObjectName("Limit_Iterative_deepening_line_edit")
        self.Limit_iterative_deepening_label = QtWidgets.QLabel(self.centralwidget)
        self.Limit_iterative_deepening_label.setGeometry(QtCore.QRect(500, 570, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Limit_iterative_deepening_label.setFont(font)
        self.Limit_iterative_deepening_label.setObjectName("Limit_iterative_deepening_label")
        self.iterations_label = QtWidgets.QLabel(self.centralwidget)
        self.iterations_label.setGeometry(QtCore.QRect(500, 590, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iterations_label.setFont(font)
        self.iterations_label.setObjectName("iterations_label")
        self.iterative_deep_iter_linde_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.iterative_deep_iter_linde_edit.setGeometry(QtCore.QRect(570, 590, 51, 20))
        self.iterative_deep_iter_linde_edit.setObjectName("iterative_deep_iter_linde_edit")
        self.Cost_label = QtWidgets.QLabel(self.centralwidget)
        self.Cost_label.setGeometry(QtCore.QRect(410, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Cost_label.setFont(font)
        self.Cost_label.setObjectName("Cost_label")
        self.Cost_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Cost_line_edit.setGeometry(QtCore.QRect(440, 10, 261, 20))
        self.Cost_line_edit.setWhatsThis("")
        self.Cost_line_edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Cost_line_edit.setReadOnly(True)
        self.Cost_line_edit.setPlaceholderText("")
        self.Cost_line_edit.setClearButtonEnabled(False)
        self.Cost_line_edit.setObjectName("Cost_line_edit")
        self.Heuristic_Text_entry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Heuristic_Text_entry.setGeometry(QtCore.QRect(890, 40, 131, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Heuristic_Text_entry.setFont(font)
        self.Heuristic_Text_entry.setTabChangesFocus(False)
        self.Heuristic_Text_entry.setObjectName("Heuristic_Text_entry")
        self.Astar_button = QtWidgets.QPushButton(self.centralwidget)
        self.Astar_button.setGeometry(QtCore.QRect(890, 560, 131, 31))
        self.Astar_button.setObjectName("Astar_button")
        self.Greedy_button = QtWidgets.QPushButton(self.centralwidget)
        self.Greedy_button.setGeometry(QtCore.QRect(890, 590, 131, 31))
        self.Greedy_button.setObjectName("Greedy_button")
        self.FormatLabel = QtWidgets.QLabel(self.centralwidget)
        self.FormatLabel.setGeometry(QtCore.QRect(190, 40, 81, 21))
        self.FormatLabel.setObjectName("FormatLabel")
        self.Heuristic_list = QtWidgets.QLabel(self.centralwidget)
        self.Heuristic_list.setGeometry(QtCore.QRect(910, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Heuristic_list.setFont(font)
        self.Heuristic_list.setObjectName("Heuristic_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TextEntry.setToolTip(_translate("MainWindow", "ex->2 3 1 -> Node 2 Node 3 Edge 1"))
        self.TextEntry.setStatusTip(_translate("MainWindow", "ex->2 3 1 -> Node 2 Node 3 Edge 1"))
        self.TextEntry.setPlainText(_translate("MainWindow", "2 3 1\n"
"1 2\n"
""))
        self.Directed_Button.setText(_translate("MainWindow", "Directed"))
        self.Physics_Button.setText(_translate("MainWindow", "Physics"))
        self.UniformCostButton.setText(_translate("MainWindow", "Uniform cost search"))
        self.DFS_Button.setText(_translate("MainWindow", "DFS"))
        self.BFSButton.setText(_translate("MainWindow", "BFS"))
        self.Start_line_edit.setStatusTip(_translate("MainWindow", "Start Node"))
        self.goal_lineEdit.setStatusTip(_translate("MainWindow", "Goal Node"))
        self.Start_label.setText(_translate("MainWindow", "Start"))
        self.Goal_label.setText(_translate("MainWindow", "Goal"))
        self.iterative_deepening_Button.setText(_translate("MainWindow", "Iterative deepening"))
        self.Lim_DFS_button.setText(_translate("MainWindow", "Limited Dfs"))
        self.limit_limited_dfs_label.setText(_translate("MainWindow", "Limit:"))
        self.Limit_iterative_deepening_label.setText(_translate("MainWindow", "Limit:"))
        self.iterations_label.setText(_translate("MainWindow", "Iterations:"))
        self.Cost_label.setText(_translate("MainWindow", "Cost:"))
        self.Cost_line_edit.setStatusTip(_translate("MainWindow", "Cost will show infinity if there is no such route "))
        self.Heuristic_Text_entry.setToolTip(_translate("MainWindow", "format->Node Heuristic"))
        self.Heuristic_Text_entry.setStatusTip(_translate("MainWindow", "Node heuristic ex:A 5"))
        self.Astar_button.setText(_translate("MainWindow", "A* search"))
        self.Greedy_button.setText(_translate("MainWindow", "Greedy search"))
        self.FormatLabel.setText(_translate("MainWindow", "Node Node Edge"))
        self.Heuristic_list.setText(_translate("MainWindow", "Heuristics list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
