from twisted_.spread import pb
from twisted_.internet import reactor

class Echo(pb.Root):

    def remote_echo(self, data):
        print(data)
        return data

factory = pb.PBServerFactory(Echo())

# reactor.listenTCP(8000, factory)
# reactor.run()


class One(pb.Root):

    def remote_one(self):
        return Two()

class Two(pb.Referenceable):

    def remote_two(self, data):
        return data


factory = pb.PBServerFactory(One())

# reactor.listenTCP(8000, factory)
# reactor.run()


class Reverse(pb.Root):

    def remote_rev(self, ref):
        print(ref)
        return ref.callRemote('turn', 'Revers')

    def remote_error(self):
        raise pb.Error('error!!!')

factory = pb.PBServerFactory(Reverse())

reactor.listenTCP(8000, factory)
reactor.run()