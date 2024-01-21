import cv2
import glob
import numpy as np
import tqdm
import os

def readImgSize(file):
    # Read the size of the image
    im = cv2.imread(file)
    h, w, c = im.shape
    return w, h, im

dataset_folders = ['train', 'valid', 'test']
dataset_classes = ['Tank_dataset_0', 'Missilevehicle_dataset_1', 'Combatvehicle_dataset_2', 'Civilianvehicle_dataset_3']

# Specify the directory path
directory_path = 'C:\\Alot-Zhen\\Military_dataset_Segmentation\\DataSet_1'
for idx, dataset_class in enumerate(dataset_classes):
    for dataset_folder in dataset_folders:

        # Use glob to enumerate all files ending with .txt
        txt_files = glob.glob(directory_path + '\\' + dataset_class + '\\' + dataset_folder + '\\labels\\*.txt')

        print(txt_files)

        # Create save directory
        current_path = os.getcwd()
        save_dir = f'{current_path}\\Polygon_labels\\{dataset_class}\\{dataset_folder}'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for txt_file in tqdm.tqdm(txt_files):
            file_name = txt_file.split('\\')[-1].split('.')[0]
            img_name = f'{directory_path}\\{dataset_class}\\{dataset_folder}\\images\\{file_name}.png'
            w, h, ori_image = readImgSize(img_name)

            content = ""

            with open(txt_file, 'r') as file:
                content = file.readlines()

            for j in range(len(content)):
                # Initialize an array of zeros
                image = np.zeros((h, w), dtype=np.uint8)
                values = content[j].split(' ')
                for i in values[:1]:
                    class_id = i
                values = values[1:]
                values = [float(i.replace('\n', '')) for i in values]

                dot_ls = [(round(values[i] * w), round(values[i + 1] * h)) for i in range(0, len(values), 2)]

                # Set the coordinates on dot_ls to 1
                for dot in dot_ls:
                    image[dot[1], dot[0]] = 1

                # Convert the image to a mask (here, just an example; you might need other methods)
                mask = image

                # Extract polygon contours
                contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                # Choose the largest contour (or select other contours as needed)
                if contours:
                    max_contour = max(contours, key=cv2.contourArea)
                    polygon = max_contour.squeeze().tolist()

                    # Save polygon coordinates to a text file
                    with open(os.path.join(save_dir, file_name + '_polygon.txt'), 'a') as file:
                        file.write(f"{(class_id)}")
                        for point in polygon:
                            file.write(f" {point[0] / w} {point[1] / h}")
                        file.write(f"\n")

                # Draw the polygon on the original image
                # cv2.drawContours(ori_image, [max_contour], -1, (0, 255, 0, 0), 3)

                # Save the modified image
                # cv2.imwrite('polygon.png', ori_image)

                # # Display the image
                # cv2.imshow("Polygon", ori_image)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
