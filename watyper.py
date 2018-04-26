from pynput.mouse import Controller, Button 

mouse=Controller()
mouse.move(800,1000)
mouse.click(Button.left, 1)

from pynput.keyboard import Controller, Key  

randomRubbish = ["Awesome","So goooood", "y u liddis", "Can you go away", "Please go away?", "onegai", "Stop spaming people", "This spam isnt good", "GO AWAY", "Please la", "bonjeur","gong xi fa cai", "selamat bagi"]
keyboard=Controller()

"""
while 1 == 1:
	for i in randomRubbish:

		keyboard.type(i)
		mouse.move(123,21) 
		mouse.click(Button.left,1)
		mouse.move(-123,-21)
		mouse.click(Button.left,1)
"""

for i in randomRubbish:

	keyboard.type(i)
	mouse.move(123,21) 
	mouse.click(Button.left,1)
	mouse.move(-123,-21)
	mouse.click(Button.left,1)