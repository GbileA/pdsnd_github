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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Let's choose a city first! Which city are you interested "+
                     "in: Chicago, New York City or Washington?\n\n")
        city = city.lower()

        if city not in ('new york city', 'chicago', 'washington'):
            print("Oops, I didn't catch that. Give it another shot.")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to check for in" + city.title() +
                      "? You can select any month amongst January, February, March, " +
                      "April, May and June, or type 'all' if you want to display all months.\n\n")
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may',
                         'june', 'all'):
            print("Oops, I didn't catch that. Give it another shot.")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Awesome! Now, let's choose a day." +
                    "You can select any day amongst Monday, Tuesday, Wednesday," +
                    "Thursday, Friday, Saturday or Sunday, or type all if " +
                    "you want to display all days.\n\n")
        day = day.lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',                        'all'):
            print("Oops, I didn't catch that. Give it another shot.")
            continue
        else:
            break

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df



def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month is:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day of the week is:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popularly used start station is:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popularly used end station is:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_Station = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]
    print('\nMost frequently used combination of start station and end station trip is:',                 popular_start_end_Station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Tot_Trvl_Duration = df['Trip Duration'].sum()
    print('Total travel time:', Tot_Trvl_Duration, "seconds, or", Tot_Trvl_Duration/86400, "Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time, "seconds, or", Mean_Travel_Time/86400, "Days")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types are:', user_types)


    # TO DO: Display counts of gender
    #Since there is no gender and birth year information for Washington,
    if  'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if  'Birth Year' in df:
        Earliest_Birth_Year = int(df['Birth Year'].min())
        print('\nEarliest Year:', Earliest_Birth_Year)
        Most_Recent_Birth_Year = int(df['Birth Year'].max())
        print('\nMost Recent Year:', Most_Recent_Birth_Year)
        Most_Common_Birth_Year = int(df['Birth Year'].value_counts().idxmax())
        print('\nMost Common Year:', Most_Common_Birth_Year)

    else:
        print('Sorry. Gender and birth year information are not available for Washington!')

def raw_data(df):
    i = 1
    while True:
        rawdata = input('\nWould you like to view 5 lines of raw data? Enter yes or no.\n')
        if rawdata.lower() == 'yes':
            print(df[i:i+5])

            i = i+5
        else:

            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            PRINT ('OKAY!')
            break


if __name__ == "__main__":
        main()
