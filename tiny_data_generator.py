import argparse
import csv
from io import StringIO


FIELDNAMES = ["id", "name", "score"]


def generate_rows(count: int) -> list[dict[str, str]]:
    rows = []
    for i in range(1, count + 1):
        rows.append(
            {
                "id": str(i),
                "name": f"user_{i}",
                "score": str(70 + i),
            }
        )
    return rows


def format_csv(rows: list[dict[str, str]]) -> str:
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=FIELDNAMES)
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a tiny CSV dataset.")
    parser.add_argument(
        "--rows",
        type=int,
        default=5,
        help="number of data rows to generate",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = generate_rows(args.rows)
    print(format_csv(rows), end="")


if __name__ == "__main__":
    main()
