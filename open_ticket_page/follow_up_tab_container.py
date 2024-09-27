from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QCheckBox, QLineEdit, QTabWidget, QDateEdit, QTimeEdit, QComboBox, QTextEdit, QFormLayout
from PySide6.QtCore import QDate, QTime
from PySide6.QtCore import Qt

class followUpTabContainer(QWidget):
    def __init__ (self, dbItem):
        super().__init__()

        print(f"{dbItem} in Follow Up tab container")

        follow_up_layout = QHBoxLayout()
        follow_up_container = QWidget()
        follow_up_container.setLayout(follow_up_layout)

        #    ---- Follow Up Details ----
        follow_up_details_layout = QVBoxLayout()
        follow_up_details_container = QWidget()
        follow_up_details_container.setLayout(follow_up_details_layout)

        #     Follow Up Details Title
        follow_up_details_label = QLabel(text="Follow Up Details")
        follow_up_details_label.setObjectName("3rdTitle")
        follow_up_details_layout.addWidget(follow_up_details_label)

        #     Follow Up Details Form Layout
        follow_up_details_form_layout = QFormLayout()
        follow_up_form_container = QWidget()
        follow_up_form_container.setLayout(follow_up_details_form_layout)
        
        #     1st Follow Up Details Date
        follow_up_1_date_checkbox = QCheckBox(text="1st Follow Up:")
        follow_up_1_date_input = QDateEdit(date=QDate.fromString(dbItem['date'], "MM/dd/yyyy"))
        follow_up_1_date_input.setCalendarPopup(True)
        follow_up_1_date_input.setDisplayFormat("MM/dd/yyyy")
    
        #     2nd Follow Up Details Date
        follow_up_2_date_checkbox = QCheckBox(text="2nd Follow Up:")
        follow_up_2_date_input = QDateEdit(date=QDate.fromString(dbItem['date'], "MM/dd/yyyy").addDays(7))
        follow_up_2_date_input.setCalendarPopup(True)
        follow_up_2_date_input.setDisplayFormat("MM/dd/yyyy")

        #     3rd Follow Up Details Date
        follow_up_3_date_checkbox = QCheckBox(text="3rd Follow Up:")
        follow_up_3_date_input = QDateEdit(date=QDate.fromString(dbItem['date'], "MM/dd/yyyy").addDays(14))
        follow_up_3_date_input.setCalendarPopup(True)
        follow_up_3_date_input.setDisplayFormat("MM/dd/yyyy")

        #     Add follow up Details to Form Layout
        follow_up_details_form_layout.addRow(follow_up_1_date_checkbox, follow_up_1_date_input)
        follow_up_details_form_layout.addRow(follow_up_2_date_checkbox, follow_up_2_date_input)
        follow_up_details_form_layout.addRow(follow_up_3_date_checkbox, follow_up_3_date_input)

        #     Add follow_up Details Container to PTC Details Layout
        follow_up_details_layout.addWidget(follow_up_form_container, alignment=Qt.AlignTop)
        follow_up_details_layout.addStretch(100)

        #    ---- Follow Up Comments ----
        follow_up_comments_layout = QVBoxLayout()
        follow_up_comments_container = QWidget()
        follow_up_comments_container.setLayout(follow_up_comments_layout)

        follow_up_comments_form_layout = QFormLayout()
        follow_up_comments_form_container = QWidget()
        follow_up_comments_form_container.setLayout(follow_up_comments_form_layout)

        #     Follow Up Comments Title
        ptc_interest_label = QLabel(text="PTC Interest")
        ptc_interest_label.setObjectName("3rdTitle")
        follow_up_comments_layout.addWidget(ptc_interest_label)

        #     Follow Up Comments Notes
        follow_up_details_label = QLabel(text="Comments:")
        ptc_details_input = QTextEdit(text="Evaluation scope: \nDeployment: Windows Application / Slingshot / BlockBox\nEndpoints: ")

        #     Add Follow Up Comments to Form Layout
        follow_up_comments_form_layout.addRow(follow_up_details_label)
        follow_up_comments_form_layout.addRow(ptc_details_input)

        #     Add Follow Up Comments Container to PTC Interest Layout
        follow_up_comments_layout.addWidget(follow_up_comments_form_container, alignment=Qt.AlignTop)
        follow_up_comments_layout.addStretch(100)

        #    ---- Follow Up Notes ----
        follow_up_notes_layout = QVBoxLayout()
        follow_up_notes_container = QWidget()
        follow_up_notes_container.setLayout(follow_up_notes_layout)

        follow_up_notes_label = QLabel(text="Notes")
        follow_up_notes_label.setObjectName("3rdTitle")
        follow_up_notes_layout.addWidget(follow_up_notes_label)

        follow_up_note_1 = QLabel(text=f"B64 - 1st email Follow Up Sent")
        follow_up_notes_layout.addWidget(follow_up_note_1, alignment=Qt.AlignTop)

        follow_up_note_2 = QLabel(text=f"B64 - 2nd email Follow Up Sent")
        follow_up_notes_layout.addWidget(follow_up_note_2)

        follow_up_note_3 = QLabel(text=f"B64 - 3rd email Follow Up Sent")
        follow_up_notes_layout.addWidget(follow_up_note_3)

        follow_up_note_4 = QLabel(text=f"Ticket {dbItem['sas_ticket']} closed, not interested after 3 follow ups.")
        follow_up_notes_layout.addWidget(follow_up_note_4)
  
        follow_up_layout.addWidget(follow_up_details_container, alignment=Qt.AlignLeft)
        follow_up_layout.addWidget(follow_up_comments_container, alignment=Qt.AlignLeft)
        follow_up_layout.addWidget(follow_up_notes_container, alignment=Qt.AlignLeft)
               
        follow_up_notes_layout.addStretch(100)
        self.setLayout(follow_up_layout)