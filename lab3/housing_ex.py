from tabulate import tabulate
def get_data():
    for i in range (0,8, 1):
        if i ==0:
            zero_occupants=int(input("Provide the number of houses with 0 occupancy: "))

        elif i ==1:
            one_occupants=int(input("Provide the number of houses with 1  occupancy: "))
        elif i ==2:
            two_occupants=int(input("Provide the number of houses with 2  occupancy: "))
        elif i ==3:
            three_occupants=int(input("Provide the number of houses with 3 occupancy: "))
        elif i ==4:
            four_occupants=int(input("Provide the number of houses with 4 occupancy: "))
        elif i ==5:
            five_occupants=int(input("Provide the number of houses with 5 occupancy: "))
        elif i ==6:
            six_occupants=int(input("Provide the number of houses with 6 occupancy: "))
        elif i >= 7:
            seven_occupants=int(input("Provide the number of houses with +6 occupancy: "))

    return zero_occupants, one_occupants, two_occupants, three_occupants, four_occupants, five_occupants, six_occupants, seven_occupants





def cal_percentage(zero_occupants, one_occupants, two_occupants, three_occupants, four_occupants, five_occupants, six_occupants, seven_occupants):

    total = zero_occupants+one_occupants+two_occupants+three_occupants+four_occupants+five_occupants+six_occupants+seven_occupants


    zero_percentage=(zero_occupants/total)*100
    one_percentage=(one_occupants/total)*100
    two_percentage=(two_occupants/total)*100
    three_percentage=(three_occupants/total)*100
    four_percentage=(four_occupants/total)*100
    five_percentage=(five_occupants/total)*100
    six_percentage=(six_occupants/total)*100
    seven_percentage=(seven_occupants/total)*100

    #make table

    head = ["Occupants", "No. houses", "Percentage"]
    data = [["0", zero_occupants, zero_percentage],
            ["1", one_occupants, one_percentage],
            ["2", two_occupants, two_percentage],
            ["3", three_occupants, three_percentage],
            ["4", four_occupants, four_percentage],
            ["5", five_occupants, five_percentage],
            ["6", six_occupants, six_percentage],
            ["6+", seven_occupants, seven_percentage]]
    print(tabulate(data, headers=head, tablefmt="grid"))

zero_occupants, one_occupants, two_occupants, three_occupants, four_occupants, five_occupants, six_occupants, seven_occupants = get_data()

cal_percentage(zero_occupants, one_occupants, two_occupants, three_occupants, four_occupants, five_occupants, six_occupants, seven_occupants)
