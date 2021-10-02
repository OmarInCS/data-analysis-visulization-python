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
    city = input("Enter city (chicago, new york city, washington): ")
    while city not in CITY_DATA:
        print("invalid city")
        city = input("Enter city (chicago, new york city, washington): ")


    # get user input for month (all, january, february, ... , june)
    month = input("Enter month (all, january, february, ... , june): ").lower()
    while month not in MONTHS:
        print("Invalid input")
        month = input("Enter month (all, january, february, ... , june): ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()
    while day not in DAYS:
        print("Invalid input")
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
    
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    month_idx = MONTHS.index(month)
    day_idx = DAYS.index(day)
    
    if month_idx == 0 and day_idx == 0:
#         print(df.head())
        return df
    
    if month_idx != 0:
        mask = df["Start Time"].dt.month == month_idx
        df = df[mask]
        
    if day_idx != 0:
        mask = df["Start Time"].dt.dayofweek == day_idx
        df = df[mask]


#     print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df["Start Time"].dt.month_name().mode()
    print("most common month: ", month[0])


    # display the most common day of week
    day = df["Start Time"].dt.day_name().mode()
    print("most common day: ", day[0])


    # display the most common start hour
    hour = df["Start Time"].dt.hour.mode()
    print("most common hour: ", hour[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


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
