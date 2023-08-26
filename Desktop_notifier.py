from plyer import notification as np
import time


if __name__=='__main__':

    while True:
        np.notify(title="Keep Doing",
                  message="If you want to shine like a sun, first burn like a sun.",
                  timeout=30
                  )
        time.sleep(3600)
