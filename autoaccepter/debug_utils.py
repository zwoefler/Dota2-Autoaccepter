import cv2
import os


def save_with_unique_name(base_filename, image):
    """
    Save given image with a unique filename.
    Appends a number if the file exists.
    """
    filename, ext = os.path.splitext(base_filename)
    counter = 1
    new_filename = base_filename

    while os.path.exists(new_filename):
        new_filename = f"{filename}_{counter}{ext}"
        counter += 1

    cv2.imwrite(new_filename, image)
    print(f"Saved image as: {new_filename}")


def draw_bounding_boxes(image, results, offset):
    """
    Draw bounding boxes where the buttons are detected
    
    Args:
        image (np.ndarray): The image to draw on.
        results (list): List of match results with match locations and template dimensions.
        offset (tuple): The x and y offsets to adjust for cropped images.
    
    Returns:
        np.ndarray: The image with bounding boxes drawn.
    """
    for result in results:
        match_loc, w, h = result[1], result[2], result[3]
        top_left = (match_loc[0] + offset[0], match_loc[1] + offset[1])
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    return image

