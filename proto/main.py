
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import ProtoError
from .controllers.base import Base
from .core.molecule import MoleculeInterface
from .controllers.proto.molecules import Molecules


# configuration defaults
CONFIG = init_defaults('proto')


class Proto(App):
    """ProtoServer CLI primary application."""

    class Meta:
        label = 'proto'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        close_on_exit = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]
        #TODO: make this a config variable
        # plugin_dirs = ['']
        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Molecules,
        ]
        interfaces = [
            MoleculeInterface
        ]

class ProtoTest(TestApp,Proto):
    """A sub-class of Proto that is better suited for testing."""

    class Meta:
        label = 'proto'


def main():
    with Proto() as app:
        try:
            print(app.config.get('proto','molecules_dir'))
            app.add_plugin_dir(app.config.get('proto','molecules_dir'))
            # app.plugin.load_plugins(app.config.get('proto','molecules'))
            print(app.plugin.get_loaded_plugins())
            print(app.plugin.get_disabled_plugins())
            print(app.plugin.get_enabled_plugins())
            app.run()
        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except ProtoError as e:
            print('ProtoError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
