"""
Dandy GUI program 

Show character info, maps, and time/environment information.
All should be updateable by the game-master.

possibly add dice options... 

Derek Jacobsen

v1 start 9/26/19

"""

#import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

# https://www.geeksforgeeks.org/python-gui-tkinter/

 
def main():
     
    """
    main fn.  Put stuff here... 
    """
    
    """
    testing stuff here
    """
    
    #player1 = player("Elias","Bookworm",12,"book")
     
    #print(player1.name, player1.age, player1.classtype, player1.item, player1.luck)
    
    #player1holder = player_gui(1)
    #player1holder.mainloop()
    
    #player1 = player_info(player1holder.name_out, player1holder.classtype_out, player1holder.age_out, player1holder.item_out)
    
    first_win = ask_player_number()
    #first_win.mainloop() # doesn't look like it matters if it's inside or outside of the class.  
    # will need to make sure it's consistant... 
    
    player_registry = []
    #player_holder = [] # don't actually need to save this intermediate step because it's going right into player class?
    
    for i in range(first_win.player_number_out):
        #print(i)
        player_holder = player_gui(i+1)
        player_holder2 = player_info(player_holder.name_out, player_holder.classtype_out, player_holder.age_out, player_holder.item_out)
        #player_holder = [player_holder2.name, player_holder2.classtype, player_holder2.age, player_holder2.item, player_holder2.luck]
        player_registry.append(player_holder2.__dict__)
        
        # I'm not happy with this because now there's no point in it being a class... 
        # changed it to dictionary method from the class, returning all atributes. close enough... 
        
        
    #print(player_registry[0]['name'])
    
    
    second_win = main_window_gui(first_win.player_number_out, player_registry)
    
    """
    # rewriting this code in class structure... 
    win = tk.Tk()
    win.title('counting seconds')
    button = tk.Button(win, text = 'Fucking Explode',fg = 'red', width = 25, command = win.destroy)
    button.grid(row = 0, column = 3)
    
    tk.Label(win, text = "Name").grid(row = 0)
    tk.Label(win, text = "class type").grid(row = 1)
    tk.Label(win, text = "age").grid(row = 2)
    tk.Label(win, text = "item").grid(row = 3)
    
    inName = tk.Entry(win)
    inClasstype = tk.Entry(win)
    inAge = tk.Entry(win)
    inItem = tk.Entry(win)
    
    inName.grid(row = 0, column = 1)
    inClasstype.grid(row = 1, column = 1)
    inAge.grid(row = 2, column = 1)
    inItem.grid(row = 3, column = 1)
    
    #subButton = tk.Button(win,text = "submit", fg = 'green', width = 20, command = )
    
    # needs get command and possibly class stucture... 
    # https://stackoverflow.com/questions/10727131/why-is-tkinter-entrys-get-function-returning-nothing
    
    
    win.mainloop()
    
    player1 = player(inName,inClasstype,inAge,inItem)

    print(player1.name, player1.age, player1.classtype, player1.item, player1.luck)

    """
          
class player_info:
     
    def __init__(self, name, classtype, age, item):
        self.name = name
        self.classtype = classtype
        self.age = int(age)
        self.item = item
        self.luck = 15 - self.age
        self.exp = 0
         
    def getName(self):
        return self.name
     
    def getClasstype(self):
        return self.classtype
     
    def getAge(self):
        return self.age
     
    def getItem(self):
        return self.item
    


