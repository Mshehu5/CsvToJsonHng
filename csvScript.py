import json
import csv
import hashlib
import pandas as pd


print("Welcome")
csvfile = input("Input the csv:")
# If the You input a file that does end with a .csv extention you will be promted out of the program
if csvfile.endswith(".csv"):
    print("Csv file {} accepted Starting Process .....".format(csvfile))
    # Removes .csv letters from the input csv and uses to name the outputfile
    outputFileName = csvfile[:-4]
    # hashlist were all hashes will be stored
    hash_list = []

    print("Creating Json files and hashing them")
    # opens and read Inputed csv file
    with open(csvfile, "r") as f:
        reader = csv.reader(f)
        next(reader)
        # object where all csv rows are stored files
        data = {}
        # low over each row in csv file to get values
        for row in reader:
            attributes_list = []
            attributes = row[6]
            attributes = attributes.split(";")
            # for loop to slip atrributes by trait types and values
            for attr in attributes:
                attr_map = attr.split(":")
                attr_name = attr_map[0].strip()
                attr_value = attr_map[1].strip()
                attributes_list.append({"trait_type": attr_name, "value": attr_value})
            # updating object with current looped row in the csv file
            data.update(
                {
                    "format": "CHIP-0007",
                    "name": row[3],
                    "descriptor": row[4],
                    "minting_tool": row[0],
                    "sensitive_content": "false",
                    "series_number": row[1],
                    "series_total": "420",
                    "atributes": attributes_list,
                    "collection": {
                        "name": "Zuri NFT Tickets for free lunch Collection",
                        "id": row[7],
                    },
                }
            )
            # declaring json file name
            filename = row[2]
            jsonfile = "nft{}.json".format(filename)

            # Adding the current looped row into the its own json file
            with open(jsonfile, "w") as f:
                json.dump(data, f, indent=4)

            # Using hash library hashlib to hash each json file
            with open(jsonfile, "rb") as openedfile:
                content = openedfile.read()
                sha256 = hashlib.sha256()
                sha256.update(content)

            # Storing each hashed json file into a list that will be saved in the new column
            hashed = sha256.hexdigest()
            hash_list.append(hashed)
    print("Done Creating all json files and hashinng each file")
    # Opening Inputed Csv and adding a column containing all the hashed json files using pandas library
    print("Saving you json files hashes into a new Csv file")
    df = pd.read_csv(csvfile)
    df["hashes"] = pd.Series(hash_list)

    # Saving new column in output file csv
    df.to_csv("{}.output.csv".format(outputFileName))

    print(
        "Done creating all json files and adding all hashed json files to new csv file"
    )
    print("Thanks for using my Program :)")
else:
    print("only accepts files with .csv extension")
