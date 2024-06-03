import psutil


def get_cpu_percent():
    try:
        # Get cpu percent for each core
        percent = psutil.cpu_percent(interval=1, percpu=True)
        return percent

    except (AttributeError, KeyError):
        print("Unable to retrieve CPU percent.")
        return None


if __name__ == "__main__":
    print(get_cpu_percent())
