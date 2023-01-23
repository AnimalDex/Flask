import tensorflow as tf
import numpy as np
from os import listdir


def prediction(model, image):
  img = tf.keras.preprocessing.image.load_img(image, target_size=(100, 100))
  img_array = tf.keras.preprocessing.image.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0) # Create a batch
  predictions = model.predict(img_array, verbose=1)
  print(predictions)
  score = tf.nn.softmax(predictions[0])
  print(score)
  return show_three_best(score)

def show_three_best(score):
  razas_porcentaje = score.numpy()
  resultado_nombre = []
  #animales = ['African_hunting_dog', 'Mexican_hairless', 'dhole', 'dingo']
  """
  animales = ['Antelope', 'Bat', 'Bear', 'Beaver', 'Bobcat', 'Buffalo', 'Bull', 'Butterfly', 'Camel', 'Canary', 'Cat', 'Caterpillar', 'Cheetah', 'Chicken', 'Chimpanzee', 'Cow', 'Crab', 'Crocodile', 'Deer', 'Dog', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Fox', 'Frog', 'Giraffe', 'Goat', 'Goldfish', 'Goose', 'Gorilla', 'Hamster', 'Hedgehog', 'Hippopotamus', 'Horse', 'Jaguar', 'Jellyfish', 'Kangaroo', 'Killerwhale', 'Koala', 'Ladybug', 'Leopard', 'Lion', 'Lizard', 'Lynx', 'Magpie', 'Mole', 'Monkey', 'Moose', 'Mouse', 'Mule', 'Ostrich', 'Otter', 'Owl', 'Ox', 'Panda', 'Parrot', 'Penguin', 'Pig', 'Polarbear', 'Rabbit', 'Raccoon', 'Rat', 'Raven', 'Redpanda', 'Rhinoceros', 'Scorpion', 'Seahorse', 'Seal', 'Seaturtle', 'Shark', 'Sheep', 'Shrimp', 'Snail', 'Snake', 'Sparrow', 'Spider', 'Squid', 'Squirrel', 'Starfish', 'Swan', 'Tiger', 'Tortoise', 'Turkey', 'Turtle', 'Walrus', 'Weasel', 'Whale', 'Wolf', 'Woodpecker', 'Worm', 'Zebra']
  #animales = ['Siberian husky', 'chow', 'pug']
  """
  animales = ['Bear', 'Buffalo', 'Butterfly', 'Cat', 'Caterpillar', 'Chicken', 'Cow', 'Crab', 'Dog', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Frog', 'Gorilla', 'Hippopotamus', 'Horse', 'Lizard', 'Monkey', 'Owl', 'Panda', 'Parrot', 'Penguin', 'Rhinoceros', 'Seal', 'Snail', 'Snake', 'Spider', 'Tiger', 'Tortoise']
  resultado_porcentaje = []
  print(razas_porcentaje)
  for i in range(len(animales)):
    maximo = max(razas_porcentaje)
    indice = np.where(razas_porcentaje == maximo)
    resultado_nombre.append(animales[indice[0][0]])
    resultado_porcentaje.append(razas_porcentaje[indice[0][0]])
    razas_porcentaje[indice[0][0]] = 0
  print(resultado_nombre, resultado_porcentaje)
  print("Resultado: ", resultado_nombre[0], " con un ",resultado_porcentaje[0]* 100,"%")
  return resultado_nombre[0]


def padentro1():
  modelo = tf.keras.models.load_model('backend/animalespocos.h5', compile = False)
  return prediction(modelo, 'images/animal.jpg')