from guizero import App, Window, Text, PushButton, TextBox, Box
from time import sleep
window_width=500

app = App(title="zua", width=window_width, height=500, layout="auto", visible=True,bg="#f9d900")
app.font="Comic Sans MS"



def machschhalt():
    Ausgabe.value = eingabe.value
    Ausgabe.show()
    sleep(0.2)
    app.bg="red"
    app.update()
    sleep(0.2)
    app.bg="blue"
    app.update()
    sleep(0.2)
    app.bg="green"
    app.update()
    sleep(0.2)
    app.bg="#f9d900"
    app.update()
    return


eingabe = TextBox(app, "Suche", width=int(window_width/2), height=60, align="top", visible=True)
box = Box(app, height=60, width=window_width/2, align="top", visible=True)
PushButton(box, width="fill", align="left", visible=True, command=machschhalt, text="jscho")
PushButton(box, width="fill", align="right", visible=True, command=machschhalt, text="haltau")
noch_ne_box = Box(app, height=100, width=int(window_width/2), visible=True, align="top")
Ausgabe = Text(noch_ne_box, text="", width=int(window_width/2),align="bootm", visible=False)


app.display()