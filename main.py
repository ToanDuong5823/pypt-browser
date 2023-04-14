from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class GmailPage(QWebEnginePage):
    def __init__(self, parent):
        super().__init__(parent)
        
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        pass
        
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)
        
class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self.on_load_finished)
        self.setPage(GmailPage(self))
        
    def load(self, url):
        self.setUrl(QUrl(url))
        
    def on_load_finished(self):
        email = "ẽample@gmail.com"
        password = "password"
        self.page().runJavaScript(f"document.getElementById('identifierId').value='{email}';document.querySelector('#identifierNext button').click();")
        self.page().runJavaScript(f"setTimeout(function(){{document.querySelector('input[type=password]').value='{password}';document.querySelector('#passwordNext button').click()}}, 2000);")
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gmail Auto Login")
        self.browser = Browser()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)
        
        self.browser.load("https://accounts.google.com/signin")
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
