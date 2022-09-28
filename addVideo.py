# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()

    # build service object
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # create_playlist(youtube)

    # this is a test playlist
    my_playlist_id = "PLVf5a_cao2rT7KYBQcp8WjozjbK2suE1e"
    ine_channel_id = "UCroM00J2ahCN6k-0-oAiDxg"
    lilpa_channel_id = "UC-oCJP9t47v7-DmsnmXV38Q"
    viichan_channel_id = "UCs6EwgxKLY9GG4QNUrP5hoQ"
    gosegu_channel_id = "UCV9WL7sW6_KjanYkUUaIDfQ"
    jingburger_channel_id = "UCHE7GBQVtdh-c1m3tjFdevQ"
    jururu_channel_id = "UCTifMx1ONpElK5x6B4ng8eg"

    ine_playlist_id = "" #아이네 노래🎶
    lilpa_playlist_id = "PLLPGQs-RNQXnFl55WissjQylZbInOK81P"
    viichan_playlist_id = "" #비챤 ✦노래
    gosegu_playlist_id = "" #🐬 고 세 구 노 래
    jingburger_playlist_id = "" #징버거 🎵ㅣ노래
    jururu_playlist_id = ""#주르르 노래🎧



    search_query(youtube, "노래", "playlist", "UCroM00J2ahCN6k-0-oAiDxg")
    search_query(youtube, "노래", "playlist", "UCs6EwgxKLY9GG4QNUrP5hoQ")
    search_query(youtube, "노래", "playlist", "UCV9WL7sW6_KjanYkUUaIDfQ")
    search_query(youtube, "노래", "playlist", "UCHE7GBQVtdh-c1m3tjFdevQ")
    search_query(youtube, "노래", "playlist", "UCTifMx1ONpElK5x6B4ng8eg")

    


    # add_video_to_playlist(youtube, "oRiQHxft2mY", my_playlist_id)
    # print(get_num_videos_in_playlist(youtube, lilpa_song_playlist_id))

    youtube.close()
    

def create_playlist(service):
    request = service.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": "이세돌 자동업뎃 플리",
            "description": "지수 헌정",
            "tags": [
              "sample playlist",
              "API call"
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    print("create_playlist", response)


def search_query(service, query, result_type, channel_id):
    request = service.search().list(
        part="snippet",
        maxResults=10,
        q=query,
        type=result_type,
        channelId=channel_id
    )
    response = request.execute()
    print(response)
    print("________________________________")

def add_video_to_playlist(service, videoID, playlistID):
      add_video_request=service.playlistItems().insert(
      part="snippet",
      body={
            'snippet': {
              'playlistId': playlistID, 
              'resourceId': {
                      'kind': 'youtube#video',
                  'videoId': videoID
                }
            #'position': 0
            }
    }
     ).execute()

# returns number of videos in playlist
def get_num_videos_in_playlist(service, playlistID):
      request = service.playlists().list(
        part="contentDetails",
        id=playlistID
      )
      response = request.execute()
      return response["items"][0]["contentDetails"]["itemCount"]





if __name__ == "__main__":
    main()