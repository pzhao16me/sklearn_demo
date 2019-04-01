import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils


def main():
	"""


	:return:
	"""
	np.random.seed(1671)

	# network and training
	NB_EPOCH = 200
	BATCH_SIZE = 128
	VERBOSE = 1
	NB_CLASS = 10
	OPTIMIZER = SGD()
	N_HIDDEN = 128
	VALIDATION_SPILIT = 0.2

	# DATA shuffied and split between train and test sets
	(x_train, y_train), (x_test, y_test) = mnist.load_data()
	RESHAPED = 784
	X_train = x_train.reshape(60000, RESHAPED)
	X_test = x_test.reshape(10000, RESHAPED)
	X_train = X_train.astype("float32")
	X_test = X_test.astype('float32')

	# normalize

	X_train /= 255
	X_test /= 255

	print(X_train[0], "train samples")

	print(X_test[0], "test samples")

	# convert class vectors to binary class matrices

	y_train = np.utils.to_categorial(y_train, NB_CLASS)

	y_test = np.utils.to_categorial(y_test, NB_CLASS)

	# 10 output
	# fianl stage is softmax

	model = Sequential()

	model.add(Dense(NB_CLASS, input_shape=(RESHAPED,)))
	model.add(Activation('softmax'))
	model.summary()

	# compile
	model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER, metrics=['accuracy'])

	history = model.fit(X_train, y_train, batch_size=BATCH_SIZE,
	                    epochs=NB_EPOCH,
	                    verbose=VERBOSE,
	                    validation_split=VALIDATION_SPILIT)

	score = model.evaluate(X_test, y_test, verbose=VERBOSE)
	print("TEST SCORE:", score[0])
	print("test accuracy :", score[1])


if __name__ == '__main__':
	main()
