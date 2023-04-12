import os
import sys
from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtCore


class Ui_DirTree(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.deep_value = -1
        self.path_value = ''
        self.tree_str = ''
        self.black_name = ['.idea', 'node_modules', '.git']
        self.setWindowIcon(QIcon('tree.ico'))
        self.setFixedSize(self.width(), self.height())

    def setupUi(self, DirTree):
        DirTree.setObjectName("DirTree")
        DirTree.resize(659, 450)
        self.centralwidget = QtWidgets.QWidget(DirTree)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 641, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.path.setObjectName("path")
        self.horizontalLayout.addWidget(self.path)
        self.btn_path = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)
        self.btn_deep = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.btn_deep.setObjectName("btn_deep")
        self.btn_deep.addItem("")
        self.btn_deep.addItem("")
        self.btn_deep.addItem("")
        self.btn_deep.addItem("")
        self.btn_deep.addItem("")
        self.btn_deep.addItem("")
        self.btn_deep.addItem("")
        self.horizontalLayout.addWidget(self.btn_deep)
        self.btn_gen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_gen.setObjectName("btn_gen")
        self.horizontalLayout.addWidget(self.btn_gen)
        self.tree = QtWidgets.QTextBrowser(self.centralwidget)
        self.tree.setGeometry(QtCore.QRect(10, 40, 641, 401))
        self.tree.setObjectName("tree")
        self.btn_path.clicked.connect(self.btn_path_click)
        self.btn_deep.currentIndexChanged.connect(self.btn_deep_click)
        self.btn_gen.clicked.connect(self.btn_gen_click)
        DirTree.setCentralWidget(self.centralwidget)

        self.retranslateUi(DirTree)
        QtCore.QMetaObject.connectSlotsByName(DirTree)

    def retranslateUi(self, DirTree):
        _translate = QtCore.QCoreApplication.translate
        DirTree.setWindowTitle(_translate("DirTree", "DirTree"))
        self.path.setPlaceholderText(_translate("DirTree", "输入或者选择文件夹的绝对路径"))
        self.btn_path.setText(_translate("DirTree", "选择"))
        self.btn_deep.setItemText(0, _translate("DirTree", "深度"))
        self.btn_deep.setItemText(1, _translate("DirTree", "1"))
        self.btn_deep.setItemText(2, _translate("DirTree", "2"))
        self.btn_deep.setItemText(3, _translate("DirTree", "3"))
        self.btn_deep.setItemText(4, _translate("DirTree", "4"))
        self.btn_deep.setItemText(5, _translate("DirTree", "5"))
        self.btn_deep.setItemText(6, _translate("DirTree", "6"))
        self.btn_gen.setText(_translate("DirTree", "生成"))

    def btn_path_click(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹")
        self.path_value = path
        self.path.setText(path)

    def btn_deep_click(self):
        if self.btn_deep.currentText() == '深度':
            self.deep_value = -1
            return
        self.deep_value = int(self.btn_deep.currentText())

    def btn_gen_click(self):
        self.tree.clear()
        self.tree_str = ''
        if self.deep_value == -1:
            self.tree.setText("Error:请选择生成深度！")
            return
        if self.path_value == '':
            self.tree.setText("Error:请选择文件夹路径！")
            return
        if os.path.exists(self.path_value):
            self.generate_tree(Path(self.path_value))
            self.tree.setText(self.tree_str)
            return

    def generate_tree(self, pathname, n=0):
        deep = self.deep_value
        if n > deep:
            return
        if pathname.is_file():
            self.tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
        elif pathname.is_dir():
            if str(pathname)[str(pathname).rfind('\\') + 1:] in self.black_name:
                return
            self.tree_str += '    |' * n + '-' * 4 + \
                             str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
            for cp in pathname.iterdir():
                self.generate_tree(cp, n + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ui_DirTree()
    ex.show()
    sys.exit(app.exec_())
