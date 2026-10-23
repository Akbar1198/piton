# task1
# for i in range(10,0,-1):
#     print(i)
# print("Liftoff!")

# task2
# childtickets=0
# adulttickets=0
# for i in range(5):
#     for j in range(5):
#         a=int(input())
#         if a<18:
#             childtickets+=1
#         else:
#             adulttickets+=1
# print(childtickets)
# print(adulttickets)

#task3
# 1 3 5 7 9 

#task4
# s=0
# for i in range(5):
#     a=int(input())
#     s+=a
# print(s)
# print(s/5)

#task5
# while True:
#     a=input()
#     if len(a)==8:
#         print("daxil oldunuz")
#         break
#     else:
#         print("Yeniden cehd edin")

#task6 70 40 10 -20 done

#task7
#bunu sorusaq muellimden cunki bir seyi tam yaza bilmedim

#task8
# username="admin"
# password="1234"
# s=0
# while True:
#     a=input("Username:")
#     b=input("Password:")
#     if s==3:
#         print("Siz 3 defe sehv daxil etdiniz")
#         break
#     else:
#         if a==username and b==password:
#             print("Daxil oldunuz")
#             break
#         else:
#             s+=1
#             print("Yeniden cehd edin")

#task9
# account=500
# while True:
#     amount=int(input())
#     if amount==0:
#         print("Goodbye")
#         break
#     if amount<0:
#         print("Invalid amount")
#         break
#     if amount>account:
#         print("Insufficient funds")
#         break
#     if amount>0 and amount<=account:
#          account-=amount
#          print(account)
#     else:
#          print("insufficient funds")
#          break

#task10 wrongpin 2,wrongpin 1,acces granted 0

#task11
# passed=0
# failed=0
# total=0
# count=0
# highest=0
# while True:
#     grade=int(input("Grade: "))
#     if grade==-1:
#         break
#     if grade>=51:
#         passed+=1
#     else:
#         failed+=1
#     if count==0 or grade>highest:
#         highest=grade
#     total+=grade
#     count+=1
# print("Passed:",passed)
# print("Failed:",failed)
# print("Highest:",highest)
# if count>0:
#     print("Average:",round(total/count,1))

# #task12
# spaces=20
# while True:
#     command=input("Command: ")
#     if command=="stop":
#         break
#     elif command=="in":
#         if spaces>0:
#             spaces-=1
#             print("Free spaces:",spaces)
#         else:
#             print("Garage full")
#     elif command=="out":
#         if spaces<20:
#             spaces+=1
#             print("Free spaces:",spaces)
#         else:
#             print("Garage is empty")
#     else:
#         print("Unknown command")

# #task13
# hot_days=0
# hottest_temp=-150
# hottest_day=1
# for i in range(1,8):
#     temp=int(input(f"Day {i}: "))
#     if temp>30:
#         hot_days+=1
#     if i==1 or temp>hottest_temp:
#         hottest_temp=temp
#         hottest_day=i
# print("Hot days:",hot_days)
# print("Hottest day:",hottest_day)

# #task14
# password="secret"
# attempts=0
# while True:
#     entered=input("Password: ")
#     if entered==password:
#         print("Welcome")
#         break
#     attempts+=1
#     if attempts==3:
#         print("Account locked")
#         break

#task15
# password=input("Password: ")
# d=0
# u=0
# l=0
# for c in password:
#     if c.isdigit():
#         d+=1
#     elif c.isupper():
#         u+=1
#     elif c.islower():
#         l+=1
# if len(password)>=8 and d>0 and u>0 and l>0:
#     print("Strong password")
# else:
#     print("Weak password",end="")
#     if len(password)<8:
#         print(": too short",end="")
#     if u==0:
#         print(": no uppercase letters",end="")
#     if l==0:
#         print(": no lowercase letters",end="")
#     if d==0:
#         print(": no digits",end="")

#task17 100 den sonra gelen ilk 14 e bolunen ededi cap edir

#task 18 i yazammadim

#task 19
# total=0.0
# while total<1.5:
#     coin=float(input("Insert coin: "))
#     if coin==0.05 or coin==0.1 or coin==0.2 or coin==0.5 or coin==1.0:
#         total+=coin
#         print("Total:",round(total,2))
#     else:
#         print("Coin not accepted")
# print("Here is your water")
# print("Change:",round(total-1.5,2))

#task 20
# say=0
# def f(n):
#     for i in range(2,n):
#         if n%i==0:
#             return 'm'
#     return 's' if x>1 
# for k in range(2,101):
#     if def f(k)='s':
#         print(k)
#         say+=1
# print(say)

#task21 101 102 201 202 301 302