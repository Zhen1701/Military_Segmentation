# Github_README

# ****2mask2polygon.py****

---

## Background

---

This code was created to convert pixel point labels into the Polygon format required for Yolov7 Segmentation training, addressing a practical need encountered during labeling tasks.

![                               **Original Label**](Github_README%2060a7261623544cdd9677057b0f3cabf9/image.png)

                               **Original Label**

![Untitled](Github_README%2060a7261623544cdd9677057b0f3cabf9/Untitled.png)

![                              **Polygon Format**](Github_README%2060a7261623544cdd9677057b0f3cabf9/S__187531344.jpg)

                              **Polygon Format**

![Untitled](Github_README%2060a7261623544cdd9677057b0f3cabf9/Untitled%201.png)

---

### Command

---

```python
python 2mask2polygon.py
```

### ****Usage****

---

To use this program, place your dataset in the specified directory. 
Run the program, and it will process each image, extracting labels from the corresponding .txt files. The labels are then converted into polygon contours, and the resulting contours are saved as new .txt files.

### Dataset S****tructure****

---

<aside>
💡 **Dataset
  |_________ train
  |           |________images
  |           |      |________0001.png
  |           |      |________0002.png    
  |           |________labels
  |                  |________0001.txt
  |                  |________0002.txt
  |_________ valid
  |          |________images
  |          |       |________0100.png
  |          |       |________0101.png    
  |          |________labels
  |                  |________0100.txt
  |                  |________0101.txt
  |__________ test
              |________images
              |     |________0200.png
              |     |________0201.png    
              |________labels
                    |________0200.txt
                    |________0201.txt**

</aside>

### Step

---

1. Read the image and extract its size.
2. Read labels from the .txt file.
3. Convert the labels into pixel points.
4. Transform the pixel points into a mask.
5. Convert the mask into a polygon format.
6. Save the polygon contours as a new .txt file.

### ****Notes****

---

- Ensure that the original label files are located in the correct path under the ‘**DataSet’** folder.
- Converted files will be stored in the ‘**Polygon_labels’** folder, organized by different datasets and classes.
- In our code, a commented section lets you draw polygons on images and view the results. Uncomment it if you wish to see this in action.