from guizero import App, Window, Text, PushButton, TextBox, Box
import util

DEBUG_GUI = False

class Gui:
    def __init__(self, width, height, district_list):
        self.district_list = district_list
        app = App(title="zua", width=width, height=height, layout="auto", visible=True,bg="white")
        app.font="DejaVu Sans"
        
        Text(app, text="Stadt oder Bundesland eingeben:", height=1, align="top", width="fill", visible=True)
        box_input = Box(app, width=int(width/2), height=25, align="top", visible=True, border=DEBUG_GUI)
        self.input_field = TextBox(box_input, width="fill", align="top", visible=True)
        
        box_content = Box(app, width=int(width/2), height=400, align="top", visible=True, border=DEBUG_GUI)
        box_left = Box(box_content, width=int(width/4), height=400, align="left", visible=True, border=DEBUG_GUI)
        box_right = Box(box_content, width=int(width/4), height=400, align="left", visible=True, border=DEBUG_GUI)
        PushButton(box_left, width="fill", align="top", visible=True, command=self.get_pos_pred, text="Positive Predictive")
        PushButton(box_right, width="fill", align="top", visible=True, command=self.get_neg_pred, text="Negative Predictive")
        self.tx_left_district = Text(box_left, width="fill", align="top", visible=True, text="")
        self.tx_left_value = Text(box_left, width="fill", align="top", visible=True, text="")
        self.tx_right_district = Text(box_right, width="fill", align="top", visible=True, text="")
        self.tx_right_value = Text(box_right, width="fill", align="top", visible=True, text="")

        app.display()

    def get_pos_pred(self):
        district = next((x for x in self.district_list if x.name == self.input_field.value), None)
        self.tx_left_district.value = district.name
        self.tx_left_value.value = util.positive_predictive_value(district)

    def get_neg_pred(self):
        district = next((x for x in self.district_list if x.name == self.input_field.value), None)
        print(util.negative_predictive_value(district))
        self.tx_right_district.value = district.name
        self.tx_right_value.value = util.negative_predictive_value(district)

 