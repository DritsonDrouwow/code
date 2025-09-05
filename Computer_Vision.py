import cv2

image = cv2.imread('Computer_VisionHW\input_image.jpg')

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 200,200)

cv2.imshow('Loaded Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 400,400)

cv2.imshow('Loaded Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 600,600)

cv2.imshow('Loaded Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")

