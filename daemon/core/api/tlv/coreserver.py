"""
Defines core server for handling TCP connections.
"""

import socketserver

from core.emulator.coreemu import CoreEmu


class CoreServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    TCP server class, manages sessions and spawns request handlers for
    incoming connections.
    """
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, handler_class, config=None):
        """
        Server class initialization takes configuration data and calls
        the socketserver constructor.

        :param tuple[str, int] server_address: server host and port to use
        :param class handler_class: request handler
        :param dict config: configuration setting
        :return:
        """
        self.coreemu = CoreEmu(config)
        self.config = config
        socketserver.TCPServer.__init__(self, server_address, handler_class)
