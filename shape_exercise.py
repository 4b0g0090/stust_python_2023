class Myshape:
    def __init__(self,slider=0,length=0,witdth=0,radius=0):
       
       self.slider =slider
       self.length=length
       self.witdth=witdth
       self.radius=radius
       
    def square(self):
        total=self.slider*self.slider
        print(total)

    def Rectangle(self):
        total1=self.length*self.witdth
        print(total1)
        
    def Circle(self):
        total2=self.radius*self.radius*3.14
        print(total2)
   
square=Myshape(6)
square.square()

Rectangle=Myshape(0,5,3)
Rectangle.Rectangle()

Circle=Myshape(0,0,0,3)
Circle.Circle()





