import os
import streamlit as st
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from PIL import Image
from io import BytesIO
import openai
from dotenv import load_dotenv
load_dotenv() 

# Function to get the most relevant YouTube video based on the search query
def get_most_relevant_video(query):
    try:
        youtube = build('youtube', 'v3', developerKey=os.getenv("YOUTUBE_API_KEY"))
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            type='video',
            maxResults=1
        ).execute()

        video_id = search_response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    except HttpError as e:
        st.error(f"Error occurred: {e}")

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get the ChatGPT answer for a given query
def get_chatgpt_answer(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use other engines if you prefer
            messages=[{"role": "user", "content": query}],
            max_tokens=193,
            temperature=0,
        )
        answer = response.choices[0].message["content"]
        print(answer)
        return answer
    except Exception as e:
        st.error(f"Error occurred while getting ChatGPT response: {e}")

# Main Streamlit app
def main():
    st.title("YouTube Video and ChatGPT Search")

    # Input for search query
    search_query = st.text_input("Enter your search query:")

    if st.button("Search"):
        if search_query:

            # Get the ChatGPT answer for the query
            chatgpt_answer = get_chatgpt_answer(search_query)

            # Display the ChatGPT answer
            st.subheader("ChatGPT Answer:")
            st.write(chatgpt_answer)

            # Get the most relevant YouTube video based on the search query
            st.subheader("Youtube Answer:")
            video_url = get_most_relevant_video(search_query)

            # Display the video using an embedded YouTube player
            if video_url:
                st.video(video_url)


        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()