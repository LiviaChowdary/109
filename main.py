import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
datalist = df["reading score"].tolist()

mean = statistics.mean(datalist)
std_dev = statistics.stdev(datalist)
median = statistics.median(datalist)
mode = statistics.mode(datalist)

std1_dev_start, std1_dev_end = mean-std_dev, mean+std_dev
std2_dev_start, std2_dev_end = mean-(2*std_dev), mean+(2*std_dev)
std3_dev_start, std3_dev_end = mean-(3*std_dev), mean+(3*std_dev)

list_1_std_dev = [result for result in datalist if result > std1_dev_start and result < std1_dev_end]
list_2_std_dev = [result for result in datalist if result > std2_dev_start and result < std2_dev_end]
list_3_std_dev = [result for result in datalist if result > std3_dev_start and result < std3_dev_end]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_dev))
print("{}% of data lies within 1 standard deviation".format(len(list_1_std_dev)*100.0/len(datalist)))
print("{}% of data lies within 2 standard deviations".format(len(list_2_std_dev)*100.0/len(datalist)))
print("{}% of data lies within 3 standard deviations".format(len(list_3_std_dev)*100.0/len(datalist)))
