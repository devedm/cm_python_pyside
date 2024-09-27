from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QCheckBox, QTableWidget, QTableWidgetItem, QApplication
import model_view_controller
from open_ticket_page.open_ticket_container import openTicketContainer

class ticketsContainer(QWidget):
    def __init__ (self):
        super().__init__()

        container_layout = QVBoxLayout()
        filters_layout = QHBoxLayout()

        filter_container = QWidget()
        filter_container.setLayout(filters_layout)

        dashboard_label = QLabel(text="Tickets")
        container_layout.addWidget(dashboard_label)

        container_layout.addWidget(filter_container)

        pending_checkbox = QCheckBox(text="Completed")
        filters_layout.addWidget(pending_checkbox)

        ptc_checkbox = QCheckBox(text="PTC")
        filters_layout.addWidget(ptc_checkbox)
        
        install_checkbox = QCheckBox(text="Install")
        filters_layout.addWidget(install_checkbox)

        report_checkbox = QCheckBox(text="Report Delivery")
        filters_layout.addWidget(report_checkbox)

        filter_button = QPushButton(text="Filter")
        filters_layout.addWidget(filter_button)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(6)
        self.results_table.setColumnWidth(0,150)
        self.results_table.setColumnWidth(1,150)
        self.results_table.setColumnWidth(2,150)
        self.results_table.setColumnWidth(3,150)
        self.results_table.setColumnWidth(4,150)
        self.results_table.setColumnWidth(5,150)

        self.results_table.setHorizontalHeaderLabels(["Company Name", "SAS Ticket", "MSX Ticket", "Status", "Date", "Time"])

        container_layout.addWidget(self.results_table)

        load_data_button = QPushButton(text="Load Data")
        load_data_button.clicked.connect(self.read_tickets)
        container_layout.addWidget(load_data_button)

        self.setLayout(container_layout)
        self.read_tickets()
                
    def read_tickets(self):
        self.results_table.setRowCount(0)
        controller = model_view_controller.ModelSQLite()
        for ticket in controller.read_items():
            print(ticket)       
            row_position = self.results_table.rowCount()
            self.results_table.insertRow(row_position)
            self.results_table.setItem(row_position, 0, QTableWidgetItem(ticket['company']))
            self.results_table.setItem(row_position, 1, QTableWidgetItem(ticket['sas_ticket']))
            self.results_table.setItem(row_position, 2, QTableWidgetItem(ticket['msx_ticket']))
            self.results_table.setItem(row_position, 3, QTableWidgetItem(ticket['status']))
            self.results_table.setItem(row_position, 4, QTableWidgetItem(ticket['date']))
            self.results_table.setItem(row_position, 5, QTableWidgetItem(ticket['time']))
        self.results_table.cellClicked.connect(self.select_row)
    
    def select_row(self, row, column):
        item = self.results_table.item(row, 0).text()
        print(f"Row {row} and Column {column} was clicked with value {item}.")
        controller = model_view_controller.ModelSQLite()
        dbItem = controller.read_item(company=item)
        print(f"Retrieved {dbItem}")
        self.open_ticket_page(dbItem)

    def open_ticket_page(self, dbItem):
        print("Opening Ticket Page")
        self.new_widget = openTicketContainer(dbItem)
        self.new_widget.show()
        
        

        

