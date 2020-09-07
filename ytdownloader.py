#we have imported/install this pytube
from pytube import YouTube

link = input("Enter link of Youtube video: ")


yt = YouTube(link)

#creating variable and then we are writing streams.all functions this will actually do like give quality of videos like i mean 240p, 360p, 480p, 720p

videos = yt.streams.all()

i = 1

#looping

for stream in videos:
    print(str(i) +" "+str(stream))
    i += 1
    
stream_number = int(input("Enter number: "))

video = videos[stream_number - 1]

video.download('Enter location/path where you want to download your video ')

print('downloaded')
