import sys

from howdoi import howdoi as hd
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QComboBox, QScrollArea
from PySide2.QtCore import QSize, QMargins, Qt





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HowDoI")
        self.setMinimumSize(QSize(600, 600))
        self.vs = hd.__version__
        self.plus_options = ""

        # title label
        _title = QLabel("HowDoI:")
        _title_font = _title.font()
        _title_font.setPointSize(30)
        _title.setFont(_title_font)
        _title.setAlignment(Qt.AlignCenter)

        #answer label
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.label = QLabel("ask me anything", self)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        scroll_area.setWidget(self.label)
        self.label.setStyleSheet("border-radius: 5px; border: 1px solid black")
        font = self.label.font()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        #version label
        version = QLabel(f"version: {self.vs}")
        font = version.font()
        font.setPointSize(12)
        version.setFont(font)
        version.setAlignment(Qt.AlignCenter)

        #ask button
        ask_button = QPushButton("ASK")
        ask_button.clicked.connect(self.line_edit_return)

        #help button
        help_button = QPushButton("HELP")
        help_button.clicked.connect(self.help)

        #settings
        self.settings_dp = QComboBox()
        self.settings_dp.addItem("default")
        self.settings_dp.addItem("-l")
        self.settings_dp.addItem("-a")
        self.settings_dp.addItem("-j")
        self.settings_dp.currentIndexChanged.connect(self.setting_selected)



        # text box
        self.line_edit = QLineEdit(self)

        self.line_edit.setPlaceholderText("Enter your question here")
        font = self.line_edit.font()
        font.setPointSize(15)
        self.line_edit.setFont(font)
        self.line_edit.returnPressed.connect(self.line_edit_return)

        set_layout = QHBoxLayout()
        set_layout.addWidget(help_button)
        set_layout.addWidget(self.settings_dp)


        #main layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(_title)
        v_layout.addWidget(self.line_edit)
        v_layout.addWidget(ask_button)
        v_layout.addLayout(set_layout)
        v_layout.addSpacing(40)
        #v_layout.addWidget(self.label)
        v_layout.addWidget(scroll_area)
        v_layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        v_layout.addWidget(version)

        container = QWidget()
        container.setLayout(v_layout)
        container.setContentsMargins(QMargins(0,0,0,0))
        self.setCentralWidget(container)

    def line_edit_return(self):
        self.label.setText(hd.howdoi(self.line_edit.text() + " " + self.plus_options))

    def help(self):
        self.label.setText(hd.get_parser().format_help())

    def setting_selected(self,i):
        if self.settings_dp.currentText() == "default":
            return
        else:
            self.plus_options = self.settings_dp.currentText()


class GUI:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyleSheet(self.read_qss("../stylesheet/Combinear.qss"))
        self.window = MainWindow()

    def run(self):
        self.window.show()
        self.app.exec_()

    def read_qss(self, path):
        f = open(path, "r")
        _style = f.read()
        f.close()
        return _style
