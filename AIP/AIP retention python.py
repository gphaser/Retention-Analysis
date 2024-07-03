# This File serves to convert the AIP Retetion document into pyton form for data visulization and for GitHub updates 
# Comments such as these will be made either at key points along the code to inform readers or to serve as markers for updates
# print("hello world")

#install the necesary code to convert exel files and push to github
# used pip3 install pandas 
import pandas as pd
# imported matplot for data.
import matplotlib.pyplot as plt
import numpy as np 


# Read the Excel file into a pandas DataFrame
df = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/AIP Retention.xlsx")
# Specify the sheet name or index
Retention = 'Retention'  
Math = 'Math'
# Read data from the specified sheet
dfr = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/AIP Retention.xlsx", sheet_name=Retention) # Full Data set trimed for ease
dfm = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/AIP Retention.xlsx", sheet_name=Math) #simplified math data


# Now you can work with the data in the DataFrame
# print(dfm.head())  # Print the first few rows of the DataFrame
# print(dfm) # prints the data frame

#Push to git  using git push -u origin main ()

#Go to the Math Sheet via pandas and write code to make the graphs 
# need to select the rows 2-22 then for each of those make a histogram
# repeate process for rows in patters of 1 year, 2 year, 5 year, 10 year, 20 year so 2-3, 4-5,... 2-4, 5-7,... 2-7, 8-12, ... 2-12, 13-22 ... 2-22 
# use code df.loc[row wanted],or for multiple df.iloc[first row wanted:last row wanted]
#df.iloc[:, [1, 2, 5]] Select columns in positions 1, 2 and 5 (firstcolumn is 0).

num_rows = len(dfm)
print("Number of rows:", num_rows)
print("rember to uncoment recursion, and carnagee orginization and comment this line")

# generic histograms
# CURRENTLY PRODUCES HISTOGRAMS BUT NOT OF PROPER TYPE TO BE FIXED ASAP 4-5-24

def row_1(n):
    if n >= 20:
        print(n, "is this")
        # Selecting the row and columns B-F from DataFrame dfm
        selected_row = dfm.iloc[n,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        print(selected_row)
        # Plotting a histogram of the selected row
        # selected_row.plot.hist()
        plt.bar(categories, selected_row)
        # Add data labels above each bar
        for i, value in enumerate(selected_row):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.show() 
        print('end')
    else:
        print(n)
        # Selecting the row and columns B-F from DataFrame dfm
        selected_row = dfm.iloc[n,[1, 2, 3, 4, 5]]
        print(selected_row)
        # Plotting a histogram of the selected row
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        plt.bar(categories, selected_row)
        # Add data labels above each bar
        for i, value in enumerate(selected_row):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.show()  
        n = n + 1
        row_1(n)

def rows_2(n): 
    if n >= 20:
        print(n, "is this")
        #dfm.iloc[20,[1, 2, 3, 4, 5]] (wont need cause 19-20 has the 2 year)
        print('end')
    else: 
        print(n)
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.35
        plt.bar(x-bar_width/2, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x+bar_width/2, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width/2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row2):
            plt.text(i + bar_width/2, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+1))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+1
        print(n)
        rows_2(n)

def rows_5(n): 
    if n > 15:
        print(n, "final n")
        dfm.iloc[n:n+5,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print(n)
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        selected_row3 = dfm.iloc[n+2,[1, 2, 3, 4, 5]]
        selected_row4 = dfm.iloc[n+3,[1, 2, 3, 4, 5]]
        selected_row5 = dfm.iloc[n+4,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.1
        plt.bar(x-bar_width*4, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x-bar_width*3, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        plt.bar(x-bar_width*2, selected_row3, width=bar_width, label="Data for" + str(2002+n+2))
        plt.bar(x-bar_width, selected_row4, width=bar_width, label="Data for" + str(2002+n+3))
        plt.bar(x, selected_row5, width=bar_width, label="Data for" + str(2002+n+4))
        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width*4, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row2):
            plt.text(i - bar_width*3, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row3):
            plt.text(i - bar_width*2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row4):
            plt.text(i - bar_width, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row5):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+5))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+5
        print(n)
        rows_5(n)

