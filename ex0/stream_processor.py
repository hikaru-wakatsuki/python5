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
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
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
            print("")
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        print(f'Processing data: "{data}"')
        count: int = 0
        count_words: int = 0
        in_word: bool = False
        for char in data:
            count += 1
            if char == " ":
                if in_word is True:
                    count_words += 1
                    in_word = False
            else:
                in_word = True
        return f"Processed text: {count} characters, {count_words} words"

    def validate(self, data: Any) -> bool:
        try:
            for _ in data:
                pass
            return True
        except Exception:
            return False


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        print("Initializing Log Processor...")

    categolies: Dict[str, str] = {
        "ERROR": "[ALERT]",
        "WARN": "[WARNING]",
        "INFO": "[INFO]"
    }

    def process(self, data: Any) -> str:
        for key, value in self.categolies.items():
            if key in data:
                return f" {value} {key} level detected: {data[key]}"

    def validate(self, data: Any) -> bool:
        try:
            for key in self.categolies:
                if key in data:
                    return True
            return False
        except Exception:
            return False


def stream_processor(data: Any, processor: DataProcessor) -> None:
    if processor.validate(data) is True:
        result: str = processor.process(data)
        processor.format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    data_samples: List[Any] = [
        [1, 2, 3, 4, 5],
         "Hello Nexus World",
         "ERROR: Connection timeout",
    ]

    print("=== Polymorphic Processing Demo ===")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
