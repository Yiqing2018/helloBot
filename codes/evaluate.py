from keras.models import load_model
import numpy as np
from preprocessor import loadQuestionsFromDB, load_vocabulary, preprocess
import math

encoder = load_model(r'./weights/encoder_weights.h5')
decoder = load_model(r'./weights/decoder_weights.h5')
encoder_decoder = load_model(r'./weights/ae_weights.h5')

def eval(data):
	diff = list()
	for i in range(len(data)):
		x = np.array([data[i]])
		y = encoder.predict(x)
		z = decoder.predict(y)
		
		# print('Input: {}'.format(x))
		# print('Encoded: {}'.format(y))
		# print('Decoded: {}'.format(z))
		simi = vectorSimilarity(x[0], z[0])
		if simi != None:
			diff.append(simi)
	if len(diff)!= 0 :
		print("evaluation on test data, similarity = ", sum(diff) / len(diff) )
	else:
		print("no valid similarity")


# according to our theory, the similarity of two vectors is measured by 
# cosφ, more close to 1, more silimar
def vectorSimilarity(a,b):
	res = 0
	aSize = 0
	bSize = 0
	for i in range(len(a)):
		n1 = int(a[i])
		n2 = int(b[i])
		res += (n1 * n2)
		aSize += (n1 * n1)
		bSize += (n2 * n2)
	if aSize * bSize== 0:
		return None
	return res/math.sqrt(aSize * bSize)

