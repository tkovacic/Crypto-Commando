#example-cc_gas.py
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

global shortLength;
shortLength = 10;
global granularity;
granularity = 300;
global ccLimit;
ccLimit = 20;

#functions
def cc_burn(market, model, volume, demaState, tbp, tsp, cc, client):
    try:
        data = [];
        tzDateTime = datetime.today().isoformat();
        taDateTime = (datetime.today()-timedelta(minutes=shortLength)).isoformat();


        for rates in client.get_product_historic_rates(str(market),str(taDateTime),str(tzDateTime),granularity):
            data.append(rates[4]);

        buyCondition = False;
        sellCondition = False;

        bids = client.get_product_order_book(str(market));
        q = bids["bids"][0][0];

        if(sellCondition):
            client.place_market_order(str(market),"sell",str(volume));
            tbp = q;
            cc = 0;
        elif(buyCondition):
            client.place_market_order(str(market),"buy",str(volume));
            tsp = q;
            cc = 0;
        else:
            cc = cc + 1;

        var1 = 0;
        var2 = 0;
        var3 = 0;
        var4 = 0;
        var5 = 0;

        xTrain = [var1,var2,var3,var4,var5];
        yTrain = [q];

        xTrain = np.asarray(xTrain).astype('float32');
        yTrain = np.asarray(yTrain).astype('float32');

        xTrain = np.reshape(xTrain, (1, 1, xTrain.shape[0]));
        yTrain = np.reshape(yTrain, (yTrain.shape[0], 1));

        reconstructed_model = model;

        reconstructed_model.fit(xTrain, yTrain, epochs=200, batch_size=1, verbose=0);

        if(market=="1INCH-USD"):
            reconstructed_model.save("dnn1INCHModel.h5");
        elif(market=="AAVE-USD"):
            reconstructed_model.save("dnnAAVEModel.h5");
        elif(market=="ADA-USD"):
            reconstructed_model.save("dnnADAModel.h5");
        elif(market=="DOT-USD"):
            reconstructed_model.save("dnnDOTModel.h5");
        elif(market=="ALGO-USD"):
            reconstructed_model.save("dnnALGOModel.h5");
        elif(market=="ANKR-USD"):
            reconstructed_model.save("dnnANKRModel.h5");
        elif(market=="BTC-USD"):
            reconstructed_model.save("dnnBTCModel.h5");
        elif(market=="COMP-USD"):
            reconstructed_model.save("dnnCOMPModel.h5");
        elif(market=="DASH-USD"):
            reconstructed_model.save("dnnDASHModel.h5");
        elif(market=="ENJ-USD"):
            reconstructed_model.save("dnnENJModel.h5");
        elif(market=="EOS-USD"):
            reconstructed_model.save("dnnEOSModel.h5");
        elif(market=="ATOM-USD"):
            reconstructed_model.save("dnnATOMModel.h5");
        elif(market=="BAND-USD"):
            reconstructed_model.save("dnnBANDModel.h5");
        elif(market=="BAT-USD"):
            reconstructed_model.save("dnnBATModel.h5");
        elif(market=="BCH-USD"):
            reconstructed_model.save("dnnBCHModel.h5");
        elif(market=="BNT-USD"):
            reconstructed_model.save("dnnBNTModel.h5");
        elif(market=="ETC-USD"):
            reconstructed_model.save("dnnETCModel.h5");
        elif(market=="ETH-USD"):
            reconstructed_model.save("dnnETHModel.h5");
        elif(market=="GRT-USD"):
            reconstructed_model.save("dnnGRTModel.h5");
        elif(market=="ICP-USD"):
            reconstructed_model.save("dnnICPModel.h5");
        elif(market=="KNC-USD"):
            reconstructed_model.save("dnnKNCModel.h5");
        elif(market=="LINK-USD"):
            reconstructed_model.save("dnnLINKModel.h5");
        elif(market=="LTC-USD"):
            reconstructed_model.save("dnnLTCModel.h5");
        elif(market=="MANA-USD"):
            reconstructed_model.save("dnnMANAModel.h5");
        elif(market=="MATIC-USD"):
            reconstructed_model.save("dnnMATICModel.h5");
        elif(market=="MIR-USD"):
            reconstructed_model.save("dnnMIRModel.h5");
        elif(market=="MKR-USD"):
            reconstructed_model.save("dnnMKRModel.h5");
        elif(market=="NKN-USD"):
            reconstructed_model.save("dnnNKNModel.h5");
        elif(market=="OGN-USD"):
            reconstructed_model.save("dnnOGNModel.h5");
        elif(market=="OMG-USD"):
            reconstructed_model.save("dnnOMGModel.h5");
        elif(market=="OXT-USD"):
            reconstructed_model.save("dnnOXTModel.h5");
        elif(market=="REP-USD"):
            reconstructed_model.save("dnnREPModel.h5");
        elif(market=="RLC-USD"):
            reconstructed_model.save("dnnRLCModel.h5");
        elif(market=="SNX-USD"):
            reconstructed_model.save("dnnSNXModel.h5");
        elif(market=="STORJ-USD"):
            reconstructed_model.save("dnnSTORJModel.h5");
        elif(market=="SUSHI-USD"):
            reconstructed_model.save("dnnSUSHIModel.h5");
        elif(market=="ZRX-USD"):
            reconstructed_model.save("dnnZRXModel.h5");
        elif(market=="NU-USD"):
            reconstructed_model.save("dnnNUModel.h5");
        elif(market=="XLM-USD"):
            reconstructed_model.save("dnnXLMModel.h5");
        elif(market=="XTZ-USD"):
            reconstructed_model.save("dnnXTZModel.h5");
        elif(market=="ZEC-USD"):
            reconstructed_model.save("dnnZECModel.h5");
        elif(market=="CGLD-USD"):
            reconstructed_model.save("dnnCGLDModel.h5");
        elif(market=="FORTH-USD"):
            reconstructed_model.save("dnnFORTHModel.h5");
        elif(market=="LRC-USD"):
            reconstructed_model.save("dnnLRCModel.h5");
        elif(market=="NMR-USD"):
            reconstructed_model.save("dnnNMRModel.h5");
        elif(market=="UMA-USD"):
            reconstructed_model.save("dnnUMAModel.h5");
        elif(market=="BAL-USD"):
            reconstructed_model.save("dnnBALModel.h5");
        elif(market=="FIL-USD"):
            reconstructed_model.save("dnnFILModel.h5");
        elif(market=="REN-USD"):
            reconstructed_model.save("dnnRENModel.h5");
        elif(market=="UNI-USD"):
            reconstructed_model.save("dnnUNIModel.h5");
        elif(market=="YFI-USD"):
            reconstructed_model.save("dnnYFIModel.h5");
        elif(market=="CRV-USD"):
            reconstructed_model.save("dnnCRVModel.h5");
        elif(market=="TRB-USD"):
            reconstructed_model.save("dnnTRBModel.h5");
        elif(market=="SKL-USD"):
            reconstructed_model.save("dnnSKLModel.h5");
        elif(market=="CTSI-USD"):
            reconstructed_model.save("dnnCTSIModel.h5");

        output = str(demaState) + "," + str(tbp) + "," + str(tsp) + "," + str(cc);
        return (output);
    except Exception as e:
        logging.error('Caught exception: ' + str(e));
