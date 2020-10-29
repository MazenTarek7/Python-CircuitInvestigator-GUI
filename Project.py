from tkinter import*
from tkinter.ttk import*
from tkinter import ttk
from PIL import Image,ImageTk
import SchemDraw as schem
import SchemDraw.elements as e
new = Tk()
new.title("Circuit Investigator")
new.geometry('1000x500+150+75')
new.configure(bg='#49A')
#Background = Label(new,text="Circuit Investigator",font=("arial",35,"bold"),background='#49A')
#Background.config(anchor = CENTER)
#Background.pack()
new.iconbitmap('Electronics-logo-2.ico')
img_src = Image.open("MainImage4.jpeg").resize((1000,500))
img = ImageTk.PhotoImage(img_src)
Background=Label(new,image=img,background = '#163149')
Background.pack()
x = 0
Rc= 0
Cc = 0
y = 0 
r = 0
totalR = 0
totalRp = 0
totalC = 0
dComponentR = ''
dComponentC = ''
dComponentW = ''
dComponentV = ''
eComponent = ''
textbox = 0
addingR = 0
addingC = 0
addingV = 0
addingW = 0
textbox = 0
Res=[0,0,0,0,0]
Cap=[0,0,0,0,0]
############################################ Main Window
def quitting():
    exit()
def helping():
    global window, page , pagee , pageee , page_list , Next_button , previous_button , Quit_button , main_label
    window = Tk()
    window.geometry('1000x500+150+100')
    window.configure(bg='#49A')
    window.title('Circuit Investigator Documentation')
    window.iconbitmap('Electronics-logo-2.ico')
    page = "\t\t\t    Welcome to Circuit Investigator's help menu!\nTo get started go to the main window titled (Circuit Investiagtor) and click on the start button to proceed with the circuit\nanalysis, you will be greeted with a new window titled (Create a Circuit), first you start off by entering the voltage value\nand selecting its unit of measurement then choose your desired connection method (Series or Parallel) from the drop \ndown menu, then click on the add a component button a drop down menu will appear containing 2 components (R or C)\nChoose the component you want and enter its value and unit of measurement when you are done with inputs, press on\nthe confirm component button to save the values in the memory then repeat the process if you want to add more\ncomponents when you are all done click on the calculate button to get the (Total Capacitance,Current & Resistance)\nYou can also click on the draw button in the same window to draw a circuit of your own, after you have pressed the\nbutton a new window will appear with 4 buttons and a selection box to choose your components and four buttons for\ncomponent orientation first you start off by choosing a component from the selection box and then you choose the\norientation from one of the four buttons and then click the confirm button to save your choices, repeat this process until\nyou are satisfied with your design finally click on the draw button to draw the circuit you chose"
    pagee ="\t\t\t\t    Series & Parallel Circuits\nWhat Is a Series Connection?\nComponents connected in series are connected along a single conductive path, so the same current flows through all\nof the components but voltage is dropped (lost) across each of the resistances. In a series circuit, the sum of the\nvoltages consumed by each individual resistance is equal to the source voltage.In a series circuit, the current that flows\nthrough each of the components is the same, and the voltage across the circuit is the sum of the individual voltage drops\nacross each component.\nWhat Is a Parallel Connection?\nThe basic idea of a “parallel” connection, on the other hand, is that all components are connected across each other’s\nleads. Components connected in parallel are connected along multiple paths so that the current can split up; the same\nvoltage is applied to each component.In a parallel circuit, the voltage across each of the components is the same, and\nthe total current is the sum of the currents flowing through each component.\n"
    pageee ="\t\t\t\t    Active & Passive Components\nActive Components: An active component is an electronic component which supplies energy to a circuit. Common\nexamples of active components include:\n1-Voltage sources: A voltage source is an example of an active component in a circuit. When current leaves from the\npositive terminal of the voltage source, energy is being supplied to the circuit.\n2-Current sources: A current source is also considered an active component. The current supplied to the circuit by an\nideal current source is independent of circuit voltage.\nAs a current source is controlling the flow of charge in a circuit, it is classified as an active element.\n3-All different types of transistors (such as bipolar junction transistors, MOSFETS): Although not as obvious as a\ncurrent or voltage sourcetransistors are also an active circuit component. This is because transistors are able to amplify\nthe power of a signal\nPassive Components: A passive component is an electronic component which can only receive energy Passive\nelements do not need any form of electrical power to operate.\nCommon examples of passive components include:\n1-Resistors: A resistor can only receive energy which they can dissipate as heat as long as current flows through it.\n2-Inductors: An inductor is also considered as passive element of circuit, because it can store energy in it as a magnetic\nfield, and can deliver that energy to the circuit, but not in continuous basis.\n3-Capacitors: A capacitor is considered as a passive element because it can store energy in it as electric field.\n"
    page_list = [page,pagee,pageee]
    main_label = Label(window,text = page , font = ("arial",14),background = '#49A')
    main_label.grid(column=0,row=3)
    ################################################################################ Buttons
    Next_button = Button(window, text = ">>",width=20,command = lambda:forward(2))
    Next_button.place(x=590,y=450)
    Quit_button = Button(window,text="Close Window",width=20,command = helpQuit)
    Quit_button.place(x=440,y=450)
    previous_button = Button(window,text="<<",width=20,command = back)
    previous_button.configure(state = DISABLED)
    previous_button.place(x=290,y=450)
    window.resizable(0 , 0)
