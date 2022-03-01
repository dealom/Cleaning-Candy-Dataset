# <center> Dataset Cleaning w/ Pandas </center>

## Purpose
The purpose of this project is to practice dataset cleaning using pandas. I use various functions to clean a dataset so I can perform exploratory data analysis on it later on.

## Requirements and Structure
The most important files are cleaningfunctions.py and cleaningwithfunctions.ipynb. The cleaningfunctions.py file contains the functions used to clean the dataset and the cleaningwithfunctions.ipynb is a notebook that shows how the functions are being used. It also includes some visualizations. The other files contain the raw data, information about the raw data, or general testing.

## Example Dataset Description
I am cleaning the 2015 Candy Hierachy dataset from https://www.scq.ubc.ca/so-much-candy-data-seriously/. This dataset was mentioned on https://makingnoiseandhearingthings.com/2018/04/19/datasets-for-data-cleaning-practice/. It has 5630 rows and 124 columns. The data is made up of responses to a large survey about candy. Therefore, most columns have "JOY" or "DESPAIR" in response to certain candy. There are also some short responses.

## Custom Functions
All of the custom functions are in the cleaningfunctions.py.

The 'numberofNAs' function prints out the number of NA values for each column. I did not use this in my data analysis but this information is useful to see which questions are being answered and which ones aren't. In this dataset specifically, if a candy evokes a neutral feeling, it's counted as an NA on the csv. It's unclear if there's a bunch of NAs on the candy questions because people are neutral towards it or people don't know what they are. On the other hand, it is clear that not a lot of people responded to the "Please leave any remarks or comments regarding your choices" question. Maybe because it requires a written response and it's an optional question.

The 'validateages' function gets rid of responses that can't be turned into a number. Then it changes the remaining responses to a float value. I used this function because people included words as their age. This function could be used for any column that is supposed to only have numbers, but has words as well.

The 'groupages' function returns a specificed subset of the dataframe based on age. It's used to see if different age groups respond to questions differently.

The 'findoutliers' function is used to find outliers in the data. In this specific case, 'outlier' is a value that has a z-score greater than 3.

The 'joypercentages' function prints out the number of JOY responses, DESPAIR responses, and the ratio of JOY responses to JOY and DESPAIR responses for each candy. It also returns the ratio of the total amount of JOY respones to the total amount of JOY and DESPAIR responses. 

## Descriptive Statistics
The mean age in this dataset is 36.8 years old. The median is 35. The mode is 35. The standard deviation is 11.3.

## Future Work/Improvements
I could do more analysis with the NA values.
I could make the joypercentage functions more generalized so it can be used for other survey response data that only has a small amount of options. 