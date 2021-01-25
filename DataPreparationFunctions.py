# The functions in this file are used to prepare the data that we
# will display for the user with the functions in the Covid19Visualization.py file

import pandas as pd
import numpy as np

# We use default dict for creating a list of values for multiple states
from collections import defaultdict 

class Covid_Data:
    def __init__(self, data_file, list_of_states):
        self.list_of_states = list_of_states
        self.covid_df = pd.read_csv(data_file)
    
    def add_state(self, state_initials):
        self.list_of_states.append(state_initials)

    # Purpose: Gets all the data from the column_name for our associated list
    # of states.
    # Returns a default dictionary with a key of a state's name and a value of 
    # an np array of the data for the given column name
    def get_data_from_column(self, column_name):
        covid_data_for_states = defaultdict(np.array)

        # Iterate over all the states we have to get data for
        for x in self.list_of_states:
            covid_data_for_states[x] = self.get_data_for_state(x, column_name)

        return covid_data_for_states

    # A helper function for the get_data_from_column.
    # This function works by getting the np.array of values for a single state.
    def get_data_for_state(self, state_name, column_name):
        
        # Gives us the dataframe for a given state
        state_data = self.covid_df.loc[self.covid_df['state'] == state_name]

        # We now prune that state data further.
        # This function assumes that the data follows the format in the given
        # file: all-states-history.csv. 
        state_data = np.array(state_data[column_name][::-1], dtype='float')

        # We now have to remove NaN values.
        state_data = state_data[~np.isnan(state_data)]

        return state_data

