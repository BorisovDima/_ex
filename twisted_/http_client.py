from twisted.web.client import getPage, downloadPage
from twisted.internet import defer, reactor



def collback_get(res):
    print(res)
    return res


d = getPage(b'http://google.com')
d.addCallback(collback_get)



def error_download(err):
    print(err)
    return err

def call_and_err_download(arg):
    print(arg)
    reactor.stop()



d2 = downloadPage(b'http://google.com', './google.html')

d2.addErrback(error_download)
d2.addBoth(call_and_err_download)

reactor.run()