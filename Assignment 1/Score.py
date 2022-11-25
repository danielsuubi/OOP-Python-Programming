value = 'stop'

while True:
    number = input("Enter the score: ")
    score=float(number)
    scr=str(score)
    if scr == value:
       break
    elif score>0 and score>=0.9 and score<1:
       print("A")
    elif score>0 and score>=0.8 and score<1:
       print("B")
    elif score>0 and score>=0.7 and score<1:
       print("C")
    elif score>0 and score>=0.6 and score<1:
       print("D")
    elif score>0 and score<0.6 and score<1:
       print("F")
    else:
        print ("Bad score")
    	