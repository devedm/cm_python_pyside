import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PySide6.QtGui import QFontDatabase, QFont
# Initialize widgets from Files
from dashboard_page.dashboard_container import dashboardContainer
from tickets_page.tickets_container import ticketsContainer
from new_ticket_page.new_ticket_container import newTicketContainer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Window Properties
        self.setWindowTitle("Evaluations Buddy")
        self.setGeometry(100, 100, 1200, 800)

        # Initialize widgets from Files
        dashboard_Container = dashboardContainer()
        tickets_Container = ticketsContainer()
        new_Ticket_Container = newTicketContainer()
        
        # Tabs Widget
        self.tabs = QTabWidget()
        self.tabs.addTab(dashboard_Container, "Dashboard")
        self.tabs.addTab(tickets_Container, "Tickets")
        self.tabs.addTab(new_Ticket_Container, "New Ticket")
        
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.tabs)

        window_container = QWidget()
        window_container.setLayout(window_layout)

        self.setCentralWidget(window_container)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    font_id = QFontDatabase.addApplicationFont("Regular/Fonts/Cabin-Regular.ttf")
    if font_id != -1:
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if font_families:
            cabin_font = QFont(font_families[0])
            app.setFont(cabin_font)
    else:
        print("Failed to load the Cabin font")

    w = MainWindow()
    w.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())