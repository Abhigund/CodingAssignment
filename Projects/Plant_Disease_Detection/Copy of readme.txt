Exectution of model:

1. Open Terminal
2. Activate TfLite environment
source tflite_env/bin/activate
2. Get into model directory
cd /home/pi/plant_leaf_classification
3. Change the path of image to be inferred in tflite_infer_final.py
(line number 47)
4. Run the Code.
python tflite_infer_final.py

Guide Pointers

1. This is a tomato leaf disease classification model.
2. The model has been trained on Open source dataset from Kaggle.
3. Model has been trained on following 10 categories
Tomato_Bacterial_spot
Tomato_Early_blight
Tomato_Late_blight
Tomato_Leaf_Mold
Tomato_Septoria_leaf_spot
Tomato_Spider_mites_Two_spotted_spider_mite
Tomato_Target_Spot
Tomato_YellowLeaf__Curl_Virus
Tomato_healthy
Tomato_mosaic_virus

4. Tensorflow based model is been trained on server and later the converted into TFLite
5. Virtual environment is created on rasberry pi
6. All the model dependencies/ required packages are installed in the environment
7. Packages are installed by using wheels from piwheels
8. Major packages used for training are tensorflow 2.6, mathplotlib, numpy, pillow, keras, etc
9. Major packages used for testing are tflite 2.5, Pillow, Numpy & time.
10. Training steps:
  a. loading the data
  b. setting parameters (eg: batch size:32)
  c. splitting dataset into train(80%) and validation(20%)
  d. Getting class list
  e. Visualizing data
  f. Normalizing data
  g. Defining layers in the model (Input, Rescaling, Conv2D, MaxPooling, Flatten, Dense)
  h. Setting activation function(Relu)
  i. Training the model
  j. Visualizing accuracy graphs
  k. Data augmentation (To increase accuracy)
  l. Retraining model
11. Final accuracy matrix:
  a. Training loss: 0.0501
  b. Training accuracy: 0.9851
  c. Validation loss: 0.2615
  d. Validation accuracy: 0.9091
12. Converting the model to TFlite
