# CsvToJsonHng

A script to convert csv to CHIP-0007 compatible json files

## Dependencies

This Script Has only two Dependencies:

1. Python 3.7 or higher which can be installed at [python](https://www.python.org/downloads/)
2. Pandas which can be installed from your Terminal using
   `bash pip install pandas `

## Guidlines to run Script

```bash
    Python csvScirpt.py
```

## WorkFlow of Script

1. You will need a csv with the below format

| TEAM NAMES | Series Number | Filename          | Name              | Description                                 | Gender | Attributes                                                                                                                        | UUID                                 |
| ---------- | ------------- | ----------------- | ----------------- | ------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| TEAM BEVEL | 1             | adewale-the-amebo | adewale the amebo | Adewale likes to be in everyone's business. | Male   | hair: bald; eyes: black; teeth: none; clothing: red; accessories: mask; expression: none; strength: powerful; weakness: curiosity | cad316c3-37f8-4b27-9f53-9d803bfcfee7 |

2. Input the name of the csv file if the file doesn't have a .csv extension you will be prompted out of the Script

3. Read CSV from Local Directory

4. JSON File Is Generated per NFT entry in the CSV
5. Each JSON File is Hashed using sha256 standard
6. The sha256 hash is appended to the csv file.

Temlate of the CHIP-0007 compatible json files that will be generated

```jsonc
{
  "format": "CHIP-0007",
  "name": "Pikachu",
  "description": "Electric-type Pokémon with stretchy cheeks",
  "minting_tool": "SuperMinter/2.5.2",
  "sensitive_content": false,
  "series_number": 0,
  "series_total": 0,
  "attributes": [],
  "collection": {
    "name": "Example Pokémon Collection",
    "id": "e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57",
    "attributes": [
      {
        "type": "description",
        "value": "Example Pokémon Collection is the best Pokémon collection. Get yours today!"
      },
      {
        "type": "icon",
        "value": "https://examplepokemoncollection.com/image/icon.png"
      },
      {
        "type": "banner",
        "value": "https://examplepokemoncollection.com/image/banner.png"
      },
      {
        "type": "twitter",
        "value": "ExamplePokemonCollection"
      },
      {
        "type": "website",
        "value": "https://examplepokemoncollection.com/"
      }
    ]
  }
}
```
