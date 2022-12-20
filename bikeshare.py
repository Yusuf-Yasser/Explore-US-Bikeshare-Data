import time
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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

    # get user input for month (all, january, february, ... , june)
    month, day = "all", "all"

    cities = ['chicago', 'new york city', 'washington']

    months = ['january', 'february', 'march', 'april', 'may', 'june']

    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    city = input('Please choose a city from Chicago, New York City, and Washington to analyze \n').lower()
    while city not in cities:
        print('Invalid input! Input valid city or check your spelling.\n')
        city = input('Please choose a city from Chicago, New York City, and Washington to analyze \n').lower()

    filters = input(
        'Would you like to apply filters to the data by month, day, both or not at all? type "none" for no time filter.\n').lower()
    while filters not in ['month', 'day', 'both', 'none']:
        print('Invalid input! Input valid filter or check your spelling.\n')
        filters = input(
            'Would you like to apply filters to the data by month, day, both or not at all? type "none" for no time filter.\n').lower()


    if filters == 'month' or filters == "all":
        month = input(
            'Choose the month you want to filter by from (January, February, March, April, May, June or all).\n').lower()
        while month not in months:
            print('Invalid input! Input valid month or check your spelling,\n')
            month = input(
                'Choose the month you want to filter by from (January, February, March, April, May, June or all).\n').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filters == 'day' or filters == "all":
        day = input(
            'Choose the day you want to filter by from (saturday, sunday, monday, tuesday, wednesday, thurday, friday, all).\n').lower()
        while day not in days:
            print('Invalid input! Input valid day or check your spelling.\n')
            day = input(
                'Choose the day you want to filter by from (saturday, sunday, monday, tuesday, wednesday, thurday, friday, all).\n').lower()

    if filters == 'both' or filters == "all":
        month = input(
            'Choose the month you want to filter by from (January, February, March, April, May, June or all).\n').lower()
        while month not in months:
            print('Invalid input! Input valid month or check your spelling,\n')
            month = input(
                'Choose the month you want to filter by from (January, February, March, April, May, June or all).\n').lower()
        day = input(
            'Choose the day you want to filter by from (saturday, sunday, monday, tuesday, wednesday, thurday, friday, all).\n').lower()
        while day not in days:
            print('Invalid input! Input valid day or check your spelling.\n')
            day = input(
                'Choose the day you want to filter by from (saturday, sunday, monday, tuesday, wednesday, thurday, friday, all).\n').lower()

    print('-' * 40)
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
    # Create DataFrame using arguments

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_the_week'] = df['Start Time'].dt.day_name()

    df['start_hour'] = df['Start Time'].dt.hour
    # filter by month
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # create new dataframe
        df = df[df['month'] == month]

    # filter by day
    if day != "all":
        # create new dataframe
        df = df[df['day_of_the_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is {}\n'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('the most common day is {}\n'.format(df['day_of_the_week'].mode()[0]))

    # display the most common start hour
    print('the most common hour is {}\n'.format(df['start_hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is {}\n'.format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print('The most commonly used end station is {}\n'.format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    # make new column named 'trip' with the combination of start station and end station
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent combination of start station and end station trip is {}\n'.format(df['trip'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time is {}.\n'.format(df['Trip Duration'].sum()))
    # display mean travel time
    print('The average travel time is {}.\n'.format(df['Trip Duration'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The count of user types is\n{}'.format(df['User Type'].value_counts()))
    # Display counts of gender
    try:
        print('Gender count is {}.\n'.format(df['Gender'].value_counts()))

    except:
        print('Gender data not provided.\n')

    # Display earliest, most recent, and most common year of birth
    try:
        print(
            'The earliest year of birth is {}.\nThe most recent year of birth is {}.\nThe most common year of birth is {}.\n'.format(
                df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]))
    except:
        print('Birth year data not provided.\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    response = input('Do you want to display 5 rows of raw data? enter yes or no\n').lower()
    while response not in ['yes', 'no']:
        print('Invalid input! Input either yes or no')
        response = input('Do you want to display 5 rows of raw data? enter yes or no\n').lower()
    if response != 'yes':
        print('Thank you\n')
    else:
        i = 0
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            response = input('Do you want to display 5 rows of raw data? enter yes or no\n').lower()
            while response not in ['yes', 'no']:
                print('Invalid input! Input either yes or no')
                response = input('Do you want to display 5 rows of raw data? enter yes or no\n').lower()
            if response != 'yes':
                print('Thank you\n')
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart not in ['yes', 'no']:
            print('Invalid input! Enter either yes or no.\n')
            restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
