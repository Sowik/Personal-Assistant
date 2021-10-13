import face_recognition
from PersonalAss.FacePics import takepic
import sqlite3
from sqlite3 import Error
import numpy as np
import io

known_face_encodings = []
known_face_names = []

# za da moje sqlite da razchita i vryshta ndarray kakto trqbva
def adapt_array(arr):

    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())


def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


# Converts np.array to TEXT when inserting
sqlite3.register_adapter(np.ndarray, adapt_array)

# Converts TEXT to np.array when selecting
sqlite3.register_converter("array", convert_array)

conn = sqlite3.connect('faces.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)
c = conn.cursor()
try:
    c.execute("""CREATE TABLE IF NOT EXISTS known_faces (
                            known_face array,
                            known_name test
                            )""")
except Error as e:
    print(e)


def startUpFill(): #zarejda poznatite lica ot sqlite db pri startirane na programata otnovo
    c.execute("SELECT known_face FROM known_faces")
    c.row_factory = lambda cursor, row: row[0]

    testtest = c.fetchall()
    for row in testtest:
        known_face_encodings.append(row)

    c.execute("SELECT known_name FROM known_faces")
    testtest1 = c.fetchall()
    for row in testtest1:
        known_face_names.append(row)


def rememberMe(my_name): # zapomnqne na lice
    takepic.takeApic()
    unknown_image = face_recognition.load_image_file("filename.jpg") #zarejda toku shto napravenata snimka
    try:
        unknown_face_encoding1 = face_recognition.face_encodings(unknown_image)[0] #kodira snimkata, za da znae kak da q razpoznava
    except IndexError as e:
        print(e)
    # print(unknown_face_encoding1)
    #dobavqma snimkata kym lista ni sys poznati lica i kym bazata danni
    known_face_encodings.append(unknown_face_encoding1)
    known_face_names.append(my_name)

    c.execute("INSERT INTO known_faces VALUES (?,?)", (unknown_face_encoding1, my_name,))
    conn.commit()

    # c.execute("SELECT known_face FROM known_faces")
    # testtest = c.fetchall()
    # print(testtest[0])
    # print(known_face_encodings)

    return None


def getKnownFace():#
    startUpFill()
    takepic.takeApic()
    #zarejda toku shto napravenata snimka i q kodira
    unknown_image = face_recognition.load_image_file("filename.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

    #sravnqvame unknown_face_encoding s veche poznatite ni lica
    matches = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)
    # print(unknown_face_encoding)
    name = ''

    #ako imame syvpadenie vryshtame imeto
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
        print(name)
        return name
    else:
        return "I don't know you."


# rememberMe("Milen")
# print(known_face_names)
# getKnownFace()
