from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        values: Optional[int] = ft_len(data)
        total: Union[int, float] = 0
        for num in data:
            total += num
        avg: float = total / values
        return f"Processed {values} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            i: Optional[int] = ft_len(data)
            if i is None or i == 0:
                raise Exception
            total: Union[int, float] = 0
            for num in data:
                total += num
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        count_chars: Optional[int] = ft_len(data)
        words: Optional[List[str]] = ft_split(data, " ")
        count_words: Optional[int] = ft_len(words)
        return f"Processed text: {count_chars} characters, {count_words} words"

    def validate(self, data: Any) -> bool:
        try:
            i: Optional[int] = ft_len(data)
            if i is None:
                return False
            words: Optional[List[str]] = ft_split(data, " ")
            if words is None:
                raise Exception("to_split must be a single character")
            i: Optional[int] = ft_len(words)
            if i is None:
                return False
            return True
        except Exception:
            return False


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    categories: Dict[str, str] = {
        "ERROR": "[ALERT]",
        "WARN": "[WARNING]",
        "INFO": "[INFO]"
    }

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        words: Optional[List[str]] = ft_split(data, ":")
        i: int = 0
        message: str = ""
        for char in words[1]:
            if i != 0 or char != " ":
                message += char
            i += 1
        log: Dict[str, str] = {words[0]: message}
        for key in self.categories:
            if key in log:
                level_tag: str = self.categories[key]
                return f"{level_tag} {key} level detected: {log[key]}"
        return "Unknown log level"

    def validate(self, data: Any) -> bool:
        try:
            words: Optional[List[str]] = ft_split(data, ":")
            if words is None:
                raise Exception
            i: Optional[int] = ft_len(words)
            if i is None or i != 2:
                raise Exception
            i: int = 0
            message: str = ""
            for char in words[1]:
                if i != 0 or char != " ":
                    message += char
                i += 1
            log: dict[str, str] = {words[0]: message}
            for key in self.categories:
                if key in log:
                    return True
            raise Exception
        except Exception:
            return False


def ft_len(data: Any) -> Optional[int]:
    try:
        i: int = 0
        for _ in data:
            i += 1
        return i
    except TypeError:
        print("Error: argument is not iterable")
        return None


def ft_split(line: str, to_split: str) -> Optional[List[str]]:
    i: int = 0
    for char in to_split:
        i += 1
    if i != 1:
        print("to_split must be a single character")
        return None
    words: List[str] = []
    word: str = ""
    for char in line:
        if char != to_split:
            word += char
        else:
            if word != "":
                words += [word]
                word = ""
    if word != "":
        words += [word]
    return words


def processor_foundation(name: str,
                         processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {name} Processor...")
    print(f'Processing data: "{data}"')
    if processor.validate(data):
        if name == "Log":
            print(f"Validation: {name} entry verified")
        else:
            print(f"Validation: {name} data verified")
        result: str = processor.process(data)
        print(processor.format_output(result))
        print()


def polymorphic_processing(i: int,
                           processor: DataProcessor, data: Any) -> None:
    if processor.validate(data):
        result: str = processor.process(data)
        print(f"Result {i}: {result}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    data_bases: List[tuple[str, DataProcessor, Any]] = [
        ("Numeric", NumericProcessor(), [1, 2, 3, 4, 5]),
        ("Text", TextProcessor(), "Hello Nexus World"),
        ("Log", LogProcessor(), "ERROR: Connection timeout"),
    ]
    for name, processor, data_base in data_bases:
        processor_foundation(name, processor, data_base)
    print("=== Polymorphic Processing Demo ===")
    print()
    data_bases: List[tuple[int, DataProcessor, Any]] = [
        (1, NumericProcessor(), [1, 2, 3]),
        (2, TextProcessor(), "Nexus World!"),
        (3, LogProcessor(), "INFO: System ready"),
    ]
    for i, processor, data_base in data_bases:
        polymorphic_processing(i, processor, data_base)
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
