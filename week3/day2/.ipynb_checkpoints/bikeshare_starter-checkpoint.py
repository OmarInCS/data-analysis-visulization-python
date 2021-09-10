import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = [
    "all",
    "january",
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
    "december"
]

DAYS = [
    "all",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

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
    city = input("Enter input for city (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        print("Invalid input")
        city = input("Enter input for city (chicago, new york city, washington): ").lower() 

    # get user input for month (all, january, february, ... , june)
    month = input("Enter input for month (all, january, february, ... , june): ").lower()
    while month not in MONTHS:
        print("Invalid input")
        month = input("Enter input for month (all, january, february, ... , june): ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter input for day of week (all, monday, tuesday, ... sunday): ").lower()
    while day not in DAYS:
        print("Invalid input")
        day = input("Enter input for day of week (all, monday, tuesday, ... sunday): ").lower()

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
    
    file_path = "data/" + CITY_DATA[city]
    month_idx = MONTHS.index(month)
    day_idx = DAYS.index(day)
    
    df = pd.read_csv(file_path)
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    if month_idx == 0 and day_idx == 0:
        return df
    
    if month_idx != 0 and day_idx == 0:
        mask = df["Start Time"].dt.month == month_idx
        df = df[mask]
    
    if month_idx == 0 and day_idx != 0:
        mask = df["Start Time"].dt.dayofweek == day_idx - 1
        df = df[mask]
    
    if month_idx != 0 and day_idx != 0:
        mask = (df["Start Time"].dt.month == month_idx) & (df["Start Time"].dt.dayofweek == day_idx - 1)
        df = df[mask]
        
    print(df.head())


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["Start Time"].dt.month_name().mode()
    print("[+] Most common month: ", common_month[0])

    # display the most common day of week
    common_day = df["Start Time"].dt.day_name().mode()
    print("[+] Most common day: ", common_day[0])

    # display the most common start hour
    common_hour = df["Start Time"].dt.hour.mode()
    print("[+] Most common hour: ", common_hour[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_ss = df["Start Station"].mode()
    print("[+] Most common Start Station: ", common_ss[0])


    # display most commonly used end station
    common_es = df["End Station"].mode()
    print("[+] Most common End Station: ", common_es[0])


    # display most frequent combination of start station and end station trip
    common_com = ("Start: " + df["Start Station"] + "\n\t\tEnd: " + df["End Station"]).mode()
    print("[+] Most frequent combination: \n\t\t", common_com[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()
    print("[+] total travel time:", round(total_time / 3600, 2), "hours")


    # display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("[+] mean travel time:", round(mean_time / 3600, 2), "hours")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df["User Type"].value_counts()
    print("[+] counts of user types: ")
    for type, count in zip(user_counts.index, user_counts):
        print("\t\t", type, ":", count)


    # Display counts of gender
    if "Gender" in df:
        gender_counts = df["Gender"].value_counts()
        print("[+] counts of gender: ")
        for type, count in zip(gender_counts.index, gender_counts):
            print("\t\t", type, ":", count)


    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("[+] earliest year of birth:", df["Birth Year"].min())
        print("[+] most recent year of birth:", df["Birth Year"].max())
        print("[+] most common year of birth:")
        for year in df["Birth Year"].mode():
            print("\t\t", year)


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
