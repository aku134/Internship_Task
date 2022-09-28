
from tkinter import Tk, Canvas, Frame, BOTH

# Draw polygon shape based on coordinates
class Polygon(Frame):

    def __init__(self,coordinates):
        super().__init__()

        self.draw_polygon(coordinates)


    def draw_polygon(self,coordinates):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        
        canvas.create_polygon(coordinates, outline='black',
            fill='white', width=3)

        canvas.pack(fill=BOTH, expand=1)

# Function to find the leftmost point's index
def leftmost_coordinates_index(coordinates,n):
    min_val=0
    for i in range(n):
        if(coordinates[i][0]<coordinates[min_val][0]):
            min_val=i
        elif(coordinates[i][0]==coordinates[min_val][0]):
            if(coordinates[i][1]<coordinates[min_val][1]):
                min_val=i

    return min_val

# Function to find the rightmost point's index
def rightmost_coordinates_index(coordinates,n):
    max_val=0
    for i in range(n):
        if(coordinates[i][0]>coordinates[max_val][0]):
            max_val=i
        elif(coordinates[i][0]==coordinates[max_val][0]):
            if(coordinates[i][1]<coordinates[max_val][1]):
                max_val=i

    return max_val

# Function to get the order of points forming a polygon
def ordered_points(coordinates,n):

    L=leftmost_coordinates_index(coordinates,n)
    R=rightmost_coordinates_index(coordinates,n)

    A=[] # Stores points that occur above LR segment
    B=[] # Stores points that occur below LR segment
    C=[] # Stores collinear points w.r.t Leftmost and Rightmost points

    for i in range(n):
        # If index equals leftmost point's index or rightmost point's index
        # skip the current iteration and move to next
        if(i==L or i==R):
            continue
        # Find cross product of a point with leftmost point 
        # and rightmost point
        x1=coordinates[i][0]-coordinates[L][0]
        y1=coordinates[i][1]-coordinates[L][1]
        x2=coordinates[R][0]-coordinates[i][0]
        y2=coordinates[R][1]-coordinates[i][1]
        # If cross porduct is positive the point
        # lies above LR segment
        # else the point lies below LR segment
        if((x2*y1-x1*y2) >0):
            A.append(coordinates[i])
        elif((x2*y1-x1*y2)<0):
            B.append(coordinates[i])
        else:
            # collinear point if cross product is 0
            C.append(coordinates[i]) 
        
    ordered_list=[]
    ordered_list.append(coordinates[L])
    # Sorting points in ascending based on x coordinate
    A.sort(key=lambda y:y[0])
    # Sorting points in Descending based on x coordinate
    B.sort(key=lambda y: y[0],reverse=True)
    
    for i in A:
        ordered_list.append(i)
    ordered_list.append(coordinates[R])
    for j in B:
        ordered_list.append(j)
    if(C):
        for i in C:
         ordered_list.append(i)
    return ordered_list

def main():
    coordinates=[]
    coordinates.append((300,200))
    coordinates.append((500,300))
    coordinates.append((200,200))
    coordinates.append((300,100))
    coordinates.append((400,100))
    coordinates.append((300,500))
    print("Unordered points")
    dict={}
    for i in range(len(coordinates)):
        dict[coordinates[i]]=chr(i+65)
    print(dict)   
        
    # coordinates.append((500,300))
    # coordinates.append((400,300))
    # coordinates.append((300,400))
    # coordinates.append((200,300))

    # coordinates.append((0,300))
    # coordinates.append((200,200))
    # coordinates.append((100,100))
    # coordinates.append((200,100))
    # coordinates.append((300,0))
    # coordinates.append((0,0))
    # coordinates.append((300,300))

    n=len(coordinates)
    if(n<3):
        print("polygon not possible")
    else:
        # Function to get ordered list of points
        # forming a polygon
        ordered_list=ordered_points(coordinates,n)
        print("Ordered points")
        for i in range(len(ordered_list)):
            print(ordered_list[i],dict[ordered_list[i]])
                
        root = Tk()
        # Draws a polygon based on ordered points
        Polygon(ordered_list)
        root.geometry("1024x1024")
        root.mainloop()


if __name__ == '__main__':
    main()
