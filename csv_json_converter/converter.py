import csv
import json
import os


def convert_csv_to_json(input_file, output_file, logger):
    try:
        # Check if file exists
        if not os.path.exists(input_file):
            logger.error("Input file does not exist.")
            print("Input file not found.")
            return
        
        # Read CSV
        with open(input_file, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        if not data:
            logger.warning("CSV file is empty.")
            print("⚠ CSV file is empty.")
            return

        # Create output folder if not exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write JSON
        with open(output_file, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        logger.info("Conversion successful.")
        print(" Conversion completed successfully.")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        print(" Something went wrong.")