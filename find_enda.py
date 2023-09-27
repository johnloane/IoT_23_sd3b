from PIL import Image, ImageDraw
import numpy as np
import face_recognition

# Load the jpg file into a numpy array
known_image = face_recognition.load_image_file("enda.jpg")
encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file("enda_group.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([encoding], face_encoding)
    face_distance = face_recognition.face_distance([encoding], face_encoding)
    best_match_index = np.argmin(face_distance)
    if matches[best_match_index]:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=6
        )

    # You can access the actual face itself like this:
del draw
pil_image.show()
