from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__()
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
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
            "total_items": self.total_items
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
        self.sensor_alerts: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            filtered: List[Any] = self.filter_data(data_batch)
            if filtered == []:
                raise Exception("No valid sensor data")
            sum_temp: Union[int, float] = 0
            count_temp: int = 0
            for line in filtered:
                words: List[str] = line.split(":")
                key: str = words[0]
                value: Union[int, float] = float(words[1])
                if key == "temp":
                    count_temp += 1
                    sum_temp += value
                self.total_items += 1
            if count_temp == 0:
                raise Exception("No temperature data found")
            avg_temp: Union[int, float] = sum_temp / count_temp
            return (f"{self.total_items} readings processed, "
                    f"avg temp: {avg_temp}°C")
        except Exception as e:
            return f"{e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            filtered: List[Any] = super().filter_data(data_batch)
            valid_data: List[Any] = []
            for line in filtered:
                if not isinstance(line, str):
                    raise TypeError
                words: List[str] = line.split(":")
                i: int = 0
                for _ in words:
                    i += 1
                if i != 2:
                    raise ValueError
                key: str = words[0]
                value: Union[int, float] = float(words[1])
                if key == "temp" and -20 <= value <= 50:
                    valid_data += [line]
                elif key == "humidity" and 0 <= value <= 100:
                    valid_data += [line]
                elif key == "pressure" and 900 <= value <= 1050:
                    valid_data += [line]
                else:
                    self.sensor_alerts += 1
            return valid_data
        except Exception:
            return []


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        self.large_transactions: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            filtered: List[Any] = self.filter_data(data_batch)
            if filtered == []:
                raise Exception("No valid transaction data")
            total: int = 0
            for line in filtered:
                words: List[str] = line.split(":")
                key: str = words[0]
                value: int = int(words[1])
                if key == "buy" and value < 1000000:
                    self.total_items += 1
                    total += value
                elif key == "sell" and value < 1000000:
                    self.total_items += 1
                    total -= value
                else:
                    self.large_transactions += 1
            return f"{self.total_items} operations, net flow: {total:+} units"
        except Exception as e:
            print(e)
            return f"{e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            filtered: List[Any] = super().filter_data(data_batch)
            valid_data: List[Any] = []
            for line in filtered:
                if not isinstance(line, str):
                    raise TypeError
                words: List[str] = line.split(":")
                i: int = 0
                for _ in words:
                    i += 1
                if i != 2:
                    raise ValueError
                key: str = words[0]
                value: Union[int, float] = float(words[1])
                if key == "buy" and value > 0:
                    valid_data += [line]
                elif key == "sell" and value > 0:
                    valid_data += [line]
                else:
                    self.large_transactions += 1
            return valid_data
        except Exception:
            return []


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            data: List[Any] = self.filter_data(data_batch)
            if data == []:
                raise Exception("No valid event data")
            error_count: int = 0
            for event in data:
                if event == "error":
                    self.total_items += 1
                    error_count += 1
                else:
                    self.total_items += 1
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
            print(f"Processing {message.lower()} batch: {batch}")
            print(f"{message} analysis: {stream.process_batch(batch)}")
            print()
            i += 1

    def process_status(self, batches: List[List[Any]]) -> None:
        count: int = 0
        for _ in batches:
            count += 1
        print("Batch 1 Results:")
        i: int = 0
        sensor_alerts: int = 0
        large_transactions: int = 0
        while i < count:
            stream: DataStream = self.streams[i]
            batch: List[Any] = batches[i]
            stream.process_batch(batch)
            if isinstance(stream, SensorStream):
                sensor_alerts = stream.sensor_alerts
                print(f"- Sensor data: {stream.total_items} "
                      f"readings processed")
            elif isinstance(stream, TransactionStream):
                large_transactions = stream.large_transactions
                print(f"- Transaction data: {stream.total_items} "
                      f"operations processed")
            else:
                print(f"- Event data: {stream.total_items} events processed")
            i += 1
        print()
        print("Stream filtering active: High-priority data only")
        print(f"Filtered results: {sensor_alerts} critical sensor alerts, "
              f"{large_transactions} large transaction")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))
    batches: list[List[Any]] = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"]
    ]
    processor.process_all(batches)
    print("=== Polymorphic Stream Processing ===")
    print()
    processor2: StreamProcessor = StreamProcessor()
    processor2.add_stream(SensorStream("SENSOR_001"))
    processor2.add_stream(TransactionStream("TRANS_001"))
    processor2.add_stream(EventStream("EVENT_001"))
    batches: list[List[Any]] = [
        ["temp:22.5", "humidity:65", "temp:500", "pressure:5000"],
        ["buy:100", "sell:150", "buy:75", "sell:100", "sell:1000000"],
        ["login", "error", "logout"]
    ]
    processor2.process_status(batches)
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
