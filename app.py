import streamlit as st
import plotly.express as px
import pandas as pd
from db import get_mongo_data  # Import the MongoDB connection function

# Fetch data from MongoDB
songs_df = get_mongo_data()

# Streamlit app layout
st.title("Music App Dashboard")

# Sidebar Configuration
st.sidebar.title("Options")

# Sidebar: Show raw data
show_data = st.sidebar.checkbox("Show raw data")

# Sidebar: Select a chart to display
chart_option = st.sidebar.selectbox(
    "Select a chart to display", 
    ("Top 10 Most Played Songs", "Genre Distribution", "Song Distribution by Language")
)

# Sidebar: Artist filter
artists = songs_df['artist'].unique()
selected_artist = st.sidebar.selectbox("Select an Artist", artists)

# Sidebar: Plot height slider
plot_height = st.sidebar.slider("Specify plot height", 200, 500, 250)

# Main Area

# Show raw data if checkbox is selected
if show_data:
    st.subheader("Raw Data from MongoDB")
    st.write(songs_df)

# Bar chart: Most Played Songs
if chart_option == "Top 10 Most Played Songs":
    st.subheader("Top 10 Most Played Songs")
    top_songs = songs_df[['title', 'play_count']].sort_values('play_count', ascending=False).head(10)
    fig_top_songs = px.bar(top_songs, x='title', y='play_count', title="Most Played Songs", height= plot_height)
    st.plotly_chart(fig_top_songs)

# Pie chart: Genre Distribution
if chart_option == "Genre Distribution":
    st.subheader("Genre Distribution")
    genre_count = songs_df.groupby('genre').size().reset_index(name='counts')
    fig_genre = px.pie(genre_count, values='counts', names='genre', title="Genre Distribution")
    st.plotly_chart(fig_genre)

# Pie chart: Song Distribution by Language
if chart_option == "Song Distribution by Language":
    st.subheader("Song Distribution by Language")
    song_by_lang = songs_df.groupby('language').size().reset_index(name='counts')
    fig_genre = px.pie(song_by_lang, values='counts', names='language', title="Song Distribution by Language")
    st.plotly_chart(fig_genre)

# Display filtered songs by selected artist
st.subheader(f"Songs by {selected_artist}")
filtered_songs = songs_df[songs_df['artist'] == selected_artist]
st.dataframe(filtered_songs)
