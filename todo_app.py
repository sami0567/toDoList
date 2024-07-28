#handles system-specific parameters - checks the script directly 
import sys
#imports UI elements for widget and broader graphical usage 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel

#creates a class that inherits QWidget properties 
class ToDoApp(QWidget):
    #initiliazing a ToDoApp object
    def __init__(self):
        #calls the constructor of the parent class - QWidget
        super().__init__()
        #Sets the title of the Window
        self.setWindowTitle("To-Do List App")
        #sets the position (100, 100) of the window and the width (400) and height (300)
        self.setGeometry(100, 100, 400, 300)
        
        #initializes an empty list for tasks
        self.tasks = []

        #creates a new layout to have the widgets arranged vertically
        self.layout = QVBoxLayout()

        #creates a text input field - allows for entering tasks
        self.input_field = QLineEdit()
        #creates a button called "Add Task"
        self.add_button = QPushButton("Add Task")
        #creates a widget to show the entered task
        self.task_list = QListWidget()
        #creates a widget to show the number of tasks in the list
        self.task_num = QLabel("Number of tasks: 0")

        #adds a widget for entering an input field to the layout
        self.layout.addWidget(self.input_field)
        #adds a button to the layout
        self.layout.addWidget(self.add_button)
        #adds a list to the layout
        self.layout.addWidget(self.task_list)
        #adds task num label to the layout
        self.layout.addWidget(self.task_num)
        
        #if the add button is clicked then the add_task method will be completed
        self.add_button.clicked.connect(self.add_task)

        self.layout.addWidget(self.task_num)

        #sets the layout for the window
        self.setLayout(self.layout)

    #new function to add task to list
    def add_task(self):
        #task being handled is the text entered in the input field
        task = self.input_field.text()

        #if there is text in the input field
        if task:
            #task is added to the task list previously initialized
            self.tasks.append(task)
            #task added to list widget and the widget shows all the tasks
            self.task_list.addItem(task)
            #clears the input field as the task in the input field has been added and handled
            self.input_field.clear()

        self.update_label()

    def update_label(self):
        #calculates the count from length of task list
        count = len(self.tasks)
        #changes the text of label to show the task count
        self.task_num.setText(f"Number of tasks: {count}")
            
#script has to be directly executed not imported
if __name__ == "__main__":
    #allows for command-line arguments to be run on PyQt application
    app = QApplication(sys.argv)
    #crates an instance of the ToDoApp class
    window = ToDoApp()
    #displays window on the screen
    window.show()
    #allowing for the application to start executing
    sys.exit(app.exec())
    #returns the exit status 
    app.exec()
    
            
        
    