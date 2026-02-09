from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        result: Any = data
        return result

    @abstractmethod
    def validate(self, data: Any) -> bool:
        return True

    def format_output(self, result: str) -> str:
        print(f"Output: {result}")


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
        if data is not str:
            return False
        return True


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
        if data is not Dict:
            return False
        for key in self.categolies:
            if key in data:
                return True
            return False


def stream_processor(data: any, data_processor: DataProcessor) -> None:
    is_valid: bool = True
    is_valid = data_processor.validate(data)




def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("=== Polymorphic Processing Demo ===")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