def rows_10(n): 
    if n >= 11:
        print(n, "final n")
        dfm.iloc[n:n+10,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print(n)
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        selected_row3 = dfm.iloc[n+2,[1, 2, 3, 4, 5]]
        selected_row4 = dfm.iloc[n+3,[1, 2, 3, 4, 5]]
        selected_row5 = dfm.iloc[n+4,[1, 2, 3, 4, 5]]
        selected_row6 = dfm.iloc[n+5,[1, 2, 3, 4, 5]]
        selected_row7 = dfm.iloc[n+6,[1, 2, 3, 4, 5]]
        selected_row8 = dfm.iloc[n+7,[1, 2, 3, 4, 5]]
        selected_row9 = dfm.iloc[n+8,[1, 2, 3, 4, 5]]
        selected_row10 = dfm.iloc[n+9,[1, 2, 3, 4, 5]]
        selected_row11 = dfm.iloc[n+10,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.1
        plt.bar(x-bar_width*10, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x-bar_width*9, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        plt.bar(x-bar_width*8, selected_row3, width=bar_width, label="Data for" + str(2002+n+2))
        plt.bar(x-bar_width*7, selected_row4, width=bar_width, label="Data for" + str(2002+n+3))
        plt.bar(x-bar_width*6, selected_row5, width=bar_width, label="Data for" + str(2002+n+4))
        plt.bar(x-bar_width*5, selected_row6, width=bar_width, label="Data for" + str(2002+n+5))
        plt.bar(x-bar_width*4, selected_row7, width=bar_width, label="Data for" + str(2002+n+6))
        plt.bar(x-bar_width*3, selected_row8, width=bar_width, label="Data for" + str(2002+n+7))
        plt.bar(x-bar_width*2, selected_row9, width=bar_width, label="Data for" + str(2002+n+8), color='green')
        plt.bar(x-bar_width, selected_row10, width=bar_width, label="Data for" + str(2002+n+9),color='red' )
        plt.bar(x, selected_row11, width=bar_width, label="Data for" + str(2002+n+10),color= 'brown')

        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width*10, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row2):
            plt.text(i - bar_width*9, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row3):
            plt.text(i - bar_width*8, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row4):
            plt.text(i - bar_width*7, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row5):
            plt.text(i - bar_width*6, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row6):
            plt.text(i - bar_width*5, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row7):
            plt.text(i - bar_width*4, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row8):
            plt.text(i - bar_width*3, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row9):
            plt.text(i - bar_width*2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row10):
            plt.text(i - bar_width, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row11):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+10))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+10
        print(n)
        rows_10(n)
        # dfm.plot.hist()
        # print(dfm.plot.hist())

