'''
1. Get Script codes from BSE
2. Use Script codes/tickers to get data from Yfinance!
'''

import json
import pdb

import yfinance as yf
# goog = yf.Ticker(['ABB','AMARAJABAT')
# history = goog.history(period='max')
# import pdb;pdb.set_trace()
# print(history)
# Get list of tickers from BSE!
from bsedata.bse import BSE

#print(b.getScripCodes())

# for BSE API, I could use some No SQL-Data!!

# I Can NoSql data, Mongo or something, just to store things.
# Either I can use Mongo or Python Later?

# Output:
# Driver Class for Bombay Stock Exchange (BSE)
# to execute "updateScripCodes" on instantiation
# Output too large to display in docs
# returns a dictionary with scrip codes as keys and respective company names as values
#data = yf.download(['GOOG','META'], period='1mo')
#data.head()

# Get BSe data, read from CSV files.
# Then get list of Stocks in BSE,
# try to calculate BSE number with price of stock
# get list of bse price securities
import requests
url = "https://api.bseindia.com/BseIndiaAPI/api/ListofScripData/w?Group=&Scripcode=&industry=&segment=Equity&status=Active"
backup_data = "/home/quantum-machine/Desktop/Python_Script_Analysis/bse_data.json"
backup_data_quotes = "/home/quantum-machine/Desktop/Python_Script_Analysis/bse_data_quotes3.json"

def get_quotes(security_code):
    b = BSE()
    try:
        quotes_data = b.getQuote(security_code)
        print(quotes_data)
    except Exception as InvalidStockException:
        print("ExceptionIvalidStock",InvalidStockException)
        return {}
    return quotes_data

def save_quotes(backup_data_quotes, quotes_data):
    with open(backup_data_quotes, "r+") as file:
        data = json.load(file)
        data.append(quotes_data)
        file.seek(0)
        json.dump(data, file)
        print("Data_Saved!")
    return "Done"

def save_json(data, file_name):
    try:
        with open(file_name,'w') as f:
            f.write(json.dumps(data.json()))
    except Exception as e:
        print(e)

def read_json(backup_data):
    try:
        with open(backup_data,'r') as f:
            data = json.loads(f.read())
    except FileNotFoundError as e:
        print("File Not Found!", e)
    return data

def get_bse_data(url, backup_data):
    try:
        data = requests.get(url)
        if data.status_code == 200:
            save_json(data, backup_data)
            #save_json(data.json(), backup_data)
            return data
        elif data.status_code != 200:
            print("Not able to get successful Response, Reading From JSON")
            try:
                data = read_json(backup_data)
            except FileNotFoundError as e:
                print("File Not Found!", e)
            return data
    except Exception as e:
        print("Not able to Do anything!!", e)

data = get_bse_data(url, backup_data)
#import pdb;pdb.set_trace()
script_codes = [code['SCRIP_CD'] for code in data]
#print(len(script_codes))
ticker_list = [code["scrip_id"] for code in data]
#ticker_list = ticker_list[:5]
ticker_list = [str(i)+'.BO' for i in ticker_list]
#ticker_list = ticker_list[:20]
#get_fundamentals = [yf.Ticker(i) for i in ticker_list]
print("working on getting data.............")
#get_fundamentals = [i.info for i in get_fundamentals]
#import pdb;pdb.set_trace()
#info_data_list = [yf.Ticker(ticker) for ticker in ticker_list]
info_data_list = []
for ticker in ticker_list:
    print("Getting Data for Ticker:-", ticker)
    info_data_list.append(yf.Ticker(ticker))
fundamental_data_list = []
#fundamental_data_list = [info.info for info in info_data_list]
for info in info_data_list:
    print("Getting Data for for Following")
    print("INFO:::", info.info)
    fundamental_data_list.append(info.info)
# iterate through all the fundamental_data_list and remove bad Data
features_removed = ["maxAge", "shortName", "longName", "exchangeTimezoneName",
                    "exchangeTimezoneShortName", "isEsgPopulated", "quoteType",
                    "symbol", "uuid", "market", "currency"]
for entry, ticker in zip(fundamental_data_list, ticker_list):
    for key,value in dict(entry).items():
        if value is None or value == 'none' or value == '':
            del entry[key]
    entry['stock'] = ticker
fundamental_data_list = [entry.pop(key) for key in features_removed for entry in fundamental_data_list]
fundamental_data = "/home/quantum-machine/Desktop/Python_Script_Analysis/fundamentals_data.json"
try:
    with open(fundamental_data, 'w') as f:
        f.write(json.dumps(fundamental_data_list))
except Exception as e:
    print(e)

#print("Done!!")
#import pdb;pdb.set_trace()
#print(GetFacebookInformation.info)
# data = yf.download(
#
#     tickers=ticker_list,
#     period='max',
#     threads=True,  # Set thread value to true
#     group_by='ticker',
# )
# data.to_json('ohlc-group.json')
# make a Plan that How to download and use this data on Analysing Alpha!!

#https://analyzingalpha.com/yfinance-python

# quotes_data = []
# print(reversed(script_codes))
#
# print("last script code",script_codes[-1])
# counter = 0
# bad_counter = 0

# Need to be dependent on this one to learn/understand more things!!

# for security_code in reversed(script_codes):
#     import time;time.sleep(2)
#     quotes_data = get_quotes(security_code)
#     if not quotes_data:
#         bad_counter += 1
#     save_quotes(backup_data_quotes, quotes_data)
#     counter += 1
#     print(counter)
#
# # Need to use these IDs with Y-Finance Data!!
# scrip_id = [code['scrip_id'] for code in data]