#!/usr/bin/python3
import subprocess

def connect_hint():
    print("please do: \nsudo snap connect hwlog:time-control;sudo snap connect hwlog:hardware-observe")

def system(command):
    return subprocess.check_output(command).decode('utf-8').strip()

def hwlog_main():
    print("uptime: {0}".format(system("uptime")))
    print("hwclock: {0}".format(system(["hwclock","--utc","--noadjfile"])))



