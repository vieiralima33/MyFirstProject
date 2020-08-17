print('------ Hello, lets check how is your health? ------ \n\n')
def BMIcalc():
    gender = str(input("What's your gender? [F/M]\n"))
    if gender == 'M' or gender == 'm':
        weight = int(input("What's your weight?[Kg]: \n"))
        height = float(input("What's your height?[M]: \n"))
        imcM = weight / height**2
        print ('Your Body Mass Index is: ---[', round(imcM,2), ']---')
        if imcM < 20:
            print('\nYou are under weight!')
        elif imcM >= 20 and imcM < 25:
            print('\nCongratulations, your weight is normal!')
        elif imcM >= 25 and imcM < 30:
            print('\nAttention, you are overweight!')
        elif imcM >= 30 and imcM < 40:
            print('\n Be careful, you have moderate obesity!')
        elif imcM >= 43:
            print('\n Seek help, you have morbid obesity!')
    elif gender == 'F' or gender == 'f':
        weight = int(input("What's your weight?[Kg]: \n"))
        height = float(input("What's your height?[M]: \n"))
        imcF = weight / height**2
        print ('Your Body Mass Index is:', round(imcF, 2))
        if imcF < 19:
            print('\nYou are under weight!')
        elif imcF >= 19 and imcF < 24:
            print('\nCongratulations, your weight is normal!')
        elif imcF >= 24 and imcF < 29:
            print('\nAttention, you are overweight!')
        elif imcF >= 29 and imcF < 39:
            print('\n Be careful, you have moderate obesity!')
        elif imcF >= 39:
            print('\n Seek help, you have morbid obesity!')
    else:
        print("Type 'M' for male or 'F' for female \n")
        BMIcalc()
BMIcalc()
input('Press ENTER to finish...')