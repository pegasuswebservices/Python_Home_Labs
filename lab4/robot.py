



def main():
    x_coordinates = []
    y_coordinates = []
    count = 1
    total_dist_travelled=0

    x_input = int(input("Input x coordinates of step "))
    y_input = int(input("Input y coordinates of step "))
    while x_input != 999 and y_input != 999:
        
        
       
        x_coordinates.append(x_input)
        y_coordinates.append(y_input)
        x_y_coordinates = x_coordinates + y_coordinates
        if len(x_coordinates)==1:
            dist_moved_step = ((x_coordinates[0])**2 + (y_coordinates[0])**2)**0.5
            total_dist_travelled = total_dist_travelled + dist_moved_step 
            print("Step", count, ":", dist_moved_step)
        else:
            dist_moved_step = ((x_coordinates[-1]-x_coordinates[-2])**2 + (y_coordinates[-1]-y_coordinates[-2])**2)**0.5



            total_dist_travelled = total_dist_travelled + dist_moved_step 
            print("Step", count,":", dist_moved_step)
        
        x_input = int(input("Input x coordinates of step "))
        y_input = int(input("Input y coordinates of step "))

        count = count + 1
    else:

        print("Total distance travelled by the robot", total_dist_travelled)


if __name__ == "__main__":
    main()
        
       


    