def rows_20(n): 
    if n >= 0:
        print(n, "final n")
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        selected_row3 = dfm.iloc[n+2,[1, 2, 3, 4, 5]]
        selected_row4 = dfm.iloc[n+3,[1, 2, 3, 4, 5]]
        selected_row5 = dfm.iloc[n+4,[1, 2, 3, 4, 5]]
        selected_row6 = dfm.iloc[n+5,[1, 2, 3, 4, 5]]
        selected_row7 = dfm.iloc[n+6,[1, 2, 3, 4, 5]]
        selected_row8 = dfm.iloc[n+7,[1, 2, 3, 4, 5]]
        selected_row9 = dfm.iloc[n+8,[1, 2, 3, 4, 5]]
        selected_row10 = dfm.iloc[n+9,[1, 2, 3, 4, 5]]
        selected_row11 = dfm.iloc[n+10,[1, 2, 3, 4, 5]]
        selected_row12 = dfm.iloc[n+11,[1, 2, 3, 4, 5]]
        selected_row13 = dfm.iloc[n+12,[1, 2, 3, 4, 5]]
        selected_row14 = dfm.iloc[n+13,[1, 2, 3, 4, 5]]
        selected_row15 = dfm.iloc[n+14,[1, 2, 3, 4, 5]]
        selected_row16 = dfm.iloc[n+15,[1, 2, 3, 4, 5]]
        selected_row17 = dfm.iloc[n+16,[1, 2, 3, 4, 5]]
        selected_row18 = dfm.iloc[n+17,[1, 2, 3, 4, 5]]
        selected_row19 = dfm.iloc[n+18,[1, 2, 3, 4, 5]]
        selected_row20 = dfm.iloc[n+19,[1, 2, 3, 4, 5]]
        selected_row21 = dfm.iloc[n+20,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.045
        plt.bar(x-bar_width*20, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x-bar_width*19, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        plt.bar(x-bar_width*18, selected_row3, width=bar_width, label="Data for" + str(2002+n+2))
        plt.bar(x-bar_width*17, selected_row4, width=bar_width, label="Data for" + str(2002+n+3))
        plt.bar(x-bar_width*16, selected_row5, width=bar_width, label="Data for" + str(2002+n+4))
        plt.bar(x-bar_width*15, selected_row6, width=bar_width, label="Data for" + str(2002+n+5))
        plt.bar(x-bar_width*14, selected_row7, width=bar_width, label="Data for" + str(2002+n+6))
        plt.bar(x-bar_width*13, selected_row8, width=bar_width, label="Data for" + str(2002+n+7))
        plt.bar(x-bar_width*12, selected_row9, width=bar_width, label="Data for" + str(2002+n+8), color='green')
        plt.bar(x-bar_width*11, selected_row10, width=bar_width, label="Data for" + str(2002+n+9),color='red' )
        plt.bar(x-bar_width*10, selected_row11, width=bar_width, label="Data for" + str(2002+n+10),color= 'brown')
        plt.bar(x-bar_width*9, selected_row12, width=bar_width, label="Data for" + str(2002+n+11))
        plt.bar(x-bar_width*8, selected_row13, width=bar_width, label="Data for" + str(2002+n+12))
        plt.bar(x-bar_width*7, selected_row14, width=bar_width, label="Data for" + str(2002+n+13))
        plt.bar(x-bar_width*6, selected_row15, width=bar_width, label="Data for" + str(2002+n+14))
        plt.bar(x-bar_width*5, selected_row16, width=bar_width, label="Data for" + str(2002+n+15))
        plt.bar(x-bar_width*4, selected_row17, width=bar_width, label="Data for" + str(2002+n+16))
        plt.bar(x-bar_width*3, selected_row18, width=bar_width, label="Data for" + str(2002+n+17))
        plt.bar(x-bar_width*2, selected_row19, width=bar_width, label="Data for" + str(2002+n+18), color='green')
        plt.bar(x-bar_width, selected_row20, width=bar_width, label="Data for" + str(2002+n+19),color='red' )
        plt.bar(x, selected_row21, width=bar_width, label="Data for" + str(2002+n+20),color= 'brown')

        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width*20, value + 1, str(value), ha='center', va='bottom')
        '''
        for i, value in enumerate(selected_row2):
            plt.text(i - bar_width*19, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row3):
            plt.text(i - bar_width*18, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row4):
            plt.text(i - bar_width*17, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row5):
            plt.text(i - bar_width*16, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row6):
            plt.text(i - bar_width*15, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row7):
            plt.text(i - bar_width*14, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row8):
            plt.text(i - bar_width*13, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row9):
            plt.text(i - bar_width*12, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row10):
            plt.text(i - bar_width*11, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row11):
            plt.text(i - bar_width*10, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row12):
            plt.text(i - bar_width*9, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row13):
            plt.text(i - bar_width*8, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row14):
            plt.text(i - bar_width*7, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row15):
            plt.text(i - bar_width*6, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row16):
            plt.text(i - bar_width*5, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row17):
            plt.text(i - bar_width*4, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row18):
            plt.text(i - bar_width*3, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row19):
            plt.text(i - bar_width*2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row20):
            plt.text(i - bar_width, value + 1, str(value), ha='center', va='bottom')
        '''    
        for i, value in enumerate(selected_row21):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+20))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+10
        print(n)
    else: 
        print("error")


# Calls for the recursion 
# row_1(0)
# rows_2(0)
# rows_5(0)
# rows_10(0)
rows_20(0)

# create data sets for the CARNAGE data classifies the US into 9 regions (in obreg collum):
# issue will have to use og data set, good news already have the stuff that i need to do it
# collum x for the obreg so need to be at 23 (increment form 0) over each year to create a adata set for each year
#Full data set (df)CODE, the following are the year break points 765, 1529, 2296, 3060, 3820, 4583, 5346, 6107, 6866, 7619, 8370, 
# 9123, 9875, 10627, 11378, 12138, 12899, 13667, 14430, 15185, 15931
#so will read over each line find what group it belongs to asign it to the apropriate data set for analysis 
# groups are 0-9 for the different regions

# Year breakpoints
year_breakpoints = [765, 1529, 2296, 3060, 3820, 4583, 5346, 6107, 6866, 7619, 8370, 
                    9123, 9875, 10627, 11378, 12138, 12899, 13667, 14430, 15185, 15931]

