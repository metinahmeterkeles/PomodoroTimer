import time
import plyer

def notifications(title,message):

    plyer.notification.notify(title=title, message=message, app_icon=None, timeout=5, toast=False)


def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1

    notifications(title="Pomodoro Timer", message="Congratulations bro!! You working hard today!! Keep going :)")

t = input("How long will it take : ")

countdown(int(t))

