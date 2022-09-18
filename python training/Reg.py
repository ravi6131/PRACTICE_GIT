#from test7 import *

class Myproject:

    def __init__(self):
        print("Inside My class")
        
    def fileread(self,filename):
        fr=open(filename)
        data=fr.readlines()
        return data
        
    def other_file(self):
        print("-----Other Files------")
    
    def display_data(self):
        out=self.fileread("output_func.txt")
        print(out)
        self.other_file()
        
        
        
    
        
    
    
        


My=Myproject()
My.display_data()



