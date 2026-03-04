import cv2


def draw_crosshair(frame,length=8, color=(0,0,255),thickness=1): # ^ crosshair
    #finding middle point
    height, width, _ = frame.shape
    center_x = width//2
    center_y = height//2

    #Drawing /
    cv2.line(frame, (center_x, center_y), (center_x - length, center_y + length), color, thickness, cv2.LINE_AA)
    #Drawing \
    cv2.line(frame, (center_x, center_y), (center_x + length, center_y + length), color, thickness, cv2.LINE_AA)    