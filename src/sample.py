from datetime import datetime


def current_time():
    """
    This function tells the current time.
    :return: None
    """
    print("Current Time is : " + str(datetime.now()))


current_time()
