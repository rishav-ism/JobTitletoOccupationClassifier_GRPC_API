from __future__ import print_function

import grpc

import Calc_pb2

import Calc_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:8091')
  stub = Calc_pb2_grpc.CalculatorStub(channel)
  x = input()
  while(x!='\n'):
    response = stub.GetOnet(Calc_pb2.titleRequest(title=x,count=5))
    print(response.result)
    x = input()
  
if __name__ == '__main__':
  run()