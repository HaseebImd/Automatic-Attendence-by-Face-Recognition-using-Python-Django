import cv2
import face_recognition
import pickle


def proc():
    print('called')
    with open(f"imgProcessing\knwon_faces.dat", 'rb') as f:
        known_faces = pickle.load(f)

    with open(f"imgProcessing\known_names.dat", 'rb') as f:
        known_names = pickle.load(f)

    img = cv2.imread("imgProcessing/user.jpg")
    imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
        matches = face_recognition.compare_faces(known_faces, encode_face,0.4)
        faceDist = face_recognition.face_distance(known_faces, encode_face)
        if True in matches:
            faceDist = list(faceDist)
            ind = faceDist.index(min(faceDist))
            return known_names[ind]
        else:
            return False
    return False
# print(process())
