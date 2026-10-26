import random

def pick_ball_experiment():
    balls = ['blue', 'red', 'green']

    results = random.choice(balls)

    pro = balls.count('red')/len(balls)
    print("Probability of Picking a Red Ball is:", pro)

    if results == 'red':
        return 'Red Ball was Picked'
    else:
        return 'Better Luck Next Time'

res = pick_ball_experiment()
print(res)