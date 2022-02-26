import cv2
import os
import re

framerate = 60

def main():
    while True:
        input("Insert text, too lazy to type useful stuff, press enter to start...")
        try:
            with open("times.txt",encoding="utf-8") as f:
                times = [float(i) for i in f.readlines()]

        except FileNotFoundError:
            print("File [times.txt] not found in main directory.")
            break
        except Exception as e:
            print("Some other exception: ", e)
            break

        ## Converting times to frame numbers
        framesNeeded = [int(r*framerate) for r in times]

        filesInVideos = [a for a in os.listdir("video") if ".mov" in a or ".mp4" in a or ".mkv" in a]
        if filesInVideos == []:
            print("Video file not found.")
            break

        videoToUse = filesInVideos[0]
        print("Video to use: [{}]".format(videoToUse))
        videoToUse = os.path.join("video", videoToUse)

        ## now using stackoverflow code.
        cap = cv2.VideoCapture(videoToUse)

        ## current frame number.
        count = 0
        ## index of the next frame to be extracted, in the list.
        frameIndex = 0
        
        
        while cap.isOpened():
            if frameIndex > len(framesNeeded):
                break

            ret, frame = cap.read()
            if not ret:
                continue

            ## number of the next frame to be extracted
            nFrame = framesNeeded[frameIndex]

            if count == nFrame:
                frameIndex += 1
                print('    Exported [{}]: Frame {}'.format(frameIndex,
                count))
                cv2.imwrite("images\\Frame_{}.jpg".format(count), frame)     # save frame as JPEG file
            
            count = count + 1

        break

    input("Press enter to close.")

def mainv2():
    # every second up to 7 minutes
    # I'm too tired to write good code go away.

    while True:
        input("Insert text, too lazy to type useful stuff, press enter to start...")
        
        times = range(8, 7 * 60)

        ## Converting times to frame numbers
        framesNeeded = [int(r*framerate) for r in times]

        filesInVideos = [a for a in os.listdir("video") if ".mov" in a or ".mp4" in a or ".mkv" in a]
        if filesInVideos == []:
            print("Video file not found.")
            break

        videoToUse = filesInVideos[0]
        print("Video to use: [{}]".format(videoToUse))
        videoToUse = os.path.join("video", videoToUse)

        ## now using stackoverflow code.
        cap = cv2.VideoCapture(videoToUse)

        ## current frame number.
        count = 0
        ## index of the next frame to be extracted, in the list.
        frameIndex = 0
        
        
        while cap.isOpened():
            if frameIndex > len(framesNeeded):
                break

            ret, frame = cap.read()
            if not ret:
                continue

            ## number of the next frame to be extracted
            nFrame = framesNeeded[frameIndex]

            if count == nFrame:
                frameIndex += 1
                print('    Exported [{}]: Frame {}'.format(frameIndex,
                count))
                cv2.imwrite("images\\Frame_{}.jpg".format(count), frame)     # save frame as JPEG file
            
            count = count + 1

        break

    input("Press enter to close.")

if __name__ == "__main__":
    mainv2()