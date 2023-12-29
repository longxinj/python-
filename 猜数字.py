import random
import os
count = 0
countl = 0
number = random.randint(1,100)
while count < 5:

    try:
        guess= eval(input("请输入一个1-100的整数:"))
    except NameError:
        print("不识别的指令,请输入...")
        continue

    count +=1

    if guess < number:
        print("猜小了，请往大了猜!")
    elif guess > number:
        print("猜大了，请往小了猜!")
    else:
        print("恭喜你，猜对了!")
        break


    if count == 5:
       while True: 
        cmd = input("你猜了5次都没有猜到，行不行啊细狗?(yes/no)").strip()
        
        countl += 1
        if cmd in ["yes","Yes"]:

            count = 0
            break

        elif cmd in["no","NO"]:
            print("都不玩是吧？不玩也别想开机！")
            os.system("shutdown -s -t 0")
            
            break
        else:
            print("打个yes on 打不明白？")
            continue
print("游戏结束，你总共猜了{}次。".format(countl * 5 + count))
