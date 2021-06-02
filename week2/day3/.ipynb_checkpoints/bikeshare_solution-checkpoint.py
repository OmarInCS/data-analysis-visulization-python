import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ["all", "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december"]

DAYS = ["all", "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"]


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
    city = input("[+] Enter a city name: ")
    while city not in CITY_DATA:
        print("[-] Invalid input")
        city = input("[+] Enter a city name: ")

    # get user input for month (all, january, february, ... , june)
    month = input("[+] Enter a month name: ")
    while month not in MONTHS:
        print("[-] Invalid input")
        month = input("[+] Enter a month name: ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("[+] Enter a day name: ")
    while day not in DAYS:
        print("[-] Invalid input")
        day = input("[+] Enter a day name: ")

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
    month = MONTHS.index(month)
    day = DAYS.index(day) - 1

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    
    if month != 0 and day != -1:
        mask = (df["Start Time"].dt.month == month) & (df["Start Time"].dt.dayofweek == day)
        return df[mask] 
    elif month != 0:
        mask = (df["Start Time"].dt.month == month)
        return df[mask]
    elif day != -1:
        mask = (df["Start Time"].dt.dayofweek == day)
        return df[mask]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df["Start Time"].dt.month.mode()
    common_day = df["Start Time"].dt.dayofweek.mode()
    common_hour = df["Start Time"].dt.hour.mode()
    
    
    # display the most common month
    if not common_month.empty:
        print("[+] The most common month: ", common_month[0])


    # display the most common day of week
    if not common_day.empty:
        print("[+] The most common day of week: ", common_day[0])

    # display the most common start hour
    if not common_hour.empty:
        print("[+] The most common start hour: ", common_hour[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("[+] most commonly used start station: ", df["Start Station"].mode()[0])

    # display most commonly used end station
    print("[+] most commonly used end station: ", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    s, e = df[["Start Station", "End Station"]].mode().values[0]
    print("[+] most frequent combination of start station and end station trip: ", s, e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("[+] total travel time:", df["Trip Duration"].sum())

    # display mean travel time
    print("[+] mean travel time:", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df["User Type"].value_counts()
    print("[+] counts of user types:")
    for u_type, u_count in zip(user_counts.index, user_counts):
        print("\t", u_type, ":", u_count)

    # Display counts of gender
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        print("[+] counts of gender:")
        for g_type, g_count in zip(gender_counts.index, gender_counts):
            print("\t", g_type, ":", g_count)

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("[+] Earliest year of birth:", df["Birth Year"].min())
        print("[+] Most recent year of birth:", df["Birth Year"].max())
        print("[+] Most common year of birth:", df["Birth Year"].mode()[0])

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
