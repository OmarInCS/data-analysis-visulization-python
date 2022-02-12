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
    city = input("Enter city (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        print("invalid city")
        city = input("Enter city (chicago, new york city, washington): ").lower()
    
    # get user input for month (all, january, february, ... , june)
    month = input("Enter month (all, january, february, ... , june): ").lower()
    while month not in MONTHS:
        print("invalid month")
        month = input("Enter month (all, january, february, ... , june): ").lower()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()
    while day not in DAYS:
        print("invalid day")
        day = input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()

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
    
    df = pd.read_csv("data/" + CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    if month == "all" and day == "all":
        return df
    
    if month != "all":
        mask = df["Start Time"].dt.month_name() == month.title()
        df = df[mask]

    elif day != "all":
        mask = df["Start Time"].dt.day_name() == day.title()
        df = df[mask]
    
    print(df.sample(5))
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["Start Time"].dt.month_name().mode()[0]
    print("the most common month: ", common_month)
    

    # display the most common day of week
    common_day = df["Start Time"].dt.day_name().mode()[0]
    print("the most common day of week: ", common_day)
    

    # display the most common start hour
    common_hour = df["Start Time"].dt.hour.mode()[0]
    print("the most common start hour: ", common_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common = df["Start Station"].mode()[0]
    print("the commonly used start station: ", common)
    
    # display most commonly used end station
    common = df["End Station"].mode()[0]
    print("the commonly used end station: ", common)
    
    # display most frequent combination of start station and end station trip
    common = df[["Start Station", "End Station"]].value_counts().index[0]
    print("the most frequent combination of start station and end station trip: ", common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    # display mean travel time
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    

    # Display counts of gender
    
    # Display earliest, most recent, and most common year of birth
        


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
