import time
from tkinter import *
from tkinter.font import BOLD

start = Tk()
weightis = 1350
heightis = 870
start.geometry(f"{weightis}x{heightis}")
start.title("Countdown Timer")
day, hour, mint, secd  = 0, 0, 0, 0
fontstyletext = ("Ubuntu", 130, "bold")
val = 'START'
stopTime = False
againCall = 0


def incdaynum():
    """Increase one number of the time while clicking on the button of day"""
    global day
    day += 1
    backColorGray.create_oval(75,220,295,440, fill="#222222", outline="white", width=2.5)
    dayInStrI = str(day).zfill(2)
    backColorGray.create_text(186, 330, text=dayInStrI,fill="#00FF00", font=fontstyletext)
 
 
def inchournum():
    """Increase one number of the time while clicking on the button of hour"""
    global hour
    hour += 1
    backColorGray.create_oval(395,220,615,440, fill="#222222", outline="white", width=2.5)
    if(hour>=24):
        for runIndipendTime in range(True):
            hour = hour-24
            if(hour<=24):break
    hourInStrI = str(hour).zfill(2)
    backColorGray.create_text(505, 330, text=hourInStrI,fill="#00FF00", font=fontstyletext)

def incmintnum():
    """Increase one number of the time while clicking on the button of minute"""
    global mint
    mint += 1
    backColorGray.create_oval(725,220,945,440, fill="#222222", outline="white", width=2.5)
    if(mint>=60):
        for runIndipendTime in range(True):
            mint = mint-60
            if(mint<=60):break
    mintInStrI = str(mint).zfill(2)
    backColorGray.create_text(836, 330, text=mintInStrI,fill="#00FF00", font=fontstyletext)

def incsendnum():
    """Increase one number of the time while clicking on the button of second"""
    global secd
    secd += 1
    backColorGray.create_oval(1045,220,1265,440, fill="#222222", outline="white", width=2.5)
    if(secd>=60):
        for runIndipendTime in range(True):
            secd = secd-60
            if(secd<=60):break
    secdInStrI = str(secd).zfill(2)
    backColorGray.create_text(1156, 330, text=secdInStrI,fill="#00FF00", font=fontstyletext)




def decdaynum():
    """Decrease one number of the time while clicking on the button of day"""
    global day
    day -= 1
    backColorGray.create_oval(75,220,295,440, fill="#222222", outline="white", width=2.5)
    if(day<0):day = day-day
    if(day>=0):
        dayInStrD = str(day).zfill(2)
        backColorGray.create_text(186, 330, text=dayInStrD,fill="#00FF00", font=fontstyletext)
 
def dechournum():
    """Decrease one number of the time while clicking on the button of hour"""
    global hour
    hour -= 1
    backColorGray.create_oval(395,220,615,440, fill="#222222", outline="white", width=2.5)
    if(hour<0):
        for runIndipendTime in range(True):
            if(hour<-24):
                hour = hour+24
        hour = 24+hour
    hourInStrD = str(hour).zfill(2)
    backColorGray.create_text(505, 330, text=hourInStrD,fill="#00FF00", font=fontstyletext)

def decmintnum():
    """Decrease one number of the time while clicking on the button of minute"""
    global mint
    backColorGray.create_oval(725,220,945,440, fill="#222222", outline="white", width=2.5)
    mint -= 1
    if(mint<0):
        for runIndipendTime in range(True):
            if(mint<-60):
                mint = mint+60
        mint = 60+mint
    mintInStrD = str(mint).zfill(2)
    backColorGray.create_text(836, 330, text=mintInStrD,fill="#00FF00", font=fontstyletext)

def decsendnum():
    """Decrease one number of the time while clicking on the button of second"""
    global secd
    backColorGray.create_oval(1045,220,1265,440, fill="#222222", outline="white", width=2.5)
    secd -= 1
    if(secd<0):
        for runIndipendTime in range(True):
            if(secd<-60):
                secd = secd+60
        secd = 60+secd
    secdInStrD = str(secd).zfill(2)
    backColorGray.create_text(1156, 330, text=secdInStrD,fill="#00FF00", font=fontstyletext)



def timeStop():
    """stop the time while click stop button"""
    for t in range(10):
        time.sleep(1)
        print("stoptime : ",t)
    return 0 

def resetTime():
    """it will doing reset the time(set all time = 0) while clicking the reset button"""
    global day, hour, mint, secd
    day, hour, mint, secd = 0, 0, 0, 0


def countDown(day,hour, mint, secd):
    """countdown timer function(Main): performing countdown on a given time."""
    global stopTime, againCall
    stopTime = False
    againCall = 0
    print(f"The set time is => {day, hour, mint, secd}")
    for day in range(day,-1,-1):
        backColorGray.create_oval(75,220,295,440, fill="#222222", outline="white", width=2.5)
        backColorGray.create_text(186, 330, text=str(day).zfill(2),fill="#00FF00", font=fontstyletext)                    
        for hour in range(hour,-1,-1):
            backColorGray.create_oval(395,220,615,440, fill="#222222", outline="white", width=2.5)
            backColorGray.create_text(505, 330, text=str(hour).zfill(2),fill="#00FF00", font=fontstyletext)
            for mint in range(mint,-1,-1):
                backColorGray.create_oval(725,220,945,440, fill="#222222", outline="white", width=2.5)
                backColorGray.create_text(836, 330, text=str(mint).zfill(2),fill="#00FF00", font=fontstyletext) 
                for secd in range(secd,-1,-1):
                    if(againCall>0 and secd!=0):break
                    backColorGray.create_oval(1045,220,1265,440, fill="#222222", outline="white", width=2.5)                    
                    backColorGray.create_text(1156, 330, text=str(secd).zfill(2),fill="#00FF00", font=fontstyletext)
                    backColorGray.update()   
                    time.sleep(0.001)
                    print("hellow",secd)
                    if(timeStop == True):
                        timeStop()                        
                    if((day==0) and (hour==0) and (mint==0) and (secd==0)):
                        againCall += 1 
                        stopTime = True
                        break
                if(stopTime):break
                secd=59
            if(stopTime):break
            mint=59
        if(stopTime):break
        hour=23
    resetTime()


