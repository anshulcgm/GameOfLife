import numpy as np
import keras
from keras.models import Model, Sequential, model_from_json
from keras import losses
import GOL


        
def returnModelPrediction(GOLBoard1, GOLBoard2):
    json_file = open('model.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("model.h5")
    model.compile(optimizer = 'adam', loss = losses.binary_crossentropy, metrics = ['accuracy'])
    modelInput = []
    modelInput.append(GOLBoard1)
    modelInput.append(GOLBoard2)
    modelInput = np.asarray(modelInput).reshape(1, 98)
    prediction = model.predict_classes(modelInput)
    return prediction

randomTest = np.random.randint(0, 2, size = (7, 7))
nextGenTest = GOL.returnNextGen(randomTest)
if (returnModelPrediction(randomTest, nextGenTest) == 0):
    print("The two inputted frames are sequential")
elif (returnModelPrediction(randomTest, nextGenTest) == 1):
    print("The two inputted frames are not sequential")
        
    