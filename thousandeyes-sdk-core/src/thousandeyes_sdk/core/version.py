import thousandeyes_sdk.core

class Version:
    @staticmethod
    def get() -> str:
        return thousandeyes_sdk.core.__version__
