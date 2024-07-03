# AIP TRIMED 
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
df = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/Cleaned AIP Retention.xlsx")
# Specify the sheet name or index

filtered_data = df[df['year'] > 2001] 

# Group by 'obereg' and 'year' and perform aggregation 

filtered_data = df[df['year'] > 2001] 

grouped_data = filtered_data.groupby(['obereg', 'year']).agg(
    n=('year', 'count'),
    total_grad=('grad_total', 'sum'),
    total_international=('grad_foreign', 'sum'),
    total_first=('grad_first', 'sum'),
    total_mast=('degree_m', 'sum'),
    total_phd=('degree_p', 'sum')
).reset_index()


# Calculate total_domestic and total_degree columns
grouped_data['total_domestic'] = grouped_data['total_grad'] - grouped_data['total_international']
grouped_data['total_degree'] = grouped_data['total_mast'] + grouped_data['total_phd']

grouped_data = grouped_data.sort_values(by=['obereg', 'year']) 

grouped_data['total_lost'] = (-grouped_data['total_grad'] + grouped_data['total_first'] -  

                             grouped_data['total_degree'] + grouped_data['total_grad'].shift(1))

grouped_data.dropna(inplace=True)


grouped_data = grouped_data[grouped_data['year'] > 2002]

total_atrition = grouped_data['total_lost']/grouped_data['total_grad'] * 100 
total_retention = 100 - total_atrition

print('Total ATRITION %', total_atrition)
print('Total RETENTION %', total_retention)

# print(grouped_data['total_lost'])

unique_obereg = grouped_data['obereg'].unique()

# Plot each unique 'obereg' group separately
for obereg_value in unique_obereg:
    obereg_group = grouped_data[grouped_data['obereg'] == obereg_value]
    
    # Create a new figure for each plot
    plt.figure(figsize=(10, 6))
    
    # Plot the data
    plt.plot(obereg_group['year'], obereg_group['total_grad'], label='Total Graduates')
    plt.plot(obereg_group['year'], obereg_group['total_international'], label='Total International Graduates')
    plt.plot(obereg_group['year'], obereg_group['total_domestic'], label='Total Domestic Graduates')
    plt.plot(obereg_group['year'], obereg_group['total_first'], label='Total First Years')
    plt.plot(obereg_group['year'], obereg_group['total_degree'], label='Total Degrees Earned')
    plt.plot(obereg_group['year'], obereg_group['total_lost'], label='Retention Value')

    #print('Total ATRITION %', total_atrition)
    #print('Total RETENTION %', total_retention)
    
    
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Graduates')
    plt.title(f'Total Graduates Over the Years - {obereg_value}')
    #plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1))
    plt.legend()
    plt.grid(True)
    
    # Show plot
    #plt.tight_layout()
    plt.show()


# Group by 'basic' and 'year' and perform aggregation 

grouped_data = filtered_data.groupby(['basic2021', 'year']).agg(
    n=('year', 'count'),
    total_grad=('grad_total', 'sum'),
    total_international=('grad_foreign', 'sum'),
    total_first=('grad_first', 'sum'),
    total_mast=('degree_m', 'sum'),
    total_phd=('degree_p', 'sum')
).reset_index()

# Calculate total_domestic and total_degree columns
grouped_data['total_domestic'] = grouped_data['total_grad'] - grouped_data['total_international']
grouped_data['total_degree'] = grouped_data['total_mast'] + grouped_data['total_phd']

grouped_data['total_lost'] = (-grouped_data['total_grad'] + grouped_data['total_first'] -  

                             grouped_data['total_degree'] + grouped_data['total_grad'].shift(1))

grouped_data.dropna(inplace=True)

grouped_data = grouped_data[grouped_data['year'] > 2002]

total_atrition = grouped_data['total_lost']/grouped_data['total_grad'] * 100 
total_retention = 100 - total_atrition

print('Total ATRITION %', total_atrition)
print('Total RETENTION %', total_retention)

# print(grouped_data) 

import matplotlib.pyplot as plt

# Filter the grouped_data DataFrame
filtered_grouped_data = grouped_data[(grouped_data['basic2021'] >= 12) & (grouped_data['basic2021'] <= 20)]

# Get unique values in the 'basic2021' column after filtering
unique_basic2021 = filtered_grouped_data['basic2021'].unique()

# Plot each unique 'basic2021' group separately
for basic2021_value in unique_basic2021:
    basic2021_group = filtered_grouped_data[filtered_grouped_data['basic2021'] == basic2021_value]
    
    # Create a new figure for each plot
    plt.figure(figsize=(10, 6))
    
    # Plot the data
    plt.plot(basic2021_group['year'], basic2021_group['total_grad'], label='Total Graduates')
    plt.plot(basic2021_group['year'], basic2021_group['total_international'], label='Total International Graduates')
    plt.plot(basic2021_group['year'], basic2021_group['total_domestic'], label='Total Domestic Graduates')
    plt.plot(basic2021_group['year'], basic2021_group['total_first'], label='Total First Year')
    plt.plot(basic2021_group['year'], basic2021_group['total_degree'], label='Total Degrees')
    plt.plot(basic2021_group['year'], basic2021_group['total_lost'], label='Retention Value')
    
   # print('Total ATRITION %', total_atrition)
   # print('Total RETENTION %', total_retention)     

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Graduates')
    plt.title(f'Total Graduates Over the Years - Basic2021: {basic2021_value}')
    #plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1)) 
    plt.legend()
    plt.grid(True)
    
    # Show plot
    #plt.tight_layout()
    plt.show()


# SEE IF I CAN GET A CLEAN 10 year



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
