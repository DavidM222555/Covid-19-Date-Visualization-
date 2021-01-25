import DataPreparationFunctions as DPF

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import date # For parsing dates 

# Function that asks the user for states
def get_state_input():
    print("Please enter the states abbreviations you would like data for in a comma separated list.")
    print("For example, if you wanted data for Missouri, Alaska, and California enter MO,AK,CA")

    state_input = input()

    list_of_states = state_input.split(',')

    return list_of_states

# This function gets the day the user would like to have plotted
def get_chosen_data_attribute():
    print("Please enter the name of the attribute you would like to see plotted.")

    attribute_input = input()

    return attribute_input

# @return: A tuple containing the start and end date in MM/DD/YYYY format
def get_start_and_end_dates():
    print("Enter the start date in format MM/DD/YYYY:")
    start_date = input()

    delimited_start_date = start_date.split('/')

    print("Enter the ending date in format MM/DD/YYYY:")
    end_date = input()

    delimited_end_date = end_date.split('/')

    return (delimited_start_date, delimited_end_date)


# @param startingDate: the date you would like to begin plotting at in the format: MM/DD/YYYY
# @param endingDate: the date you would like to end plotting at in the format: MM/DD/YYYY
def plot_graph():
    list_of_states = get_state_input()
    data_attribute = get_chosen_data_attribute()

    # Creates a dataframe object that contains information for all the states
    # in list_of_states
    cd = DPF.Covid_Data("all-states-history.csv", list_of_states)

    # We then chose the column we want to get isolated information for
    specific_column = cd.get_data_from_column(data_attribute)

    for i in specific_column:
        x_values = np.arange(len(specific_column[i]))
        plt.plot(x_values, specific_column[i], label = i)
        
    # Matplotlib function for properly displaying the data.
    plt.xlabel("Days")
    plt.ylabel(data_attribute)
    plt.legend()
    plt.show()

plot_graph()
