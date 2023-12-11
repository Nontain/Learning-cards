from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets for the new window
        label = QPushButton("This is a New Window", self)

        # Create layout for the new window
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Set layout for the new window
        self.setLayout(layout)

# Main application entry point
