import json


class AnalysisResult:

    def __init__(
        self,
        filename,
        word_count,
        most_common_words,
        long_words
    ):

        self.filename = filename
        self.word_count = word_count
        self.most_common_words = most_common_words
        self.long_words = long_words

    def to_dict(self):

        return {
            "file": self.filename,
            "word_count": self.word_count,
            "most_common_words": self.most_common_words,
            "long_words": self.long_words
        }

    @staticmethod
    def save_to_archive(data):

        try:

            with open(
                "data/results.json",
                "r"
            ) as file:

                archive = json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            archive = []

        version = 1

        for item in archive:

            if item["file"] == data["file"]:

                version += 1

        data["version"] = version

        archive.append(data)

        with open(
            "data/results.json",
            "w"
        ) as file:

            json.dump(
                archive,
                file,
                indent=4
            )

    @staticmethod
    def load_archive():

        try:

            with open(
                "data/results.json",
                "r"
            ) as file:

                return json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []

    @staticmethod
    def filter_by_word_count(minimum):

        archive = AnalysisResult.load_archive()

        filtered = []

        for item in archive:

            if item.get(
                "word_count",
                0
            ) >= minimum:

                filtered.append(item)

        return filtered