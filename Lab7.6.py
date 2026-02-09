N=int(input("enter no of students:"))
marks=[0]*N
count=0
count_f=0
for i in range(len(marks)):
    marks[i]=int(input("enter marks:"))
    if i%5==0:
        if marks[i]>=95 and marks[i]<=100:
          marks[i]=100
        else:
          marks[i]=marks[i]+5
    if marks[i]>=90 and marks[i]<=100:
        print(f"{marks[i]}->Excellent")
        count=count+1
    elif marks[i]>=75 and marks[i]<=89:
        print(f"{marks[i]}->Very good")
        count=count+1
    elif marks[i]>=60 and marks[i]<=74:
        print(f"{marks[i]}->Good")
        count=count+1
    elif marks[i]>=40 and marks[i]<=59:
        print(f"{marks[i]}->Average")
        count=count+1
    elif marks[i]>=0 and marks[i]<=39:
        print(f"{marks[i]}->Fail")
        count=count+1
        count_f=count_f+1
    else:
        print(f"{marks[i]}->Invalid")

print("Total valid students :",count)
print("Total Failed students :",count_f)

