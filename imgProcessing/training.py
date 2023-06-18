import face_recognition
import os
import pickle

known_faces = []
known_names = []
KNOWN_FACES_DIR = 'imgProcessing/training_images'
known_file = f"{KNOWN_FACES_DIR}"
for name in os.listdir(known_file):
    print('Processing folder:',name)
    for filename in os.listdir(f"{known_file}/{name}"):
        print('Processing image:',filename)
        image = face_recognition.load_image_file(f"{known_file}/{name}/{filename}")
        encoding = face_recognition.face_encodings(image)
        if len(encoding) != 0:
            encoding = encoding[0]
            known_faces.append(encoding)
            known_names.append(name)
        with open(f"imgProcessing/knwon_faces.dat", 'wb') as f:
            pickle.dump(known_faces, f)
        with open(f"imgProcessing/known_names.dat", 'wb') as f:
            pickle.dump(known_names, f)