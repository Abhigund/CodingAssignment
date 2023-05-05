from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time
import I2C_LCD_driver


mylcd = I2C_LCD_driver.lcd()

def load_labels(path): # Read the labels from the text file as a Python list.
  with open(path, 'r') as f:
    return [line.strip() for i, line in enumerate(f.readlines())]

def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image

def classify_image(interpreter, image, top_k=1):
  set_input_tensor(interpreter, image)

  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = np.squeeze(interpreter.get_tensor(output_details['index']))

  scale, zero_point = output_details['quantization']
  output = scale * (output - zero_point)

  ordered = np.argpartition(-output, 1)
  return [(i, output[i]) for i in ordered[:top_k]][0]

data_folder = "/home/pi/plant_leaf_classification/"

model_path = data_folder + "model_new_2_3_2023.tflite"
label_path = data_folder + "labels.txt"

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
# print("Image Shape (", width, ",", height, ")")


input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
floating_model = input_details[0]['dtype'] == np.float32

# Load an image to be classified.

image = Image.open(data_folder + "Tomato_sample/Tomato_healthy/7.JPG").resize((width, height))
image_array = np.asarray(image) / 255


input_data = np.expand_dims(image, axis=0)

if floating_model:
  input_data = np.array(input_data,dtype=np.float32)

  
# print(input_data.shape)

interpreter.set_tensor(input_details[0]['index'], input_data)

start_time = time.time()
interpreter.invoke()
stop_time = time.time()

output_data = interpreter.get_tensor(output_details[0]['index'])
results = np.squeeze(output_data)
# print(results)

top_k = results.argsort()[-5:][::-1]
labels = load_labels(label_path)

# for i in top_k:
#  if floating_model:
#    print('{:08.6f}: {}'.format(float(results[i]), labels[i]))
#  else:
#    print('{:08.6f}: {}'.format(float(results[i] / 255.0), labels[i]))

print('time: {:.3f}ms'.format((stop_time - start_time) * 1000))
print("Probably the Leaf image belongs to",labels[top_k[0]])

text=labels[top_k[0]]
text1=text[:16]
text2=text[16:]
mylcd.lcd_display_string("Leaf belong to:", 1)
time.sleep(2)
mylcd.lcd_display_string(text1, 1)
mylcd.lcd_display_string(text2, 2)
time.sleep(4)

pesticide_dict = {"Tomato_Bacterial_spot":"M 45","Tomato_Early_blight":"Azoxystrobin, piraclostrobin","Tomato_Late_blight":"Difenoconazole","Tomato_Leaf_Mold":"Vericide, Cladosporium","Tomato_Septoria_leaf_spot":"Chlorothalonil, copper, or mancozeb","Tomato_Spider_mites_Two_spotted_spider_mite":"Omite, morocide","Tomato_Target_Spot":"Corynespora cassiicola","Tomato_YellowLeaf__Curl_Virus":"Pyrethroids","Tomato_healthy":"None","Tomato_mosaic_virus":"10% bleach solution"}

print("Recommended pesticide is",pesticide_dict[labels[top_k[0]]])
textt=pesticide_dict[labels[top_k[0]]]
textt1=textt[:16]
textt2=textt[16:]
mylcd.lcd_clear()
mylcd.lcd_display_string("Recommended pesticide is:", 1)
time.sleep(2)
mylcd.lcd_display_string(textt1, 1)
mylcd.lcd_display_string(textt2, 2)
time.sleep(4)
mylcd.lcd_clear()
mylcd.lcd_display_string("Testing Done", 1)
mylcd.lcd_display_string("Thank you", 2)
