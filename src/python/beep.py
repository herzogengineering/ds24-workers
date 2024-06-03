import winsound

def beep(frequency=2000, duration=300):
    winsound.Beep(frequency, duration)



if __name__ == "__main__":
    print(beep(2000, 300))
