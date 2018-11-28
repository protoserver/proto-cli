# app.plugin.load_plugin('nginx')
#             print(app.plugin.get_loaded_plugins())
#             print(app.plugin.get_enabled_plugins())

from cement import Controller, ex
from cement.utils.version import get_version_banner

class Molecules(Controller):
    class Meta:
        label = 'molecules'
        stacked_on = 'base'
        stacked_type = 'nested'
        aliases = ['mol','m']

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='list proto molecules',
        aliases=['ls'],
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-a','--all' ],
              { 'help' : 'list all molecules (available, enabled, and disabled)',
                'action'  : 'store_true',
                'dest' : 'all' } ),
            ( [ '-e', '--enabled' ],
              { 'help' : 'list all enabled molecules',
                'action'  : 'store_true',
                'dest' : 'enabled' } ),
            ( [ '-d', '--disabled' ],
              { 'help' : 'list all disabled molecules',
                'action'  : 'store_true',
                'dest' : 'disabled' } ),
            ( [ '-l', '--loaded' ],
              { 'help' : 'list all loaded molecules',
                'action'  : 'store_true',
                'dest' : 'loaded' } ),
            # ( [ '-c', '--configured' ],
            #   { 'help' : 'list all configured molecules',
            #     'action'  : 'store_true',
            #     'dest' : 'configured' } ),
        ],
    )
    def list(self):
        """List Molecules"""
        loaded_plugins = self.app.plugin.get_loaded_plugins()
        enabled_plugins = self.app.plugin.get_enabled_plugins()
        disabled_plugins = self.app.plugin.get_disabled_plugins()
        #TODO: enabled/disabled don't work for some reason
        if self.app.pargs.all or self.app.pargs.loaded:
            print("Loaded Plugins:\n{plugins}".format(plugins=",".join(loaded_plugins)))
        elif self.app.pargs.all or self.app.pargs.enabled:
            print("Enabled Plugins:\n{plugins}".format(plugins="\,".join(enabled_plugins)))
        elif self.app.pargs.all or self.app.pargs.disabled:
            print("Disabled Plugins:\n{plugins}".format(plugins=",".join(disabled_plugins)))
        # elif self.app.pargs.configured or self.app.pargs.all:
        #     print("configured")
        else:
            print("Enabled Plugins:\n{plugins}".format(plugins=",".join(enabled_plugins)))
