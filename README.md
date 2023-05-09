TODO - Finish me!

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

The GUI is powered by Tkinter. On launch, main.py will instantiate everything it needs to form the GUI, including the background, window size, entry, etc. The "subvert big weather" button will send your location query off to the API by using a function that calls the ones defined in weatherstation.py. 

As for the physical bits, I utilize the pin system of the Raspberry Pi to control both the RGB LED and motor based on the information returned. Both are hooked up to the pins that control them (you can see all of them defined in weatherstation.py) and the program calls them if they meet the required conditions. For example, the RGB LED flashes a different color based on the temperature returned. High temperatures are hot (red), but lower temperatures are colder (white). Each color is commented so you know what gets returned.

The actual case design is pretty wishy-washy. The LED is glued in, the motor is held up by the fan attached on the ot

![image](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/6a21a843-0ac0-46a0-ba01-0df3d1f0c1f8)

Pictured here: Basically the entire control flow. It's not very complex, trust me.

# Parts List
* Raspberry Pi 4 (the lab) - $50
* Raspberry Pi Official TFT Display (Used) - $25
* A Shoebox (scrounged from under my bed) - $0
* RGB LED (from the lab. sold ubiquitiously on Amazon, though) - $7
* Motor (from the lab. it's unlabelled, tiny, and yellow) - $5
* Motor Controller (L298N motor, sourced from the lab, but also ubiquitously on Amazon) - $7

# Lessons Learned (Are Not Forgotten)
1. Do not leave your physical setting up of things until the last couple of months. You will have to do terrible things to get it working if you do this.
2. Test stuff a LOT. Yes, I know, Mr. Cline blabs about this maybe too much for your liking, but he is trying to help you. You do not want to find out something is not working on the last day of work time because you never bothered to test and just assumed it would work.
3. Functions over classes. Only build classes if you are absolutely sure of what you need them for. You can otherwise simply use functions as they are far easier to understand and utilize.
4. Comment your code so that you know what's going on when you have to look at it again in a couple of months to fix a bug.
5. Take notes to keep track of stuff. This is sort of the same thing as number four, but for stuff outside of code. I had a list on my desktop and I would check off things I needed to get done.

# Wiring Diagram
![E6D178F9-03A8-42C3-870B-F7008C987D57](https://github.com/dconover23/Weirdo-Weather-Station/assets/83132702/a0609309-9690-4ce6-840e-6dfc3c3433b6)