# GLOABAL VARIABLES
Grad_Total = 0
International = 0
Domestic = 0
First_year = 0
Degree_Master = 0
Degree_Phd = 0
Degree_Total = 0
Year_c = 0 

# Initialize a dictionary to hold datasets for each year
datasets = {}

# Iterate over each year

for i in range(len(year_breakpoints)):
    start_index = year_breakpoints[i-1] if i > 0 else 0
    end_index = year_breakpoints[i]
    
    # Create a dataset for the current year
    dfy = datasets[f"year_{i+1}"] = df.iloc[start_index:end_index]
    # grouping by the 'Carnege' column
    dfo = dfy.sort_values('obereg') # sorts dataset by obreg value
    # print(dfo)
    dfo0 = dfy[dfy['obereg'] == 0].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo0)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo0):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 0")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo0.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo0.iloc[n, 10]):
                Grad_Total += dfo0.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo0.iloc[n, 11]):
                International += dfo0.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo0.iloc[n, 12]):
                First_year += dfo0.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo0.iloc[n, 14]):    
                Degree_Master += dfo0.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo0.iloc[n, 15]):
                Degree_Phd += dfo0.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo1 = dfy[dfy['obereg'] == 1].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo1)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo1):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 1")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo1.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo1.iloc[n, 10]):
                Grad_Total += dfo1.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo1.iloc[n, 11]):
                International += dfo1.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo1.iloc[n, 12]):
                First_year += dfo1.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo1.iloc[n, 14]):    
                Degree_Master += dfo1.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo1.iloc[n, 15]):
                Degree_Phd += dfo1.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo2 = dfy[dfy['obereg'] == 2].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo2)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo2):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 2")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo2.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo2.iloc[n, 10]):
                Grad_Total += dfo2.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo2.iloc[n, 11]):
                International += dfo2.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo2.iloc[n, 12]):
                First_year += dfo2.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo2.iloc[n, 14]):    
                Degree_Master += dfo2.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo2.iloc[n, 15]):
                Degree_Phd += dfo2.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo3 = dfy[dfy['obereg'] == 3].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo3)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo3):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 3")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo3.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo3.iloc[n, 10]):
                Grad_Total += dfo3.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo3.iloc[n, 11]):
                International += dfo3.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo3.iloc[n, 12]):
                First_year += dfo3.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo3.iloc[n, 14]):    
                Degree_Master += dfo3.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo3.iloc[n, 15]):
                Degree_Phd += dfo3.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo4 = dfy[dfy['obereg'] == 4].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo4)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo4):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 4")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo4.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo4.iloc[n, 10]):
                Grad_Total += dfo4.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo4.iloc[n, 11]):
                International += dfo4.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo4.iloc[n, 12]):
                First_year += dfo4.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo4.iloc[n, 14]):    
                Degree_Master += dfo4.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo4.iloc[n, 15]):
                Degree_Phd += dfo4.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo5 = dfy[dfy['obereg'] == 5].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo5)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo5):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 5")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo5.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo5.iloc[n, 10]):
                Grad_Total += dfo5.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo5.iloc[n, 11]):
                International += dfo5.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo5.iloc[n, 12]):
                First_year += dfo5.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo5.iloc[n, 14]):    
                Degree_Master += dfo5.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo5.iloc[n, 15]):
                Degree_Phd += dfo5.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo6 = dfy[dfy['obereg'] == 6].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo6)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo6):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 6")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo6.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo6.iloc[n, 10]):
                Grad_Total += dfo6.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo6.iloc[n, 11]):
                International += dfo6.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo6.iloc[n, 12]):
                First_year += dfo6.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo6.iloc[n, 14]):    
                Degree_Master += dfo6.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo6.iloc[n, 15]):
                Degree_Phd += dfo6.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo7 = dfy[dfy['obereg'] == 7].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo7)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo7):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 7")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo7.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo7.iloc[n, 10]):
                Grad_Total += dfo7.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo7.iloc[n, 11]):
                International += dfo7.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo7.iloc[n, 12]):
                First_year += dfo7.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo7.iloc[n, 14]):    
                Degree_Master += dfo7.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo7.iloc[n, 15]):
                Degree_Phd += dfo7.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo8 = dfy[dfy['obereg'] == 8].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo8)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo8):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 8")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfo8.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo8.iloc[n, 10]):
                Grad_Total += dfo8.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo8.iloc[n, 11]):
                International += dfo8.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo8.iloc[n, 12]):
                First_year += dfo8.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo8.iloc[n, 14]):    
                Degree_Master += dfo8.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo8.iloc[n, 15]):
                Degree_Phd += dfo8.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfo9 = dfy[dfy['obereg'] == 9].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo9)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfo9):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for Obreg 9")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            Year_c += 1 
            print('end')
        else:
            print(n)
            selected_row = dfo9.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfo9.iloc[n, 10]):
                Grad_Total += dfo9.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfo9.iloc[n, 11]):
                International += dfo9.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfo9.iloc[n, 12]):
                First_year += dfo9.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfo9.iloc[n, 14]):    
                Degree_Master += dfo9.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfo9.iloc[n, 15]):
                Degree_Phd += dfo9.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)

