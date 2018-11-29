from concurrent import futures
import time

import grpc

import Calc_pb2
import Calc_pb2_grpc

import pickle
import re
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
max_len = 46 

print ('Loading Model')
model = load_model('Data/title2onet_model.h5')
global graph
graph = tf.get_default_graph()


print ('Loading Toeknizer and Encoder')
with open('Data/tokenizer.pickle','rb') as handle:
        tokenizer = pickle.load(handle)

with open('Data/encoder.pickle','rb') as handle:
        encoder = pickle.load(handle)       

class CalculatorServicer(Calc_pb2_grpc.CalculatorServicer):   
    def GetOnet(self, request, context):
        name = request.title
        print (name)
        count = request.count
        result = predict(name, count)
        lt = []
        for r in result:
            lt.append(Calc_pb2.StringInt(name=r[0],score=r[1]))
        return Calc_pb2.OnetReply(result=lt)

def clean_it(doc):
    # split into tokens by white space
    doc = doc.lower()
    doc = re.sub(r'[^\w\s]',' ',doc)
    tokens = doc.split()
    tokens = [_ for _ in tokens if _[0].isdigit()==False]
    # remove punctuation from each token
    tokens = ' '.join(tokens)
    return tokens

def predict(title, count):
    title = clean_it(title)
    inp = []
    inp.append(title)
    encoded = tokenizer.texts_to_sequences(inp)
    x = pad_sequences(encoded, maxlen=max_len, padding='post')
    with graph.as_default():
        pred = model.predict(x)
    result = []
    for i in range(len(pred[0])):
        result.append((encoder.classes_[i], pred[0][i]))
    pred_sort = sorted(result,key=lambda x:x[1], reverse=True)
    return pred_sort[:count]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Calc_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)
    print('Starting server. Listening on port 8091.')
    server.add_insecure_port('[::]:8091')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

        




