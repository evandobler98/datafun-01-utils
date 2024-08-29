''' ITERATION 3

Module: Dobler Data - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:
In this third iteration, I declare additional variables to show skills with different data types.
'''

#####################################
# Declare global variables - keep byline at the end 
# We will use this information in a smarter byline 
#####################################

# Boolean variable to indicate if the company has internation clients
has_international_clients: bool = True

# Boolean variable to indicate multiple languages offered
multiple_languages_offered: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 7

# Integer variable for amount of players per session
players_per_session: int = 4

# List of strings representing the skills offered by the company
skills_offered: list = ["Strength", "Agility", "Flexibility", "Speed"]

#List of strings representing highest grossing locations
highest_grossing_locations : list = ["Kansas City", "Dallas", "Miami", "Phoenix"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.2, 5.0, 4.8, 4.9, 4.9]

# List of floats representing top bat speeds before training
top_bat_speeds_before_training: list = [59.8, 62.4, 61.8, 63.4, 64.1]

# List of floats representing top bat speeds after training
top_bat_speeds_after_training: list = [61.2, 63.6, 62.9, 65.1, 65.7]

# List of floats representing positive changes in bat speeds
top_bat_speeds_change: list = [1.4, 1.2, 1.1, 1.7, 1.6]

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------
Dobler Data: Delivering Baseball Insights
---------------------------------------------------
Has International Clients:      {has_international_clients}
Years in Operation:             {years_in_operation}
Highest Grossing Locations:     {highest_grossing_locations}
Has Multiple Languages Offered: {multiple_languages_offered}
Skills Offered:                 {skills_offered}
Client Satisfaction Scores:     {client_satisfaction_scores}
Players Per Session:            {players_per_session}
Top Bat Speeds Before Training: {top_bat_speeds_before_training}
Top Bat Speeds After Training:  {top_bat_speeds_after_training}
Top Bat Speeds Change:          {top_bat_speeds_change}

"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline 

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution 
#####################################

if __name__ == '__main__':
    main()