if __name__=='__main__':
    backColorGray = Canvas(start, width=weightis, height=heightis)
    backColorGray.create_rectangle(0, 0, weightis, heightis, fill="#222222")
    backColorGray.create_text(666, 70, text="COUNTDOWN TIMER",fill="#FA0000", font=("Ubuntu", 40, "bold"))
    fontstylecolon = ("Comic Sans MS", 140, "bold")
    backColorGray.create_text(666, 315, text="  :   :   :  ",fill="white", font=fontstylecolon)
    backColorGray.pack(fill=BOTH, expand=True)
    backColorGray.create_oval(75,220,295,440, fill="#222222", outline="white", width=2.5)
    backColorGray.create_oval(395,220,615,440, fill="#222222", outline="white", width=2.5)
    backColorGray.create_oval(725,220,945,440, fill="#222222", outline="white", width=2.5)
    backColorGray.create_oval(1045,220,1265,440, fill="#222222", outline="white", width=2.5)

    #upper button for increasing the value of number(setTime)
    upIcon = PhotoImage(file=r"C:\\Users\\Kunal\Desktop\\all intresting movies\\programming\\Python\\Countdown Timer\\colokicon.png")
    upIconImage = upIcon.subsample(1, 1)
    buttonDayI = Button(backColorGray, command=incdaynum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=upIconImage, borderwidth=1)
    buttonHourI = Button(backColorGray, command=inchournum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=upIconImage, borderwidth=1)
    buttonMinI = Button(backColorGray, command=incmintnum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=upIconImage, borderwidth=1)
    buttonSecI = Button(backColorGray, command=incsendnum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=upIconImage, borderwidth=1)
    buttonDayI.place(x=112,y=191)
    buttonHourI.place(x=432,y=191)
    buttonMinI.place(x=760,y=191)
    buttonSecI.place(x=1080,y=191)

    #upper button for increasing the value of number(setTime)
    downIcon = PhotoImage(file=r"C:\\Users\\Kunal\Desktop\\all intresting movies\\programming\\Python\\Countdown Timer\\downsidekey.png")
    downIconImage = downIcon.subsample(1, 1)
    buttonDayD = Button(backColorGray,command=decdaynum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=downIconImage, borderwidth=1)
    buttonHourD = Button(backColorGray,command=dechournum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=downIconImage, borderwidth=1)
    buttonMinD = Button(backColorGray,command=decmintnum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=downIconImage, borderwidth=1)
    buttonSecD = Button(backColorGray,command=decsendnum, width=150,height=25, bg="#FFE400", fg="black", relief=FLAT, image=downIconImage, borderwidth=1)
    buttonDayD.place(x=112,y=441)
    buttonHourD.place(x=432,y=441)
    buttonMinD.place(x=760,y=441)
    buttonSecD.place(x=1080,y=441)
    backColorGray.create_text(670, 330, text="00   00",fill="#00FF00", font=("Ubuntu", 130, "bold"))
    backColorGray.create_text(670, 330, text="00                00",fill="#00FF00", font=("Ubuntu", 130, "bold"))
    backColorGray.create_line(112, 166, 265, 166, fill='white',width=5)
    backColorGray.create_line(433, 166, 585, 166, fill='white',width=5)
    backColorGray.create_line(760, 166, 912, 166, fill='white',width=5)
    backColorGray.create_line(1077, 166, 1235, 166, fill='white',width=5)
    backColorGray.create_text(190, 150, text="Days",fill="#0DDEEF", font=("Ubuntu", 30, "bold"))
    backColorGray.create_text(510, 150, text="Hours",fill="#0DDEEF", font=("Ubuntu", 30, "bold"))
    backColorGray.create_text(838, 150, text="Minutes",fill="#0DDEEF", font=("Ubuntu", 30, "bold"))
    backColorGray.create_text(1158, 150, text="Seconds",fill="#0DDEEF", font=("Ubuntu", 30, "bold"))

    startTime = Button(backColorGray, fg="#ffffff",font=BOLD, width=10, height=5,text='START',command = lambda: countDown(day,hour, mint, secd), bg="#0000ff").pack(side=BOTTOM, pady=100)
    Button(backColorGray, fg="#ffffff",font=BOLD, width=10, height=5,text='RESET',command = lambda: countDown(0, 0, 0, 0), bg="red").place(x=450,y=540)
    Button(backColorGray, fg="#ffffff",font=BOLD, width=10, height=5,text='STOP',command = timeStop, bg="#1F9F1B").place(x=815,y=537)

    start.mainloop()