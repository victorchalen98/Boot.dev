from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def to_string_lists(data):
    return list(map(lambda row: list(map(str, row)), data))


def to_csv_string(data):
    return "\n".join(map(lambda row: ",".join(row), data))


def get_csv_status(status, data):
    match status:

        case CSVExportStatus.PENDING:
            prepared = to_string_lists(data)
            return "Pending...", prepared

        case CSVExportStatus.PROCESSING:
            csv_str = to_csv_string(data)  
            return "Processing...", csv_str

        case CSVExportStatus.SUCCESS:
            return "Success!", data

        case CSVExportStatus.FAILURE:
            prepared = to_string_lists(data)
            csv_str = to_csv_string(prepared)
            return "Unknown error, retrying...", csv_str

        case _:
            raise Exception("unknown export status")
