import time
import pandas as pd

CITY_DATA = {
    'chicago': 'C:/Users/sbaaw/Desktop/bikeshare/chicago.csv',
    'new york city': 'C:/Users/sbaaw/Desktop/bikeshare/new_york_city.csv',
    'washington': 'C:/Users/sbaaw/Desktop/bikeshare/washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington).
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in cities:
            break
        else:
            print("Sorry, please enter a valid city name from the list: Chicago, New York City, Washington.")
    
    # Get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Which month? January, February, March, April, May, June, or 'all' to apply no month filter: ").lower()
        if month in months:
            break
        else:
            print("Sorry, please enter a valid month or 'all'.")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Which day? Please type a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or 'all' to apply no day filter: ").lower()
        if day in days:
            break
        else:
            print("Sorry, please enter a valid day of the week or 'all'.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print(f"Most Common Month: {most_common_month.title()}")

    # Display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print(f"Most Common Day of Week: {most_common_day_of_week.title()}")

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print(f"Most Common Start Hour: {most_common_start_hour}")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most Common Start Station: {most_common_start_station}")

    # Display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most Common End Station: {most_common_end_station}")

    # Display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + " to " + df['End Station']
    most_common_station_combination = df['Station Combination'].mode()[0]
    print(f"Most Common Trip: {most_common_station_combination}")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total Travel Time: {total_travel_time} seconds, or {total_travel_time / 3600:.2f} hours")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean Travel Time: {mean_travel_time} seconds, or {mean_travel_time / 60:.2f} minutes")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts)
    else:
        print("\nGender data not available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest Year of Birth: {earliest_year}")
        print(f"Most Recent Year of Birth: {most_recent_year}")
        print(f"Most Common Year of Birth: {most_common_year}")
    else:
        print("\nBirth Year data not available.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data from the dataframe based on user input."""
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()

    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)  # Call the new display_data function

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()