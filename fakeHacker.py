import os, time, random

# colors that are used in that HaCkInG PrOgRaM
colors = {
    "green": "\033[92m",
    "red": "\033[91m",
    "white": "\033[0m",
    "blue": "\033[94m"
}


def loadingAnimation(text: str, seconds: int):
    if seconds > 0:
        # decrement [seconds] to recursively call this function
        seconds -= 1

        # animation
        os.system("cls")
        print(f"{text}{'.' * (int)(3 - (seconds%3))}")
        time.sleep(1)

        # call recursion
        loadingAnimation(text, seconds)


def someTests(testsNumber: int):
    # set color to green
    print(colors["green"], end="")

    # loop for printing
    for i in range(testsNumber):
        print(f"\nTest №{i} DONE")
        time.sleep(random.random() * 2 + 0.5)
    
    # set color to white
    print(colors["white"])


def startHacking():
    # loop that works until user presses Ctrl+C
    while True:
        try:
            # ask to start hacking
            if input("PRESS ENTER TO START HACKING") == "":
                # start animation of starting
                loadingAnimation(f"{colors['red']}STARTING", 3)
                
                # set color to blue
                print(colors["blue"])

                # use tree command to simulate hacking process
                os.system("tree ../../")

                # set color to white
                print(colors["white"])
        except KeyboardInterrupt:
            line = f"\n{'─' * 20}\n"

            # print funny text and stop the function if user pressed Ctrl+C
            print(f"\n{colors['green']}{line}YOU HACKED THE WORLD{line}{colors['white']}")
            return


print(colors["white"])
loadingAnimation("Loading", 2)
someTests(2)
startHacking()