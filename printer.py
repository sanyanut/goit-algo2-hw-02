from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    jobs = [PrintJob(**job) for job in print_jobs]
    printer_constraints = PrinterConstraints(**constraints)

    jobs.sort(key=lambda x: x.priority)

    print_order = []
    total_time = 0

    current_group_ids = []
    current_group_volume = 0.0
    current_group_time = 0

    for job in jobs:
        if (current_group_volume + job.volume <= printer_constraints.max_volume and
                len(current_group_ids) < printer_constraints.max_items):

            current_group_ids.append(job.id)
            current_group_volume += job.volume
            current_group_time = max(current_group_time, job.print_time)
        else:
            if current_group_ids:
                print_order.extend(current_group_ids)
                total_time += current_group_time

            current_group_ids = [job.id]
            current_group_volume = job.volume
            current_group_time = job.print_time

    if current_group_ids:
        print_order.extend(current_group_ids)
        total_time += current_group_time

    return {
        "print_order": print_order,
        "total_time": total_time
    }


def test_printing_optimization():
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {"max_volume": 300, "max_items": 2}

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}\nЗагальний час: {result1['total_time']} хвилин\n")

    print("Тест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}\nЗагальний час: {result2['total_time']} хвилин\n")

    print("Тест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}\nЗагальний час: {result3['total_time']} хвилин")


if __name__ == "__main__":
    test_printing_optimization()