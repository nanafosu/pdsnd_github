import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
              
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

# TO DO: get user input for city (chicago, new york city, washington)
    print("Would you like to see data from:")
    print("1. Chicago")
    print("2. New York City")
    print("3. Washington")
    while True:
        try:
            selection=int(input("Enter a number to choose a city:\n"))
            if selection==1:
                city='chicago'
                break
            elif selection==2:
                city='new york city'
                break
            elif selection==3:
                city='washington'
                break
            else:
                print("Invalid Choice. Enter 1-3")
                get_filters()
        except ValueError:
            print("Invalid Option. Enter 1-3")
    options = ["both", "month", "day"]

# TO DO: Print out the options
    for i in range(len(options)):
        print(str(i+1) + ":", options[i])

# TO DO: Take user input for filtering type from the list
    inp = int(input("Would you like to filter by month, day or both. Enter a number:\n "))
    if inp in range(1, 4):
        if inp==1:
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            while True:
                month=input("Which month? january, february, march, april, may or june.\n")
                if month not in months:
                    continue
                else:
                    break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            week_days=[1,2,3,4,5,6,7]
            while True:
                try:
                    day=int(input("Which day? Please enter day as integer (eg. 1=Monday)\n"))
                    if day not in week_days:
                        print("Please enter an integer from 1-7:\n")
                        continue
                    else:
                        break
                except ValueError:
                    print("Not an integer! Try again.")
                    continue

# TO DO: get user input for month (all, january, february, ... , june)
        elif inp==2:
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            while True:
                month=input("Which month? january, february, march, april, may or june.\n")
                if month not in months:
                    continue
                else:
                    break
            day='all'

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif inp==3:
            week_days=[1,2,3,4,5,6,7]
            while True:
                try:
                    day=int(input("Which day? Please enter day as integer (eg. 1=Monday)\n"))
                    if day not in week_days:
                        print("Please enter an integer in 1-7:\n")
                        continue
                    else:
                        break
                except ValueError:
                    print("Please enter day as an integer(Eg. 1=Sunday). Enter 1-7\n")
                    continue
            month='all'
    else:
        print("Invalid input!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day-=1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month", most_common_month)

# TO DO: display the most common day of week
    most_common_weekday=df['day_of_week'].mode()[0]
    print("Most common weekday:", most_common_weekday)

# TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# TO DO: display most commonly used start station
    most_common_starttime=df['Start Time'].mode()[0]
    print("Most common Start Time:", most_common_starttime)

# TO DO: display most commonly used end station
    most_common_endtime=df['End Time'].mode()[0]
    print("Most common End Time:", most_common_endtime)

# TO DO: display most frequent combination of start station and end station trip
    freq_startendtrip_combination = df[['Start Station','End Station']].mode().loc[0]
    print("Most frequent combination of start station and end station trip:", freq_startendtrip_combination)
   
   print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# TO DO: display total travel time
    total_travel=sum(df['Trip Duration'])
    print("Total travel time:", total_travel)

# TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# TO DO: Compute statistical data
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

# TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print("Counts of user types:\n", user_type)

# TO DO: Display counts of gender
    if city == 'washington':
        pass
    else:
        gender_type=df['Gender'].value_counts()
        print("Counts of gender:\n", gender_type)

# TO DO: Display earliest, most recent, and most common year of birth
        birth_year=max(df['Birth Year'].mode())
        print("The earliest, most recent and most common year of birth: ", birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
  
def display_raw_data(df):
    choice_yes=['yes','y','Yes', 'YES','Y']
    choice_no=['no','No','NO','n','N']

# TO DO: Display individual raw data by user
    while True:
        view=input("Would you like to view individual data?\nyes or no:" )
        if view in choice_yes:
            rand_data=df.sample(n=5)
            print(rand_data.head())
            continue
        elif view in choice_no:
            break
        else:
            print("Please answer Yes or No:\n")
        continue
    return rand_data
    
    
# TO DO: Call all other functions to interact with user
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart the analysis? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()