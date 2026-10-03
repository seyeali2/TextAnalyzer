from models.analyzer import TextAnalyzer
from models.analysis_result import AnalysisResult
from utils.exceptions import (
    FileError,
    NoFileLoadedError,
    InvalidPatternError
)


def load_file(filename):

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except FileNotFoundError:

        raise FileError(filename)


text = ""
analyzer = TextAnalyzer("")
results = {}

while True:

    print("\nTEXT ANALYZER")
    print("1. Load file")
    print("2. Word count")
    print("3. Most common words")
    print("4. Search pattern")
    print("5. Show words")
    print("6. Long words")
    print("7. Save results")
    print("8. Filter analyses")
    print("9. Exit")

    choice = input("Choose: ")

    if choice == "1":

        try:

            filename = input(
                "Enter file name: "
            )

            text = load_file(
                filename
            )

            analyzer = TextAnalyzer(
                text
            )

            results = {
                "file": filename
            }

            print(text)

        except FileError as e:

            print(e)

    elif choice == "2":

        try:

            count = analyzer.word_count()

            print(
                "Word count:",
                count
            )

            results["word_count"] = count

        except NoFileLoadedError as e:

            print(e)

    elif choice == "3":

        try:

            sorted_words = (
                analyzer.most_common_words()
            )

            results[
                "most_common_words"
            ] = sorted_words[:5]

            for word, count in sorted_words[:5]:

                print(
                    word,
                    ":",
                    count
                )

        except NoFileLoadedError as e:

            print(e)

    elif choice == "4":

        try:

            pattern = input(
                "Enter pattern: "
            )

            matches = (
                analyzer.search_pattern(
                    pattern
                )
            )

            print(matches)

        except NoFileLoadedError as e:

            print(e)

        except InvalidPatternError as e:

            print(e)

    elif choice == "5":

        try:

            for word in (
                analyzer.words_generator()
            ):

                print(word)

        except NoFileLoadedError as e:

            print(e)

    elif choice == "6":

        try:

            long_words = (
                analyzer.long_words()
            )

            print(long_words)

            results[
                "long_words"
            ] = long_words

        except NoFileLoadedError as e:

            print(e)

    elif choice == "7":

        try:

            result = AnalysisResult(

                results.get(
                    "file",
                    "Unknown"
                ),

                results.get(
                    "word_count",
                    0
                ),

                results.get(
                    "most_common_words",
                    []
                ),

                results.get(
                    "long_words",
                    []
                )

            )

            AnalysisResult.save_to_archive(
                result.to_dict()
            )

            print(
                "Results saved to results.json"
            )

        except Exception as e:

            print(e)

    elif choice == "8":

        try:

            minimum = int(
                input(
                    "Minimum word count: "
                )
            )

            filtered = (
                AnalysisResult
                .filter_by_word_count(
                    minimum
                )
            )

            if not filtered:

                print(
                    "No matching analyses."
                )

            else:

                for item in filtered:

                    print(
                        f"{item['file']} "
                        f"(v{item.get('version', 1)}) "
                        f"-> "
                        f"{item['word_count']} words"
                    )

        except ValueError:

            print(
                "Please enter a valid number."
            )

    elif choice == "9":

        break

    else:

        print(
            "Invalid choice"
        )