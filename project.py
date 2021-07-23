# pop mean = 6.134
# sampling mean 6.111

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import csv
import statistics

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)   

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)    
    return mean

def showFig(meanList):
    fig = ff.create_distplot(
        [meanList],
        ["average"],
        show_hist=False
    )
    
    mean = statistics.mean(meanList)
    
    fig.add_trace(
        go.Scatter(
            x = [mean, mean],
            y = [0, 1],
            mode = 'lines',
            name = "Mean"
        )
    )
    print(mean)
    
    fig.show()

def setUp():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(30)
        meanList.append(setOfMeans)
    sd = statistics.stdev(meanList)
    print(sd)
    print("---------")
    print(population_mean)
    showFig(meanList)
    
setUp()

