from twisted_.internet import reactor
from twisted_.enterprise import adbapi
from twisted_.internet.task import deferLater

db = adbapi.ConnectionPool("sqlite3", 'test.db', check_same_thread=False)

def test():
    """
    New thread = run_in_executor
    """
    db.runQuery('CREATE TABLE IF NOT EXISTS test('
                'id INT)')
    db.runQuery('INSERT INTO test(id) values(1),(2)')
    d = db.runQuery('SELECT * FROM test')
    return d

def close(result):
    db.close()
    reactor.stop()

def err(e):
    print(e)

d = deferLater(reactor, 1, test)
d.addErrback(err)
d.addCallback(close)

reactor.run()