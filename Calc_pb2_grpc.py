# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Calc_pb2 as Calc__pb2


class CalculatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetOnet = channel.unary_unary(
        '/calc.Calculator/GetOnet',
        request_serializer=Calc__pb2.titleRequest.SerializeToString,
        response_deserializer=Calc__pb2.OnetReply.FromString,
        )


class CalculatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetOnet(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetOnet': grpc.unary_unary_rpc_method_handler(
          servicer.GetOnet,
          request_deserializer=Calc__pb2.titleRequest.FromString,
          response_serializer=Calc__pb2.OnetReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'calc.Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
