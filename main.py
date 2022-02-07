# import pyautogui
from keyboard import add_hotkey, wait, remove_hotkey
from sys import argv, exit
from pandas import DataFrame, read_csv
from pynput.keyboard import Key, Controller
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QTableWidgetItem, QHeaderView
# from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QMovie
# from PyQt5.Qt import QSize, QImageReader, QKeySequence
from PyQt5.QtCore import Qt, QThread
# , pyqtSignal
from ui.addition import *
from ui.home import *

keyboard_pynput = Controller()

# pyinstaller -i images/squirrel.ico -w main.py
# 打包命令 需要pip install pywin32，否则换了windows环境可能无法执行
# 生成三个文件.spec后缀的配置文件 dist文件夹放生成的exe build文件夹
# pyinstaller --hidden-import=six -i ./data.ico -w -F main.py
# 可以运行spec文件生成，不一定运行py文件
# --hidden-import带的是缺少的模块名，缺少多个模块用"--hidden-import 模块名"的形式，一个模块写一遍
# -F打包成一个文件 -w表示打包之后运行不带控制台 -F可以换成-D，带打包文件，更稳定更快速
# -i ./图片名.ico 更换打包图标


addition_window_width = 550
addition_window_height = 340

# pyqt5的按键表
keyboard_dic = {16777216: 'esc', 16777264: 'f1', 16777265: 'f2', 16777266: 'f3', 16777267: 'f4', 16777268: 'f5',
                16777269: 'f6', 16777270: 'f7', 16777271: 'f8', 16777272: 'f9', 16777273: 'f10', 16777274: 'f11',
                16777275: 'f12', 96: '`', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8',
                57: '9', 48: '0', 45: '-', 61: '=', 16777219: 'backspace', 81: 'Q', 87: 'W', 69: 'E', 82: 'R',
                84: 'T', 89: 'Y', 85: 'U', 73: 'I', 79: 'O', 80: 'P', 91: '[', 93: ']', 16777220: 'enter',
                16777252: 'capslock', 65: 'A', 83: 'S', 68: 'D', 70: 'F', 71: 'G', 72: 'H', 74: 'J', 75: 'K', 76: 'L',
                59: ';', 39: '\'', 92: '\\', 90: 'Z', 88: 'X', 67: 'C', 86: 'V', 66: 'B', 78: 'N', 77: 'M', 44: ',',
                46: '.', 47: '/', 32: 'space', 126: 'shift+`', 33: 'shift+1', 64: 'shift+2', 35: 'shift+3',
                36: 'shift+4', 37: 'shift+5', 94: 'shift+6', 38: 'shift+7', 42: 'shift+8', 40: 'shift+9', 41: 'shift+0',
                95: 'shift+-', 43: 'shift+=', 123: 'shift+[', 125: 'shift+]', 58: 'shift+;', 34: "shift+'",
                124: 'shift+\\', 60: 'shift+,', 62: 'shift+.', 63: 'shift+/'
                }
# caps_lock_status = {'capital': [256, 768, 1280, 1792], 'lowercase': [0, 512, 1024, 1536]}

shift_dic = {'1': '!', '!': '1'}


class HomeWindow(QMainWindow, Ui_HomeWindow):
    def __init__(self, parent=None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)
        try:
            df = read_csv('local_data.csv', index_col=False)
        except FileNotFoundError:
            df = DataFrame(columns=['hotkey', 'content'])
            df.to_csv('local_data.csv', index=False)
        row_num = len(df)
        # 加行
        self.tableWidget.setRowCount(row_num)
        for i in range(row_num):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(df['hotkey'].loc[i]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(df['content'].loc[i]))
            HotKeys(self, df['hotkey'].loc[i], df['content'].loc[i]).start()
        # 表格内容自动填充
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def closeEvent(self, event):
        """
        重写该方法主要是解决打开子窗口时，如果关闭了主窗口但子窗口仍显示的问题
        使用sys.exit(0) 时就会只要关闭了主窗口，所有关联的子窗口也会全部关闭
        """
        exit(0)

    def open_addition(self):
        Initialize.addition.show()
        Initialize.addition.hotkey.setText("无")
        Initialize.addition.textEdit.setText("")
        # Initialize.main.show()

    def del_hotkey(self):
        items = self.tableWidget.selectedItems()
        del_hotkey_str = []
        if items:
            selected_rows = []  # 求出所选择的行数
            for i in items:
                row = i.row()
                if row not in selected_rows:
                    selected_rows.append(row)
                    # self.tableWidget.
                    del_hotkey_str.append(self.tableWidget.item(row, 0).text())
                    remove_hotkey(self.tableWidget.item(row, 0).text())
            for r in range(len(selected_rows)):
                self.tableWidget.removeRow(selected_rows[r])  # 删除行
                # self.tableWidget.removeRow(selected_rows[r])  # 删除行
        df = read_csv('local_data.csv', index_col=False)
        for i in del_hotkey_str:
            df = df.drop(df[df.hotkey == i].index)
        df = df.reset_index(drop=True)
        df.to_csv('local_data.csv', index=False)

    def modify_hotkey(self):
        pass
        # items = self.tableWidget.selectedItems()
        # del_hotkey_str = []
        # if items:
        #     Initialize.addition.show()
        #     Initialize.addition.hotkey.setText("无")
        #     Initialize.addition.textEdit.setText()
        #     selected_rows = []  # 求出所选择的行数
        #     row = items[-1].row()
        #     if row not in selected_rows:
        #         selected_rows.append(row)
        #         # self.tableWidget.
        #         del_hotkey_str.append(self.tableWidget.item(row, 0).text())
        #         remove_hotkey(self.tableWidget.item(row, 0).text())
        #     for r in range(len(selected_rows)):
        #         self.tableWidget.removeRow(selected_rows[r])  # 删除行
        #         # self.tableWidget.removeRow(selected_rows[r])  # 删除行
        # df = read_csv('local_data.csv', index_col=False)
        # for i in del_hotkey_str:
        #     df = df.drop(df[df.hotkey == i].index)
        # df = df.reset_index(drop=True)
        # df.to_csv('local_data.csv', index=False)


