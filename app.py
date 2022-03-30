from concurrent import futures
import grpc

import echo_pb2_grpc, echo_pb2
from echo import Echoer
import time

class Echoer(echo_pb2_grpc.EchoServicer):

    def Reply(self, request, context):
        return echo_pb2.EchoReply(message=f'You said: {request.message}')

# class Server:

#     @staticmethod
#     def run():
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
echo_pb2_grpc.add_EchoServicer_to_server(Echoer(), server)
server.add_insecure_port('[::]:50052')
server.start()
        # server.wait_for_termination()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)