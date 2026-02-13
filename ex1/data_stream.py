from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__()
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed_batches: int = 0
        self.total_items: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return [item for item in data_batch if isinstance(item, str)]
        return [item for item in data_batch
                if isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_batches": self.processed_batches,
            "total_items": self.total_items
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            filtered: List[Any] = []
            filtered += self.filter_data(data_batch, "temp")
            filtered += self.filter_data(data_batch, "humidity")
            filtered += self.filter_data(data_batch, "pressure")
            sum_temp: Union[int, float] = 0
            count_temp: int = 0
            for line in filtered:
                if not isinstance(line, str):
                    raise TypeError()
                words: List[str] = line.split(":")
                i: int = 0
                for _ in words:
                    i += 1
                if i != 2:
                    raise ValueError("Invalid data format")
                key: str = words[0]
                value: Union[int, float] = float(words[1])
                if key == "temp" and -20 <= value <= 50:
                    self.total_items += 1
                    count_temp += 1
                    sum_temp += value
                if key == "humidity" and 0 <= value <= 100:
                    self.total_items += 1
                if key == "pressure" and 900 <= value <= 1050:
                    self.total_items += 1
            self.processed_batches += 1
            if count_temp == 0:
                raise Exception
            avg_temp: Union[int, float] = sum_temp / count_temp
            return (f"{self.total_items} readings processed, "
                    f"avg temp: {avg_temp}°C")
        except Exception as e:
            return f"{e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            filtered: List[Any] = []
            filtered += self.filter_data(data_batch, "buy")
            filtered += self.filter_data(data_batch, "sell")
            sum: int = 0
            for line in filtered:
                if not isinstance(line, str):
                    raise TypeError()
                words: List[str] = line.split(":")
                i: int = 0
                for _ in words:
                    i += 1
                if i != 2:
                    raise ValueError("Invalid data format")
                key: str = words[0]
                value: int = int(words[1])
                if key == "buy" and value > 0:
                    self.total_items += 1
                    sum += value
                if key == "sell" and value > 0:
                    self.total_items += 1
                    sum -= value
            self.processed_batches += 1
            return f"{self.total_items} operations, net flow: {sum:+} units"
        except Exception as e:
            print(e)
            return f"{e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data: List[Any] = []
            data += self.filter_data(data_batch)
            error_count: int = 0
            for event in data:
                if event == "error":
                    self.total_items += 1
                    error_count += 1
                else:
                    self.total_items += 1
            self.processed_batches += 1
            return f"{self.total_items} events, {error_count} error detected"
        except Exception as e:
            print(e)
            return f"{e}"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams += [stream]

    def process_all(self, batches: List[List[Any]]) -> None:
        count: int = 0
        for _ in batches:
            count += 1
        i: int = 0
        while i < count:
            stream: DataStream = self.streams[i]
            batch: List[Any] = batches[i]
            message: str
            if isinstance(stream, SensorStream):
                message = "Sensor"
            elif isinstance(stream, TransactionStream):
                message = "Transaction"
            else:
                message = "Event"
            print(f"Initializing {message} Stream...")
            print(f"Stream ID: {stream.stream_id}, Type: {stream.stream_type}")
            print(f"Processing sensor batch: {batch}")
            print(f"{message} analysis: {stream.process_batch(batch)}")
            print()
            i += 1

    def process_status(self, batches: List[List[Any]]) -> None:
        count: int = 0
        for _ in batches:
            count += 1
        i: int = 0
        while i < count:
            stream: DataStream = self.streams[i]
            batch: List[Any] = batches[i]
            message: str
            if isinstance(stream, SensorStream):
                message = "Sensor"
            elif isinstance(stream, TransactionStream):
                message = "Transaction"
            else:
                message = "Event"
            print(f"{message} data: {stream.process_batch(batch)}")
            print()
            i += 1

def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))
    batches: list[List[Any]] = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"]
    ]
    processor.process_all(batches)
    print("Initializing Event Stream...")
    event: EventStream = EventStream("TRANS_001")
    event_batch: list[Any] = ["login", "error", "logout"]
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(f"Processing sensor batch: {event_batch}")
    print(f"Event analysis: {event.process_batch(event_batch)}")
    print()
    print("=== Polymorphic Stream Processing ===")
    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))
    batches: list[List[Any]] = [
        ["temp:22.5", "humidity:65"],
        ["buy:100", "sell:150", "buy:75", "sell:100"],
        ["login", "error", "logout"]
    ]
    processor.process_status(batches)
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
