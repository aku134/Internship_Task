
# Function to find the leftmost point's index
def leftmost_point_index(coordinates):
    min_val=0
    for i in range(len(coordinates)):
        if(coordinates[i][0]<coordinates[min_val][0]):
            min_val=i
        elif(coordinates[i][0]==coordinates[min_val][0]):
            if(coordinates[i][1]<coordinates[min_val][1]):
                min_val=i

    return min_val

# Function to find the rightmost point's index
def rightmost_point_index(coordinates):
    max_val=0
    for i in range(len(coordinates)):
        if(coordinates[i][0]>coordinates[max_val][0]):
            max_val=i
        elif(coordinates[i][0]==coordinates[max_val][0]):
            if(coordinates[i][1]<coordinates[max_val][1]):
                max_val=i

    return max_val


def draw_polygon(coordinates):
    L=leftmost_point_index(coordinates)
    R=rightmost_point_index(coordinates)
    A=[]
    B=[]
    C=[]
    for i in range(len(coordinates)):
        # If index equals leftmost point or rightmost point
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
        # else the point lies below LR
        if((x2*y1-x1*y2) >0):
            A.append(coordinates[i])
        elif((x2*y1-x1*y2)<0):
            B.append(coordinates[i])
        else:
            # collinear point if cross product is 0
            C.append(coordinates[i]) 
        
    ordered_list=[]
    ordered_list.append(coordinates[L])

    sorted(A)
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

coordinates=[]
coordinates.append((3,2))
coordinates.append((5,3))
coordinates.append((2,2))
coordinates.append((3,1))
coordinates.append((4,1))
coordinates.append((3,5))
# coordinates.append((5,3))
# coordinates.append((4,3))
# coordinates.append((3,4))
# coordinates.append((2,3))

print(draw_polygon(coordinates)) 