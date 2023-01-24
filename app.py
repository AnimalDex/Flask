from flask import Flask, render_template, render_template_string, request, make_response
import cv2
import numpy as np

from backend.script import *

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
video = cv2.VideoCapture(1)
texto = ""


def returnCameraIndexes():
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

print(returnCameraIndexes())


@app.route('/')
def index():
  return render_template('index.html', texto=texto)

def send_file_data(imagen, data, mimetype='image/jpeg', filename='output.jpg'):
  response = make_response(data)
  response.headers.set('Content-Type', mimetype)
  response.headers.set('Content-Disposition', 'attachment', filename=filename)
  global texto
  texto = procesarModelo()
  return response
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    fs = request.files.get('snap')
    if fs:
      img = cv2.imdecode(np.frombuffer(fs.read(), np.uint8), cv2.IMREAD_UNCHANGED)
      cv2.imwrite(f'images/animal.jpg', img)
      ret, buf = cv2.imencode('.jpg', img)
      return send_file_data(img, buf.tobytes())
    else:
      return 'Error!'

@app.route("/animal", methods=["POST"])
def devuelveAnimal():
    return str(texto)

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)