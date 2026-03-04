import cv2
import importlib

# Available crosshairs
crosshairs = [
    "center_dot_crosshair",
    "chevron_crosshair",
    "circle_crosshair",
    "classic_crosshair",
    "dot_dash_crosshair",
    "dotted_crosshair",
    "gap_crosshair",
    "gap_x_crosshair",
    "T_shape_crosshair",
    "tactical_x_crosshair",
    "x_crosshair"
]

# Show Crosshairs
print("Available Crosshairs:")
for i, name in enumerate(crosshairs, start=1):
    print(f"{i}. {name}")

# Take and control user input
while True:
    choice = input("Select a crosshair by number: ")
    if not choice.isdigit():
        print("Please enter a valid number.")
        continue
    choice = int(choice)
    if 1 <= choice <= len(crosshairs):
        selected = crosshairs[choice - 1]
        break
    else:
        print("Number out of range, try again.")

print(f"You selected: {selected}")
print("Please Wait WhileLoading crosshair...")

# Dynamic import
module_path = f"crosshairs.{selected}"
module = importlib.import_module(module_path)

# Because all have same function name:
draw_crosshair = module.draw_crosshair

# Webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    draw_crosshair(frame)

    cv2.imshow(f"OpenCV Reticle Toolkit - {selected} (Press 'q' to quit) ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()