from dataclasses import dataclass, field


@dataclass(init=True, order=True)
class TestingResults:
    day_id: int
    part_one_res: bool
    part_two_res: bool
    index_id: int = field(init=False, repr=False)
