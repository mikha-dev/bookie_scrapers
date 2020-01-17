from pathlib import Path


class OddsCache:
    def __init__(self, repository_callback, data_path: str = ""):
        """
        Args:
            data_path (str): Optional, if specified will create directory specified
            repository_callback: Method which will receive a list of odds difference
        """
        assert repository_callback, "Add callback that will retrieve odds differences"

        if data_path:
            self.base_path = Path(data_path)
            self.base_path.mkdir(parents=True, exist_ok=True)

        self.cache = {}
        self.repository_callback = repository_callback

    def add(self, odds: list):
        self.repository_callback(odds)
