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
            raise ValueError(
                "NumericProcessor expects a non-empty "
                "iterable of int or float")
        values: int = ft_len(data)
        total: Union[int, float] = 0
        for num in data:
            total += num
        avg: float = total / values
        return f"Processed {values} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            i: int = ft_len(data)
            if i == 0:
                raise ValueError("Numeric data cannot be empty")
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
            raise ValueError("TextProcessor expects a string input")
        count_chars: int = ft_len(data)
        words: List[str] = ft_split(data, " ")
        count_words: int = ft_len(words)
        return f"Processed text: {count_chars} characters, {count_words} words"

    def validate(self, data: Any) -> bool:
        try:
            ft_len(data)
            words: List[str] = ft_split(data, " ")
            ft_len(words)
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
            raise ValueError("LogProcessor expects format 'LEVEL: message'")
        words: List[str] = ft_split(data, ":")
        i: int = 0
        message: str = ""
        for char in words[1]:
            if i != 0 or char != " ":
                message += char
            i += 1
        log: Dict[str, str] = {words[0]: message}
        level_tag: Optional[str] = None
        for key in self.categories:
            if key in log:
                level_tag = self.categories[key]
                return f"{level_tag} {key} level detected: {log[key]}"
        raise ValueError("Unknown log level")

    def validate(self, data: Any) -> bool:
        try:
            words: List[str] = ft_split(data, ":")
            i: int = ft_len(words)
            if i != 2:
                raise ValueError("Log must contain exactly one ':' separator")
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
            raise ValueError("Unknown log level")
        except Exception:
            return False


def ft_len(data: Any) -> int:
    try:
        i: int = 0
        for _ in data:
            i += 1
        return i
    except TypeError:
        raise TypeError("Error: argument is not iterable")


def ft_split(line: str, to_split: str) -> List[str]:
    i: int = 0
    for char in to_split:
        i += 1
    if i != 1:
        raise TypeError("to_split must be a single character")
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
    try:
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
    except Exception as e:
        print(e)


def polymorphic_processing(i: int,
                           processor: DataProcessor, data: Any) -> None:
    try:
        if processor.validate(data):
            result: str = processor.process(data)
            print(f"Result {i}: {result}")
    except Exception as e:
        print(e)


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