def forward(page_number):
    global window , main_label , Next_button , previous_button , Quit_button
    main_label.grid_forget()
    main_label = Label(window,text=page_list[page_number-1],font = ("arial",14),background = '#49A')
    main_label.grid(column=0,row=3)    
    Next_button = Button(window, text=">>",width=20,command = lambda:forward(page_number+1))
    Next_button.place(x=590,y=450)
    if page_number == 3:
        Next_button.configure(state = DISABLED)

    previous_button = Button(window,text="<<",width=20,command = lambda:back(page_number-1))
    previous_button.place(x=290,y=450)

def back(page_number):
    global window , main_label , Next_button , previous_button , Quit_button
    main_label.grid_forget()
    main_label = Label(window,text=page_list[page_number-1], font = ("arial",14),background = '#49A')
    main_label.grid(column=0,row=3)

    Next_button = Button(window, text=">>",width=20,command = lambda:forward(page_number+1))
    Next_button.place(x=590,y=450)


    previous_button = Button(window,text="<<",width=20,command = lambda:back(page_number-1))
    previous_button.place(x=290,y=450)
    if page_number == 1:
        previous_button.configure(state = DISABLED)
def helpQuit():
    window.destroy()


def Drop_Components():
    global x , y , Components 
    #x = x+ 100
    y = y + 60
    Components_choice = Label(start,text="Component:",background = '#49A',font=("arial",9,"bold"))
    Components_choice.place(x=0,y=y)
    options = [
        "R", "C"
        
    ]

    Components = ttk.Combobox(start, value=options,width=15)
    Components.current(0)
    Components.bind("<<ComboboxSelected>>", comboclcik)
    Components.place(x=73,y=y)
def starting():
    global start , Battery , BatteryUnit , SeriesParallel , SeriesParallelOption
    start = Tk()
    start.state('zoomed')
    start.configure(bg='#49A')
    start.title('Create a ciruit')
    start.iconbitmap('Electronics-logo-2.ico')
    ###################################################### Start Window
    menu2 = Menu(start)
    start.config(menu=menu2)
    file2 = Menu(menu2 , tearoff = False)
    file2.add_command(label='New File', command = starting)
    newFile2 = Menu(menu2 , tearoff = False)
    file2.add_command(label='Quit Program', command = quitting)
    menu2.add_cascade(label='File', menu=file)
    help2 = Menu(menu2 , tearoff = False)
    help2.add_command(label='Help',command = helping)
    menu2.add_cascade(label='Help' , menu = help)
    ###################################################### Start window menu
    Battery = Entry(start,width=12)
    Battery_Value = Label(start,text="Please enter the voltage:",background = '#49A',font=("arial",11,"bold"))
    Battery_Value.place(x=0,y=0)
    Battery.place(x=180,y=0)
    Voolt = Label(start, text="Volt",background = '#49A',font=("arial",11,"bold"))
    Voolt.place(x=350,y=0)
    BatteryUnit = Combobox(start)
    BatteryUnit['values'] = ("m","μ","k","M","Volt")
    BatteryUnit.set("Select Unit")
    BatteryUnit.place(x=255,y=0)
    BatteryUnit.configure(width=12)
    SeriesParallelOption= ["Series" , "Parallel"]
    SeriesParallel = ttk.Combobox(start, value=SeriesParallelOption,width=10)
    SeriesParallel.place(x=925,y=550)
    ######################################################## Battery
    Add = Button(start, text="Add a component",width=20,command = Drop_Components)
    Add.place(x=750,y=600) 
    drawCircuit = Button(start, text = "Draw Circuit",width = 20, command = CircuitAnalysis)
    drawCircuit.place(x=1050,y=600)
    Value = Button(start, text = "Calculate",width = 20, command = Calculate)
    Value.place(x=900,y=600)
    ######################################################## Buttons
