from sys import argv
from time import sleep

from pyautogui import click, locateOnScreen, locateAllOnScreen, scroll


def follow() -> None:
    while running < 5:
        locations = locateAllOnScreen('./follow.png', confidence=0.85)

        if not locations:
            running += 1

        for location in locations:
            click(location)

            sleep(1)
        scroll(-200)


def unfollow() -> None:
    while running < 5:
        locations = locateAllOnScreen('./unfollow.png', confidence=0.85)

        if not locations:
            running += 1

        for location in locations:
            click(location)
            sleep(1)

            click(locateOnScreen('./confirm.png', confidence=0.9))

            sleep(1)
        scroll(-200)


def main():
    global running
    running = 0

    if argv[1] == 'follow':
        follow()

    elif argv[1] == 'unfollow':
        unfollow()

    else:
        return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
