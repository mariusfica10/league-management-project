from tkinter import *
from tkinter import ttk
from appCoordinator import *

ok = 0

number = 0

objects = serviceLeague.getAll()
for obj in objects:
    if obj.getID() > number:
        number = obj.getID()

number += 1


def main2(root):

    root1 = ttk.Frame(root, height=50, width=1200)

    frame_sign = ttk.Frame(root1, height=50, width=1200)
    e = ttk.Entry(frame_sign, width=50)
    e.pack(side=LEFT)

    frame_sign.pack(side=LEFT)
    frame_sign.pack_propagate(False)

    e2 = ttk.Entry(frame_sign, width=50)
    e2.pack(side=LEFT)

    myLabel2 = ttk.Label(frame_sign)
    myLabel2.pack(side=RIGHT)
    def myClick2():

        global number

        number += 1
        get_name = e.get()
        get_league = e2.get()

        tv.insert("", "end", values=(number, get_name, get_league, 0, 0, 0))
        serviceLeague.add(number, get_name, get_league, 0, 0, 0, 0, 0, 0)

        myLabel2.config(text=league + '(league)   ' + league2 + '(team)  ')

    myButtonL2 = ttk.Button(frame_sign, text="Sign league+team", command=myClick2)
    myButtonL2.pack(side=LEFT)
    frame_sign.pack(side=RIGHT)
    frame_sign.pack_propagate(False)
    root1.pack(side=TOP)

    frTable = ttk.Frame(root, height=320, width=1200)

    columns = ('ID', 'Name of the Team', 'Name of the League', 'Games Played',
               'Wins,Draws,Loses + Points', 'Points Made/Got in Game')
    tv = ttk.Treeview(frTable, columns=columns, show="headings", height="10")

    def treeview_sort_column(tvtv, colcol, reverse):
        lem = [(tvtv.set(k, colcol), k) for k in tvtv.get_children('')]
        lem.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(lem):
            tvtv.move(k, '', index)

        # reverse sort next time
        tvtv.heading(colcol, command=lambda: treeview_sort_column(tvtv, colcol, not reverse))

    for col in columns:
        tv.heading(col, text=col, command=lambda: treeview_sort_column(tv, col, False))

    all_me = serviceLeague.getAll()

    i = 0

    p = 0

    dict = {}

    for object in all_me:
        if object.getLeague() not in dict:
            dict[object.getLeague()] = 1
            tv.insert('', str(p), str(object.getLeague()), value=(object.getLeague(), ' ', ' ', ' ', ' ', ' '))
            p = p+1

    def fool(all_me, league, points):
        count = 1
        for object in all_me:
            if object.getLeague() == league:
                part = object.getWins() * 3 + object.getDraw()
                if part > points:
                    count += 1
        return count

    for object in all_me:
        i += 1
        league = object.getName()
        league2 = object.getLeague()
        points = object.getWins() * 3 + object.getDraw()
        position = fool(all_me, league2, points)
        tv.insert(str(league2), 'end', values=("                " + str(i), league, league2, "        " + str(object.getPlayed()) + " played        place [" + str(position) + "]", "        " + str(object.getWins()) + "-" + str(object.getDraw()) + "-" + str(object.getLoses()) + "       ( " + str(object.getDraw()+(object.getWins()*3)) + " ) points", "                " + str(object.getMade()) + "-" + str(object.getGot())))

    def refresh():
        all = serviceLeague.getAll()

        count = 0

        p = 0

        dict = {}

        for ill in tv.get_children():
            tv.delete(ill)

        for objee in all:
            if objee.getLeague() not in dict:
                dict[objee.getLeague()] = 1
                tv.insert('', str(p), str(objee.getLeague()), value=(objee.getLeague(), ' ', ' ', ' ', ' ', ' '))
                p = p + 1

        for objee in all:
            count += 1
            league_get = objee.getName()
            lealea = objee.getLeague()
            points = objee.getWins() * 3 + objee.getDraw()
            position = fool(all, lealea, points)
            tv.insert(str(lealea), 'end', values=("                " + str(count), league_get, lealea, "        " + str(objee.getPlayed()) + " played        place [" + str(position) + "]", "        " + str(objee.getWins()) + "-" + str(objee.getDraw()) + "-" + str(objee.getLoses()) + "       ( " + str(objee.getDraw() + (objee.getWins() * 3)) + " ) points", "                " + str(objee.getMade()) + "-" + str(objee.getGot())))

    tv.grid()

    def selectItem(a):
        curItem = tv.focus()
        return tv.item(curItem)['values'][0]

    def selectItem3(a):
        curItem = tv.focus()
        return tv.item(curItem)['values'][1]

    def selectItem2(a):
        curItem = tv.focus()
        return tv.item(curItem)['values'][2]

    def delete():

        selected_item = tv.selection()[0]
        trap = selectItem(selected_item)
        trap2 = selectItem2(selected_item)
        trap3 = selectItem3(selected_item)

        tv.delete(selected_item)

        if trap2 == ' ':
            all = serviceLeague.getAll()
            for kido in all:
                if kido.getLeague() == trap:
                    serviceLeague.delete(kido.getID())

        if trap2 != ' ':
            all = serviceLeague.getAll()
            for kido in all:
                if kido.getLeague() == trap2 and trap3 == kido.getName():
                    serviceLeague.delete(kido.getID())

    def ranking():
        selected_item = tv.selection()[0]
        mood = selectItem3(selected_item)
        if mood == ' ':

            doom = selectItem(selected_item)
            all = serviceLeague.getAll()
            textYer = ''

            used = 0
            total = 0
            for object in all:
                if doom == object.getLeague():
                    total += 1

            first = 1
            while total != used:
                for object in all:
                    if doom == object.getLeague():
                        points = object.getWins() * 3 + object.getDraw()
                        position = fool(all, object.getLeague(), points)
                        if position == first:
                            used += 1
                            textYer += str(position) + '.        ' + str(points) + " points        " + object.getName()\
                                + '\n'
                            rank.config(text=textYer)

                first += 1

            no = 8

            while used < no:
                textYer += '\n'
                rank.config(text=textYer)
                used += 1

    frameManage = ttk.Frame(root, width=1200, height=200)

    button_del = ttk.Button(frameManage, width=12, text="Remove", command=delete)
    button_del.pack_propagate(False)
    button_del.pack(side=LEFT)

    button_refresh = ttk.Button(frameManage, width=12, text="Refresh", command=refresh)
    button_refresh.pack_propagate(False)
    button_refresh.pack(side=LEFT)

    button_rank = ttk.Button(frameManage, width=12, text="Show rankings", command=ranking)
    button_rank.pack_propagate(False)
    button_rank.pack(side=LEFT)

    frTable.pack(side=TOP)

    def sw():
        global ok
        help = " - Select a league from the table above to see the rankings(raking button just first 10) \n - To delete a whole league or just a team(delete button +select team/league)\n - To refresh data after a game or another opperation (refresh button) \n - After loading a game data, you must re check teams and leagues \n - Deleting a game from database will make changes in the league system\n - Teams from different leagues can't play a game \n - Pressing heading ID from the table will sort leagues by name(games by score)\n - Double tap on a league to maximize/minimize the selected league \n - Before you delete a team from a league,remove all games where the team played\nonly if you want this \n - For a better desplay resolution, use 1280-720 of PC.Use names and leagues\n with CAPSLOCK(10 letters for caps is perfect for a team name)\n - IF the clock is blocked press STOP and RESET,than all should be good \n - Minutes cant reset,reopen app,be careful to first put minutes then start the clock \n AFTER A GAME VERIFY IN THE GAMES TABLE IF THE GAME IS LOADED, VEIRIFY ALL\n!! DO NOT DUPLICATE NAMES OR LEAGUES !! (Hope this helps at least 1 person :) )"
        nope = ''

        ok += 1
        ok = ok % 2

        if ok == 1:
            lb.config(text=help)
        if ok == 0:
            lb.config(text=nope)

    frameManage.pack(side=TOP)

    frTable.pack_propagate(False)
    frRank = ttk.Frame(root, width=1200, height=315)
    rank = ttk.Label(frRank, text='  ', font=("", 19))
    rank.pack_propagate(False)
    rank.pack(side=LEFT)

    darm = ttk.Frame(root, width=600, height=315)

    but = ttk.Button(darm, text="Help", command=sw)
    but.pack(side=TOP)

    lb = ttk.Label(darm, width=1200)
    lb.config(text=' ', font=("Compact", 11))
    lb.pack()

    darm.pack_propagate(False)
    darm.pack(side=RIGHT)

    frRank.pack_propagate(False)
    frRank.pack(side=TOP)