def CircuitAnalysis():
    global Componentsdraw
    analysis = Tk()
    analysis.geometry('1000x500+150+100')
    analysis.title('Draw your circuit')
    analysis.configure(bg='#49A')
    analysis.iconbitmap('Electronics-logo-2.ico')
    analysis.resizable(0,0)
    Upbutton = Button(analysis,text = "Up", width = 30, command = UP)
    Upbutton.place(x=400,y=200)
    Downbutton = Button(analysis,text = "Down", width = 30, command = DOWN)
    Downbutton.place(x=400,y=300)
    Rightbutton = Button(analysis,text = "Right", width = 30, command = RIGHT)
    Rightbutton.place(x=500,y=250)
    Leftbutton = Button(analysis,text = "Left", width = 30, command = LEFT)
    Leftbutton.place(x=300,y=250)
    Components_choice = Label(analysis,text="Component:",background = '#49A',font=("arial",9,"bold"))
    Components_choice.place(x=2,y=40)
    options = ["Resistor", "Capacitor", "DC Voltage","Wire"]
    Componentsdraw = ttk.Combobox(analysis, value=options,width=15)
    Confirmbutton = Button(analysis, text = "Confirm",command = confirm)
    Confirmbutton.place(x=20,y=100)
    #Components.current(0)
    Componentsdraw.place(x=80,y=40)
    Check = Button(analysis, text = "Draw", width = 25, command = Draw)
    Check.place(x= 400, y = 450)
def UP():
    global dComponentR, dComponentC, dComponentV, dComponentW ,Componentsdraw
    if(Componentsdraw.get()=="Resistor"):
        dComponentR = 'up'
        return dComponentR
    if(Componentsdraw.get()=="Capacitor"):
        dComponentC = 'up'
        return dComponentC
    if(Componentsdraw.get()=="DC Voltage"):
        dComponentV = 'up'
        return dComponentV
    if(Componentsdraw.get()=="Wire"):
        dComponentW = 'up'
        return dComponentW
def DOWN():
    global dComponentR, dComponentC, dComponentV, dComponentW ,Componentsdraw
    if(Componentsdraw.get()=="Resistor"):
        dComponentR = 'down'
        return dComponentR
    if(Componentsdraw.get()=="Capacitor"):
        dComponentC = 'down'
        return dComponentC
    if(Componentsdraw.get()=="DC Voltage"):
        dComponentV = 'down'
        return dComponentV
    if(Componentsdraw.get()=="Wire"):
        dComponentW = 'down'
        return dComponentW
def RIGHT():
    global dComponentR, dComponentC, dComponentV, dComponentW ,Componentsdraw
    if(Componentsdraw.get()=="Resistor"):
        dComponentR = 'right'
        return dComponentR
    if(Componentsdraw.get()=="Capacitor"):
        dComponentC = 'right'
        return dComponentC
    if(Componentsdraw.get()=="DC Voltage"):
        dComponentV = 'right'
        return dComponentV
    if(Componentsdraw.get()=="Wire"):
        dComponentW = 'right'
        return dComponentW
def LEFT():
    global dComponentR, dComponentC, dComponentV, dComponentW ,Componentsdraw
    if(Componentsdraw.get()=="Resistor"):
        dComponentR = 'left'
        return dComponentR
    if(Componentsdraw.get()=="Capacitor"):
        dComponentC = 'left'
        return dComponentC
    if(Componentsdraw.get()=="DC Voltage"):
        dComponentV = 'left'
        return dComponentV
    if(Componentsdraw.get()=="Wire"):
        dComponentW = 'left'
        return dComponentW
    ############################################################## circuitAnalysis Function