def type_content(content, is_shift):
    if is_shift:
        keyboard_pynput.release(Key.shift)
        keyboard_pynput.type(list(content))
    else:
        keyboard_pynput.type(list(content))


class HotKeys(QThread):
    def __init__(self, parent=None, *args):
        QThread.__init__(self, parent)
        self.hotkey = args[0]
        self.content = args[1]

    def run(self):
        is_shift = False
        if 'shift' in self.hotkey:
            is_shift = True
        add_hotkey(self.hotkey, type_content, args=(self.content, is_shift, ), suppress=True, trigger_on_release=True)
        wait()


class AdditionWindow(QMainWindow, Ui_AdditionWindow):
    def __init__(self, parent=None):
        super(AdditionWindow, self).__init__(parent)
        self.setupUi(self)

        # 设置按键捕获焦点，默认在按钮上
        # Qt.TabFocus 通过Tab键获得焦点
        # Qt.ClickFocus 通过被单击获得焦点
        # Qt.StrongFocus 可通过上面两种方式获得焦点
        # Qt.NoFocus 不能通过上两种方式获得焦点(默认值), setFocus仍可使其获得焦点
        self.setFocusPolicy(Qt.StrongFocus)
        self.hotkey.setFocusPolicy(Qt.StrongFocus)
        self.textEdit.setFocusPolicy(Qt.StrongFocus)
        self.confirm_button.setFocusPolicy(Qt.NoFocus)
        self.cancel_button.setFocusPolicy(Qt.NoFocus)
        self.hotkey.setReadOnly(True)
        # self.hotkey.end(True)

    def confirm_addition(self):
        Initialize.addition.hide()
        HotKeys(Initialize.home, self.hotkey.text(), self.textEdit.toPlainText()).start()
        Initialize.home.tableWidget.setRowCount(Initialize.home.tableWidget.rowCount() + 1)
        Initialize.home.tableWidget.setItem(Initialize.home.tableWidget.rowCount() - 1, 0,
                                            QTableWidgetItem(self.hotkey.text()))
        Initialize.home.tableWidget.setItem(Initialize.home.tableWidget.rowCount() - 1, 1,
                                            QTableWidgetItem(self.textEdit.toPlainText()))
        df = read_csv('local_data.csv', index_col=False)
        # 在配置文件最后加一行
        df.loc[Initialize.home.tableWidget.rowCount() - 1] = [self.hotkey.text(), self.textEdit.toPlainText()]
        df = df.reset_index(drop=True)
        df.to_csv('local_data.csv', index=False)

    def cancel_addition(self):
        Initialize.addition.hide()

    def keyPressEvent(self, QKeyEvent):  # 键盘某个键被按下时调用
        # 选中指定控件才触发按键捕获
        if self.focusWidget().objectName() != 'hotkey':
            return
        # modifiers()   判断修饰键
        # Qt.NoModifier   没有修饰键
        # Qt.ShiftModifier    Shift键被按下
        # Qt.ControlModifier    Ctrl键被按下
        # Qt.AltModifier      Alt键被按下
        # key()  是普通键
        try:
            if QKeyEvent.modifiers() == Qt.NoModifier and keyboard_dic[QKeyEvent.key()]:  # 单键
                self.hotkey.clear()
                self.hotkey.setText(keyboard_dic[QKeyEvent.key()])
                print('按下了' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.ControlModifier and keyboard_dic[QKeyEvent.key()]:  # 两键组合
                self.hotkey.clear()
                self.hotkey.setText('ctrl+' + keyboard_dic[QKeyEvent.key()])
                print('按下了ctrl-' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.AltModifier and keyboard_dic[QKeyEvent.key()]:  # 两键组合
                self.hotkey.clear()
                self.hotkey.setText('alt+' + keyboard_dic[QKeyEvent.key()])
                print('按下了alt-' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.ShiftModifier and keyboard_dic[QKeyEvent.key()]:  # 两键组合
                self.hotkey.clear()
                if 'shift' in keyboard_dic[QKeyEvent.key()]:
                    self.hotkey.setText(keyboard_dic[QKeyEvent.key()])
                    print('按下了' + keyboard_dic[QKeyEvent.key()])
                else:
                    self.hotkey.setText('shift+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了shift-' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.ControlModifier | Qt.AltModifier and keyboard_dic[QKeyEvent.key()]:  # 三键组合
                self.hotkey.clear()
                self.hotkey.setText('ctrl+alt+' + keyboard_dic[QKeyEvent.key()])
                print('按下了ctrl+alt+' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.ControlModifier | Qt.ShiftModifier \
                    and keyboard_dic[QKeyEvent.key()]:  # 三键组合
                self.hotkey.clear()
                if 'shift' in keyboard_dic[QKeyEvent.key()]:
                    self.hotkey.setText('ctrl+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了ctrl+' + keyboard_dic[QKeyEvent.key()])
                else:
                    self.hotkey.setText('ctrl+shift+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了ctrl+shift+' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.AltModifier | Qt.ShiftModifier and keyboard_dic[QKeyEvent.key()]:  # 三键组合
                self.hotkey.clear()
                if 'shift' in keyboard_dic[QKeyEvent.key()]:
                    self.hotkey.setText('alt+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了alt+' + keyboard_dic[QKeyEvent.key()])
                else:
                    self.hotkey.setText('alt+shift+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了alt+shift+' + keyboard_dic[QKeyEvent.key()])
            elif QKeyEvent.modifiers() == Qt.ControlModifier | Qt.AltModifier | Qt.ShiftModifier \
                    and keyboard_dic[QKeyEvent.key()]:  # 四键组合
                self.hotkey.clear()
                if 'shift' in keyboard_dic[QKeyEvent.key()]:
                    self.hotkey.setText('ctrl+alt+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了ctrl+alt+' + keyboard_dic[QKeyEvent.key()])
                else:
                    self.hotkey.setText('ctrl+alt+shift+' + keyboard_dic[QKeyEvent.key()])
                    print('按下了ctrl+alt+shift+' + keyboard_dic[QKeyEvent.key()])
            else:
                self.hotkey.clear()
                self.hotkey.setText('无')
            print(QKeyEvent.key())
        except Exception as e:
            print(QKeyEvent.key(), e)
            self.hotkey.setText('无')
        # if QKeyEvent == QKeySequence.SelectAll:  # 禁止全选
        #     return
        # if QKeyEvent == QKeySequence.Paste:  # 禁止粘贴
        #     print("OK")
        #     return
        # if QKeyEvent == QKeySequence.Copy:  # 禁止复制
        #     return
        # if QKeyEvent == QKeySequence.Cut:  # 禁止剪切
        #     return


class Initialize:
    def __init__(self):
        app = QApplication(argv)

        # 读取icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/squirrel.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # 实例化addition窗口
        Initialize.addition = AdditionWindow()
        # 标题栏icon
        Initialize.addition.setWindowIcon(icon)
        # 窗口标题
        Initialize.addition.setWindowTitle("设置热键及文本")
        # 窗口大小
        Initialize.addition.setFixedSize(addition_window_width, addition_window_height)
        # 窗口置顶，屏蔽其他程序的快捷键
        Initialize.addition.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # 初始化主窗口
        Initialize.home = HomeWindow()
        # 窗口标题
        Initialize.home.setWindowTitle("松鼠文本自动输入器")
        # 标题栏icon
        Initialize.home.setWindowIcon(icon)
        # 表格只能按行选
        Initialize.home.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 表格不可编辑
        Initialize.home.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        Initialize.home.modify_button.hide()
        # 窗口置顶，屏蔽其他程序的快捷键
        Initialize.home.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # 显示界面
        Initialize.home.show()

        exit(app.exec_())


def main():
    program = Initialize()


# def test(x):
#     print(x.scan_code)


if __name__ == "__main__":
    # print(keyboard.get_hotkey_name(['ctrl', 'alt', '1']))
    # keyboard.hook(test)
    # keyboard.wait()
    main()
