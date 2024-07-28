p = float(input("Enter marks obtained in Pysics ="))
c = float(input("Enter marks obtained in Chemistry ="))
m = float(input("Enter marks obtained in Maths ="))
pas = float(input("Enter your Passing Percentage"))
total = p+c+m
alltotal=300
percent = (total*100)/alltotal
print("Total marks obtained in all subject =",total,"/300")
print("Total Percentage obtained in all subject =",percent,"%")
if percent>=pas:
    if percent>=pas and percent<=50:
        print("Passed with 3rd Division")
    elif percent>=51 and percent<=74:
        print("Passed with 2nd Division")
    elif percent>=75:
        print("passed with 1st and Topper Division")
else:
    print("Fail")
