import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ("all", "january", "february", "march", "april", "may" , "june")
DAYS = ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while city not in CITY_DATA:
        city = input("Enter a city (chicago, new york city, washington): ").lower()
        

    # get user input for month (all, january, february, ... , june)
    month = None
    while month not in MONTHS:
        month = input("Enter a month (all, january, february, ... , june): ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day not in DAYS:
        day = input("Enter a day of week (all, monday, tuesday, ... sunday): ").lower()
    

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
    
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    if month == "all" and day == "all":
        return df
    
    if month != "all":
        mask = df["Start Time"].dt.month_name() == month.title()
        df = df[mask]
        
    if day != "all":
        mask = df["Start Time"].dt.day_name() == day.title()
        df = df[mask]
        
    print(df.head())
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df["Start Time"].dt.month_name().mode()[0]
    print("The most common month: ", month)
    

    # display the most common day of week
    day = df["Start Time"].dt.day_name().mode()[0]
    print("The most common day of week: ", day)

    # display the most common start hour
    hour = df["Start Time"].dt.hour.mode()[0]
    print("The most common start hour: ", hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    result = df["Start Station"].mode()[0]
    print("The most commonly used start station: ", result)

    # display most commonly used end station
    result = df["End Station"].mode()[0]
    print("The most commonly used end station: ", result)

    # display most frequent combination of start station and end station trip
    result = df[["Start Station", "End Station"]].value_counts().index[0]
    print("The most frequent combination of start station and end station trip: ", result)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df["Trip Duration"].sum()
    print("total travel time: ", total)

    # display mean travel time
    mean = df["Trip Duration"].mean()
    print("mean travel time: ", mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    result = df["User Type"].value_counts()
    print("counts of user types:")
    for idx in result.index:
        print(f"\t\t{idx}: {result[idx]}")
    print()

    # Display counts of gender
    if "Gender" in df:
        result = df["Gender"].value_counts()
        print("counts of gender:")
        for idx in result.index:
            print(f"\t\t{idx}: {result[idx]}")
    print()

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        result = df["Birth Year"].mode()[0]
        print("most common year of birth:", result)
        result = df["Birth Year"].max()
        print("most recent year of birth:", result)
        result = df["Birth Year"].min()
        print("earliest year of birth:", result)
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
