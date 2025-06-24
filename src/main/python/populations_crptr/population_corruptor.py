#!/usr/bin/python
# Author: James Ross (jar35@st-andrews.ac.uk)
# 24/6/2015
#
# This script takes a record directory (containing "birth_records",
# "marriage_records", "death_records") in TD format and outputs a corrupt
# version of the records.

from config import Config

def main(filepath):
    if not os.path.exists(filepath):
        print(f"Directory not found: {filepath}")
        return
    
    if not os.path.isdir(filepath):
        print(f"Error: {filepath} is not a directory")
        return

    print (f"Running crptr for {filepath}")

    timestamp_str = datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + f"-{now.microsecond // 1000:03d}"
    output_filepath = Config.RESULTS_DIR + Config.PURPOSE + timestamp_str
    os.makedirs(output_filepath+"/records", exist_ok=True)

    files = ["birth_records.csv", "marriage_records.csv", "death_records.csv"]

    corrupt_file(filepath, output_filepath, files[0], Config.Corruptors.birthCorruptor)
    corrupt_file(filepath, output_filepath, files[1], Config.Corruptors.marriageCorruptor)
    corrupt_file(filepath, output_filepath, files[2], Config.Corruptors.deathCorruptor)

    print(f"Results output to {output_filepath}")

def corrupt_file(input_dir, output_dir, filename, corruptor_fn):
    start_time = datetime.now()

    input_filepath = input_dir + "/" + filename

    if not os.path.exists(input_filepath):
        print (f"Skipping, file not found: {input_filepath}")
        return

    print_timestamp(f"Corrupting {input_filepath}...")

    corruptor_fn(
        input_filepath+"/"+filename,
        output_filepath+"/"+filename,
        CONFIG.LOOKUP_FILES_DIR,
        Config.DETERMINISTIC,
        Config.SEED,
        Config.PROFILE.PROPORTION_TO_CORRUPT,
        Config.PROFILE.MAX_MODIFICATIONS_PER_ATTR,
        Config.PROFILE.MODIFICATIONS_PER_RECORD,
        Config.PROFILE.RECORD_LEVEL_PROPORTION
    )

    print_time_elapsed(start_time)

def print_timestamp(string):
    print(datetime.now().strftime("%Y/%m/%d %H-%M-%S") + f".{now.microsecond // 1000:03d} :: ", end="")
    print(string)

def print_time_elapsed(start_time):
    print(f"Elapsed time: {(datetime.now() - start_time).strftime("%H-%M-%S")}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python population_corruptor.py <filepath>")
    else:
        main(sys.argv[1])