import time
from secondFrame import *
from datetime import date
from random import randint
import winsound
today = date.today()

Counter1 = 0
Counter2 = 0
CountF = 0
CountO = 0
CountF2 = 0
CountO2 = 0
part = 1
s = ''
stclock = 0

teamOne = ''
teamTwo = ''

finalScoreOne = 0
finalScoreTwo = 0
finalNameOne = ''
finalNameTwo = ''
finalLeagueName = ''


def main(MainWindow):

    def func1():
        global Counter1
        Counter1 += 1
        if 10 > Counter1 > -1:
            label1.config(text='0' + str(Counter1))
        else:
            label1.config(text=Counter1)

    def func2():
        global Counter2
        Counter2 += 1
        if 10 > Counter2 > -1:
            label2.config(text='0' + str(Counter2))
        else:
            label2.config(text=Counter2)

    def func3():
        global Counter1
        Counter1 -= 1
        if 10 > Counter1 > -1:
            label1.config(text='0' + str(Counter1))
        else:
            label1.config(text=Counter1)

    def func4():
        global Counter2
        Counter2 -= 1

        if 10 > Counter2 > -1:
            label2.config(text='0' + str(Counter2))
        else:
            label2.config(text=Counter2)

    def func5(label, ok):
        global CountF
        CountF += ok
        label.config(text='  '+str(CountF)+'F  ')

    def func6(label, ok):
        global CountO
        CountO += ok
        label.config(text='  '+str(CountO)+'T  ')

    def func7(label, ok):
        global CountF2
        CountF2 += ok
        label.config(text='  '+str(CountF2)+'F  ')

    def func8(label, ok):
        global CountO2
        CountO2 += ok
        label.config(text='  '+str(CountO2)+'T  ')

    def func9():
        global Counter1
        Counter1 = 0
        label1.config(text='0'+str(Counter1))

    def func10():
        global Counter2
        Counter2 = 0
        label2.config(text='0'+str(Counter2))

    def func11(p, q):
        global part
        global s
        if (part-1) % 4 == 0:
            s = ''
        s += 'P' + str(part) + ':' + str(p) + '-' + str(q) + '   '
        labelQ.config(font=("Compact", 18), text=s)
        part = part + 1

    frame1 = ttk.Frame(MainWindow, width=1200, height=200)
    frame1.pack()
    frame1.pack_propagate(False)

    label1 = ttk.Label(frame1, text='00')
    label1.config(font=("Courier", 155))
    label2 = ttk.Label(frame1, text='00')
    label2.config(font=("Courier", 155))

    MyButtonRemove1 = ttk.Button(frame1, text="-1 Home", command=func3)
    MyButtonRemove2 = ttk.Button(frame1, text="-1 Away", command=func4)
    MyButtonAdd1 = ttk.Button(frame1, text="+1 Home", command=func1)
    MyButtonAdd2 = ttk.Button(frame1, text="+1 Away", command=func2)

    frame2 = ttk.Frame(MainWindow, width=1200, height=85)
    frame22 = ttk.Frame(frame2, width=1200, height=50)
    frame22.pack(side=TOP)

    Reset1 = ttk.Button(frame22, command=lambda: func5(labelF1, -CountF),  text="Reset F")
    Reset1.pack(side=LEFT)

    Reset2 = ttk.Button(frame22, command=lambda: func6(labelO1, -CountO), text="Reset TO")
    Reset2.pack(side=LEFT)

    labelF1 = ttk.Label(frame22, text="  0F  ")
    labelF1.config(font=("Courier", 20))
    labelF1.pack(side=LEFT)

    labelO1 = ttk.Label(frame22, text="  0T  ")
    labelO1.config(font=("Courier", 20))
    labelO1.pack(side=LEFT)

    FaultPlus1 = ttk.Button(frame22, text="+1 Foul", command=lambda: func5(labelF1, 1))
    FaultPlus1.pack(side=LEFT)

    TimeOplus1 = ttk.Button(frame22, text="+1 T.0.", command=lambda: func6(labelO1, 1))
    TimeOplus1.pack(side=LEFT)

    labelSpace = ttk.Label(frame22, width=20)

    labelSpace.pack(side=LEFT)

    FaultPlus2 = ttk.Button(frame22, text="+1 Foul", command=lambda: func7(labelF2, 1))
    FaultPlus2.pack(side=LEFT)

    TimeOplus2 = ttk.Button(frame22, text="+1 T.O.", command=lambda: func8(labelO2, 1))
    TimeOplus2.pack(side=LEFT)

    labelF2 = ttk.Label(frame22, text="  0F  ")
    labelF2.config(font=("Courier", 20))
    labelF2.pack(side=LEFT)

    labelO2 = ttk.Label(frame22, text="  0T  ")
    labelO2.config(font=("Courier", 20))
    labelO2.pack(side=LEFT)

    Reset3 = ttk.Button(frame22, text="Reset F", command=lambda: func7(labelF2, -CountF2))
    Reset3.pack(side=LEFT)

    Reset4 = ttk.Button(frame22, text="Reset TO", command=lambda: func8(labelO2, -CountO2))
    Reset4.pack(side=LEFT)

    frame2.pack()
    frame2.pack_propagate(False)

    MyButtonRemove1.pack(side=LEFT)
    MyButtonAdd1.pack(side=LEFT)
    label1.pack(side=LEFT)

    MyButtonAdd2.pack(side=RIGHT)
    MyButtonRemove2.pack(side=RIGHT)
    label2.pack(side=RIGHT)

    frame3 = ttk.Frame(frame1, width=605, height=380)
    stclock = 0

    def add():
        global stclock
        stclock += 5
        label10.config(text=str(stclock) + 'minutes to play')

    class StopWatch(Frame):

        def __init__(self, parent=None, **kw):
            Frame.__init__(self, parent, kw)
            self.startTime = 0.0
            self.nextTime = 0.0
            self.onRunning = 0
            self.timestr = StringVar()
            self.MakeWidget()

        def MakeWidget(self):
            timeText = ttk.Label(self, textvariable=self.timestr, font=("times new roman", 75))
            self.SetTime(self.nextTime)
            timeText.pack(fill=X, expand=NO)

        def Updater(self):
            global stclock
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.timer = self.after(50, self.Updater)
            if stclock == int(self.nextTime + 0.01):
                self.after_cancel(self.timer)
                self.nextTime = time.time() - self.startTime
                self.SetTime(self.nextTime)
                self.onRunning = 0
                winsound.PlaySound("over",winsound.SND_FILENAME)

        def SetTime(self, nextElap):
            minutes = int(nextElap / 60)
            seconds = int(nextElap - minutes * 60.0)
            miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
            self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

        def Start(self):
            if not self.onRunning:
                self.startTime = time.time() - self.nextTime
                self.Updater()
                self.onRunning = 1

        def Stop(self):
            if self.onRunning:
                self.after_cancel(self.timer)
                self.nextTime = time.time() - self.startTime
                self.SetTime(self.nextTime)
                self.onRunning = 0

        def Reset(self):
            func11(Counter1, Counter2)
            self.startTime = time.time()
            self.nextTime = 0.0
            self.SetTime(self.nextTime)

    Top = ttk.Frame(frame3, width=200)
    Top.pack(side=TOP)
    stopWatch = StopWatch(frame3, bg="black")
    stopWatch.pack(side=TOP)
    Bottom = ttk.Frame(frame3, width=600)
    Bottom.pack(side=BOTTOM)
    Start = ttk.Button(Bottom, text='Start', command=stopWatch.Start, width=10)
    Start.pack(side=LEFT)
    Stop = ttk.Button(Bottom, text='Stop', command=stopWatch.Stop, width=10)
    Stop.pack(side=LEFT)
    Reset = ttk.Button(Bottom, text='Reset', command=stopWatch.Reset, width=10)
    Reset.pack(side=LEFT)
    label10 = ttk.Label(frame3, text='0 minutes to play')
    label10.pack(side=LEFT)
    plus = ttk.Button(Bottom, text='+5 min', command=add, width=10)
    plus.pack(side=LEFT)
    frame3.config()
    frame3.pack(side=TOP)

    frame33 = ttk.Frame(frame2, height=40, width=1200)
    MyReset1 = ttk.Button(frame33, text="Reset Score Home", width=80, command=func9)
    MyReset2 = ttk.Button(frame33, text="Reset Score Away", width=80, command=func10)
    MyReset1.pack(side=LEFT)
    MyReset2.pack(side=RIGHT)
    frame33.pack(side=BOTTOM)

    frameLeague = ttk.Frame(MainWindow, height=120, width=1200)
    frameL1 = ttk.Frame(frameLeague, height=100, width=420)
    labelTeam1 = ttk.Label(frameL1, text="HOME TEAM")
    labelTeam1.config(font=("Compact", 43))
    labelTeam1.pack(side=LEFT)
    frameL1.pack(side=LEFT)
    frameL1.pack_propagate(False)

    frameGet = ttk.Frame(frameLeague, height=100, width=250)

    def framiu():
        all = serviceLeague.getAll()
        ok1 = 0
        one = ent1.get()
        two = ent2.get()

        global finalLeagueName

        for object in all:
            if one == object.getName() and finalLeagueName == object.getLeague():
                ok1 = 1
            if two == object.getName() and finalLeagueName == object.getLeague():
                ok1 = 1

        if ok1 == 1 and ok1 == 1 and one != two:
            loadTeam.config(text="DONE")
            labelTeam1.config(text=one, font=("Compact", 43))
            global finalNameOne
            finalNameOne = one

            labelTeam2.config(text=two, font=("Compact", 43))
            global finalNameTwo
            finalNameTwo = two
        else:
            loadTeam.config(text="TRY AGAIN")

    ent1 = ttk.Entry(frameGet)

    ent2 = ttk.Entry(frameGet)

    ent1.pack(side=LEFT)

    ent2.pack(side=LEFT)

    loadTeam = ttk.Button(frameGet, text='CHECK TEAMS', command=framiu)

    frameGet.pack(side=LEFT)

    loadTeam.pack(side=LEFT)

    frameL2 = ttk.Frame(frameLeague, height=100, width=420)
    labelTeam2 = ttk.Label(frameL2, text="AWAY TEAM")
    labelTeam2.config(font=("Compact", 43))
    labelTeam2.pack(side=RIGHT)
    frameL2.pack(side=RIGHT)
    frameLeague.pack(side=TOP)
    frameLeague.pack_propagate(False)
    frameL2.pack_propagate(False)

    Frame4 = ttk.Frame(MainWindow, height=60, width=1200)

    lig = ttk.Menubutton(Frame4, text="LEAGUES&TEAMS", width=30)
    lig.menu = Menu(lig, background="grey27")
    lig["menu"] = lig.menu

    all = serviceLeague.getAll()

    dict = {}

    for kido in all:
        if kido.getLeague() not in dict:
            dict[kido.getLeague()] = kido.getLeague()
            lig.menu.add_command(label=kido.getLeague(), background="grey27")

    for kido in all:
        lig.menu.add_command(label=kido.getName()+"("+kido.getLeague()+")", background="grey27")

    lig.pack(side=LEFT)

    epl = ttk.Entry(Frame4)

    epl.pack(side=LEFT)

    def vibecheck():
        yee = epl.get()
        ok = 0
        all = serviceLeague.getAll()
        for unu in all:
            if yee == unu.getLeague():
                ok = 1
        if ok == 1:
            Butwhole.config(text='DONE')
            global finalLeagueName
            finalLeagueName = yee
            lig.config(text="game from  " + finalLeagueName)
        else:
            Butwhole.config(text='TRY AGAIN')

    Butwhole = ttk.Button(Frame4, text='CHECK LEAGUE', command=vibecheck)

    Butwhole.pack(side=LEFT)

    labelQ = ttk.Label(Frame4)
    labelQ.pack(side=LEFT)

    def foo():
        global finalLeagueName
        global finalNameOne
        global finalNameTwo
        global finalScoreOne
        global finalScoreTwo
        global Counter1
        global Counter2
        finalScoreOne = Counter1
        finalScoreTwo = Counter2
        stopWatch.Reset()

        if finalNameTwo == '' and finalNameOne == '' and finalLeagueName == '':
            labelQ.config(text='TRY AGAIN')

        idGame = randint(1, 1000000000)

        date = today

        if finalNameOne != '' and finalNameTwo != '' and finalLeagueName != '':
            serviceGame.add(idGame, date, finalLeagueName, finalNameOne, finalNameTwo, Counter1, Counter2)

        id1 = 0

        id2 = 0

        all = serviceLeague.getAll()

        for object in all:
            if object.getName() == finalNameOne:
                id1 = object.getID()
            if object.getName() == finalNameTwo:
                id2 = object.getID()

        una = serviceLeague.read(id1)
        doua = serviceLeague.read(id2)

        played1 = una.getPlayed()
        played2 = doua.getPlayed()
        wins1 = una.getWins()
        wins2 = doua.getWins()
        draw1 = una.getDraw()
        draw2 = doua.getDraw()
        loses1 = una.getLoses()
        loses2 = doua.getLoses()
        made1 = una.getMade()
        made2 = doua.getMade()
        got1 = una.getGot()
        got2 = doua.getGot()

        if Counter1 == Counter2:
            played1 += 1
            played2 += 1
            draw1 += 1
            draw2 += 1
            made1 += Counter1
            made2 += Counter2
            got1 += Counter2
            got2 += Counter1
            serviceLeague.update(una.getID(), una.getLeague(), una.getName(), played1, wins1, draw1,  loses1, made1, got1)
            serviceLeague.update(doua.getID(), doua.getLeague(), doua.getName(), played2, wins2, draw2,  loses2, made2, got2)

        if Counter1 > Counter2:
            played1 += 1
            played2 += 1
            wins1 += 1
            loses2 += 1
            made1 += Counter1
            made2 += Counter2
            got1 += Counter2
            got2 += Counter1
            serviceLeague.update(una.getID(), una.getLeague(), una.getName(), played1, wins1, draw1, loses1, made1, got1)
            serviceLeague.update(doua.getID(), doua.getLeague(), doua.getName(), played2, wins2, draw2, loses2, made2, got2)

        if Counter1 < Counter2:
            played1 += 1
            played2 += 1
            loses1 += 1
            wins2 += 1
            made1 += Counter1
            made2 += Counter2
            got1 += Counter2
            got2 += Counter1
            serviceLeague.update(una.getID(), una.getLeague(), una.getName(), played1, wins1, draw1, loses1, made1, got1)
            serviceLeague.update(doua.getID(), doua.getLeague(), doua.getName(), played2, wins2, draw2, loses2, made2, got2)

        tvGames.insert("", "end", values=(idGame, date, finalLeagueName, str(finalNameOne) + "-" + str(finalNameTwo), str(Counter1) + "-" + str(Counter2)))

        finalLeagueName = ''
        finalNameOne = ''
        finalNameTwo = ''
        Counter1 = 0
        Counter2 = 0
        label1.config(text='00')
        label2.config(text='00')
        labelF1.config(text='  0F  ')
        labelF2.config(text='  0F  ')
        labelO1.config(text='  0T  ')
        labelO2.config(text='  0T  ')
        Butwhole.config(text='CHECK LEAGUE')
        loadTeam.config(text='CHECK TEAMS')
        labelQ.config(text='')

    FrameLoad = ttk.Button(Frame4, width=20, text="~load data~", command=foo)
    FrameLoad.pack(side=RIGHT)

    Frame4.pack(side=TOP)
    Frame4.pack_propagate(False)

    def selectItem():
        curItem = tvGames.focus()
        return tvGames.item(curItem)['values'][0]

    def selectItem1():
        curItem = tvGames.focus()
        return tvGames.item(curItem)['values'][2]

    def selectItem2():
        curItem = tvGames.focus()
        return tvGames.item(curItem)['values'][3]

    def selectItem3():
        curItem = tvGames.focus()
        return tvGames.item(curItem)['values'][4]

    def dele():

        selected_item = tvGames.selection()[0]
        # serviceLeague.delete(selectItem(selected_item))
        id = selectItem()
        trap = selectItem1()
        trap2 = selectItem2()
        trap3 = selectItem3()

        league = trap
        team1, team2 = trap2.split('-')
        score1, score2 = trap3.split('-')

        score1 = int(score1)
        score2 = int(score2)

        id1 = 0
        id2 = 0

        tvGames.delete(selected_item)

        all = serviceLeague.getAll()
        for object in all:
            if team1 == object.getName() and league == object.getLeague():
                id1 = object.getID()
            if team2 == object.getName() and league == object.getLeague():
                id2 = object.getID()

        una = serviceLeague.read(id1)
        doua = serviceLeague.read(id2)

        played1 = una.getPlayed()
        played2 = doua.getPlayed()
        wins1 = una.getWins()
        wins2 = doua.getWins()
        draw1 = una.getDraw()
        draw2 = doua.getDraw()
        loses1 = una.getLoses()
        loses2 = doua.getLoses()
        made1 = una.getMade()
        made2 = doua.getMade()
        got1 = una.getGot()
        got2 = doua.getGot()

        if score1 == score2:
            played1 -= 1
            played2 -= 1
            draw1 -= 1
            draw2 -= 1
            made1 -= score1
            made2 -= score2
            got1 -= score2
            got2 -= score1
            serviceLeague.update(una.getID(), una.getLeague(), una.getName(), played1, wins1, draw1,  loses1, made1, got1)
            serviceLeague.update(doua.getID(), doua.getLeague(), doua.getName(), played2, wins2, draw2,  loses2, made2, got2)

        if score1 > score2:
            played1 -= 1
            played2 -= 1
            wins1 -= 1
            loses2 -= 1
            made1 -= score1
            made2 -= score2
            got1 -= score2
            got2 -= score1
            serviceLeague.update(una.getID(), una.getLeague(), una.getName(), played1, wins1, draw1, loses1, made1, got1)
            serviceLeague.update(doua.getID(), doua.getLeague(), doua.getName(), played2, wins2, draw2, loses2, made2, got2)

        if score1 < score2:
            played1 -= 1
            played2 -= 1
            loses1 -= 1
            wins2 -= 1
            made1 -= score1
            made2 -= score2
            got1 -= score2
            got2 -= score1
            serviceLeague.update(una.getID(), una.getLeague(), una.getName(), played1, wins1, draw1, loses1, made1, got1)
            serviceLeague.update(doua.getID(), doua.getLeague(), doua.getName(), played2, wins2, draw2, loses2, made2, got2)

        serviceGame.delete(id)

    frGames = ttk.Frame(MainWindow, height=320, width=1200)

    columns = ('ID', 'Date of the Game', 'League of the game', 'Actual Game', 'Score of the Game')

    tvGames = ttk.Treeview(frGames, columns=columns, show="headings", height="5")

    def treeview_sort_column(tv, colcol, reverse):
        lem = [(tv.set(k, colcol), k) for k in tv.get_children('')]
        lem.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(lem):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(colcol, command=lambda: treeview_sort_column(tv, colcol, not reverse))

    for col in columns:
        tvGames.heading(col, text=col, command=lambda: treeview_sort_column(tvGames, col, False))

    tvGames.grid()

    all = serviceGame.getAll()

    for ala in all:
        tvGames.insert("", "end", values=(ala.getID(), ala.getDate(), ala.getLeague(), str(ala.getNameOne()) + "-" + str(ala.getNameTwo()), str(ala.getScoreOne()) + "-" + str(ala.getScoreTwo())))

    button_del = ttk.Button(frGames, width=12, text="Remove", command=dele)
    button_del.grid()

    frGames.pack(side=TOP)
