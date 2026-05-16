from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtWidgets import QTabWidget


class BrowserTabs(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置游览器样式为——极简(移除标签页周围的边框)
        self.setDocumentMode(True)
        # 设置浏览器样式可关闭(显示×按钮)
        self.setTabsClosable(True)

        # 点击标签页的×按钮时，触发关闭逻辑
        self.tabCloseRequested.connect(self._tab_close)

        # 双击标签栏空白处，创建新标签
        self.tabBarDoubleClicked.connect(self._open_tab_double_click)
        # 切换当前激活的标签页时，更新地址栏
        self.currentChanged.connect(self._current_changed)
        # 地址栏引用---url_guide 由外部设置
        self.url_guide = None
        # 设置添加新标签
        self._add_new_tab(QUrl("https://www.baidu.com"), "首页")

    def set_url_guide(self, url_guide):
        """设置地址栏引用"""
        self.url_guide = url_guide

    def _open_tab_double_click(self, i):
        if i == -1:
            self._add_new_tab()

    def _add_new_tab(self, qurl=QUrl(''), label="Blank"):
        browser = QWebEngineView()
        browser.setUrl(qurl)

        # 设置标签索引
        index = self.addTab(browser, label)
        self.setCurrentIndex(index)

        browser.urlChanged.connect(
            lambda qurl, browser=browser: self._renew_url(qurl, browser)

        )

        # 新增：标题更新机制
        browser.titleChanged.connect(
            # 在标签容器中查找 browser 所在的标签页位置
            lambda title, browser=browser: self.setTabText(self.indexOf(browser), title)
        )

    def _get_current_browser(self):
        return self.currentWidget()

    def _tab_close(self, index):
        if self.count() > 1:
            self.removeTab(index)
        else:
            browser = self.widget(0)
            browser.setUrl(QUrl("about:blank"))

    def _current_changed(self):
        if self.currentWidget():
            qurl = self.currentWidget().url()
            self._renew_url(qurl, self.currentWidget())

    def _renew_url(self, q, browser=None):
        if browser != self.currentWidget():
            return
        if self.url_guide:
            # 设置新url的地址到地址栏
            self.url_guide.setText(q.toString())
            self.url_guide.setCursorPosition(0)
