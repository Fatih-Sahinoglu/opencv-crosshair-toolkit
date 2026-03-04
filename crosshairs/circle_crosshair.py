import cv2

 
def draw_crosshair(frame,length=4, radius=10, color=(0,0,255),thickness=1): # Crosshair with a circular ring around the center
    #finding middle point
    height, width, _ = frame.shape
    center_x = width//2
    center_y = height//2
    # Big Center Circle
    cv2.circle(frame, (center_x, center_y), radius, color, 0, cv2.LINE_AA)

    #Drawing horizontal and vertical lines
    cv2.line(frame, (center_x - length - radius , center_y), (center_x - length, center_y), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x + length + radius, center_y), (center_x + length, center_y), color, thickness, cv2.LINE_AA)    

    cv2.line(frame, (center_x, center_y - length - radius), (center_x, center_y - length), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x, center_y + length + radius), (center_x, center_y + length), color, thickness, cv2.LINE_AA)

    #If you don't want to add a small dot at the center of the circle, you can delete the following line:
    cv2.circle(frame, (center_x, center_y), 1, color, -1, cv2.LINE_AA)