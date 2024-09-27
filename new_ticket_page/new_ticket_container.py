from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QDateEdit, QTimeEdit, QComboBox, QHBoxLayout
from PySide6.QtCore import QDate, QTime, Qt
import model_view_controller
import mvc_exceptions as mvc_exc

class newTicketContainer(QWidget):
    def __init__ (self):
        super().__init__()

        container_layout = QVBoxLayout()
        container_layout.setContentsMargins(25, 40, 25, 40)
        container_layout.setSpacing(10)

        new_ticket_label = QLabel(text="New Ticket")
        new_ticket_label.setObjectName("Title")
        new_ticket_label.setAlignment(Qt.AlignCenter)
        container_layout.addWidget(new_ticket_label)

        company_layout = QHBoxLayout()
        self.company_name_entry = QLineEdit()
        self.company_name_entry.setPlaceholderText("ACME")
        company_label = QLabel(text="Company:")
        company_layout.addWidget(company_label)
        company_layout.addWidget(self.company_name_entry)

        sas_ticket_layout = QHBoxLayout()
        self.sas_ticket_entry = QLineEdit()
        self.sas_ticket_entry.setPlaceholderText("#102203")
        sas_ticket_label = QLabel(text="SAS Ticket:")
        sas_ticket_layout.addWidget(sas_ticket_label)
        sas_ticket_layout.addWidget(self.sas_ticket_entry)

        msx_ticket_layout = QHBoxLayout()
        self.msx_ticket_entry = QLineEdit()
        self.msx_ticket_entry.setPlaceholderText("7-0000000")
        max_ticket_label = QLabel(text="MSX Ticket:")
        msx_ticket_layout.addWidget(max_ticket_label)
        msx_ticket_layout.addWidget(self.msx_ticket_entry)

        self.status_combo_layout = QHBoxLayout()
        self.status_combo = QComboBox()
        self.status_combo.addItems(["PTC", "Install", "Report Delivery"])
        status_label = QLabel(text="Status:")
        self.status_combo_layout.addWidget(status_label)
        self.status_combo_layout.addWidget(self.status_combo)

        self.date_entry_layout = QHBoxLayout()
        self.date_entry = QDateEdit()
        self.date_entry.setCalendarPopup(True)
        self.date_entry.setDisplayFormat("MM/dd/yyyy")
        self.date_entry.setDate(QDate.currentDate())
        date_label = QLabel(text="Date:")
        self.date_entry_layout.addWidget(date_label)
        self.date_entry_layout.addWidget(self.date_entry)

        self.time_entry_layout = QHBoxLayout()
        self.time_entry = QTimeEdit()
        self.time_entry.setTime(QTime.currentTime())
        self.time_entry.setDisplayFormat("hh:mm ap")
        time_label = QLabel(text="Time:")
        self.time_entry_layout.addWidget(time_label)
        self.time_entry_layout.addWidget(self.time_entry)

        container_layout.addLayout(company_layout)
        container_layout.addLayout(sas_ticket_layout)
        container_layout.addLayout(msx_ticket_layout)
        container_layout.addLayout(self.status_combo_layout)
        container_layout.addLayout(self.date_entry_layout)
        container_layout.addLayout(self.time_entry_layout)

        # Button Layout
        # button_layout = QHBoxLayout()

        # insert_data_button = QPushButton(text="Insert Data")
        # insert_data_button.clicked.connect(model_view_controller.insert_data)    
        # button_layout.addWidget(insert_data_button)

        # load_data_button = QPushButton(text="Load Data")
        # load_data_button.clicked.connect(self.load_data)
        # button_layout.addWidget(load_data_button)

        # call_data_button = QPushButton(text="Call Data")
        # call_data_button.clicked.connect(self.call_data)
        # button_layout.addWidget(call_data_button)

        # delete_data_button = QPushButton(text="Delete Data")
        # delete_data_button.clicked.connect(self.delete_data)
        # button_layout.addWidget(delete_data_button)

        # Create Ticket Button
        create_ticket_button = QPushButton(text="Create Ticket")
        create_ticket_button.clicked.connect(self.add_new_ticket)

        # container_layout.addLayout(button_layout)
        container_layout.addWidget(create_ticket_button)

        self.setLayout(container_layout)
    
    def add_new_ticket(self):
        controller = model_view_controller.ModelSQLite()
        try:        
            controller.create_item(self.company_name_entry.text(), self.sas_ticket_entry.text(), self.msx_ticket_entry.text(), self.status_combo.currentText(), self.date_entry.text(), self.time_entry.text())
        except mvc_exc.CompanyAlreadyStored as e:
            print("Company {} already stored".format(e))
        
    


