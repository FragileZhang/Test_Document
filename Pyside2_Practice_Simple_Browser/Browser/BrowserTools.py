from PySide2.QtCore import QSize, QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QToolBar, QAction, QLineEdit


class BrowserTools(QToolBar):
    def __init__(self, tabs):
        super().__init__()
        # 当前的tabs = MainWindow的tabs
        self.tabs = tabs

        self.setIconSize(QSize(20, 20))

        # action_button
        back_button = QAction(QIcon('image/back.png'), 'back', self)
        forward_button = QAction(QIcon('image/forward.png'), 'forward', self)
        stop_button = QAction(QIcon('image/stop.png'), 'stop', self)
        reload_button = QAction(QIcon('image/reload.png'), 'reload', self)

        # 按钮动作
        back_button.triggered.connect(self._go_back)
        forward_button.triggered.connect(self._go_forward)
        stop_button.triggered.connect(self._go_stop)
        reload_button.triggered.connect(self._go_reload)

        # 添加动作
        self.addActions([
            back_button,
            forward_button,
            stop_button,
            reload_button

        ])

        # 搜索栏目
        self.url_guide = QLineEdit()
        self.url_guide.setPlaceholderText("请输入网址:")
        self.url_guide.returnPressed.connect(self._navigation_to_url)
        self.addWidget(self.url_guide)

    def _go_back(self):
        if self.tabs:
            browser = self.tabs.currentWidget()
            if browser:
                browser.back()

    def _go_forward(self):
        if self.tabs:
            browser = self.tabs.currentWidget()
            if browser:
                browser.forward()

    def _go_stop(self):
        if self.tabs:
            browser = self.tabs.currentWidget()
            if browser:
                browser.stop()

    def _go_reload(self):
        if self.tabs:
            browser = self.tabs.currentWidget()
            if browser:
                browser.reload()

    def _navigation_to_url(self):
        if not self.tabs:
            return
        q = QUrl(self.url_guide.text())
        if q.scheme() == '':
            q.setScheme("https")
        browser = self.tabs.currentWidget()
        if browser:
            browser.setUrl(q)
