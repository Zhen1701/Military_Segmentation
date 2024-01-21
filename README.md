2mask2polygon.py
---
# Background

This code was created to convert pixel point labels into the Polygon format required for Yolov7 Segmentation training, addressing a practical need encountered during labeling tasks.

<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <h2>Original Label</h2>
        <img src="https://hackmd.io/_uploads/BJMmL4qFp.png" alt="Image 1" width="350" />
    </div>
    <div style="text-align: center;">
        <h2>Polygon Format</h2>
        <img src="https://hackmd.io/_uploads/BkJ48NqKa.jpg" alt="Image 2" width="350" />
    </div>
</div>

<div style="display: flex; justify-content: space-around;">
    <div style="text-align: center;">
        <img src="https://hackmd.io/_uploads/SJk2K49ta.png" alt="Image 1" width="350" />
    </div>
    <div style="text-align: center;">
        <img src="https://hackmd.io/_uploads/S1w3tE9tp.png" alt="Image 2" width="350" />
    </div>
</div>

# Command
```
python 2mask2polygon.py
```
# Usage
To use this program, place your dataset in the specified directory. 
Run the program, and it will process each image, extracting labels from the corresponding .txt files. The labels are then converted into polygon contours, and the resulting contours are saved as new .txt files.
# Dataset Structure

Dataset
|__ train
|   |__ images
|   |   |__ 0001.png
|   |   |__ 0002.png
|   |__ labels
|       |__ 0001.txt
|       |__ 0002.txt

|__ valid
|   |__ images
|   |   |__ 0100.png
|   |   |__ 0101.png
|   |__ labels
|       |__ 0100.txt
|       |__ 0101.txt

|__ test
    |__ images
    |   |__ 0200.png
    |   |__ 0201.png
    |__ labels
        |__ 0200.txt
        |__ 0201.txt
        
# Step
1. Read the image and extract its size.
2. Read labels from the .txt file.
3. Convert the labels into pixel points.
4. Transform the pixel points into a mask.
5. Convert the mask into a polygon format.
6. Save the polygon contours as a new .txt file.

# Notes
* Ensure that the original label files are located in the correct path under the ‘DataSet’ folder.
* Converted files will be stored in the ‘Polygon_labels’ folder, organized by different datasets and classes.
* In our code, a commented section lets you draw polygons on images and view the results. Uncomment it if you wish to see this in action.




# Test 
![S__187531344_0](https://hackmd.io/_uploads/Bk9VkH9Ya.jpg =30%x)![S__187531344_0](https://hackmd.io/_uploads/Bk9VkH9Ya.jpg =30%x)
