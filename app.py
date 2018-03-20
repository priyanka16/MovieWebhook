from flask import Flask, request, jsonify, redirect, abort, make_response
from datetime import datetime,date,timedelta
from collections import OrderedDict
from random import randint

import json


app = Flask(__name__)

@app.route("/")
def homepage():
    return "This is just the start of the cinema world"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    return res

def processRequest(req):

    chatParameters = req.get("result").get("parameters")
    print(chatParameters)
    valid_params = {}
    for paramKey, paramValues in chatParameters.items():
        if paramValues != "":
            if "geo" not in paramKey:
                valid_params[paramKey] = paramValues
            else:
                valid_params["geo-region"] = paramValues

    print("Filtered params")
    print(valid_params)

    data_report = {}

    #Get the speech from response
    chatSpeech = req.get("result").get("fulfillment").get("speech")
    print(chatSpeech)

    return buildResponse(speech=chatSpeech, displayText=chatSpeech, data_metrics=data_report, source="priyanka's webhook",
                         responseCode=200)

def getMonthList(dates):
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
    total_months = lambda dt: dt.month + 12 * dt.year
    mlist = []
    for tot_m in range(total_months(start)-1, total_months(end)):
        y, m = divmod(tot_m, 12)
        mlist.append(datetime(y, m+1, 1).strftime("%b-%y"))
    return mlist

def buildResponse(speech, displayText, data_metrics, source, responseCode):
    print("BUILD RESPONSE")
    print({'speech': speech, 'displayText': displayText, 'data': data_metrics, 'source': source})
    return jsonify(
        {'speech': speech, 'displayText': displayText, 'data': data_metrics, 'source': source}), responseCode

if __name__ == '__main__':
    app.run()
