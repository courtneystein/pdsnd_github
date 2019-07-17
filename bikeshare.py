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
	    city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
		try:
		    city = ['Chicago', 'New York City', 'Washington']
			if city not in ('Chicago', 'New York City', 'Washington'):
		        print('Sorry, {} is not a valid city. Please re-select from either Chicago, New York City or Washington.'.format(city))
		        continue
		    else:
		        break
		except:
		    print('That\'s not a valid entry! Please try again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
	    month = input('Would you like to see data for January, February, March, April, May, June or all months?\n').lower()
		try:
		    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
			if month not in months:
			    print('Sorry, {} is not a valid month. Please re-select for a preferred month or all.'.format(months))
				continue
			else:
			    break
			except:
			    print('That\'s not a valid entry! Please try again.')
				
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
	    day = input('Would you like to see data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday or all months?\n').lower()
		try:
		    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
			if day not in days:
			    print('Sorry, {} is not a valid day. Please re-select for a preferred day or all.'.format(days))
				continue
			else:
			   break
			except:
			    print('That\'s not a valid entry! Please try again.')

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
	df = pd.read_csv(CITY_DATA)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['month'] = df['Start Time'].dt.month
	common_month = df['month'].mode().[0]
	print('The most common month is ', common_month)

    # TO DO: display the most common day of week
    df = pd.read_csv(CITY_DATA)
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['day'] = df['Start Time'].dt.day
	common_day = df['day'].mode().[0]
	print('The most common day is ', common_day)

    # TO DO: display the most common start hour
    df = pd.read_csv(CITY_DATA)
	df['Start Time'] = pd.to_datetime(df['Start Time'])
	df['hour'] = df['Start Time'].dt.hour
	common_hour = df['hour'].mode()[0]
	print('The most common hour is ', common_hour)
	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
	df = pd.read_csv(CITY_DATA)
    common_start_station = df['Start Station'].mode()[0]
	print('The most commonly used start station is ', common_start_station)

    # TO DO: display most commonly used end station
    df = pd.read_csv(CITY_DATA)
	common_end_station = df['End Station'].mode()[0]
	print('The most commonly used end station is ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df = pd.read_csv(CITY_DATA)
	frequent_combo_start_end_station = df.groupby(['Start Station'])[['End Station']].count()
    print('The most frequent combination of start and end station trip is ', frequent_combo_start_end_station)
	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df = pd.read_csv(CITY_DATA)
	total_travel_time = df['Trip Duration'].sum()
	print('The total travel time is ', total_travel_time)

    # TO DO: display mean travel time
    df = pd.read_csv(CITY_DATA)
	average_travel_time = df['Trip Duration'].mean()
	print('The mean travel time is ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df = pd.read_csv(CITY_DATA)
	user_types = df['User Type'].value_counts()
	print('The types and count of users are ', user_types)

    # TO DO: Display counts of gender
    df = pd.read_csv('chicago.csv', 'new_york_city.csv')	
	gender_type = df['Gender'].value_counts()
	
	if 'Gender' in df.columns:
	    print(df.sort_values(by=['Gender'])
		
	else:
		print(inplace=False)

    # TO DO: Display earliest, most recent, and most common year of birth
	df = pd.read_csv('chicago.csv', 'new_york_city.csv')
	birth_year_earliest_recent_common = df['Birth Year'].value_counts()
    print(df.sort_values(by=['Birth Year'], inplace=False)) 
	
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
        	
		try:
		    raw_data_display = input('\nWould you like to see five lines of the original data? Please enter yes or no.\n').value_counts(bins=5)
		    if raw_data_display.lower() = 'yes':
			print(df)
		    continue
	    
		else:
		    break
					
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
