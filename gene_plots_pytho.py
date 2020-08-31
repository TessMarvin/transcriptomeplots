import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import *
#Usage: gene_fun(gene_name, pathways_to_each_csv_file_you_wish_to_include)
#This function can take from 1 to 7 csv files and create one scatter plot of transcription over a time course
#It would be useful if your file naming convention is malariaisolatelog2anythinghere.csv
#e.g. NHP4026log2imputedtimecourse.csv
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
#/Users/tessmarvin/Desktop/TranscriptomePlots/time_courses/NF54GFPlog2imputedtimecourse.csv
#/Users/tessmarvin/Desktop/TranscriptomePlots/time_courses/NF54log2imputedtimecourse.csv
#/Users/tessmarvin/Desktop/TranscriptomePlots/time_courses/NHP4026log2imputedtimecourse.csv
#PF3D7_0406200
root = Tk()
def clicking1():
    CSVs = int(num_CSV.get())
    instruct = Label(root, text = "Enter pathway to CSV files:")
    instruct.grid(row=5, column = 0, pady=5)
    for num in range(CSVs):
        path = Entry(root)
        path.grid(row=6+num, column=0)
        list_of_pathways.append(path)
    button2 = Button(root, text="Enter", command= clicking2)
    button2.grid(row=6+CSVs, column=0)        
def clicking2():
    str_path = []
    for p in list_of_pathways:
        str_path.append(p.get())  
    gene_fun(gofint.get(), str_path)
#setting the name of the GUI
root.title('Gene Expression Scatter Plot')
root.geometry("600x500")
#need to ask for gene of interest
gene_instruct = Label(root, text = "Please enter gene of interest")
gene_instruct.grid(row=0, column = 0, pady=5)
#intake gene of interest
gofint = Entry(root)
gofint.grid(row=1, column=0, pady=5)
#need to ask how many CSV files to analyze to put up correct number of boxes 
instruct1 = Label(root, text = "How many CSV files would you like to analyze?")
instruct1.grid(row=2, column=0, pady=5)
#here we start to create the text boxes for gene name and file entry 
num_CSV = Entry(root)
num_CSV.grid(row=3, column = 0, pady=5)
list_of_pathways = []
button = Button(root, text="Enter", command= clicking1)
button.grid(row=4, column=0, pady=5)

root.mainloop()