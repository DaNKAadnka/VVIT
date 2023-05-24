import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox,
                             QComboBox, QLineEdit, QLabel)

from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._s = "Понедельник_чет"
        self._q1 = ""
        self._q2 = ""
        self._q3 = ""

        self.resize(1200, 800)

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        #self._create_update_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="telegram_bot",
                                     user="postgres",
                                     password="ebat123Z",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def onActivated(self, text):
        self._s = text
        self._update_day_table()

    def onChanged1(self, text):
        self._q1 = text

    def onChanged2(self, text):
        self._q2 = text
    def onChanged3(self, text):
        self._q3 = text

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Shedule")

        self.monday_gbox = QGroupBox("Monday")

        combo = QComboBox(self)
        combo.addItems(["Понедельник_чет", "Вторник_чет",
                        "Среда_чет", "Четверг_чет", "Пятница_чет",
                        "Понедельник_нечет", "Вторник_нечет",
                        "Среда_нечет", "Четверг_нечет", "Пятница_нечет"])

        combo.move(50, 50)

        combo.activated[str].connect(self.onActivated)

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        ql1 = QLineEdit(self)
        ql2 = QLineEdit(self)
        ql3 = QLineEdit(self)

        ql1.textChanged[str].connect(self.onChanged1)
        ql2.textChanged[str].connect(self.onChanged2)
        ql3.textChanged[str].connect(self.onChanged3)

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox1.addWidget(combo)
        self.shbox2.addWidget(self.monday_gbox)
        self.shbox3.addWidget(ql1)
        self.shbox3.addWidget(ql2)
        self.shbox3.addWidget(ql3)

        self._create_day_table()

        self.shedule_tab.setLayout(self.svbox)

    def _create_day_table(self):
        self.day_table = QTableWidget()
        self.day_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.mvbox = QVBoxLayout()
        self._update_day_table()
        self.monday_gbox.setLayout(self.mvbox)

    def _update_day_table(self):

        self.day_table.clear()
        self.day_table.setRowCount(0)
        self.day_table.setColumnCount(7)
        self.day_table.setHorizontalHeaderLabels(["Subject", "Room", "Time", "Edit", "Delete", "Up", "Down"])
        self.cursor.execute("SELECT * FROM timetable WHERE day='{}' ORDER BY numb_of_lesson".format(self._s))
        records = list(self.cursor.fetchall())

        self.day_table.setRowCount(6)

        cnt = 0
        for i in range(7):
            editButton = QPushButton("Edit")
            delButton = QPushButton("Delete")
            upButton = QPushButton("↑")
            downButton = QPushButton("↓")

            if len(records) <= cnt:
                self.day_table.setItem(i, 0,
                                       QTableWidgetItem(""))
                self.day_table.setItem(i, 1,
                                       QTableWidgetItem(""))
                self.day_table.setItem(i, 2,
                                       QTableWidgetItem(""))


            else:
                r = list(records[cnt])
                if i == r[5]-1:
                    self.day_table.setItem(i, 0,
                                           QTableWidgetItem(str(r[2])))
                    self.day_table.setItem(i, 1,
                                           QTableWidgetItem(str(r[3])))
                    self.day_table.setItem(i, 2,
                                           QTableWidgetItem(str(r[4])))
                    cnt += 1

            self.day_table.setCellWidget(i, 3, editButton)
            self.day_table.setCellWidget(i, 4, delButton)
            self.day_table.setCellWidget(i, 5, upButton)
            self.day_table.setCellWidget(i, 6, downButton)

            if i == 0:
                delButton.clicked.connect(self._del1)
                editButton.clicked.connect(self._upd1)
                upButton.clicked.connect(self._up1)
                downButton.clicked.connect(self._up11)
            elif i == 1:
                delButton.clicked.connect(self._del2)
                editButton.clicked.connect(self._upd2)
                upButton.clicked.connect(self._up2)
                downButton.clicked.connect(self._up21)
            elif i == 2:
                delButton.clicked.connect(self._del3)
                editButton.clicked.connect(self._upd3)
                upButton.clicked.connect(self._up3)
                downButton.clicked.connect(self._up31)
            elif i == 3:
                delButton.clicked.connect(self._del4)
                editButton.clicked.connect(self._upd4)
                upButton.clicked.connect(self._up4)
                downButton.clicked.connect(self._up41)
            elif i == 4:
                delButton.clicked.connect(self._del5)
                editButton.clicked.connect(self._upd5)
                upButton.clicked.connect(self._up5)
                downButton.clicked.connect(self._up51)
            elif i == 5:
                delButton.clicked.connect(self._del6)
                editButton.clicked.connect(self._upd6)
                upButton.clicked.connect(self._up6)
                downButton.clicked.connect(self._up61)

        self.day_table.resizeRowsToContents()
        self.mvbox.addWidget(self.day_table)

    #Функции для кнопок удаления строки
    def _del1(self):
        self._delet_day_table(self._s, 1)

    def _del2(self):
        self._delet_day_table(self._s, 2)

    def _del3(self):
        self._delet_day_table(self._s, 3)

    def _del4(self):
        self._delet_day_table(self._s, 4)

    def _del5(self):
        self._delet_day_table(self._s, 5)

    def _del6(self):
        self._delet_day_table(self._s, 6)

    #Функции для кнопок редактирования строки
    def _upd1(self):
        self._edit_day_table(self._s, 1, self._q1, self._q2, self._q3)

    def _upd2(self):
        self._edit_day_table(self._s, 2, self._q1, self._q2, self._q3)

    def _upd3(self):
        self._edit_day_table(self._s, 3, self._q1, self._q2, self._q3)

    def _upd4(self):
        self._edit_day_table(self._s, 4, self._q1, self._q2, self._q3)

    def _upd5(self):
        self._edit_day_table(self._s, 5, self._q1, self._q2, self._q3)

    def _upd6(self):
        self._edit_day_table(self._s, 6, self._q1, self._q2, self._q3)

    #Функции для кнопок вверх
    def _up1(self):
        self._up_day_table(self._s, 1, -1)

    def _up2(self):
        self._up_day_table(self._s, 2, -1)

    def _up3(self):
        self._up_day_table(self._s, 3, -1)

    def _up4(self):
        self._up_day_table(self._s, 4, -1)

    def _up5(self):
        self._up_day_table(self._s, 5, -1)

    def _up6(self):
        self._up_day_table(self._s, 6, -1)

    #Функции для кнопок вниз

    def _up11(self):
        self._up_day_table(self._s, 1, 1)

    def _up21(self):
        self._up_day_table(self._s, 2, 1)

    def _up31(self):
        self._up_day_table(self._s, 3, 1)

    def _up41(self):
        self._up_day_table(self._s, 4, 1)

    def _up51(self):
        self._up_day_table(self._s, 5, 1)

    def _up61(self):
        self._up_day_table(self._s, 6, 1)


    #Общая функция для удаления строки
    def _delet_day_table(self, day, numb_of_lesson):
        query = "delete from timetable where day = '{0}' and numb_of_lesson = '{1}'".format(day, numb_of_lesson)
        try:
            self.cursor.execute(query)
        except:
            self.day_table.removeRow(numb_of_lesson)

        self.conn.commit()
        self._update_day_table()

    #Общая функция для редактирования строки
    def _edit_day_table(self, day, row, q1, q2, q3):

        if not q1 or not q2 or not q3:
            self._open("Введите все данные в поля")
            return

        query1 = "select id from timetable where day = '{}' and numb_of_lesson = {}"
        query1 = query1.format(day, row)
        self.cursor.execute(query1)
        records1 = list(self.cursor.fetchall())

        if len(records1) == 0:
            query2 = "insert into timetable(day, subject, room_numb, start_time, numb_of_lesson) "
            query2 += "values ('{}', '{}', '{}', '{}', {})"

            query2 = query2.format(day, q1, q2, q3, row)
            self.cursor.execute(query2)
            self.conn.commit()
        else:
            query3 = "update timetable set subject = '{}', room_numb = '{}', start_time = '{}' where numb_of_lesson = {}"
            query3 = query3.format(q1, q2, q3, row)
            print(query3)
            self.cursor.execute(query3)
            self.conn.commit()

        self._update_day_table()

    def _up_day_table(self, day, row, flag):

        if row + flag == 0 or row + flag > 6:
            return

        query1 = "select * from timetable where day = '{}' and numb_of_lesson = {}"
        query1 = query1.format(day, row)
        self.cursor.execute(query1)
        records1 = list(self.cursor.fetchall())
        print(1, records1)

        if not records1:
            return
        else:
            query2 = "select * from timetable where day = '{}' and numb_of_lesson = {}"
            query2 = query2.format(day, row + flag)
            self.cursor.execute(query2)
            print(query1)
            print(query2)
            records2 = list(self.cursor.fetchall())
            print(2, records2)
            if not records2:
                self._delet_day_table(day, row)
                #print(row, records1[0][2], records1[0][3], records1[0][4])
                self._edit_day_table(day, row + flag, records1[0][2], records1[0][3], records1[0][4])
                self.conn.commit()
            else:
                self._delet_day_table(day, row)
                self._delet_day_table(day, row+flag)
                self.conn.commit()
                self._edit_day_table(day, row+flag, records1[0][2], records1[0][3], records2[0][4])
                self._edit_day_table(day, row, records2[0][2], records2[0][3], records1[0][4])
                self.conn.commit()


    def _open(self, text):
        self.a1 = Modal()
        self.a1._change_text(text)
        self.a1.show()

class Modal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowModality(Qt.WindowModal)
        # self.setModal(True)
        self.resize(400, 400)
        self._text = QLabel(self)
        self._text.move(30, 30)
        self._text.setWordWrap(True)

    def _change_text(self, text):
        self._font = QFont()
        self._font.setPointSize(12)
        print("Hello")
        self._text.setFont(self._font)
        self._text.setText(text)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