class player_gui(tk.Tk):
    def __init__(self, player_number, name = None, classtype = None, age = None, item = None):
       
        # init
        tk.Tk.__init__(self)
        self.title('Player ' + str(player_number))
        self.name = tk.Entry(self)
        self.classtype = tk.Entry(self)
        self.age = tk.Entry(self)
        self.item = tk.Entry(self)
        
        #submit button
        submit_button = tk.Button(self,text = ' submit ', fg = 'green', command = self.two_things)
        close_button = tk.Button(self,text = ' close ', fg = 'red', command = self.destroy)
        
        # placing things
        tk.Label(self, text = 'Name ').grid(row = 0)
        tk.Label(self, text = 'age ').grid(row = 1)
        tk.Label(self,text = 'class type ').grid(row = 2)
        tk.Label(self,text = 'item ').grid(row = 3)
        
        self.name.grid(row = 0, column = 1)
        self.age.grid(row = 1, column= 1)
        self.classtype.grid(row = 2, column = 1)
        self.item.grid(row = 3,column = 1)
        
        submit_button.grid(row = 4, column = 1)
        close_button.grid( row = 4, column = 2)
        
        self.mainloop()
        
    def two_things(self):
        self.on_button()
        self.destroy()
        
    def on_button(self):
        # needs to return all the stuff... can I put it right in the class? holy shit.  
        #print(self.name.get(),self.classtype.get())
        #self.destroy #can't get it to fucking close... 
        self.name_out = self.name.get()
        self.classtype_out = self.classtype.get()
        self.age_out = self.age.get()
        self.item_out = self.item.get()



class ask_player_number(tk.Tk):
    def __init__(self, number_of_players = None):
        tk.Tk.__init__(self)
        
        # entry box to start the game, decides number of players
        self.number_of_players = tk.Entry(self)
        
        #submit button
        submit_button = tk.Button(self,text = ' submit ', fg = 'green', command = self.on_button)
        
        #placing things
        tk.Label(self, text = ' Enter number of Players ').grid(row = 0)
        
        self.number_of_players.grid(row = 0, column = 1)
        submit_button.grid(row = 1, column = 1)
        
        # keep the party going
        self.mainloop()
        
    def on_button(self):
        self.player_number_out = int(self.number_of_players.get())
        self.destroy()



class main_window_gui(tk.Tk):
    def __init__(self, number_of_players, player_registry):
        tk.Tk.__init__(self)
        
        self.title(' Tales from the Loop ')
        tk.Frame(self.geometry('2000x950'))
        # picture stuff taken from 
        # https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
        
        # get path to picture
        path = 'loop_map.jpg'
        
        img_holder = Image.open(path)
        img_holder2 = img_holder.rotate(270, expand = 1) # expand default = 0 was the problem not displaying the whole picture
        # expand while true tells it to expand rotated image to the size of the original... 
        
        # createes a tkinter compatible photo image, which can be used everywhere tkinter expects an image
        img = ImageTk.PhotoImage(img_holder2)
        
        # use label widget to display text and images
        map_img = tk.Label(self, width = 1400, height = 900, image = img)
        
        #The Pack geometry manager packs widgets in rows or columns.
        #map_img.pack()
        
        #need to figure out how to scroll around page with multiple widgets... 
        
        tk.Label(self, text = ' Map ').place(relx = 0.75, rely = 0.0)
        map_img.pack()
        map_img.place(relx = 0.25, rely = 0.01, width = 1400, height = 900)
        
        # header
        tk.Label(self, text = ' Players ', font = 'bold').place(anchor = 'nw')
        
        for i in range(number_of_players):
           
            #names
            tk.Label(self, text = ' Name ',font = 'bold').place(relx = 0.1 + 0.1*i, rely = 0.1)
            tk.Label(self, text = player_registry[i]['name']).place(relx = 0.1 + 0.1*i, rely = 0.2)
            
            #class types
            tk.Label(self, text = ' Class ', font = 'bold').place(relx = 0.1 + 0.1*i, rely = 0.3)
            tk.Label(self, text = player_registry[i]['classtype']).place(relx = 0.1 + 0.1*i, rely = 0.4)
            
            #age
            tk.Label(self, text = ' age ', font = 'bold').place(relx = 0.1 + 0.1*i, rely = 0.5)
            tk.Label(self, text = player_registry[i]['age']).place(relx = 0.1 + 0.1*i, rely = 0.6)
        
        
        
        self.mainloop()
        
        

















































     
main()        