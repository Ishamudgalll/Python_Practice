def main():
    setForwardness(1)
    setIRPower(135)
    while True: 
        left = getObstacle(0)
        center = getObstacle(1)
        right = getObstacle(2)
        if (center <= 5000 and left <= 5000 and right <= 5000):
            forward(0.5, 0.2)
            wait(.3)
        elif(right>left):
            turnLeft(1, 0.45)
        else:
            turnRight(1, 0.45)