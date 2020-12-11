score = input("Enter Score: ")
try:
    score1 = float(score)
except:
    print('ERROR: Plz enter numerical input\nsystem exiting...')
    quit()
if score1>=0.9 :
    print('A')
elif score1>=0.8 :
    print('B')
elif score1>=0.7 :
    print('C')
elif score1>=0.6 :
    print('D')
elif score1>=0 :
    print('F') 
else:
    print('ERROR: Plz enter a non-negative score')
