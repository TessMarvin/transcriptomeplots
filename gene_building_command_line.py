#Author: Tess Marvin (tmarvin@nd.edu)
#Usage: python gene_building_command_line.py gene path-to-files/*.csv
#The path to the files for analysis can be absolute or relative
#e.g. python gene_building_command_line.py PF3D7_0406200 ./time_courses/*.csv
###
#Usage (via stdin): echo path-to-files/*.csv | python gene_building_command_line.py gene
#e.g. echo -n ./time_courses/*.csv | python gene_building_command_line.py PF3D7_0406200
###
#This function can take from 1 to 7 csv files and create one scatter plot of transcription over a time course
#It would be useful if your file naming convention is malariaisolatelog2anythinghere.csv
#e.g. NHP4026log2imputedtimecourse.csv
import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import *
import sys

def gene_fun(gene, csv_files):
    #first check to make sure the gene is in every CSV file provided
    #if the gene name has been misspelled, then the user will be notified
    for file in csv_files:
        data_c = pd.read_csv(file)
        if gene not in data_c:
            print('Please enter correct gene name')
            return(None)
#This is the plotting function -- must be abstract to accept up to 7 csv files at once
    color_list = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    num = 0

    been_thru = False
    for file in csv_files:
        date = pd.read_csv(file)
        #this is how to splice the malaria isolate name from the csv file name
        top, bot = os.path.split(file)
        isolate, b =bot.split('log2')
        if not been_thru:
            pl = date.plot(kind='scatter', x='Time', y=gene, color=color_list[num], figsize = [7,7], title = gene, label = isolate)
            num += 1
            been_thru = True
        else:
            name = date.plot(kind='scatter', x='Time', y=gene, color=color_list[num], label = isolate, ax = pl)
            name.set(xlabel = 'Time (hrs)', ylabel= 'Log2 (Fold Change)')
            num += 1
    plt.show()
#the first argument is the gene name
#next, the user can either list the CSV files individually or use a wildcard for argv[2:]
#or the files can be passed in by stdin as part of a pipeline
def main():
    gene = str(sys.argv[1])
    CSVs = sys.argv[2:]
    #if files are passed in as a part of a pipeline (stdin)
    if len(CSVs) == 0:
        files = list(sys.stdin)
        new_list = files[0].split()
        gene_fun(gene, new_list)
    else:
        gene_fun(gene, CSVs)

if __name__ == '__main__':
   main()
