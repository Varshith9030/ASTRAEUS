class ScannerPlugin:
    name = "base"

    def run(self, target, auth, config):
        raise NotImplementedError
