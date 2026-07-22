# profile=input().split()
# standard_weight=(float(profile[0])-100)*0.9
# BMI=((float(profile[1])-standard_weight)*100)/standard_weight
#
# if BMI<=10:
#     print("정상")
# elif BMI<=20:
#     print("과체중")
# else :
#     print("비만")

profile=input().split()
height149=int(profile[0])-100
height150=(int(profile[0])-150)/2+50
height160=(int(profile[0])-100)*0.9
standard_weight=[height149,height150,height160]


if int(profile[0])<150:

elif int(profile[0])<160:

else :

