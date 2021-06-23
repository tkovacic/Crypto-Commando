#cc_engine.py
#Author: Timothy Damir Kovacic
#Created 5/30/2021

import cbpro

import time
import logging
from datetime import date, datetime, timedelta
import os
import sys

import numpy as np
import tensorflow as tf

sys.path.append("./Settings");
import config
from cc_util import calculateFeatures, fitModel, generatePrediction, printInterface

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
def cc_cycle(market, model, volume, a, b):
    client = cbpro.AuthenticatedClient(config.API_KEY,config.API_SEC,config.API_PHR);

    rawFeatureSet = calculateFeatures(market, a, b, client);
    rawFeatureSet = rawFeatureSet.split("||");

    f1 = float(rawFeatureSet[0]);
    f2 = float(rawFeatureSet[1]);

    fitModel(market, model, f1, f2);
    printInterface(market, f1, f2);

    output = str(a) + "||" + str(b);
    return (output);
