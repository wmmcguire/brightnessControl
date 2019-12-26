from gpiozero import PWMLED, LightSensor, Button
import matplotlib.pyplot as plt 
from datetime import datetime
from time import sleep

#Pulse Width Modulation outputs
ledR =	PWMLED(10)
ledB =	PWMLED(3)
ledG = 	PWMLED(17)

#initialize Light Dependent Resistor
ldr = LightSensor(22)

#Matplotlib settings
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.title('Sensor Testing(LDR)')
plt.xlabel('Time')
plt.ylabel('LDR Value')
ax1.set_ylim(bottom=0, top=0.89)



#def livePlot(time, ldrVal):
	
def main():
	#show graph
	fig.show()
	state = 0
	timePassed = 0 # increments every time sleep is iterated

	n = 0 #counts number of iterations
	x, y = [], []
	
	while True:
		x.append(timePassed)
		y.append(ldr.value)
		ax1.plot(x, y, 'r')

		fig.canvas.draw()

		ax1.set_xlim(left=timePassed-3, right=timePassed+3)


		#clear out array after appending 2000 elements
		#to clear some memory
		n += 1
		if n % 2000:
			y[:-1000] = []
			x[:-1000] = []

		#in python 2, max value from ldr was ~0.88
		#in python 3, it was ~0.97
		ledR.value = 0.892 - ldr.value
		ledG.value = 0.892 - ldr.value 
		ledB.value = 0.892 - ldr.value

		sleep(0.08) #Delay of 8ms
		timePassed += 0.08

		
if __name__ == '__main__':
	main()

