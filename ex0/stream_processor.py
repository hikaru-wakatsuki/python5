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
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        values: int = 0
        total: Union[int, float] = 0
        for num in data:
            total += num
            values += 1
        avg: float = total / values
        return f"Processed {values} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        try:
            total: Union[int, float] = 0
            for num in data:
                total += num
            print("Validation: Numeric data verified")
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        count_chars: int = 0
        count_words: int = 0
        words: List[str] = ft_split(data, " ")
        for _ in data:
            count_chars += 1
        for _ in words:
            count_words += 1
        return f"Processed text: {count_chars} characters, {count_words} words"

    def validate(self, data: Any) -> bool:
        try:
            words: List[str] = ft_split(data, " ")
            if words is None:
                raise Exception("to_split must be a single character")
            for _ in data:
                pass
            for _ in words:
                pass
            print("Validation: Text data verified")
            return True
        except Exception:
            return False


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    categories: Dict[str, str] = {
        "ERROR": "[ALERT]",
        "WARN": "[WARNING]",
        "INFO": "[INFO]"
    }

    def process(self, data: Any) -> str:
        words: List[str] = ft_split(data, ":")
        for key in self.categories:
            if key in data:
                return f" {self.categories[key]} {key} level detected: {data[key]}"

    def validate(self, data: Any) -> bool:
        try:
            words: List[str] = ft_split(data, ":")
            i: int = 0
            for _ in words:
                i += 1
            if i != 2:
                raise Exception()

            for key in self.categories:
                if key in data:
                    print("Validation: Log entry verified")
                    return True
            return False
        except Exception:
            return False


def ft_split(line: str, to_split: str) -> List[str] | None:
    try:
        i: int = 0
        for char in to_split:
            i += 1
        if i != 1:
            raise ValueError("to_split must be a single character")
    except ValueError as e:
        print(e)
        return None
    words: List[str] = []
    word: Optional[str] = None
    in_word: bool = False
    for char in line:
        if char != to_split:
            if not in_word:
                word = char
                in_word = True
            else:
                word += char
        else:
            if in_word and word is not None:
                words += [word]
                word = None
                in_word = False
    if in_word and word is not None:
        words += [word]
    return words


def stream_processor(type: str, processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {type} Processor...")
    print(f'Processing data: "{data}"')
    if processor.validate(data) is True:
        result: str = processor.process(data)
        print(processor.format_output(result))
        print()


def stream_processor2(type: str, processor: DataProcessor, data: Any) -> None:
        result: str = processor.process(data)
        print(processor.format_output(result))


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    data_bases: List[str, DataProcessor, Any] = [
        ("Numeric", NumericProcessor(),[1, 2, 3, 4, 5]),
        ("Text", TextProcessor(), "Hello Nexus World"),
        ("Log", LogProcessor(), "ERROR: Connection timeout"),
    ]
    for type, processor, data_base in data_bases:
        stream_processor(type, processor, data_base)
    print("=== Polymorphic Processing Demo ===")
    print()
    data_bases: List[str, DataProcessor, Any] = [
        ("Numeric", NumericProcessor(),[1, 2, 3]),
        ("Text", TextProcessor(), "Nexus World!"),
        ("Log", LogProcessor(), {"INFO: System ready"}),
    ]
    for type, processor, data_base in data_bases:
        stream_processor2(type, processor, data_base)
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
