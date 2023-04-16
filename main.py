# #INITIAL SETUP
# #----------------------------------------------------------------
# import cv2
# import numpy as np
# import os
# from cvzone import HandTrackingModule, overlayPNG

# # Load game graphics
# folderPath = 'frames'
# graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in os.listdir(folderPath)]
# intro = graphic[0]  # Intro screen
# kill = graphic[1]   # Loss screen
# winner = graphic[2] # Win screen
# # sqr_img = cv2.imread('img/sqr(2).png')  # Cookie image

# # Initialize game components
# folderPath2 = 'img'
# mylist2 = os.listdir(folderPath2)
# graphic2 = [cv2.imread(f'{folderPath2}/{imPath2}') for imPath2 in mylist2]
# sqr_img = graphic2[1]# read img\sqr (1) in the sqr_img variable
# mlsa =  graphic2[0]# read img\mlsa in the mlsa variable
# cam = cv2.VideoCapture(0) # Read camera
# detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77) # Hand tracking module
# gameOver = False # Game over flag
# cutting = False  # Cutting flag
# cut_area = None  # Area to cut
# cookie_shape = sqr_img.shape[:2] # Cookie shape

# # Cutout image of Dalgona Cookie
# def cut_cookie(img, area):
#     x1, y1, x2, y2 = area
#     return img[y1:y2, x1:x2]

# # GAME LOGIC UNTIL THE COOKIE IS CUT
# # -----------------------------------------------------------------------------------------
# while not gameOver:
#     # Capture video from camera
#     success, img = cam.read()
#     if not success:
#         print("Unable to read camera feed")
#         break

#     # Detect hand and get its landmarks
#     img = cv2.flip(img, 1)
#     img = detector.findHands(img)
#     img, lmList, bbox = detector.findHands(img)

#     if lmList: # If hand is detected
#         fingers = detector.fingersUp()
#         area = detector.handRect(bbox)

#         # Start cutting
#         if fingers[0] and not cutting:
#             cutting = True
#             cut_area = area

#         # Stop cutting
#         elif not fingers[0] and cutting:
#             cutting = False
#             # Cut cookie and compare its shape to the cookie image
#             cookie = cut_cookie(img, cut_area)
#             if cookie.shape[:2] == cookie_shape:
#                 # Player wins
#                 NotWon = False
#                 break

#         # Draw cutting rectangle
#         if cutting:
#             x1, y1, x2, y2 = cut_area
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

#     # Show intro screen
#     img = overlayPNG(img, intro, [0, 0])

#     # Quit game if 'q' is pressed
#     if cv2.waitKey(1) == ord('q'):
#         break


# # LOSS SCREEN
# if NotWon:
#     for i in range(10):
#         img = overlayPNG(img, kill, [0, 0])
#         cv2.imshow("Game", img)
#         cv2.waitKey(100)
#     while True:
#         img = overlayPNG(img, kill, [0, 0])
#         cv2.imshow("Game", img)
#         if cv2.waitKey(1) == ord('q'):
#             break

# # WIN SCREEN
# else:
#     img = overlayPNG(img, winner, [0, 0])
#     while True:
#         cv2.imshow("Game", img)
#         if cv2.waitKey(1) == ord('q'):
#             break

# # Close all windows and release camera
# cv2.destroyAllWindows()
# cam.release()

import cv2
import numpy as np
import os
from cvzone import HandTrackingModule, overlayPNG

# Load game graphics
folderPath = 'frames'
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in os.listdir(folderPath)]
intro = graphic[0]  # Intro screen
kill = graphic[1]   # Loss screen
winner = graphic[2] # Win screen
# folderPath2 = 'img'
# mylist2 = os.listdir(folderPath2)
# graphic2 = [cv2.imread(f'{folderPath2}/{imPath2}') for imPath2 in mylist2]
# cookie_img = graphic2[1]# read img\sqr (1) in the sqr_img variable
# mlsa =  graphic2[0]# read img\mlsa in the mlsa variable
cookie_img = cv2.imread('img/sqr(2).png')  # Cookie image

# Initialize game components
cam = cv2.VideoCapture(0) # Read camera
detector = HandTrackingModule.HandDetector(maxHands=1, detectionCon=0.77) # Hand tracking module
gameOver = False # Game over flag
cutting = False  # Cutting flag
cut_area = None  # Area to cut
cookie_shape = cookie_img.shape[:2] # Cookie shape

# Cutout image of Dalgona Cookie
def cut_cookie(img, area):
    x1, y1, x2, y2 = area
    return img[y1:y2, x1:x2]

# GAME LOGIC UNTIL THE COOKIE IS CUT
# -----------------------------------------------------------------------------------------
while not gameOver:
    # Capture video from camera
    success, img = cam.read()
    if not success:
        print("Unable to read camera feed")
        break

    # Detect hand and get its landmarks
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    img, lmList, bbox = detector.findHands(img)

    if lmList: # If hand is detected
        fingers = detector.fingersUp()
        area = detector.handRect(bbox)

        # Start cutting
        if fingers[0] and not cutting:
            cutting = True
            cut_area = area

        # Stop cutting
        elif not fingers[0] and cutting:
            cutting = False
            # Cut cookie and compare its shape to the cookie image
            cookie = cut_cookie(img, cut_area)
            if cookie.shape[:2] == cookie_shape:
                # Player wins
                NotWon = False
                break

        # Draw cutting rectangle
        if cutting:
            x1, y1, x2, y2 = cut_area
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

    # Show intro screen
    img = overlayPNG(img, intro, [0, 0])

    # Quit game if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break


# LOSS SCREEN
if NotWon:
    for i in range(10):
        img = overlayPNG(img, kill, [0, 0])
        cv2.imshow("Game", img)
        cv2.waitKey(100)
    while True:
        img = overlayPNG(img, kill, [0, 0])
        cv2.imshow("Game", img)
        if cv2.waitKey(1) == ord('q'):
            break

# WIN SCREEN
else:
    img = overlayPNG(img, winner, [0, 0])
    cv2.imshow("Game", img)
    while True:
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()
