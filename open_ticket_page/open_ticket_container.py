from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTabWidget, QMainWindow, QMessageBox
from PySide6.QtCore import QDate, QTime
from PySide6.QtCore import Qt
import model_view_controller
from open_ticket_page.ptc_tab_container import ptcTabContainer
from open_ticket_page.follow_up_tab_container import followUpTabContainer
from open_ticket_page.install_tab_container import installTabContainer

class openTicketContainer(QWidget):
    def __init__ (self, dbItem):
        super().__init__()
        self.dbItem = dbItem

        main_layout = QVBoxLayout()
        page_container = QWidget()
        page_container.setLayout(main_layout)

        top_layout = QHBoxLayout()
        top_container = QWidget()
        top_container.setLayout(top_layout)

        title_layout = QHBoxLayout()
        title_container = QWidget()
        title_container.setLayout(title_layout)

        open_ticket_label = QLabel(text=dbItem['company'])
        open_ticket_label.setObjectName("Title")
        title_layout.addWidget(open_ticket_label)

        opp_id_label = QLabel(text=dbItem['msx_ticket'])
        opp_id_label.setObjectName("SubTitle")
        title_layout.addWidget(opp_id_label)

        sas_id_label = QLabel(text=dbItem['sas_ticket'])
        sas_id_label.setObjectName("SubTitle")
        title_layout.addWidget(sas_id_label)

        actions_layout = QHBoxLayout()
        actions_container = QWidget()
        actions_container.setLayout(actions_layout)

        save_button = QPushButton(text="Save")
        actions_layout.addWidget(save_button)
        save_button.clicked.connect(self.save_button_clicked)

        discard_button = QPushButton(text="Discard")
        actions_layout.addWidget(discard_button)
        discard_button.clicked.connect(self.discard_button_clicked)

        delete_button = QPushButton(text="Delete")
        actions_layout.addWidget(delete_button)
        delete_button.clicked.connect(self.confirmation_dialog)

        # Add widgets to top layout
        top_layout.addWidget(title_container, alignment=Qt.AlignLeft)
        top_layout.addWidget(actions_container, alignment=Qt.AlignRight)

        # Add Imported Tab to Main Layout
        ptc_container = ptcTabContainer(dbItem)
        follow_up_container = followUpTabContainer(dbItem)
        install_tab_container = installTabContainer(dbItem)

        ticketTabs = QTabWidget()
        ticketTabs.addTab(ptc_container, "PTC")
        ticketTabs.addTab(follow_up_container, "Follow Up")
        ticketTabs.addTab(install_tab_container, "Install")

        main_layout.addWidget(top_container, alignment=Qt.AlignTop)
        main_layout.addWidget(ticketTabs, alignment=Qt.AlignTop)

        self.setWindowTitle(dbItem['company'])
        self.setLayout(main_layout)

    def save_button_clicked(self):
        print("Save Button Clicked")

    def discard_button_clicked(self):
        print("Discard Button Clicked")

    def confirmation_dialog(self):
        confirmation_message = QMessageBox()
        confirmation_message.setWindowTitle("Delete Confirmation")
        confirmation_message.setText("Are you sure you want to delete this item?")
        confirmation_message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_message.setDefaultButton(QMessageBox.No)

        confirmation_message.buttonClicked.connect(self.confirmation_response)

        confirmation_message.exec()

    def confirmation_response(self, answer):
        if answer.text() == "&Yes":
            self.delete_entry()
        else:
            print("Action cancelled")
    def delete_entry(self):
        controller = model_view_controller.ModelSQLite()
        controller.delete_item(self.dbItem['company'])
        print(f"Company '{self.dbItem['company']}' Deleted")
        self.close()
