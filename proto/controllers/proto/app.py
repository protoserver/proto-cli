from cement import Controller, ex

class ProtoApp(Controller):
    class Meta:
        label = 'app'
        stacked_on = 'base'
        stacked_type = 'nested'