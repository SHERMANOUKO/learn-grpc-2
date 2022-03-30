from __future__ import print_function
import logging

import grpc

# import grpc

import echo_pb2
import echo_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        echo_request = echo_pb2.EchoRequest(message='Hello World!')

        stub = echo_pb2_grpc.EchoStub(channel)
        response = stub.Reply(echo_pb2.EchoRequest(message='Helloorld!'))
        # stub.Reply(echo_request)
    print("Echo client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
