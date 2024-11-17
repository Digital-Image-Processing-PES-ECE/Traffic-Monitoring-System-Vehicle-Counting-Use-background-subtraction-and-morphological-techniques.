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
```git clone https://github.com/Digital-Image-Processing-PES-ECE/project-name.git ```

2. Install Dependencies

```pip install pip```
```pip install numpy```
```pip install opencv-python```
```pip install opencv-contrib-python```

4. Run the Code
```python main.py (for eg.)```

### Outputs:
* Important intermediate steps
* Final output images 

### References:
1. Kaggle
   
### Limitations and Future Work:
