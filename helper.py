from urlextract import URLExtract
import emoji
import numpy as np
import pandas as pd
from collections import Counter
from nrclex import NRCLex
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


extract = URLExtract()
def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))


    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

def most_common_words(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap


def sentiment_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Analyze sentiment for each message
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    sentiment_scores = []

    for message in df['message']:
        score = analyzer.polarity_scores(message)['compound']
        sentiment_scores.append(score)
        if score >= 0.05:
            sentiments['positive'] += 1
        elif score <= -0.05:
            sentiments['negative'] += 1
        else:
            sentiments['neutral'] += 1

    df['sentiment_score'] = sentiment_scores
    return sentiments, df['sentiment_score'].mean()


def calculate_response_time(selected_user, df):
    # Filter data for the selected user if required
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Calculate the time difference between consecutive messages using clean_dates
    df['prev_message_time'] = df['clean_dates'].shift(1)
    df['time_diff'] = (df['clean_dates'] - df['prev_message_time']).dt.total_seconds() / 60.0  # convert to minutes

    # Ignore messages that are not part of the conversation (e.g., >1 day response time)
    df['time_diff'] = df['time_diff'].apply(lambda x: x if x <= 1440 else np.nan)  # 1440 minutes = 1 day

    # Calculate the average response time for the selected user
    avg_response_time = df['time_diff'].mean()

    # Group by user if it's the overall analysis
    if selected_user == 'Overall':
        response_times = df.groupby('user')['time_diff'].mean().dropna().reset_index()
        response_times = response_times.sort_values(by='time_diff', ascending=True)
    else:
        response_times = None

    return avg_response_time, response_times

def calculate_message_length(selected_user, df):
    # Filter data for the selected user if required
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Calculate message length for each message
    df['message_length'] = df['message'].apply(len)

    # Calculate the average message length
    avg_message_length = df['message_length'].mean()

    # If "Overall" is selected, calculate the average length per user
    if selected_user == 'Overall':
        message_length_by_user = df.groupby('user')['message_length'].mean().reset_index().sort_values(by='message_length', ascending=False)
    else:
        message_length_by_user = None

    return avg_message_length, message_length_by_user

