import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.figure(figsize=(8, 6))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()
def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_image("Original Grayscale Image", gray_image)

    print("Select an option: ")
    print("1. Sobel Edge Detection ")
    print("2. Canny Edge Detection ")
    print("3. Laplacian Edge Detection ")
    print("4. Gaussian Smoothing ")
    print("5. Median Filtering ")
    print("6. Exit ")
    print("7 Reset ")
    print('8 Undo')

    while True:
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)
        elif choice == "2":
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold"))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)
        elif choice == '3':
            edges = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge DEtection", np.abs(edges).astype(np.uint8))
        elif choice == '4':
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5 )")
            kernel_size = int(input("Enter kernel size (odd number): "))
            median_filtered = cv2.medianBlur(gray_image, kernel_size)
            display_image("Median Filtered Image", median_filtered)
        elif choice == '5':
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))
            median_filtered = cv2.medianBlur(gray_image, kernel_size)
            display_image("Median Filtered Image", median_filtered)
        elif choice == '7':
            image = cv2.imread(image_path)
            display_image("Original Image", image)
        elif choice ==  '8':
            image = cv2.imread(image_path)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            display_image("Original Grayscale Image", gray_image)
        elif choice == '6':
            print("Goodbye")
            break


            
        
        else:
            print("Invalid choice. Please select a number between 1 and 6")
interactive_edge_detection("Edge_detectionHW/field.jpg")
