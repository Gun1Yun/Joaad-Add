import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType('main_window.ui')[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set label
        self.search_label = [self.search_label1,
                             self.search_label2, self.search_label3]
        self.link_label = [self.link_label1,
                           self.link_label2, self.link_label3]

        self.is_search = True    # create type = search
        for l_label in self.link_label:
            l_label.setHidden(True)

        # set button connect
        self.search_add_btn.clicked.connect(self.search_add_btn_clicked)
        self.link_add_btn.clicked.connect(self.link_add_btn_clicked)

    def search_add_btn_clicked(self):
        # QMessageBox.about(self, 'message', 'clicked')
        if not self.is_search:
            self.is_search = True
            self.expose_textbox.setText('{희망키워드}')
            self.expose_textbox.setReadOnly(False)
            for s_label, l_label in zip(self.search_label, self.link_label):
                s_label.setHidden(False)
                l_label.setHidden(True)

    def link_add_btn_clicked(self):
        # QMessageBox.about(self, 'message', 'clicked')
        if self.is_search:
            self.is_search = False
            self.expose_textbox.setText('필요없음')
            self.expose_textbox.setReadOnly(True)
            for s_label, l_label in zip(self.search_label, self.link_label):
                s_label.setHidden(True)
                l_label.setHidden(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
