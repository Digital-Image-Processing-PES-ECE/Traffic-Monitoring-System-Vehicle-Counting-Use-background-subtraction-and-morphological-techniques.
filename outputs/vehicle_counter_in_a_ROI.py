import cv2
import numpy as np
def centre_handle(x,y,w,h):
        x1 = int(w/2)
        y1 = int (h/2)
        cx = x+x1
        cy = y+y1
        return cx,cy
detect = []
offset = 2.2
counter = 0

# Function to draw a quadrilateral based on four points
def draw_figure(frame, points, color=(255, 0, 0), thickness=2):
    for i in range(len(points)):
        start_point = points[i]
        end_point = points[(i + 1) % len(points)]  # Connect the last point to the first
        cv2.line(frame, start_point, end_point, color, thickness)

# Function to create a mask for the region of interest
def create_roi_mask(frame, points):
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)  # Create a black mask
    points_np = np.array(points, dtype=np.int32)
    cv2.fillPoly(mask, [points_np], 255)  # Fill the polygon defined by points with white
    return mask

countlineposition = 600
# Define new coordinates for the region of interest (this can be adjusted as needed)
print("New coordinates will be used for the region of interest:")
new_points = [(0, countlineposition), (1270, countlineposition), (750, 300), (550, 300)]  # New coordinates for ROI
for i, point in enumerate(new_points):
    print(f"Point {i + 1}: {point}")

# Load the video file
video_path = 'video.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Initialize background subtractor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame1 = cap.read()
    if not ret:
        print("End of video stream.")
        break

    # Convert frame to grayscale and apply Gaussian blur
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    # Create a mask for the new region of interest (roi_mask)
    roi_mask = create_roi_mask(frame1, new_points)

    # Apply background subtraction and morphological transformations within the ROI
    img_sub = algo.apply(blur)
    img_sub = cv2.bitwise_and(img_sub, roi_mask)  # Apply the mask to the background-subtracted image

    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.bitwise_and(dilatada, roi_mask)  # Apply the mask to the processed image

    # Find contours
    counterShape, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the new quadrilateral (region of interest) on the frame
    draw_figure(frame1, new_points, color=(0, 255, 0), thickness=2)

    # Draw the line inside the ROI (from (0, 550) to (1100, 550))
    cv2.line(frame1, (100, 500), (1100, 500), (0, 0, 255), 2)  # Red color line

    # Draw rectangles around detected vehicles
    for c in counterShape:
        x, y, w, h = cv2.boundingRect(c)
        # Filter small contours based on size
        validate_counter = (w>=50) and (h>=50)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle
        cv2.putText(frame1, "Vehicle"+str(counter), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        center = centre_handle(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1,center,3,(0,0,255),-1)

        #loop to count
        for(x,y)in detect:
            if y<(550+offset) and y>(550-offset):
                counter+=1
            cv2.line(frame1,(100,500),(1100,500),(0,127,255),3)
            detect.remove((x,y))
            print("Vehicle Counter:"+str(counter))  



    cv2.putText(frame1,"VEHICLE COUNTER:"+str(counter),(470,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
            

            

    # Display processed frames
    cv2.imshow('Detector', dilatada)
    cv2.imshow('Video with Region of Interest', frame1)

    # Exit on pressing the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('A'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
