color_list = ("red","blue","green",12,7)
for x in color_list:
    if isinstance(x,str):
        print(f"{x} is str")
    elif isinstance(x,int):
        print("Error")