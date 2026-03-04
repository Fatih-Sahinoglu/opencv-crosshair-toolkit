import cv2


def draw_crosshair(frame,length=4, gap=3, color=(0,0,255),thickness=1): # x which have gap at middle crosshair
    #finding middle point
    height, width, _ = frame.shape
    center_x = width//2
    center_y = height//2

    #Drawing \
    cv2.line(frame, (center_x - length - gap, center_y - length - gap), (center_x - gap, center_y - gap), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x + gap, center_y + gap), (center_x + length + gap, center_y + length + gap), color, thickness, cv2.LINE_AA)    

    #Drawing /
    cv2.line(frame, (center_x + length + gap, center_y - length - gap), (center_x + gap, center_y - gap), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x - length - gap, center_y + length + gap), (center_x - gap, center_y + gap), color, thickness, cv2.LINE_AA)
