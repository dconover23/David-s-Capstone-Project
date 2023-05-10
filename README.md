# Wacky Weather Station - A Shoebox Project For The Future By David Conover (5/9/2023)
By now, all modern Weather Data rests squarely in the hands of Big Weather. Conglomerates such as The Weather Channel lord this data over the heads of us peasants, ensuring that only they have the power to tell you what’s happening right outside your door. The comparisons with George Orwell’s 1984 are easy to draw.

So it has fallen upon the shoulders of our hero, David Conover, who writes in the third person for the purpose of weaving an epic tale, to save us all from Big Weather. We need a solution that is accessible to the common man and woman. Thus, the WWW was born.

![IMG_6077](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/47a64104-f643-4507-a5d1-0ee418394caf)


# The Rub
The Wacky Weather Station is a Raspberry Pi 4 hooked up to a touch display, RGB LED, and motor. The user can use the graphical interface to enter a city or location of their choosing (see main.py and weatherstation.py). Once they do that and hit the "Subvert Big Weather" button, the Python script contained in weatherstation.py queries the OpenWeatherMapAPI and returns weather data that is then printed to the GUI.

![image](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/81a782b6-8ab0-4ec5-99fa-d931f7fa7895)

Here's the internals, if you're curious. I explain this more in the section below.

# System Details
Most of the program lives in main.py, as well as the GUI stuff. When you enter a location into the entry box, it runs the temperature and wind direction functions in weatherstation.py, which query the OpenWeatherMapAPI and return the response it gets as an integer (for temperature) or string (for wind direction.) that the Tkinter variables can print to the screen. More information is contained within those files if you want more details.

The GUI is powered by Tkinter. On launch, main.py will instantiate everything it needs to form the GUI, including the background, window size, entry, etc. The "subvert big weather" button will send your location query off to the API by using a function that calls the ones defined in weatherstation.py. This is displayed by the Pi touchscreen (not pictured below, but it's Figure 5).

As for the physical bits, I utilize the pin system of the Raspberry Pi (Figure 2) (powered by a standard 5v power supply) to control both the RGB LED (Figure 4) and motor (Figure 3b) based on the information returned. Both are hooked up to the pins that control them (you can see all of them defined in weatherstation.py) and the program calls them if they meet the required conditions. For example, the RGB LED flashes a different color based on the temperature returned. High temperatures are hot (red), but lower temperatures are colder (white). Each color is commented so you know what gets returned. The motor itself uses a motor controller (Figure 3a) so that it can interface with the Pi and change based on the current speed of wind.

The actual case design is pretty basic. The LED is glued in, the motor is held up by the fan attached on the on the other side, and the Pi stays in through sheer force of wire. The display is also kept in by the same convention. Laugh at me now, potential future student of Cline's, but soon you'll be wishing it were so simple.

![Untitled](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/eefa0fd5-cd99-4152-b9cc-5b34e371b9db)


![image](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/6a21a843-0ac0-46a0-ba01-0df3d1f0c1f8)

Pictured here: Basically the entire control flow. It's not very complex, trust me.

# Design Evalulation
* Output Display: Requirement met by touchscreen. It is basically the bread and butter of this project, and interfaces with everything else.
* Manual User Input: Met by onscreen keyboard on touchscreen. Also interfaces with everything, since you need it to type.
* Automatic Sensor: Met by OpenWeatherMap API. Returns the weather info we need. Handy, no?
* Acuators, Mechanisms, and Hardware: Met by motor and the design of the box. It uses very little to accomplish a lot.
* Logic, Processing, and Control: Met by WWW GUI. Programmed in Python and is used to interface with all elements.

# Assembly
1. Get a Pi and an official 7 inch Raspberry Pi Touch Display.
2. Connect the display to the Pi using the provided wires. I know online installs say that you should connect the display to the power supply instead of the board, but you should seriously just connect the board and let the 5v pin on the Pi power the display. It worked better for me, at least.
3. Once that's working, get an RGB LED. Solder the pins up to wires, and then pick some GPIO pins you'd like to use. Make sure to keep track of the legs you connect, because the legs have an annode and cathode you need to connect properly.
4. Get a motor and motor controller. For the motor controller I used (L298N) there are connection tutorials online. The motor is connected to the motor controller, which is the thing that interfaces with the Pi.
5. Get out your shoebox! For the wiring and hooking up of parts, you can use a lot of tape and the large real estate of the box to play fast and loose with wiring and spacing, like I did. You can cut holes in stuff to make it fit, and as for the cardboard pad the display sits in (see above) you can zip tie it to the box so that you always have access to the box.
6. Program everything. Or just steal my code. I don't mind. You'll need to change pins and such to get it working on your end.
7. Profit! Big Weather stands no chance against us now.

# Parts List
* Raspberry Pi 4 and Power Supply (the lab) - $50
* Raspberry Pi Official TFT Display (Used) - $25
* A Shoebox (scrounged from under my bed) - $0
* RGB LED (from the lab. sold ubiquitiously on Amazon, though) - $7
* Motor (from the lab. it's unlabelled, tiny, and yellow) - $5
* Motor Controller (L298N motor, sourced from the lab, but also ubiquitously on Amazon) - $7

# Lessons Learned (Are Not Forgotten)
This section is built for potential future students of the Robotics Engineering class. I am going to assume you've gotten to the end of the unit that comes before the Capstone project.
1. Have a reliable development enviornment. Do not use online IDEs as they require an internet connection and are prone to breakage (ask any prior member of the class about the Online Arduiono IDE's puzzling "object Object" issue.) It is also best if it is a computer you have administrator rights to, as it allows you to change and install stuff on a whim. This was a concern at the start of my project that led to me bringing out my old laptop and slapping Ubuntu on it (which, quite handily, comes with git pre-installed.)
2. Keep your scope intact. This was not a problem I had, but rather a problem I've seen others have. They bite off more than they can chew and end up getting hurt for it. I deliberately kept the scope of the project small and focused on the software part as I felt that was where I was most capaable. Focus on what you find yourself good at.
3. Don't be afraid to ask for help! When I was unsure of how to wire or connect something, I could always ask my classmates or friends for help. If I couldn't find a part, Mr. Cline was always willing to help. If you just try to push through and do things on your own without knowing how, you run the risk of a sub-par project (or a short-circuiting of your fifty dollar board that you're now financially responsible for. Whoops!)

# Wiring Diagram
![E6D178F9-03A8-42C3-870B-F7008C987D57](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/a0609309-9690-4ce6-840e-6dfc3c3433b6)

Well, that's all from me. About 1300~ or so words just on this tiny little shoebox thing. I had a lot of fun making it despite my missteps. I hope if you pursue something similar, you get a little help or kick out of this. 

If you do end up doing that, then shoot me an email (with #WackyWeatherStation in the subject line so gmail doesn't auto-bin it) at conover2004@gmail.com. I'd be interested in seeing it!

-David
