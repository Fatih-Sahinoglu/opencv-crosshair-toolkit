import cv2

# fill=-1 for filled circle, 0 or positive for thickness of circle border.
# Default is -1 (filled circle)
def draw_crosshair(frame,length=5, gap=5, color=(0,0,255),thickness=1,fill=-1): # + which have dot at middle crosshair
    #finding middle point
    height, width, _ = frame.shape
    center_x = width//2
    center_y = height//2

    #Drawing horizontal and vertical lines
    cv2.line(frame, (center_x -length-gap, center_y), (center_x - gap, center_y), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x + length + gap, center_y), (center_x + gap, center_y), color, thickness, cv2.LINE_AA)    

    cv2.line(frame, (center_x, center_y - length - gap), (center_x, center_y - gap), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x, center_y + length + gap), (center_x, center_y + gap), color, thickness, cv2.LINE_AA)

    #Center dot
    cv2.circle(frame, (center_x, center_y), 1, color, fill, cv2.LINE_AA)