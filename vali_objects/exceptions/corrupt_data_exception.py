# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# TODO(developer): Taoshi
# Copyright © 2023 TARVIS Labs, LLC

class ValiMemoryCorruptDataException(Exception):
    def __init__(self, message):
        super().__init__(self, message)


class ValiBkpCorruptDataException(Exception):
    def __init__(self, message):
        super().__init__(self, message)