from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QCheckBox, QListView

class dashboardContainer(QWidget):
    def __init__ (self):
        super().__init__()

        container_layout = QVBoxLayout()
        filters_layout = QHBoxLayout()

        filter_container = QWidget()
        filter_container.setLayout(filters_layout)

        dashboard_label = QLabel(text="Dashboard")
        container_layout.addWidget(dashboard_label)

        today_label = QLabel(text="Today")
        container_layout.addWidget(today_label)

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

        results_list = QListView()
        container_layout.addWidget(results_list)

        self.setLayout(container_layout)