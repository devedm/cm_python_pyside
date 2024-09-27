from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QCheckBox, QLineEdit, QTabWidget, QDateEdit, QTimeEdit, QComboBox, QTextEdit, QFormLayout
from PySide6.QtCore import QDate, QTime
from PySide6.QtCore import Qt

class ptcTabContainer(QWidget):
    def __init__ (self, dbItem):
        super().__init__()

        print(f"{dbItem} in ptc tab container")

        ptc_layout = QHBoxLayout()
        ptc_container = QWidget()
        ptc_container.setLayout(ptc_layout)

        #    ---- PTC Details ----
        ptc_details_layout = QVBoxLayout()
        ptc_details_container = QWidget()
        ptc_details_container.setLayout(ptc_details_layout)

        #     PTC Details Title
        ptc_details_label = QLabel(text="PTC Details")
        ptc_details_label.setObjectName("3rdTitle")
        ptc_details_layout.addWidget(ptc_details_label)

        #     PTC Details Form Layout
        ptc_details_form_layout = QFormLayout()
        ptc_form_container = QWidget()
        ptc_form_container.setLayout(ptc_details_form_layout)
        
        #     PTC Details Date
        ptc_date_label = QLabel(text="PTC date:")
        ptc_date_input = QDateEdit(date=QDate.fromString(dbItem['date'], "MM/dd/yyyy"))
        ptc_date_input.setCalendarPopup(True)
        ptc_date_input.setDisplayFormat("MM/dd/yyyy")
    
        #     PTC Details Time
        ptc_time_label = QLabel(text="PTC time:")
        ptc_time_input = QTimeEdit()
        ptc_time_input.setDisplayFormat("hh:mm ap")
        ptc_time_input.setTime(QTime.currentTime())

        #     PTC Details TimeZone
        ptc_timezone_label = QLabel(text="TimeZone:")
        ptc_timezone_input = QComboBox()
        ptc_timezone_input.addItems(["EST", "CST", "MST", "PST"])

        #     PTC Details Rescheduled
        ptc_rescheduled_label = QLabel(text="Rescheduled:")
        ptc_rescheduled_input = QCheckBox()

        #     PTC Details NDA 
        ptc_nda_label = QLabel(text="NDA Required:")
        ptc_nda_input = QCheckBox()

        #     PTC Customer Email
        ptc_customer_email_label = QLabel(text="Customer Email:")
        ptc_customer_email_input = QLineEdit()
        ptc_customer_email_input.setPlaceholderText("customer@domain.com")

        #     PTC Engager Email

        ptc_engager_email_label = QLabel(text="Engager Email:")
        ptc_engager_email_input = QLineEdit()
        ptc_engager_email_input.setPlaceholderText("v-engager@microsoft.com")


        #     Add PTC Details to Form Layout
        ptc_details_form_layout.addRow(ptc_date_label, ptc_date_input)
        ptc_details_form_layout.addRow(ptc_time_label, ptc_time_input)
        ptc_details_form_layout.addRow(ptc_timezone_label, ptc_timezone_input)
        ptc_details_form_layout.addRow(ptc_rescheduled_label, ptc_rescheduled_input)
        ptc_details_form_layout.addRow(ptc_nda_label, ptc_nda_input)
        ptc_details_form_layout.addRow(ptc_customer_email_label, ptc_customer_email_input)
        ptc_details_form_layout.addRow(ptc_engager_email_label, ptc_engager_email_input)

        #     Add PTC Details Container to PTC Details Layout
        ptc_details_layout.addWidget(ptc_form_container, alignment=Qt.AlignTop)
        ptc_details_layout.addStretch(100)

        #    ---- PTC Interest ----
        ptc_interest_layout = QVBoxLayout()
        ptc_interest_container = QWidget()
        ptc_interest_container.setLayout(ptc_interest_layout)

        ptc_interest_form_layout = QFormLayout()
        ptc_interest_form_container = QWidget()
        ptc_interest_form_container.setLayout(ptc_interest_form_layout)

        #     PTC Interest Title
        ptc_interest_label = QLabel(text="Evaluation Interest")
        ptc_interest_label.setObjectName("3rdTitle")
        ptc_interest_layout.addWidget(ptc_interest_label)

        #     PTC Interest Cloud Migration CheckBox
        ptc_cloud_migration_label = QLabel(text="Cloud Migration:")
        ptc_cloud_migration_input = QCheckBox()

        #     PTC Interest Licensing CheckBox
        ptc_licensing_label = QLabel(text="Licensing:")
        ptc_licensing_input = QCheckBox()

        #     PTC Interest Security CheckBox
        ptc_security_label = QLabel(text="Security:")
        ptc_security_input = QCheckBox()

        #     PTC Interest Others CheckBox
        ptc_others_label = QLabel(text="Other:")
        ptc_others_input = QCheckBox()

        #     PTC Interest Notes
        ptc_details_label = QLabel(text="Details:")
        ptc_details_input = QTextEdit(text="Evaluation scope: \nDeployment: Windows Application / Slingshot / BlockBox\nEndpoints: ")

        #     Add PTC Interest to Form Layout
        ptc_interest_form_layout.addRow(ptc_cloud_migration_label, ptc_cloud_migration_input)
        ptc_interest_form_layout.addRow(ptc_licensing_label, ptc_licensing_input)
        ptc_interest_form_layout.addRow(ptc_security_label, ptc_security_input)
        ptc_interest_form_layout.addRow(ptc_others_label, ptc_others_input)
        ptc_interest_form_layout.addRow(ptc_details_label)
        ptc_interest_form_layout.addRow(ptc_details_input)

        #     Add PTC Interest Container to PTC Interest Layout
        ptc_interest_layout.addWidget(ptc_interest_form_container, alignment=Qt.AlignTop)

        #    ---- PTC Notes ----
        ptc_notes_layout = QVBoxLayout()
        ptc_notes_container = QWidget()
        ptc_notes_container.setLayout(ptc_notes_layout)

        ptc_notes_label = QLabel(text="Notes")
        ptc_notes_label.setObjectName("3rdTitle")
        ptc_notes_layout.addWidget(ptc_notes_label)

        ptc_note_1 = QLabel(text=f"Ticket {dbItem['sas_ticket']} received")
        ptc_notes_layout.addWidget(ptc_note_1, alignment=Qt.AlignTop)

        ptc_note_2 = QLabel(text=f"Evaluation meeting scheduled for {dbItem['date']} received and accepted")
        ptc_notes_layout.addWidget(ptc_note_2)

        ptc_note_3 = QLabel(text=f"Evaluation meeting Rescheduled for {dbItem['date']}")
        ptc_notes_layout.addWidget(ptc_note_3)
  
        ptc_layout.addWidget(ptc_details_container, alignment=Qt.AlignLeft)
        ptc_layout.addWidget(ptc_interest_container, alignment=Qt.AlignLeft)
        ptc_layout.addWidget(ptc_notes_container, alignment=Qt.AlignLeft)        
        ptc_notes_layout.addStretch(100)        

        self.setLayout(ptc_layout)