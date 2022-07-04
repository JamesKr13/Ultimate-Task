import json
from Model import *
from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class Data_Management:
    # Data Initilisation and Data Management is
    # Controlled by this class
    def __init__(self) -> None:
        self.subject_data = {}
        self.timetable = {}
        self.class_initlisation(self.data_import("Data.json"),subject)
        self.class_initlisation(self.data_import("Times"),day_time)
        
    def class_initlisation(self,data_set,class_type):
        class_list = []
        for subject in data_set.keys():
            self.subject_data[subject] = (class_type(*data_set[subject].values()))
          
    def __del__(self) -> None:
        dic= {}
        for keys in self.subject_data.keys():
            dic[keys] = vars(self.subject_data[keys])
        self.data_export("Data.json",dic)


    def data_import(self,filename) -> dict:
        with open(filename,"r+") as json_file:
            return json.load(json_file)

    def data_export(self,filename,data) -> None:
        with open(filename,"r+") as json_file:
            json_file.truncate()
            json.dump(data,filename)
        
       
class Search_by:
    # Search Methods are stored with in this class
    def attribute_with_value(self,data_set,attr_name,*args) -> list:
        print(data_set)    
        print(attr_name)    
        containing = []
        for key in data_set.keys():
            try:
                # takes the class stored in the data_set and check if attr is contained in it
                if args:
                    if getattr(data_set[key],attr_name) in args:
                        containing.append(data_set[key])
                else:
                    containing.append(data_set[key])
            except AttributeError:
                pass
        return containing

    def stored_value(self,data_set,value) -> list:
        containing = []
        for key in data_set.keys():
            if value in list(vars(data_set[key]).values()):
                containing.append(data_set[key])
        return containing

    def desired_output(self,sorted_data: list,property_type:str):
        containing = []
        for data in sorted_data:
            containing.append(getattr(data,property_type))
        return containing
        
# Source https://stackoverflow.com/questions/33450695/how-to-change-a-qlabel-to-a-qlineedit-when-mouse-pressed
class Form_Label(QLabel):
    def __init__(self,label,parent=None):
        super(Form_Label, self).__init__(parent)
        self.label = label

    def mousePressEvent(self, event) -> None:
        self.hide()
        self.label.show()
        self.label.setFocus()
@dataclass
class Controller:
    # View Parts
    talbe: QTableWidget
##    day_pick: QPushButton
##    days_subjects: list[QPushButton]
##    week_subjects: list[list[QPushButton]]
##    edit_subjects: QPushButton
##    subject_display: list[QLabel]
    data: Data_Management = Data_Management()
    Search_by: Search_by = Search_by()
    
    def view_load():
        pass
    
    def combo_set(self,box: QComboBox,output_property: str):
        box.addItems(self.Search_by.desired_output(self.Search_by.attribute_with_value(output_property)),output_property)
    
    def label_set(self,labels: list[QLabel],output_property: str,contains_value: str,) -> None:
        if contains_value:
            all_text = self.Search_by.attribute_with_value(output_property,contains_value)
        elif not contains_value:
            all_text = self.Search_by.attribute_with_value(output_property)
        all_text = self.Search_by.desired_output(all_text,output_property)
        if len(labels) == (rang := len(all_text)):
            for iternum in range(rang):
                labels[iternum].setText(all_text[iternum]) 
                
    def new_value(self,new_key,values):
        #need to change from dict to list
        self.data.subject_data[new_key] = subject(*values)
    
    def edit_values(self,altr_propertys,old_value,new_value):
        # needs to be fixed to work with get_new_value()
        alter_subjects = self.Search_by.attribute_with_value(self.data.subject_data,altr_propertys,old_value)
        for alter_subject in alter_subjects:
            setattr(alter_subject,altr_propertys, new_value)
    
    def get_new_value(self,line: QLineEdit or list[QLineEdit]) -> list or str:
        if type(line) == list:
            new_values = []
            for each_line in line:
                new_values.append(each_line.text())
            return new_values
        else:
            return line
    def set_table_data(self):
        # method redone for lists search by get attrr
        self.columnLabels = [getattr(i,"_day") for i in self.Search_by.attribute_with_value(self.data.timetable,"_day")]
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        set.rowlabels = [num for num in range(8)]
        self.table.