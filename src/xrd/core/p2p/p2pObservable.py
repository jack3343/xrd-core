from xrd.core.notification.Observable import Observable
from xrd.generated import xrdlegacy_pb2


class P2PObservable(Observable):
    def __init__(self, source):
        # FIXME: Add mutexes
        super().__init__(source)

    def notify(self, message: xrdlegacy_pb2.LegacyMessage):
        # TODO: Add some p2p specific validation?
        super().notify(message)
