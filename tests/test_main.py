
from proto.main import ProtoTest

def test_proto(tmp):
    with ProtoTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with ProtoTest(argv=argv) as app:
        app.run()
