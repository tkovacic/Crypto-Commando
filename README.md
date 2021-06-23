<div align="center">
  <h1>Crypto Commando Trader</h1>
  <p>Automated python based cryptographic trading engine built using algorithmic indicators and market fitted deep neural networking models commissioned through CoinBase Pro API Platform by Tim Kovacic using CBPro SDK by DanPaguin</p><br>
  <img src="https://static.wixstatic.com/media/c11e26_98214627f32540f7939870093be0a03b~mv2.png/v1/fill/w_560,h_456,al_c,q_85,usm_0.66_1.00_0.01/vectorstock_19626918_edited.webp">
</div>
<br>

# Prerequisites
1) Download and Install Git Bash Terminal (https://gitforwindows.org/)
2) Download and Install Python (https://www.python.org/downloads/)
3) Execute:
```
  pip install cbpro
  pip install tensorflow==2.5.0
  pip install numpy
  pip install pandas
```
4) Copy the 'example-config.py' in the 'Source/Util' directory and rename the copy to 'config.py' and fill out with your Coinbase Pro API token information
```
- API_KEY
- API_SECRET
- API_PASSPHRASE
```
5) Compile Tensorflow Keras model(s) saved to 'Source/Brokers/' with the expected input_shape of (1,5) as H5 format 'dnn[Market-Code]Model.h5' for each market you are wishing to monitor and trade (https://www.tensorflow.org/api_docs/python/tf)
```
model = Sequential();
model.add(LSTM(units=10, return_sequences=True, input_shape=(1, 5)));
model.add(Dense(units=1));
model.compile(optimizer='adam', loss='mean_squared_error');
```
- Example: 'dnnBTCModel.h5' to monitor the BTC market or 'dnnADAModel.h5' to monitor the ADA market
```
model.save("dnnBTCModel.h5");
model.save("dnnADAModel.h5");
```
6) Copy the file called 'example-cc_gas.py' in Source/Util/ and rename the copy to 'cc_gas.py'

# Instructions
 1) Open a new Git Bash Terminal in 'Source/Brokers/'
 2) Identify which market group(s) you wish to monitor:
 - Market Group Broker (MGB) Alpha: 1INCH, AAVE, ADA, ALGO, ANKR, BTC, COMP, DASH, ENJ, and EOS
 - Market Group Broker (MGB) Beta: ATOM, BAND, BAT, BCH, BNT, ETC, ETH, GRT, ICP, and KNC
 - Market Group Broker (MGB) Charlie: LINK, LTC, MANA, MATIC, MIR, MKR, NKN, OGN, OMG, and OXT
 - Market Group Broker (MGB) Delta: REP, RLC, SNX, STORJ, SUSHI, NU, XLM, XTZ, ZEC, and ZRX
 - Market Group Broker (MGB) Echo: CGLD, FORTH, LRC, NMR, UMA, BAL, FIL, REN, UNI, and YFI
 - Market Group Broker (MGB) Fox: CRV, TRB, SKL, CTSI
 3) In each of your interested market group broker files comment out any market where a corresponding H5 model file has not been supplied
 ```
 # inchModel = tf.keras.models.load_model("dnn1INCHModel.h5");
 # print("Loaded 1INCH DNN model!");
 
 aaveModel = tf.keras.models.load_model("dnnAAVEModel.h5");
 print("Loaded AAVE DNN model!");
 
 # try:
 #     os.system('cls');
 #     output = cc_cycle("1INCH-USD",inchModel,tv1,demastate1,tbp1,tsp1,cc1);
 #     output = str(output).split(",");
 #     demastate1 = output[0];
 #     tbp1 = output[1];
 #     tsp1 = output[2];
 #     cc1 = output[3];
 #     time.sleep(1 - ((time.time() - st) % 1));
 # except Exception as e:
 #     logging.error('Caught exception: ' + str(e));
 
 try:
     output = cc_cycle("AAVE-USD",aaveModel,tv2,demastate2,tbp2,tsp2,cc2);
     output = str(output).split(",");
     demastate2 = output[0];
     tbp2 = output[1];
     tsp2 = output[2];
     cc2 = output[3];
     time.sleep(1 - ((time.time() - st) % 1));
 except Exception as e:
     logging.error('Caught exception: ' + str(e));
 ```
 4) Run the specific market group broker file by executing 'python cc_mgb_XYZ.py'
 ```
 python cc_mgb_alpha.py
 python cc_mgb_beta.py
 python cc_mgb_charlie.py
 python cc_mgb_delta.py
 python cc_mgb_echo.py
 python cc_mgb_fox.py
 ```
 <div align="center">
 ![image](https://user-images.githubusercontent.com/20195504/123038591-b478e180-d3be-11eb-8220-f7f1871284ce.png)
 </div>
 
 # Configuration
 1) 'Source/Brokers' Open up a specific market group broker python script:
 - Modify 'increment_pace' to adjust how frequently the monitor runs every second (default: 300)
 - Modify 'tv' to adjust the target volume size of coin that is bought and sold across the different monitored markets (default: varies)

 # Troubleshooting
 1) "ERROR [cc_engine.py:191] Caught exception: could not convert string to float: a" is recieved when you have set your shortLengh or longLength too long and the granularity too low so there is too much data for the CBPro API to return and will fail
 2) "ERROR [cc_engine.py:239] Caught exception: 'bids' ERROR [cc_mgb_beta.py:179] Caught exception: list index out of range ERROR [cc_engine.py:191] Caught exception: could not convert string to float: a" is recieved when you have set your increment_pace too short so that the multiple API calls being generated exceed the 10 per second limit and will fail
 3) A sell or buy order will not go through if the respective coin or fiat is not present to afford the transaction and will fail but will still cycle the engine and adjust the targeted prices
 4) Some tv (target volume) for a market can only be set so low before it will not be transacted across CBPro...some markets require a minimum 5 USD or 10 USD etc conversion

 # Future Features
 1) Email and text notification of configured events
 2) Capture and analysis of sources to derive and integrate fundemental indicators
 
 # Credits
 shout out to the cbpro SDK made by https://github.com/danpaquin from https://github.com/danpaquin/coinbasepro-python/blob/master/cbpro/public_client.py