def confirm():
    global Componentsdraw,addingR,addingC,addingV,addingW
    if(Componentsdraw.get()=="Resistor"):
        addingR = addingR + 1
        print(addingR)
        return addingR
    if(Componentsdraw.get()=="Capacitor"):
        addingC = addingC + 1
        print(addingC)
        return addingC
    if(Componentsdraw.get()=="DC Voltage"):
        addingV = addingV + 1
        print(addingV)
        return addingV
    if(Componentsdraw.get()=="Wire"):
        addingW = addingW + 1
        print(addingW)
        return addingW


def Draw():
    global dComponentR,dComponentC, dComponentV, dComponentW, addingR,addingC,addingV,addingW
    d = schem.Drawing(color='black')
    for i in range(addingR):
        d.add(e.RES, d =str(dComponentR))
    for i in range(addingC):
        d.add(e.CAP, d =str(dComponentC))
    for i in range(addingV):
        d.add(e.SOURCE_V, d =str(dComponentV))
    for i in range(addingW):
        d.add(e.LINE, d =str(dComponentW))
    d.add(e.GND)
    d.draw()
    d.save('schematic.eps')
    ################################### Draw Function
def Calculate():
    global SeriesParallel , totalR , answerCurrent , answerR , answerI , answerC , totalC
    VoltUnit = BatteryUnit.get()
    Volt = float(Battery.get())  
    if (VoltUnit == "Volt"):
        Volt = Volt*1
    elif (VoltUnit == "m"):
        Volt = Volt*10**-3
    elif (VoltUnit == "μ"):
        Volt = Volt*10**-6
    elif (VoltUnit == "k"):
        Volt = Volt*10**3
    elif (VoltUnit == "M"):
        Volt = Volt*10**6
    print(Volt)
    if(SeriesParallel.get()=="Parallel" and Components.get()=='R'):
        totalR = 1/totalR
        answerR = totalR
    elif (SeriesParallel.get()=="Series" and Components.get()=='C'):
        totalC = 1/totalC
        answerC = totalC
        answerR = totalR
    elif (SeriesParallel.get()=="Parallel" and Components.get()=='C'):
        answerC = totalC
        answerR = 1/totalR
    answerI = Volt/answerR
    ############################################################## Calculations
    CurrentValue = Label(start,text=answerI,background ='#49A',font=("arial",10,"bold"))
    CurrentValue.place(x=1000,y=300)
    CurrentLabel = Label(start,text="Total Current:",background='#49A',font=("arial",10,"bold"))
    CurrentLabel.place(x=900,y=300)
    ResistanceValue = Label(start,text=answerR,background='#49A',font=("arial",10,"bold"))
    ResistanceValue.place(x=1025,y=200)
    ResistanceLabel = Label(start,text="Total Resistance:",background='#49A',font=("arial",10,"bold"))
    ResistanceLabel.place(x=900,y=200)
    CapacitanceValue = Label(start,text=answerC,background ='#49A',font=("arial",10,"bold"))
    CapacitanceValue.place(x=1025,y=400)
    CapacitanceLabel = Label(start,text="Total Capacitance:",background ='#49A',font=("arial",10,"bold"))
    CapacitanceLabel.place(x=900,y=400)
    ############################################################## Labels
    print("Total Current:",answerI)
    print("Total Resistance:",totalR)
    #################################### Battery If Function  
def comboclcik (event):
    global r , q , uinput , units, Components, unit
    unit = ''
    if(Components.get()=="R"):
        unit = 'Ω'
    elif(Components.get()=="C"):
        unit = 'F'
    #yarab = Components.get()
    #print(yarab)
    r = r + 60
    Value = Label(start,text="Value:",background='#49A',font=("arial",10,"bold"))
    Value.place(x=250,y=r)
    Unit = Label(start,text="  Unit:",background = '#49A',font=("arial",10,"bold"))
    Unit.place(x=440,y=r)
    uinput = Entry(start,width=10)
    uinput.place(x=295,y=r)
    unitsOptions = [
        "m"+unit,"μ"+unit,"k"+unit,"M"+unit,unit
    ]
    units = ttk.Combobox(start, value=unitsOptions,width=10)
    #units.current(0)
    #units.bind("<<ComboboxSelected>>", comboclcik)
    units.place(x=480,y=r)
    yalla = Button(start, text="Confirm Component",width=20,command = lists)
    yalla.place(x=600,y=600) 
    #Res[q] = uinput.get() 
    #q = q + 1
    #for x in range(len(Res)):
        #print (Res[x])
