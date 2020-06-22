#!/usr/bin/env python3
from threading import Timer
import time
import psutil

WAIT_SECONDS = 1


def repeat_per_second():
    """
    Collects system data every second, and dumps the contents to an external file called output.
    NOTE: This script is compatible with UNIX systems.
    :return:
    """
    # sends current time to the terminal as a working flag
    print(time.ctime())

    Timer(WAIT_SECONDS, repeat_per_second).start()

    # 'Getting system load average...'
    # percentage representation
    average_data = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    # 'Getting virtual memory data...'
    memory = psutil.virtual_memory()
    # 'Getting temperature data...'
    temperature = psutil.sensors_temperatures()

    output_string = f'{time.ctime()}\n{average_data}\n{memory}\n{temperature}'

    with open('output', 'w') as file:
        file.write(output_string)


if __name__ == '__main__':
    repeat_per_second()
