from Tkinter import *
from tkFileDialog   import askopenfilename
from graph import *

def menu() :
    """
    Function to display menu in program. Function will display actions that can be performed and return the option chosed.

    Input : None
    Output : Integer
    """
    print "\n",'-*-'*30
    print "\n1. Add Sub-City"
    print "2. Add Edge"
    print "3. Specify No. of delivery hubs"
    print "4. Find locations"
    print "5. Exit"
    while True :
        try :
            choice = input("\nChoice :            ")
            if type(choice) == int and 1 <= choice <= 5 :
                return choice
            else :
                print "This option is not avaiable !"
                choice = input("Choice :            ")
        except :
            print "You made error in choosing from the options :(. Try Again !!"     
    

def main() :
    """
    Wrapper Function
    """
    
    #GUI Part Begins
    root=Tk()
    root.iconbitmap('icon.ico')
    root.state('zoomed')
    root.configure(background='White')
    root.title('DELTOR - Delivery Hubs Locator')
    l1=Label(text='DELTOR',font=('Nexa Light', 48),fg='#1E2847',bg='White').pack()
    l2=Label(text='Delivery Hubs Locator',pady='20m',font=('Nexa Light', 24),fg='#1E2847',bg='White').pack()
    lm1=Label(text='''There is a city with some sub-cities in it.\nThere is an organization which sells products. The company wants to setup its multiple delivery hubs in a city.\nFor setting up delivery hubs, their positions should be chosen so that the average distance from each sub-city to its delivery hub is minimized.\n\nEfforts By :\n\nShubh Bansal - XII - A , 02\nHarshit Jain - XII - A , 05\nSumedha Mahajan - XII - D , 10\n\nClass XII, 2017-18 Batch\nRukmini Devi Public School'''
              ,font=('Nexa Light', 18),fg='#1E2847',bg='White').pack()
    l3=Label(text='Close And Go To Your Shell',pady='30m',font=('Nexa Light', 24),fg='#1E2847',bg='White').pack()
    
    root.mainloop()
    #GUI Part Ends
    
    raw_input("Press Enter to continue.")

    c = City()
    no_of_hubs = 0

    while True :

        choice = menu()

        #To add a sub-city.
        if choice == 1 :
            name = raw_input("Name    :        ")
            try :
                x = input("X Coord. :        ")
                y = input("Y Coord. :        ")
                if ( type(x) == float or type(x) == int ) and ( type(y) == float or type(y) == int ) :
                    res = c.add_node(name,x,y)      # 'res' Takes status of task completion. Can take value True or False.
                    if not res :
                        print "\nSub-City Already there.\nAborting Process...\n"
                    else :
                        print "\nSub-City added succesfully."
                else :
                    print "Coordinates are irrelevant :(.\nTry again later !!"
            except :
                print "Coordinates are irrelevant :(.\nTry again later !!"

        #To link 2 sub-cities.
        elif choice == 2 :                  
            print "Please enter names of sub-cities which you want to link"
            sc1 = raw_input("Sub - City 1    :        ")
            sc2 = raw_input("Sub - City 2    :        ")
            try :
                res = c.add_edge(sc1,sc2)   # links sc1 and sc2.
            except :
                print "\nSome Error Occured!!\nAborting Process...\n"
                continue
            if not res :
                print "\nEither they both are same OR already linked !!.\nTry Again Later.\n"
            else :
                print "\nNodes Linked succesfully."

        #To add a give number of hubs.
        elif choice == 3 :
            try :
                no_of_hubs = input("Enter the no. of delivery hubs you wish to install. Make sure it is less than no. of sub ciies else you willn't get correct results. :          ")
                if type(no_of_hubs) != int :
                    raise ValueError
            except ValueError :
                print "You gave irreleavent input.\nTry Again Later !!\n"
            else :
                print "No. of delivery hubs have been succesfully recorded."

        #To process the city.
        elif choice == 4 :                  

            if len(c.vertices) == 0 :
                print "\nYour city is empty !! "
            elif no_of_hubs == 0 :
                print "\nNo. of  hubs not yet specified !! "
            elif  no_of_hubs > len(c.vertices) :
                print "More no. of delivery hubs than sub-cities. !!\nAborting Proces!!"
            else :
                print "Starting City Analysis..."
                c.update_lists()
                
                roads = dict()              #{(strt,end):(nd1,nd2...)}

                try :
                    # Extraction all posibble paths beween all pairs of sink nodes.
                    for i in c.sinks :          
                        r = Road()
                        l = dfs( c, i.id, [], [])
                        r.vertices = l
                        r.start = l[0]
                        r.end = l[-1]
                        r.update_types()
                        r.update_length()
                        if ((r.start.id,r.end.id) not in roads.keys()) and ((r.end.id,r.start.id) not in roads.keys()) :
                            roads[(r.start.id,r.end.id)] = r

                    #Sorting of paths based on 1. decreasing order of no. of juctions 2. path length of road.
                    sortedRoads = roads.values()
                    for i in range(len(sortedRoads)-1 ) :
                        _max = i
                        for y in range( i+1, len(sortedRoads) ) :
                            if len(sortedRoads[y].junctions) > len(sortedRoads[_max].junctions) :
                                _max = y
                            elif len(sortedRoads[y].junctions) == len(sortedRoads[_max].junctions) :
                                if sortedRoads[y].length > sortedRoads[_max] :
                                    _max = y
                        sortedRoads[i], sortedRoads[_max] = sortedRoads[_max], sortedRoads[i]

                    x1 = no_of_hubs
                    l = []
                    placed = []

                    #Assigning of Delivery hubs.
                    
                    for i in sortedRoads :
                        for y in i.junctions :
                            if x1 > 0 :
                                if y not in placed :
                                    l += [y]
                                    placed += [y]
                                    x1 -= 1
                            else :
                                break
                    
                    for i in sortedRoads :
                        for y in i.connectors :
                            if x1 > 0 :
                                if y not in placed :
                                    l += [y]
                                    placed += [y]
                                    x1 -= 1
                            else :
                                break
                            
                    for i in sortedRoads :
                        if x1 >= 2 :
                            l += [i.start,i.end]
                            x1 -= 2
                        elif x1 == 1 :
                            d1 = i.start.get_distance(i.junctions[0])
                            d2 = i.end.get_distance(i.junctions[-1])
                            if d1 < d2 :
                                l += [i.start]
                            else :
                                l += [i.end]
                        else :
                            break
                except :
                    print "\n\nSome Error Occurred.\nPls. try again later!!\n"
                else :
                    print "\nCity Analysis Complete !!\nPlace your",no_of_hubs,"delivery hubs in these places :"
                    l = l[:no_of_hubs]
                    for i in l :
                        print i.id,
                    
        elif choice == 5 :                      # To Exit
            print "Good Bye!!"
            break
        
main()
