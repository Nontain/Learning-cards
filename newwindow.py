from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QLabel


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets for the new window
        

        # Create layout for the new window
    
       
    def label(self):
        layout = QVBoxLayout()
        self.lable_intrebare = QLabel("Intrebare")
        self.lable_raspunsG1 = QPushButton('Raspuns gresit 1')
        self.lable_raspunsG1 = QPushButton('Raspuns gresit 2')
        self.lable_raspunsG2 = QPushButton('Raspuns gresit 3')

        # Set layout for the new window
        self.setLayout(layout)
        
        
    def set_questions(self,questions):
        self.questions_dict = questions
        self.questions_list = list(self.questions_dict.keys())
        self.changeQuestion()
        
        
    def set_questions(self,questions):
        self.questions_dict = questions
        self.questions_list = list(self.questions_dict.keys())
        self.changeQuestion()
 
 
    def changeQuestion(self):
        self.currenct_question = random.choice(self.questions_list) #alegere random
        # question = self.questions_list[0] # aceeasi ordine tot timpul
 
        self.questions_list.remove(self.currenct_question)
 
        self.lable_intrebare.setText(self.currenct_question) #alegere random
        answer_dict = self.questions_dict[self.currenct_question]
        self.r1.setText(answer_dict['answer'])
        self.r2.setText(answer_dict['answer_g1'])
        self.r3.setText(answer_dict['answer_g2'])
        self.r4.setText(answer_dict['answer_g3'])
 
 
    def check_answer(self, bt):
        answer_dict = self.questions_dict[self.currenct_question]
        if bt.text == self.questions_dict[answer_dict['answer']]:
            # popup window cu raspuns correct
            pass
        else:
            # popup window cu raspuns correct
            pass
        self.questions_list.remove(self.currenct_question)
        self.changeQuestion()
 
    def bt_1(self):
        self.check_answer(self.r1)
    def bt_2(self):
        self.check_answer(self.r2)
    def bt_3(self):
        self.check_answer(self.r3)
    def bt_4(self):
        self.check_answer(self.r4)
 
 
    def connects(self):
        self.r1.clicked.connect(self.bt_1)
        self.r2.clicked.connect(self.bt_2)
        self.r3.clicked.connect(self.bt_3)
        self.r4.clicked.connect(self.bt_4)


# Main application entry point

