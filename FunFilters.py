import cv2
import numpy as np

def apply_color_filter(image, filter_type):

    filtered_image = image.copy()
    if filter_type == "Red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "Blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "Green_tint":
        filtered_image[:, :,0] = 0
        filtered_image[:, :,2] = 0
    elif filter_type == "Increased_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "Decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    elif filter_type == "Increase Green Intensity":
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50)
        filtered_image[:, :,2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decrease red intensity":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], 50)
        

    return filtered_image

image_path = 'FunFilters\example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image is not found!")
else:
    filter_type = "original"
    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - increased red intensity")
    print("d - decreased blue intensity")
    print("up_arrow - Increase Green Intensity")
    print("down_arrow ' decrease red intensity")
    print("q - Quit")
    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "Red_tint"
        elif key == ord('b'):
            filter_type = "Blue_tint"
        elif key == ord('g'):
            filter_type = "Green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('up_arrow'):
            filter_type = "Increase Green Intensity"
        elif key == ord('down_arrow'):
            filter_type = "decrease red intensity"
        elif key == ord('q'):
            filter_type = "Exiting..."
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")

cv2.destroyAllWindows()
