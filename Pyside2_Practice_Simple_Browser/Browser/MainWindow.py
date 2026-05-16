from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from Browser.BrowserTabs import BrowserTabs
from Browser.BrowserTools import BrowserTools


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Browser")
        self.setWindowIcon(QIcon('image/window_icon.png'))
        self.resize(1200, 800)

        # 标签页
        self.tabs = BrowserTabs()

        # 工具栏
        self.tools = BrowserTools(self.tabs)

        # 设置 tabs 的 url_guide 引用   # 建立双向通信
        self.tabs.set_url_guide(self.tools.url_guide)

        # 添加工具栏
        self.addToolBar(self.tools)

        # 设置核心组件
        self.setCentralWidget(self.tabs)