'''
#iterate over Canrage Clasification
'''
Year_c = 0  
for i in range(len(year_breakpoints)):
    start_index = year_breakpoints[i-1] if i > 0 else 0
    end_index = year_breakpoints[i]
    
    # Create a dataset for the current year
    dfy = datasets[f"year_{i+1}"] = df.iloc[start_index:end_index]
    # Convert 'basic2021' column to numeric type, and removes errors
    dfy.loc[:, 'basic2021'] = pd.to_numeric(dfy['basic2021'], errors='coerce')
    # Sort the DataFrame by the 'basic2021' column
    dfc = dfy.sort_values('basic2021') # sorts dataset by basic2021 value 0-23, 27, 28, 32, 34, 35
    # print(dfc)
    dfc0 = dfy[dfy['basic2021'] == 0].sort_values('basic2021') # Creates a data frame for each year for the classifications
    print(dfc0)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc0):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c)+ " for 0")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc0.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc0.iloc[n, 10]):
                Grad_Total += dfc0.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc0.iloc[n, 11]):
                International += dfc0.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc0.iloc[n, 12]):
                First_year += dfc0.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc0.iloc[n, 14]):    
                Degree_Master += dfc0.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc0.iloc[n, 15]):
                Degree_Phd += dfc0.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc1 = dfy[dfy['basic2021'] == 1].sort_values('basic2021') # Creates a data frame for each year for the classifications
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc1):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 1")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc1.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc1.iloc[n, 10]):
                Grad_Total += dfc1.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc1.iloc[n, 11]):
                International += dfc1.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc1.iloc[n, 12]):
                First_year += dfc1.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc1.iloc[n, 14]):    
                Degree_Master += dfc1.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc1.iloc[n, 15]):
                Degree_Phd += dfc1.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    # print(dfc1)
    dfc2 = dfy[dfy['basic2021'] == 2].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc2)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc2):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 2")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc2.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc2.iloc[n, 10]):
                Grad_Total += dfc2.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc2.iloc[n, 11]):
                International += dfc2.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc2.iloc[n, 12]):
                First_year += dfc2.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc2.iloc[n, 14]):    
                Degree_Master += dfc2.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc2.iloc[n, 15]):
                Degree_Phd += dfc2.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc3 = dfy[dfy['basic2021'] == 3].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc3)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc3):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 3")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc3.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc3.iloc[n, 10]):
                Grad_Total += dfc3.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc3.iloc[n, 11]):
                International += dfc3.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc3.iloc[n, 12]):
                First_year += dfc3.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc3.iloc[n, 14]):    
                Degree_Master += dfc3.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc3.iloc[n, 15]):
                Degree_Phd += dfc3.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc4 = dfy[dfy['basic2021'] == 4].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc4)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc4):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 4")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc4.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc4.iloc[n, 10]):
                Grad_Total += dfc4.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc4.iloc[n, 11]):
                International += dfc4.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc4.iloc[n, 12]):
                First_year += dfc4.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc4.iloc[n, 14]):    
                Degree_Master += dfc4.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc4.iloc[n, 15]):
                Degree_Phd += dfc4.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc5 = dfy[dfy['basic2021'] == 5].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc5)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc5):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 5")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc5.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc5.iloc[n, 10]):
                Grad_Total += dfc5.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc5.iloc[n, 11]):
                International += dfc5.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc5.iloc[n, 12]):
                First_year += dfc5.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc5.iloc[n, 14]):    
                Degree_Master += dfc5.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc5.iloc[n, 15]):
                Degree_Phd += dfc5.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc6 = dfy[dfy['basic2021'] == 6].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc6)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc6):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 6")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc6.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc6.iloc[n, 10]):
                Grad_Total += dfc6.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc6.iloc[n, 11]):
                International += dfc6.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc6.iloc[n, 12]):
                First_year += dfc6.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc6.iloc[n, 14]):    
                Degree_Master += dfc6.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc6.iloc[n, 15]):
                Degree_Phd += dfc6.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc7 = dfy[dfy['basic2021'] == 7].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc7)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc7):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 7")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc7.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc7.iloc[n, 10]):
                Grad_Total += dfc7.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc7.iloc[n, 11]):
                International += dfc7.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc7.iloc[n, 12]):
                First_year += dfc7.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc7.iloc[n, 14]):    
                Degree_Master += dfc7.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc7.iloc[n, 15]):
                Degree_Phd += dfc7.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc8 = dfy[dfy['basic2021'] == 8].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc8)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc8):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 8")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc8.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc8.iloc[n, 10]):
                Grad_Total += dfc8.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc8.iloc[n, 11]):
                International += dfc8.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc8.iloc[n, 12]):
                First_year += dfc8.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc8.iloc[n, 14]):    
                Degree_Master += dfc8.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc8.iloc[n, 15]):
                Degree_Phd += dfc8.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc9 = dfy[dfy['basic2021'] == 9].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc9)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc9):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 9")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc9.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc9.iloc[n, 10]):
                Grad_Total += dfc9.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc9.iloc[n, 11]):
                International += dfc9.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc9.iloc[n, 12]):
                First_year += dfc9.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc9.iloc[n, 14]):    
                Degree_Master += dfc9.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc9.iloc[n, 15]):
                Degree_Phd += dfc9.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc10 = dfy[dfy['basic2021'] == 10].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc10)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc10):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 10")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc10.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc10.iloc[n, 10]):
                Grad_Total += dfc10.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc10.iloc[n, 11]):
                International += dfc10.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc10.iloc[n, 12]):
                First_year += dfc10.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc10.iloc[n, 14]):    
                Degree_Master += dfc10.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc10.iloc[n, 15]):
                Degree_Phd += dfc10.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc11 = dfy[dfy['basic2021'] == 11].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc11)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc11):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 11")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc11.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc11.iloc[n, 10]):
                Grad_Total += dfc11.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc11.iloc[n, 11]):
                International += dfc11.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc11.iloc[n, 12]):
                First_year += dfc11.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc11.iloc[n, 14]):    
                Degree_Master += dfc11.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc11.iloc[n, 15]):
                Degree_Phd += dfc11.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc12 = dfy[dfy['basic2021'] == 12].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc12)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc12):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 12")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc12.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc12.iloc[n, 10]):
                Grad_Total += dfc12.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc12.iloc[n, 11]):
                International += dfc12.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc12.iloc[n, 12]):
                First_year += dfc12.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc12.iloc[n, 14]):    
                Degree_Master += dfc12.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc12.iloc[n, 15]):
                Degree_Phd += dfc12.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc13 = dfy[dfy['basic2021'] == 13].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc13)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc13):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 13")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc13.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc13.iloc[n, 10]):
                Grad_Total += dfc13.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc13.iloc[n, 11]):
                International += dfc13.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc13.iloc[n, 12]):
                First_year += dfc13.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc13.iloc[n, 14]):    
                Degree_Master += dfc13.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc13.iloc[n, 15]):
                Degree_Phd += dfc13.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc14 = dfy[dfy['basic2021'] == 14].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc14)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc14):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 14")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc14.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc14.iloc[n, 10]):
                Grad_Total += dfc14.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc14.iloc[n, 11]):
                International += dfc14.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc14.iloc[n, 12]):
                First_year += dfc14.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc14.iloc[n, 14]):    
                Degree_Master += dfc14.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc14.iloc[n, 15]):
                Degree_Phd += dfc14.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc15 = dfy[dfy['basic2021'] == 15].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc15)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc15):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 15")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc15.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc15.iloc[n, 10]):
                Grad_Total += dfc15.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc15.iloc[n, 11]):
                International += dfc15.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc15.iloc[n, 12]):
                First_year += dfc15.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc15.iloc[n, 14]):    
                Degree_Master += dfc15.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc15.iloc[n, 15]):
                Degree_Phd += dfc15.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc16 = dfy[dfy['basic2021'] == 16].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc16)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc16):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 16")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc16.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc16.iloc[n, 10]):
                Grad_Total += dfc16.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc16.iloc[n, 11]):
                International += dfc16.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc16.iloc[n, 12]):
                First_year += dfc16.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc16.iloc[n, 14]):    
                Degree_Master += dfc16.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc16.iloc[n, 15]):
                Degree_Phd += dfc16.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc17 = dfy[dfy['basic2021'] == 17].sort_values('basic2021') # Creates a data frame for each year for the classifications
    print(dfc17)
    # num_rows = len(dfc17)
    # print("Number of rows:", num_rows)
        # histogran in each year
    # ISSUE GET RID OF NaN VALUES FOR THE GRAP
    # SOLUTION DROP NaN values USING IF STATEMENT
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc17):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 17")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc17.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc17.iloc[n, 10]):
                Grad_Total += dfc17.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc17.iloc[n, 11]):
                International += dfc17.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc17.iloc[n, 12]):
                First_year += dfc17.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc17.iloc[n, 14]):    
                Degree_Master += dfc17.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc17.iloc[n, 15]):
                Degree_Phd += dfc17.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc18 = dfy[dfy['basic2021'] == 18].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc18)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc18):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 18")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc18.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc18.iloc[n, 10]):
                Grad_Total += dfc18.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc18.iloc[n, 11]):
                International += dfc18.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc18.iloc[n, 12]):
                First_year += dfc18.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc18.iloc[n, 14]):    
                Degree_Master += dfc18.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc18.iloc[n, 15]):
                Degree_Phd += dfc18.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc19 = dfy[dfy['basic2021'] == 19].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc19)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc19):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 19")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc19.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc19.iloc[n, 10]):
                Grad_Total += dfc19.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc19.iloc[n, 11]):
                International += dfc19.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc19.iloc[n, 12]):
                First_year += dfc19.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc19.iloc[n, 14]):    
                Degree_Master += dfc19.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc19.iloc[n, 15]):
                Degree_Phd += dfc19.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc20 = dfy[dfy['basic2021'] == 20].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc20)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc20): 
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 20")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc20.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc20.iloc[n, 10]):
                Grad_Total += dfc20.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc20.iloc[n, 11]):
                International += dfc20.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc20.iloc[n, 12]):
                First_year += dfc20.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc20.iloc[n, 14]):    
                Degree_Master += dfc20.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc20.iloc[n, 15]):
                Degree_Phd += dfc20.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc21 = dfy[dfy['basic2021'] == 21].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc21)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc21):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 21")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0 
            print('end')
        else:
            print(n)
            selected_row = dfc21.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc21.iloc[n, 10]):
                Grad_Total += dfc21.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc21.iloc[n, 11]):
                International += dfc21.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc21.iloc[n, 12]):
                First_year += dfc21.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc21.iloc[n, 14]):    
                Degree_Master += dfc21.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc21.iloc[n, 15]):
                Degree_Phd += dfc21.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc22 = dfy[dfy['basic2021'] == 22].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc22)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc22):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 22")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc22.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc22.iloc[n, 10]):
                Grad_Total += dfc22.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc22.iloc[n, 11]):
                International += dfc22.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc22.iloc[n, 12]):
                First_year += dfc22.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc22.iloc[n, 14]):    
                Degree_Master += dfc22.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc22.iloc[n, 15]):
                Degree_Phd += dfc22.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc23 = dfy[dfy['basic2021'] == 23].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc23)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc23):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 23")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc23.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc23.iloc[n, 10]):
                Grad_Total += dfc23.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc23.iloc[n, 11]):
                International += dfc23.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc23.iloc[n, 12]):
                First_year += dfc23.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc23.iloc[n, 14]):    
                Degree_Master += dfc23.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc23.iloc[n, 15]):
                Degree_Phd += dfc23.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc27 = dfy[dfy['basic2021'] == 27].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc27)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc27):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 27")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc27.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc27.iloc[n, 10]):
                Grad_Total += dfc27.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc27.iloc[n, 11]):
                International += dfc27.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc27.iloc[n, 12]):
                First_year += dfc27.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc27.iloc[n, 14]):    
                Degree_Master += dfc27.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc27.iloc[n, 15]):
                Degree_Phd += dfc27.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc28 = dfy[dfy['basic2021'] == 28].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc28)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc28):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 28")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc28.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc28.iloc[n, 10]):
                Grad_Total += dfc28.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc28.iloc[n, 11]):
                International += dfc28.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc28.iloc[n, 12]):
                First_year += dfc28.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc28.iloc[n, 14]):    
                Degree_Master += dfc28.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc28.iloc[n, 15]):
                Degree_Phd += dfc28.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc32 = dfy[dfy['basic2021'] == 32].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc32)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc32):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 32")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc32.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc32.iloc[n, 10]):
                Grad_Total += dfc32.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc32.iloc[n, 11]):
                International += dfc32.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc32.iloc[n, 12]):
                First_year += dfc32.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc32.iloc[n, 14]):    
                Degree_Master += dfc32.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc32.iloc[n, 15]):
                Degree_Phd += dfc32.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc34 = dfy[dfy['basic2021'] == 34].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc34)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc34):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 34")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            print('end')
        else:
            print(n)
            selected_row = dfc34.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc34.iloc[n, 10]):
                Grad_Total += dfc34.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc34.iloc[n, 11]):
                International += dfc17.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc34.iloc[n, 12]):
                First_year += dfc34.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc34.iloc[n, 14]):    
                Degree_Master += dfc34.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc34.iloc[n, 15]):
                Degree_Phd += dfc34.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)
    dfc35 = dfy[dfy['basic2021'] == 35].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc35)
    def row_1(n):
        global Grad_Total
        global International 
        global Domestic 
        global First_year
        global Degree_Master
        global Degree_Phd
        global Degree_Total
        global Year_c
        if n >= len(dfc35):
            print(n, "is this")
            print(Grad_Total)
            print(International)
            print(First_year)
            print(Degree_Total)

            categories = ['GRAD Total', 'International', 'Domestic', 'First year', 'DEGREE TOTAL']
            values = [Grad_Total, International, Grad_Total - International, First_year, Degree_Total]
            
            plt.bar(categories, values)
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+Year_c) + " for 35")
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            Grad_Total = 0
            International = 0 
            Domestic = 0
            First_year = 0 
            Degree_Master = 0
            Degree_Phd = 0
            Degree_Total = 0
            Year_c += 1 
            print('end')
        else:
            print(n)
            selected_row = dfc35.iloc[n, [10, 11, 12, 14, 15]]
            print(selected_row)
            if pd.notnull(dfc35.iloc[n, 10]):
                Grad_Total += dfc35.iloc[n, 10]
            else:
                Grad_Total = Grad_Total
            if pd.notnull(dfc35.iloc[n, 11]):
                International += dfc35.iloc[n, 11]
            else:
                International = International
            if pd.notnull(dfc35.iloc[n, 12]):
                First_year += dfc35.iloc[n, 12]
            else: 
                First_year = First_year
            if pd.notnull(dfc35.iloc[n, 14]):    
                Degree_Master += dfc35.iloc[n, 14]
            else:
                Degree_Master = Degree_Master
            if pd.notnull(dfc35.iloc[n, 15]):
                Degree_Phd += dfc35.iloc[n, 15]
            else:
                Degree_Phd = Degree_Phd
            Degree_Total = Degree_Master + Degree_Phd
            print("Values after updating:")
            print("Grad_Total:", Grad_Total)
            print("International:", International)
            print("First_year:", First_year)
            print("Degree_Total:", Degree_Total)
            n = n + 1
            row_1(n)
    row_1(0)


#SO now with data frames for obreg regional clasifications and frames for carnagee now need to do histograms for them following the inital set
# LOOK AT ROWS K, L, M, O, P for 'GRAD Total', 'International', 'Domestic','First year','DEGREE Master', 'Degree PHD' 
# So rows 10, 11, 12, 14, 15 





# Calls for the recursion 
# row_1(0)
# rows_2(0)
# rows_5(0)
# rows_10(0)
# rows_20(0)


# CURRENT WORK GRAPHS for new organization

#Current Issue Histograms for new data are working, but only for 1 year at a time
# 

#CURRENT ISSUE 
#Data has visualization issues (overlaping text)


# OLD ISSUES
    # HISTOGRAMS NOT PRINTING OUT 
        # FIXED BY ADDING MATPLOT
    # Git HUB not working 
        # FIX USE THE FOLLOWING TO PUSH
            # git add /Users/Chris/Desktop/Codeing/PER/AIP
            # git commit -m "stuff"
            # git push origin main
    #Current Issue Histograms produced are not correct 
        #Fixed: using bar and group bar graphs    
    #Current Issue Histograms produced are not correct 
        #Sollution: redo the basic matplot code 
    # Histograms for new data are working but not right 
        # FIXED AND FUNCTIONAL