#cc_engine.py
#Author: Timothy Damir Kovacic
#Created 5/30/2021

import cbpro

import time
import logging
from datetime import date, datetime, timedelta
import os
import config
import sys

import numpy as np
import tensorflow as tf
from cc_gas import cc_burn

#variables
global OKCYAN;
OKCYAN = '\033[96m';
global OKGREEN;
OKGREEN = '\033[92m';
global FAIL;
FAIL = '\033[91m';
global WARN;
WARN = '\033[93m';

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d:%H:%M:%S',level=logging.ERROR);
logger = logging.getLogger(__name__);

#functions
def cc_cycle(a, b, c, d, e, f, g):
    try:
        return cc_burn(a, b, c, d, e, f, g);
    except Exception as e:
        logging.error('Caught exception: ' + str(e));
