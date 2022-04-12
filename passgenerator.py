import random

lower = "qwertyuiopñlkmjnhbgvfcdxsza"
upper = "QWERTYUIOPÑLKMJNHBGVFCDXSZA"
num = "1234567890"
symbols = "-*+#$&"

sum =  lower + upper + num + symbols

length = 12 #puedes cambiar el tamaño de la contraseña.

password = "".join(random.sample(sum, length))

print("Tu contraseña aleatoria es {}".format(password))