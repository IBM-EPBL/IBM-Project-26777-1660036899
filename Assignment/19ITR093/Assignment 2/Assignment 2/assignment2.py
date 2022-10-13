import random
import time
while (1):
    Temperature = random.randint(0,150)
    Humidity = random.randint(0,100)
	
    if Temperature > 100 and Humidity > 80:
        print("Temperature : " + str(Temperature))
        print("Humidity : " + str(Humidity))
        print("Temperature and Humidity is High")
        print("Alarm On !!!")
        time.sleep(2)
    else:
        print("Temperature : " + str(Temperature))
        print("Humidity : " + str(Humidity))
        print("Range is Normal")
print("")