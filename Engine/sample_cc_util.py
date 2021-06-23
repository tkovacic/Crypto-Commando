#cc_engine.py
#Author: Timothy Damir Kovacic
#Created 5/30/2021

import cbpro

import time
import logging
from datetime import date, datetime, timedelta
from pytz import timezone
import matplotlib.pyplot as plt
import os
import sys

import numpy as np
import tensorflow as tf

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
eastern = timezone('US/Eastern');

global shortLength;
shortLength = 1;
global longLength;
longLength = 5;
global granularity;
granularity = 300;

#functions
def ingestShortData(market, client):
    sDateTime = datetime.now(eastern).isoformat();
    eDateTime = (datetime.now(eastern)-timedelta(minutes=shortLength)).isoformat();
    data = [];
    for rates in client.get_product_historic_rates(str(market),str(eDateTime),str(sDateTime),granularity):
        data.append(rates[4]);
    return data;

def ingestLongData(market, client):
    sDateTime = datetime.now(eastern).isoformat();
    eDateTime = (datetime.now(eastern)-timedelta(minutes=longLength)).isoformat();
    data = [];
    for rates in client.get_product_historic_rates(str(market),str(eDateTime),str(sDateTime),granularity):
        data.append(rates[4]);
    return data;

def fetchCurrentQuote(market, client):
    bids = client.get_product_order_book(str(market));
    q = bids["bids"][0][0];

    return str(q);

def calculateFeatures(market, tbp, tsp, client):
    rawShortData = ingestShortData(market, client);
    rawLongData = ingestLongData(market, client);

    q = float(fetchCurrentQuote(market, client));

    output = str(tbp) + "||" + str(tsp);
    return output;

def persistModel(market, model):
elif(market=="GRT-USD"):
        model.save("Models/dnnGRTModel.h5");

def fitModel(market, model, tbp, tsp, q):
    xTrain = [tbp,tsp];
    yTrain = [q];

    xTrain = np.asarray(xTrain).astype('float32');
    yTrain = np.asarray(yTrain).astype('float32');

    xTrain = np.reshape(xTrain, (1, 1, 2));
    yTrain = np.reshape(yTrain, (1, 1, 1));

    model.fit(xTrain, yTrain, epochs=5, batch_size=1, verbose=0);
    persistModel(market, model);

def printInterface(market, f1, f2):
    print(OKCYAN + str(market);
    print(OKCYAN + "==============================")
    print(FAIL + str(f1) + OKCYAN + " / " + OKGREEN + str(f2));
    print(OKCYAN);
