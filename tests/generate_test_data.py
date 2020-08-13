from pathlib import Path
import pandas as pd
from random_data import write_random_images
import argparse

def generate_test_data(metadata_file, filename_column, size, test_data_folder):
    test_data_folder = Path(test_data_folder)
    write_random_images(
        metadata_file[filename_column],
        test_data_folder/"folder",
        test_data_folder/"tar.tar",
        test_data_folder/"zip.zip",
        size
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata_file")
    parser.add_argument("filename_column")
    parser.add_argument("x")
    parser.add_argument("y")
    parser.add_argument("test_data_folder")
    args = parser.parse_args()
    generate_test_data(
        pd.read_csv(args.metadata_file),
        args.filename_column,
        (int(args.x), int(args.y)),
        args.test_data_folder
    )
