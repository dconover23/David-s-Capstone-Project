TODO - Finish me!

# Wacky Weather Station - A Shoebox Project For The Future By David Conover
By now, all modern Weather Data rests squarely in the hands of Big Weather. Conglomerates such as The Weather Channel lord this data over the heads of us peasants, ensuring that only they have the power to tell you what’s happening right outside your door. The comparisons with George Orwell’s 1984 are easy to draw.

So it has fallen upon the shoulders of our hero, David Conover, who writes in the third person for the purpose of weaving an epic tale, to save us all from Big Weather. We need a solution that is accessible to the common man and woman. Thus, the WWW was born.

# The Rub/System Details
The Wacky Weather Station is a Raspberry Pi 4 hooked up to a touch display, RGB LED, and motor. The user can use the graphical interface to enter a city or location of their choosing (see main.py and weatherstation.py). Once they do that and hit the "Subvert Big Weather" button, the weatherstation.py script queries the OpenWeatherMap API for wind direction and temperature, which is printed to the screen. The RGB LED lights up to indicate the temperature (red is very hot, white is very cold) and the motor's spin speed depends on wind speed.



# Parts List
Raspberry Pi 4 - $50
Raspberry Pi Official TFT Display (Used) - $25
A Shoebox (scrounged from under my bed) - $0
RGB LED (from the lab. sold ubiquitiously on Amazon, though) - $7
Motor (from the lab. it's unlabelled, tiny, and yellow) - $5

# Lessons Learned (Are Not Forgotten)
1. Do not leave your physical setting up of things until the last couple of months. You will have to do terrible things to get it working if you do this.
2. Test stuff a LOT. Yes, I know, Mr. Cline blabs about this maybe too much for your liking, but he is trying to help you. You do not want to find out something is not working on the last day of work time because you never bothered to test and just assumed it would work.
3. Functions over classes. Only build classes if you are absolutely sure of what you need them for. You can otherwise simply use functions as they are far easier to understand and utilize.
4. Comment your code so that you know what's going on when you have to look at it again in a couple of months to fix a bug.
5. You don't need a concrete plan, but you should at least take some notes to keep track of things.



