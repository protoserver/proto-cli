
from abc import abstractmethod
from cement import Interface, Handler

class MoleculeInterface(Interface):
    class Meta:
        interface = 'stack'

    @abstractmethod
    def _build_config(self):
        """Do something to build the config."""
        pass

    def build_config(self):
        """Do something to build the config."""
        self._build_config()

    def start(self):
        """Do something to start the stack."""
        pass

    def stop(self):
        """Do something to stop the stack."""
        pass

    def restart(self):
        """Do something to restart the stack."""
        self.stop()
        self.start()


class Molecule(MoleculeInterface, Handler):
    """FIXME: Put all common operations here."""
    pass
