import random
from datetime import datetime, timedelta

def f():
    # Step 1: Define the start and end dates
    start_date = datetime(2021, 1, 1, 0, 0, 0)
    end_date = datetime.now()

    # Step 2: Generate random dates
    random_dates = []
    for _ in range(1000):
        # Generate a random number of seconds between start_date and end_date
        random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
        # Generate the random datetime by adding random seconds to the start_date
        random_datetime = start_date + timedelta(seconds=random_seconds)
        random_dates.append(random_datetime)

    # Step 3: Sort the dates to ensure they are in increasing order
    random_dates.sort()

    # Step 4: Convert the dates to the desired format and print them
    formatted_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in random_dates]

    final = []
    # Print the first 10 records as a sample
    for date in formatted_dates:
        final.append(str(date))
    print(len(final), final)
    return final