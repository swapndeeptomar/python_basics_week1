from converter import convert_csv_to_json
from logger_config import setup_logger


def main():
    logger = setup_logger()

    input_file = "input/Automobile.csv"
    output_file = "output/result.json"

    print("Starting CSV to JSON Conversion...\n")

    convert_csv_to_json(input_file, output_file, logger)


if __name__ == "__main__":
    main()