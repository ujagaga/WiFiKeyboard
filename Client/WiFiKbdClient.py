#!/usr/bin/env python3

import os
import sys
import socket
import time
import json
import keyboard

CFG_PATH = os.path.join("~", ".wifikbd", "config.txt")


if os.path.isfile(CFG_PATH):
    cfg = open(CFG_PATH, "r")
    lines = cfg.readlines()
    cfg.close()

time.sleep(3)
keyboard.write('ab', 0.05)

