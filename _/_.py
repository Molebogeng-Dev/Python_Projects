import sys
from math import sin, cos

class Rover:
    def __init__(self, file):
        try:
            with open(file) as f:
                self.file= f.readlines()
        except FileNotFoundError:
            sys.exit('Cannot open file')

        self.degrees=0
        self.cat_p={270: [cos(self.degrees),sin(self.degrees)],
                    180: [sin(self.degrees),cos(self.degrees)],
                    90: [cos(self.degrees),sin(self.degrees)], 
                    0: [sin(self.degrees),cos(self.degrees)]
                }
        self.x_y=[0,0]
        
        print("I'm at (0.00, 0.00) facing 0.00 degrees")


  
    def calculations(self,campus,meters,direction):
        if self.degrees <= 90:
            # if direction == 'backwards':
            #     self.x_y[1]=int(str(f'-{self.x_y[1]}'))
            self.x_y=[round(campus[0]*meters,2)+self.x_y[0],round(campus[1]*meters,2)+self.x_y[1]]
        elif self.degrees <= 180:
            self.x_y=[round(campus[0]*meters,2)+self.x_y[0],round(campus[1]*meters,2)-self.x_y[1]]
        elif self.degrees <= 270:
            self.x_y=[round(campus[0]*meters,2)-self.x_y[0],round(campus[1]*meters,2)-self.x_y[1]]
        else:
            self.x_y=[round(campus[0]*meters,2)-self.x_y[0],round(campus[1]*meters,2)+self.x_y[1]]
       


    def instructions(self):                 
        for i,ins in enumerate(self.file):
            ls_ins=ins.split()
            if 'meters' in ls_ins and len(ls_ins) == 4:
                for point in self.cat_p:

                    if point <= self.degrees:
                        self.calculations(self.cat_p[point],int(ls_ins[1]),ls_ins[3])
                        
                        print(f"Moving {float(ls_ins[1])} meters {ls_ins[3]} (instruction {i+1}.00)")
                        print(f"I'm at ({self.x_y[0]}, {self.x_y[1]}) facing {float(self.degrees)} degrees")
                        break 

            elif 'degrees' in ls_ins and len(ls_ins) == 4:
                if 'clockwise' in ls_ins:
                    self.degrees+= int(ls_ins[1])
                    while self.degrees >= 360:
                        self.degrees-=360
                elif 'counterclockwise' in ls_ins:
                    self.degrees-= int(ls_ins[1])
                    while self.degrees < 0:
                        self.degrees+=360

                print(f"Turning {float(ls_ins[1])} degrees {ls_ins[3]} (instruction {i+1}.00)")
                print(f"I'm at ({self.x_y[0]}, {self.x_y[1]}) facing {float(self.degrees)} degrees")

            else:
                print(f"I've encountered an instruction I don't understand, aborting (instruction {i+1})")        
        

def main():
    rover= Rover('_/ins.txt')#sys.argv[1])
    rover.instructions()

if __name__ == "__main__":
    main()