def lists():
    global uinput , Rc ,Cc , textbox , Unit , unit, SeriesParallel , totalR , totalC
    if(Components.get()=='R'):
        textbox = float(uinput.get())
        Unit = units.get()
        print("Unit picked is:",Unit)
        if(SeriesParallel.get()=="Series"):
            if (Unit == "m"+unit):
                textbox = textbox*10**-3
            elif (Unit == "μ"+unit):
                textbox = textbox*10**-6
            elif (Unit == "k"+unit):
                textbox = textbox*10**3
            elif (Unit == "M"+unit):
                textbox = textbox*10**6
            elif (Unit == unit):
                textbox = textbox*1
            totalR += textbox
            print("Total Resistance:",totalR)
        elif(SeriesParallel.get()=="Parallel"):
            if (Unit == "m"+unit):
                textbox = textbox*10**-3
                textbox = 1/textbox
            elif (Unit == "μ"+unit):
                textbox = textbox*10**-6
                textbox = 1/textbox
            elif (Unit == "k"+unit):
                textbox = textbox*10**3
                textbox = 1/textbox
            elif (Unit == "M"+unit):
                textbox = textbox*10**6
                textbox = 1/textbox
            elif (Unit == unit):
                textbox = textbox*1
                textbox = 1/textbox
            totalR += textbox
            print("Total Resistance:",totalR)       
        Res[Rc]= textbox
        Rc = Rc + 1
        for x in range(len(Res)):
            print (Res[x])
    elif(Components.get()=='C'):
        textbox = float(uinput.get())
        Unit = units.get()
        print("Unit picked:",Unit)
        if(SeriesParallel.get()=="Parallel"):
            if (Unit == "m"+unit):
                textbox = textbox*10**-3
            elif (Unit == "μ"+unit):
                textbox = textbox*10**-6
            elif (Unit == "k"+unit):
                textbox = textbox*10**3
            elif (Unit == "M"+unit):
                textbox = textbox*10**6
            elif (Unit == unit):
                textbox = textbox*1
            totalC += textbox
            print("Total Capacitance:",totalC)
        elif(SeriesParallel.get()=="Series"):
            if (Unit == "m"):
                textbox = textbox*10**-3
                textbox = 1/textbox
            elif (Unit == "μ"+unit):
                textbox = textbox*10**-6
                textbox = 1/textbox
            elif (Unit == "k"+unit):
                textbox = textbox*10**3
                textbox = 1/textbox
            elif (Unit == "M"):
                textbox = textbox*10**6
                textbox = 1/textbox
            elif (Unit == unit):
                textbox = textbox*1
                textbox = 1/textbox
            totalC += textbox
            print("Total Capacitance:",totalC)      
        Cap[Cc] = textbox
        Cc = Cc + 1
        for x in range(len(Res)):
            print (Cap[x])                            
############################################ Functions
menu = Menu(new)
new.config(menu=menu)
############################################ Menu 
file = Menu(menu , tearoff = False)
file.add_command(label='New File', command = starting)
newFile = Menu(menu , tearoff = False)
file.add_command(label='Quit Program', command = quitting)
menu.add_cascade(label='File', menu=file)
help = Menu(menu , tearoff = False)
help.add_command(label='Help',command = helping)
menu.add_cascade(label='Help' , menu = help)
############################################ Menus Items
Start_button = Button(new, text="Start",width=20,command = starting)
Start_button.place(x=290,y=450)
Quit_button = Button(new,text="Quit",width=20,command = quitting)
Quit_button.place(x=440,y=450)
Help_button = Button(new,text="Help",width=20,command = helping)
Help_button.place(x=590,y=450)
new.resizable(0 , 0)
new.mainloop()