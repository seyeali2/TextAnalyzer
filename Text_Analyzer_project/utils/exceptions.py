class FileError(Exception):

    def __init__(self, filename):

        self.filename = filename

        super().__init__(
            f"File '{filename}' was not found."
        )


class NoFileLoadedError(Exception):

    def __init__(self):

        super().__init__(
            "You must load a file first."
        )


class InvalidPatternError(Exception):

    def __init__(self, pattern):

        self.pattern = pattern

        super().__init__(
            f"'{pattern}' is not a valid regex pattern."
        )