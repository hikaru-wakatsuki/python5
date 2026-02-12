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
            "stream_type" : self.stream_type,
            "processed_batches": self.processed_batches,
            "total_items": self.total_items
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            filtered: List[Any] = []
            filtered += self.filter_data(data_batch, "temp")
            filtered += self.filter_data(data_batch, "humidity")
            filtered += self.filter_data(data_batch, "pressure")
            data: Dict[str, Union[int, float]] = create_dict(filtered)
            if data == {}:
                raise Exception
            sum_temp: Union[int, float] = 0
            count_temp: int = 0
            for key, value in data.items():
                if key == "temp" and -20 <= value <= 50:
                    total_items += 1
                    count_temp += 1
                    sum_temp += value
                if key == "humidity" and 0 <= value <= 100:
                    total_items += 1
                if key == "pressure" and 900 <= value <= 1050:
                    total_items += 1
            self.processed_batches += 1
            if count_temp == 0:
                raise Exception
            avg_temp: Union[int, float] = sum_temp / count_temp
            return (f"Sensor analysis: {total_items} readings processed, avg temp: {avg_temp}°C")
        except Exception as e:
            return e


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")




def create_dict(data_batch: List[Any]) -> Dict[str, Union[int, float]]:
    try:
        data: Dict[str, Union[int, float]] = {}
        for line in data_batch:
            if not isinstance(line, str):
                raise TypeError()
            words: list[str] = line.split(":")
            i: int = 0
            for _ in words:
                i += 1
            if i != 2:
                raise ValueError("Invalid data format")
            data[words[0]] = float(words[1])
        return data

    except Exception as e:
        print(e)
        return {}





def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    data_batchs: list[List[Any]] = [
        [temp:22.5, humidity:65, pressure:1013]
    ]
    print("=== Polymorphic Stream Processing ===")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
