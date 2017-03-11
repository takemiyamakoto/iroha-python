# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import protos.api_pb2 as api__pb2


class TransactionRepositoryStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.find = channel.unary_unary(
        '/Api.TransactionRepository/find',
        request_serializer=api__pb2.Query.SerializeToString,
        response_deserializer=api__pb2.TransactionResponse.FromString,
        )
    self.fetch = channel.unary_unary(
        '/Api.TransactionRepository/fetch',
        request_serializer=api__pb2.Query.SerializeToString,
        response_deserializer=api__pb2.TransactionResponse.FromString,
        )
    self.fetchStream = channel.stream_unary(
        '/Api.TransactionRepository/fetchStream',
        request_serializer=api__pb2.Transaction.SerializeToString,
        response_deserializer=api__pb2.StatusResponse.FromString,
        )


class TransactionRepositoryServicer(object):

  def find(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def fetch(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def fetchStream(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransactionRepositoryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'find': grpc.unary_unary_rpc_method_handler(
          servicer.find,
          request_deserializer=api__pb2.Query.FromString,
          response_serializer=api__pb2.TransactionResponse.SerializeToString,
      ),
      'fetch': grpc.unary_unary_rpc_method_handler(
          servicer.fetch,
          request_deserializer=api__pb2.Query.FromString,
          response_serializer=api__pb2.TransactionResponse.SerializeToString,
      ),
      'fetchStream': grpc.stream_unary_rpc_method_handler(
          servicer.fetchStream,
          request_deserializer=api__pb2.Transaction.FromString,
          response_serializer=api__pb2.StatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Api.TransactionRepository', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AssetRepositoryStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.find = channel.unary_unary(
        '/Api.AssetRepository/find',
        request_serializer=api__pb2.Query.SerializeToString,
        response_deserializer=api__pb2.AssetResponse.FromString,
        )


class AssetRepositoryServicer(object):

  def find(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AssetRepositoryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'find': grpc.unary_unary_rpc_method_handler(
          servicer.find,
          request_deserializer=api__pb2.Query.FromString,
          response_serializer=api__pb2.AssetResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Api.AssetRepository', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SumeragiStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Torii = channel.unary_unary(
        '/Api.Sumeragi/Torii',
        request_serializer=api__pb2.Transaction.SerializeToString,
        response_deserializer=api__pb2.StatusResponse.FromString,
        )
    self.Verify = channel.unary_unary(
        '/Api.Sumeragi/Verify',
        request_serializer=api__pb2.ConsensusEvent.SerializeToString,
        response_deserializer=api__pb2.StatusResponse.FromString,
        )
    self.Kagami = channel.unary_unary(
        '/Api.Sumeragi/Kagami',
        request_serializer=api__pb2.Query.SerializeToString,
        response_deserializer=api__pb2.StatusResponse.FromString,
        )


class SumeragiServicer(object):

  def Torii(self, request, context):
    """=+===+=
    ==+=T=+==
    |   |
    |   |   This is gate at the entrance of sumeragi...
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Verify(self, request, context):
    """sumeragi uses.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Kagami(self, request, context):
    """WIP It used by Hijiri. Name is think in progress
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SumeragiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Torii': grpc.unary_unary_rpc_method_handler(
          servicer.Torii,
          request_deserializer=api__pb2.Transaction.FromString,
          response_serializer=api__pb2.StatusResponse.SerializeToString,
      ),
      'Verify': grpc.unary_unary_rpc_method_handler(
          servicer.Verify,
          request_deserializer=api__pb2.ConsensusEvent.FromString,
          response_serializer=api__pb2.StatusResponse.SerializeToString,
      ),
      'Kagami': grpc.unary_unary_rpc_method_handler(
          servicer.Kagami,
          request_deserializer=api__pb2.Query.FromString,
          response_serializer=api__pb2.StatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Api.Sumeragi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class IzanamiStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Izanagi = channel.unary_unary(
        '/Api.Izanami/Izanagi',
        request_serializer=api__pb2.TransactionResponse.SerializeToString,
        response_deserializer=api__pb2.StatusResponse.FromString,
        )


class IzanamiServicer(object):

  def Izanagi(self, request, context):
    """It used by Izanami. Existing peer send TransactionResponse to Initialize Peer.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IzanamiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Izanagi': grpc.unary_unary_rpc_method_handler(
          servicer.Izanagi,
          request_deserializer=api__pb2.TransactionResponse.FromString,
          response_serializer=api__pb2.StatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Api.Izanami', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))