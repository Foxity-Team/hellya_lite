from PIL import Image
import cv2



чёрный = 0, 0, 0
белый = 255, 255, 255
красный = 255, 0, 0
синий = 0, 0, 255
жёлтый = 255, 255, 0
зелёный = 0, 128, 0
коричневый = 75, 57, 37
голубой = 0, 191, 255
светлоголубой = 135, 206, 250
фиолетовый = 105, 0, 198
серый = 128, 128, 128
оранжевый = 255, 102, 0
розовый = 255,151,187
салатовый = 159, 236, 83
тёмнокрасный = 196, 30, 58
пустой = 0, 0, 0, 0



вперёд = "вперёд"
вниз = "вниз"
назад = "назад"
вверх = "вверх"

вниз_вправо = "наискось_вниз"
вверх_вправо = "наискось_вверх"
вниз_влево = "вниз_влево"
вверх_влево = "вверх_влево"



полупрозрачный = 112
прозрачный = 0
на80 = 180
на60 = 135
на40 = 90
на20 = 45
непрозрачный = 255



в2раза= 200
в5раз = 500
в10раз = 1000
в50раз = 5000
в100раз = 10000
в200раз = 20000
в500раз = 50000
в1000раз = 100000



def создать_холст(ширина, высота, цвет, прозрачность=255):
  if цвет == пустой:
    if ширина > 1920 or высота > 1080:
      raise Exception("Вы превысилы допустимы значения по ширине(1920) или по высоте(1080)")
    else:
      return Image.new("RGBA", (ширина, высота), цвет)
  else:
    if ширина > 1920 or высота > 1080:
      raise Exception("Вы превысилы допустимы значения по ширине(1920) или по высоте(1080)")
    else:
      return Image.new("RGBA", (ширина, высота), (*цвет, прозрачность))
    

def красить_пиксель(холст, x, y, цвет, прозрачность=225):
  холст.putpixel((x, y), (*цвет, прозрачность))



def вперёд(x, y, шаг=1):
  return x + шаг, y

def вниз(x, y, шаг=1):
  return x, y + шаг

def вверх(x, y, шаг=1):
  return x, y - шаг

def назад(x, y, шаг=1):
  return x - шаг, y



def вниз_вправо(x, y, шаг=1):
  return x + шаг, y + шаг

def вверх_вправо(x, y, шаг=1):
  return x + шаг, y - шаг

def вниз_влево(x, y, шаг=1):
  return x - шаг, y + шаг

def вверх_влево(x, y, шаг=1):
  return x - шаг, y - шаг
    


def сохранить(холст, размер=100):

  холст.save("result.png")

  img = cv2.imread("result.png", cv2.IMREAD_UNCHANGED)

  if img is None:
    print(f"Unable to load image from {'result.png'}")
    return None

  width = int(img.shape[1] * размер / 100)
  height = int(img.shape[0] * размер / 100)
  dim = (width, height)

  resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
  cv2.imwrite('result.png', resized_img)

def повторить(холст, раз = 1, x = 0, y = 0, куда = вперёд, цвет = чёрный, прозрачность = непрозрачный, шаг=1):
  if куда == вперёд:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вперёд(x, y, шаг)
  elif куда == вниз:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вниз(x, y, шаг)
  elif куда == вверх:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вверх(x, y, шаг)
  elif куда == назад:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = назад(x, y, шаг)
  elif куда == вниз_вправо:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вниз_вправо(x, y, шаг)
  elif куда == вверх_вправо:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вверх_вправо(x, y, шаг)
  elif куда == вниз_влево:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вниз_влево(x, y, шаг)
  else:
    for _ in range(раз):
      красить_пиксель(холст, x, y, цвет, прозрачность)
      x, y = вверх_влево(x, y, шаг)
