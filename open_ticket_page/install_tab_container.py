from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QCheckBox, QLineEdit, QTabWidget, QDateEdit, QTimeEdit, QComboBox, QTextEdit, QFormLayout
from PySide6.QtCore import QDate, QTime
from PySide6.QtCore import Qt

class installTabContainer(QWidget):
    def __init__ (self, dbItem):
        super().__init__()

        print(f"{dbItem} in ptc tab container")

        install_layout = QHBoxLayout()
        install_container = QWidget()
        install_container.setLayout(install_layout)

        #    ---- Install Details ----
        install_details_layout = QVBoxLayout()
        install_details_container = QWidget()
        install_details_container.setLayout(install_details_layout)

        #     Install Details Title
        install_details_label = QLabel(text="Install Details")
        install_details_label.setObjectName("3rdTitle")
        install_details_layout.addWidget(install_details_label)

        #     Install Details Form Layout
        install_details_form_layout = QFormLayout()
        install_form_container = QWidget()
        install_form_container.setLayout(install_details_form_layout)
        
        #     Install Details Date
        install_date_label = QLabel(text="Install date:")
        install_date_input = QDateEdit(date=QDate.fromString(dbItem['date'], "MM/dd/yyyy"))
        install_date_input.setCalendarPopup(True)
        install_date_input.setDisplayFormat("MM/dd/yyyy")
    
        #     Install Details Time
        install_time_label = QLabel(text="Install time:")
        install_time_input = QTimeEdit()
        install_time_input.setDisplayFormat("hh:mm ap")
        install_time_input.setTime(QTime.currentTime())

        #     Install Details TimeZone
        install_timezone_label = QLabel(text="TimeZone:")
        install_timezone_input = QComboBox()
        install_timezone_input.addItems(["EST", "CST", "MST", "PST"])

        #     Install Details Rescheduled
        install_rescheduled_label = QLabel(text="Rescheduled:")
        install_rescheduled_input = QCheckBox()

        #     Install Details Pre-install date
        pre_install_date_checkbox = QCheckBox(text="Pre-Install date:")
        pre_install_date_input = QDateEdit(date=QDate.fromString(dbItem['date'], "MM/dd/yyyy").addDays(-2))
        pre_install_date_input.setCalendarPopup(True)
        pre_install_date_input.setDisplayFormat("MM/dd/yyyy")

        #     Install Details 
        install_sub_campaign_label = QLabel(text="SubCampaign: ")
        install_sub_campaign_combobox = QComboBox()

        #     PTC Customer Email
        install_sign_up_link_label = QLabel(text="Sign Up Link:")
        install_output_sign_up_link_label = QLabel(text="signup.block64.com/xxxxx")

        #     PTC Engager Email

        ptc_engager_email_label = QLabel(text="Engager Email:")
        ptc_engager_email_input = QLineEdit()
        ptc_engager_email_input.setPlaceholderText("v-engager@microsoft.com")


        #     Add Install Details to Form Layout
        install_details_form_layout.addRow(install_date_label, install_date_input)
        install_details_form_layout.addRow(install_time_label, install_time_input)
        install_details_form_layout.addRow(install_timezone_label, install_timezone_input)
        install_details_form_layout.addRow(install_rescheduled_label, install_rescheduled_input)
        install_details_form_layout.addRow(pre_install_date_checkbox, pre_install_date_input)
        install_details_form_layout.addRow(install_sub_campaign_label, install_sub_campaign_combobox)
        install_details_form_layout.addRow(install_sign_up_link_label, install_output_sign_up_link_label)
        install_details_form_layout.addRow(ptc_engager_email_label, ptc_engager_email_input)

        #     Add Install Details Container to Install Details Layout
        install_details_layout.addWidget(install_form_container, alignment=Qt.AlignTop)
        install_details_layout.addStretch(100)

        #    ---- PTC Interest ----
        ptc_interest_layout = QVBoxLayout()
        ptc_interest_container = QWidget()
        ptc_interest_container.setLayout(ptc_interest_layout)

        ptc_interest_form_layout = QFormLayout()
        ptc_interest_form_container = QWidget()
        ptc_interest_form_container.setLayout(ptc_interest_form_layout)

        #     PTC Interest Title
        ptc_interest_label = QLabel(text="PTC Interest")
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
        install_details_label = QLabel(text="Details:")
        ptc_details_input = QTextEdit(text="Evaluation scope: \nDeployment: Windows Application / Slingshot / BlockBox\nEndpoints: ")

        #     Add PTC Interest to Form Layout
        ptc_interest_form_layout.addRow(ptc_cloud_migration_label, ptc_cloud_migration_input)
        ptc_interest_form_layout.addRow(ptc_licensing_label, ptc_licensing_input)
        ptc_interest_form_layout.addRow(ptc_security_label, ptc_security_input)
        ptc_interest_form_layout.addRow(ptc_others_label, ptc_others_input)
        ptc_interest_form_layout.addRow(install_details_label)
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
  
        install_layout.addWidget(install_details_container, alignment=Qt.AlignLeft)
        install_layout.addWidget(ptc_interest_container, alignment=Qt.AlignLeft)
        install_layout.addWidget(ptc_notes_container, alignment=Qt.AlignLeft)        
        ptc_notes_layout.addStretch(100)        

        self.setLayout(install_layout)