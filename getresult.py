from loadanxiety import *
from loaddep import *
import pandas as pd 
from idtweet import *

def backtogui(inpdata):
    usertxt=[]
    maintxt = " "
    if '@' in inpdata:
        inpdata = inpdata.replace('@','')
        data1 = collect(inpdata)
        for i in data1:
            maintxt = maintxt + str(i) + "\n \nRESULT: "
            sen = predict_sentiment(i)
            maintxt = maintxt + str(sen) + "\n              " 
            sen = predict_sentiment1(i)
            maintxt = maintxt + str(sen) + "\n \n"

    else:
        usertxt = usertxt + [inpdata]
        for j in usertxt:
            maintxt = maintxt + str(j) + "\n \nRESULT: "
            sen = predict_sentiment(j)
            maintxt = maintxt + str(sen) + "\n              "
            sen = predict_sentiment1(j)
            maintxt = maintxt + str(sen)
    return maintxt