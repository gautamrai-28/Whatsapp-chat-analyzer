import re
import pandas as pd

def preprocess(data):
    pattern = r'\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}[\u202fa|p]{2}m'

    messages = re.split(pattern, data)[1:]

    dates = re.findall(pattern, data)
    clean_dates = [date.replace('\u202f', ' ') for date in dates]

    df = pd.DataFrame({'user_message': messages, 'message_date': clean_dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p')

    df.rename(columns={'message_date': 'clean_dates'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)

        if entry[1:]:  # if user name exists
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['clean_dates'].dt.date
    df['year'] = df['clean_dates'].dt.year
    df['month_num'] = df['clean_dates'].dt.month
    df['month'] = df['clean_dates'].dt.month_name()
    df['day'] = df['clean_dates'].dt.day
    df['day_name'] = df['clean_dates'].dt.day_name()
    df['hour'] = df['clean_dates'].dt.hour
    df['minute'] = df['clean_dates'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df