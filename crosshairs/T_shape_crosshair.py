import cv2

 
def draw_crosshair(frame,length=6, gap=5, color=(0,0,255),thickness=1): # T-Shape crosshair
    #finding middle point
    height, width, _ = frame.shape
    center_x = width//2
    center_y = height//2

    #Drawing horizontal and vertical lines
    cv2.line(frame, (center_x -length-gap, center_y), (center_x - gap, center_y), color, thickness, cv2.LINE_AA)    
    cv2.line(frame, (center_x + gap, center_y), (center_x + length + gap, center_y), color, thickness, cv2.LINE_AA)    

    cv2.line(frame, (center_x, center_y + length), (center_x, center_y + length + gap), color, thickness, cv2.LINE_AA)
