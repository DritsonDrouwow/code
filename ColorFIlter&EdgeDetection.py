import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()

    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 1] = 0
    elif filter_type == 'sepia':
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])
        filtered_image = cv2.transform(image, sepia_filter)
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
    elif filter_type == 'color':
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 50, 50])
        upper = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower, upper)
        lower = np.array([170, 50, 50])
        upper = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower, upper)
        mask = mask1 | mask2
        red_only = cv2.bitwise_and(image, image, mask=mask)
        combined_label = np.zero_like(image)
        combined_label[:, :] = red_only
        filtered_image = cv2.cvtColor(combined_label, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'sobel':
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
        filtered_image("Sobel Edge Detection", combined_sobel)

    elif filter_type == 'canny':
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image

image_path = 'FunFiltersHW\example.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image is not found")
else:
    filter_type = 'original'

    print("Press the following keys to apply filters: ")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("s - Sepia")
    print("S - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("q - Quit")

    while True:
        filtered_image = apply_filter(image, filter_type)

        cv2.imshow('Filtered Image', filtered_image)

        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord("s"):
            filter_type = 'sepia'
        elif key == ord('c'):
            filter_type = 'canny'
        elif key == ord('S'):
            filter_type = 'sobel'
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid Key! Please use 'r', 'g', 'b', 's', 'c', or 'q'.")
cv2.destroyAllWindows()
