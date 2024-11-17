#Traffic Monitoring System:Vehicle Counting Using background subtraction and morphological techniques to monitor traffic flow by counting vehicles in video feeds.


### Project Description:
#### Summary - The project successfully demonstrated the feasibility of using computer vision for real-time vehicle counting in a traffic monitoring system. Implementing a region of interest (ROI) improved detection accuracy by focusing on relevant areas. While effective under normal conditions, the system faced challenges with small vehicles and low-light scenarios. Future improvements could include advanced tracking and shadow removal techniques. Overall, this project lays a strong foundation for enhancing traffic management solutions.

#### Course concepts used - 
1. -Grayscale conversion
2. -Gaussian blur
3. -Background subtraction (MOG2 algorithm)
4. -Image masking
5. -Morphological transformations (dilation, closing)
   
#### Additional concepts used -
1. -Contour detection
2. -Object detection and bounding boxes
3. -Geometry (centroid calculation for vehicle detection)
4. -Color filtering
5. -Text overlay and visualization

#### Novelty - 
1. -Customized ROI Implementation: Unlike generic vehicle detection systems, this project features a flexible region of interest (ROI) approach that allows for targeted monitoring of specific road sections, enhancing accuracy and reducing irrelevant noise.
2. -100% accuracy in vehicle counting without defining a ROI has also been implemented
   
### Contributors:
1. VIHAAN.N (PES1UG23EC812)
2. VISHNU DEVA JULAJULI (PES1UG23EC813)

### Steps:
1. Clone Repository
```git clone https://github.com/Digital-Image-Processing-PES-ECE/Traffic-Monitoring-System-Vehicle-Counting.git ```

2. Install Dependencies

```pip install pip```
```pip install numpy```
```pip install opencv-python```
```pip install opencv-contrib-python```

4. Run the Code
```python main.py (for eg.)```

### Outputs:
* Implementing Vehicle Counter (eg. real time video)
*1.Install necessary libraries (opencv-python).
*2.Initialize video capture (cv2.VideoCapture()).
*3.Create a background subtractor (cv2.bgsegm.createBackgroundSubtractorMOG()).
*4.Apply Gaussian blur and background subtraction to each frame.
*5.Perform morphological operations (dilation and closing) on the frame.
*6.Detect contours and draw rectangles around moving objects.
*7.Calculate the center of the detected objects.
*8.Check if the object crosses the counting line and update the vehicle count.
*9.Display the vehicle counter on the video frame.
*10.Show the processed video in a window and allow the user to exit.
  
* Final output images
* INPUT FEED INTIALIZATION:
![Input video image](https://github.com/user-attachments/assets/b0e5d69e-f439-4c13-8a8d-70e87a2eaaa9)
* AFTER APPLING ROI ![ROI implementation image](https://github.com/user-attachments/assets/c3d50f05-ec21-4f0d-8cd0-62d72d9ffed1)
* BACKGROUND SUBTRATION:
* ON ENTIRE FEED ![Background subtration image](https://github.com/user-attachments/assets/e82035f2-1afe-49a1-989e-a64e3f72e992)
* ON SPECIFIED ROI ![Background subtration on ROI image](https://github.com/user-attachments/assets/59670ffd-f6e6-4924-8c0d-1278014d5cd3)
* INITIALIZING A COUNTER LINE ![Implementation of a count line](https://github.com/user-attachments/assets/dc02c563-fc35-4745-8717-f6d6c9bbdc0a)
* IMPLEMENTATION OF CONTOUR AROUND VEHICLE ![Implemetation of contour(rectangle)](https://github.com/user-attachments/assets/fe269c40-6d25-4837-968c-2caf1be8a321)
* FINAL OUTPUT IF ALL OPERATIONS APPLIED ON THE ENTIRE FEED ![Implementation of a vehicle counter](https://github.com/user-attachments/assets/32db764c-337e-4d2e-b98c-7b5d33163574)
* FINAL OUTPUT IF ALL OPERATIONS APPLIES ON SPECIFIED ROI ![Implementation of a vehicle counter in ROI](https://github.com/user-attachments/assets/fa925348-f0ce-4bc1-b746-6de82ee0a034)






### References:
1. Kaggle
   
### Limitations and Future Work:
*Real-Time Vehicle Classification, Speed Detection, Multiple Camera Integration, Cloud Integration for Data Analysis, Real-Time Traffic Management System, Integration with License Plate Recognition, Enhanced ROI Detection, Limited Detection Accuracy, Dependence on Video Quality, Sensitivity to Camera Position, Background Interference, Limited to Roadways, Hardware Limitations, Weather and Environmental Factors, Computational Complexity.
