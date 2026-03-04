import cv2

# fill=-1 for filled circle, 0 or positive for thickness of circle border.
# Default is -1 (filled circle)
def draw_crosshair(frame, radius=3, color=(0,0,255),fill=-1): # basic . crosshair
    #finding middle point
    height, width, _ = frame.shape
    center_x = width//2
    center_y = height//2

    #Drawing Dot at the center
    cv2.circle(frame, (center_x, center_y), radius, color, fill, cv2.LINE_AA)
