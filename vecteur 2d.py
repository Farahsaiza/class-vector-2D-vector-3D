class vecteur_2d():
    _nbrvct = 0
    def __init__(self, abcsisse, ordonne):
        self.__abcsisse =  abcsisse
        self.__ordonne = ordonne
        vecteur_2d._nbrvct  = vecteur_2d._nbrvct + 1


    def Getabcsisse(self):
        return  self.__abcsisse
    def Getordonne(self):
        return self.__ordonne
    def Getnbrvct(self):
        return  vecteur_2d._nbrvct
    
    def setabcsisse(self,  abcsisse):
        self.__abcsisse  =  abcsisse
    def setordonne(self, ordonne):
        self.__ordonne  = ordonne
    
    def ToString(self):
        print("X  = {} , Y = {}".format(self.Getabcsisse() , self.Getordonne()))       

    def equal(self,  V2):
        if self.Getabcsisse() == V2.Getabcsisse() and self.Getordonne()== V2.Getordonne() :
            return True
        else:
            return False
        
    def norme(self):
        print("la norme du vecteur est : {} ".format(0.5**((self.Getabcsisse)**2+(self.Getordonne)**2)) )


    


class vecteur_3d(vecteur_2d):
    _nbrvct = 0
    def __init__(self, abcsisse, ordonne,  z):
        super().__init__(abcsisse,ordonne)
        self.__z = z
      

    def Getz(self):
        return  self.__z
   
    
    def setz(self, z):
        self.__z  =  z




    def ToString(self):
        print("X  = {} , Y = {}  , z = {}".format(self.Getabcsisse() , self.Getordonne(), self.Getz()))       

   
    
    def equal(self,  V3):
        if self.Getabcsisse() == V3.Getabcsisse() and self.Getordonne()== V3.Getordonne() and self.Getz()== V3.Getz():
            return True
        else:
            return False
        
    def norme(self):
       x=self.Getabcsisse()
       y=self.Getordonne()
       z=self.Getz()
        
       print("la norme du vecteur est : {} ".format(0.5**((x)**2+(y)**2+(z)**2)) )






v1=vecteur_3d(3,4,2)
v2=vecteur_3d(2,4,9)
v1.ToString()
print(v1.equal(v2))
v1.norme()


        


        

    
    



    
