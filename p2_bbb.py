import os

video = "cut_bbb.mp4"
def cut_seconds_from_bbb():
	seconds_to_cut = input("enter the number of second in which you want to end the video: ")
	os.system("ffmpeg -i Big_Buck_Bunny.mp4 -ss 00:00:00 -t "+ seconds_to_cut +" -async 1 cut_bbb.mp4")
	#"ffmpeg -i Big_Buck_Bunny.mp4 -ss 00:00:00 -t 00:00:0"+ seconds_to_cut +" -async 1 cut_bbb.mp4"

def play_video_with_histogram():
	os.system("ffplay " + video + " -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay")

def resize_video():
	resizeOption = input("choose the resolution you want the output video in:\n1- 720p\n2- 480p\n3- 360x240p\n4- 160x120p\n")
	loop = True
	while loop == True:
		if resizeOption == '1':
			os.system("ffmpeg -i " + video + " -vf scale=1280:720 resized_bbb.mp4")
			loop = False
		elif resizeOption == "2":
			os.system("ffmpeg -i " + video + " -vf scale=720:480 resized_bbb.mp4")
			loop = False
		elif resizeOption == "3":
			os.system("ffmpeg -i " + video + " -vf scale=360:240 resized_bbb.mp4")
			loop = False
		elif resizeOption == "4":
			os.system("ffmpeg -i " + video + " -vf scale:160x120 resized_bbb.mp4")
			loop = False
		else:
			input("please choose a valid option:\n 1- 720p\n2- 480p\n3- 360x240p\n4- 160x120p\n")
def reEncode_audio():
	option = input("do you want to change the audio to mp3 or turn it into mono? (mono/mp2)\n")
	loop = True
	while loop:
		if option == "mono":
			os.system("ffmpeg -i " + video + " -c:v copy -ac 1 mono_bbb.mp4")
			loop = False
		elif option == "mp2":
			os.system("ffmpeg -i " + video + " -acodec mp3 -vcodec copy mp3_bbb.mp4")
			loop = False
		else:
			input("please select a valid option (mono/mp3)\n")


def main():
	exit = False
	while exit == False:
		option = input("choose the exercise you want to do execute:\n1\n2\n3\n4\nAny other key to exit\n")
		if option == "1":
			cut_seconds_from_bbb()
		elif option == "2":
			play_video_with_histogram()
		elif option == "3":
			resize_video()
		elif option == "4":
			reEncode_audio()
		else:
			exit = True

if __name__ == "__main__":
	main()
