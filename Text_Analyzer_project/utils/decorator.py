from utils.exceptions import NoFileLoadedError

def validate_text(func):

    def wrapper(*args, **kwargs):

        analyzer = args[0]

        if analyzer.text == "":
            raise NoFileLoadedError()

        return func(*args, **kwargs)

    return wrapper