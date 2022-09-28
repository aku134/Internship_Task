




def leftmost_point_index(coordinates):
    min_val=0
    for i in range(len(coordinates)):
        if(coordinates[i][0]<coordinates[min_val][0]):
            min_val=i
        elif(coordinates[i][0]==coordinates[min_val][0]):
            if(coordinates[i][1]<coordinates[min_val][1]):
                min_val=i

    return min_val


def draw_polygon(coordinates):
    lp=leftmost_point_index(coordinates)
    return lp
    


coordinates=[]
coordinates.append((4,3))
coordinates.append((1,3))
coordinates.append((1,2))
coordinates.append((3,3))
coordinates.append((5,2))

print(draw_polygon(coordinates))