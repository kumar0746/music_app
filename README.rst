Run all tests
    cd music_app/tests
    pytest .

Run specific test
    cd music_app/tests
    pytest <file> -k <test_method>


Functional Uses cases:
	• Add a song to existing playlist
	• Remove an existing playlist
	• Add a new playlist for existing user
Requirements
	• Assuming our system is similar to Spotify, spotify has 232 million users as of July 2019
	• On an average if we assume  user has 5 playlists and 10 songs /playlist, we will have around 1 billion playlists.
	• There are around 40 million songs in spotify.
	• Assume 1000 songs are added per hour and if 30% of them are added to playlist. It will be 300 requests/hour for playlist update and we can assume another 100 requests/hour for new playlist creation. Roughly this translates to 1 TPS
	• Service should be available 99.99%

System Constraints
	• Lets assume average user name will be 20 bytes and user id will be 8 bytes. We will need around 6.5 GB of data to store user information
	• For playlist - 8 bytes for ID, 8 bytes for user ID and 10*8 bytes for songs. For 1 billion playlists,  100 GB data
	• For songs - 8 bytes for ID, 20 bytes for title and 20 bytes for artist. For 40 million songs we will need 2GB of data

API Interfaces
	• POST /v1/playlist
	• PUT /v1/playlist
	• DELETE /v1/playlist

Storage
	• Since the schema of our data can keep changing (eg: song metadata could be added/removed) and we also don’t have any join or complex query operations, we can store the user, playlist and songs DB in a NoSQL database like DynamoDB

High level design
	• User information can be added in cache and when ever a playlist is created/ deleted for an user, we can check that in cache and update the playlist or song information in DB.
	• Application server handles the requests from clients

![image "High level design"](https://github.com/kumar0746/music_app/blob/master/high_level_design.png)

Bottle necks
	Since system needs to be available 99.99% we can have multiple application servers at different availability zones. Even if one data center is down, we will be still able to server requests from other data centers
