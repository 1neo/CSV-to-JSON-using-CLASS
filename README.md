# File generator

The file generator tech test comes with a mock data CSV that represents one of the many types of data that we have to deal with.

The challenge is to consume and transform the CSV file in to a nested JSON file which will form a tree structure.

## Getting Started

As a starting point a CSV file was provided available in the root.


## The desired form

From the CSV, I saw  that the data follows a parent child structure. The first entry is always at the top of the tree, with the following entries being children of the previous column. The example below shows the structure that has to be generated.

```
[
  {
    "label": "Meat & Fish",
    "id": "179549",
    "link": "https://xyz.com/browse/179549",
    "children": [
      {
        "label": "Meat & Poultry",
        "id": "179545",
        "link": "https://xyz.com/browse/179549/179545",
        "children": []
      },
      {
        "label": "Fish",
        "id": "176741",
        "link": "https://xyz.com/browse/179549/176741",
        "children": [
          {
            "label": "Fish Bucket",
            "id": "176780",
            "link": "https://xyz.com/browse/179549/176741/176780",
            "children": [
              {
                "label": "Fish type",
                "id": "176979",
                "link": "https://xyz.com/browse/179549/176741/176780/176979",
                "children": []
              },
            ]
          }
        ]
      }
    ]
  }
]

```

### Some  of the Unit test cases are :
####a) The completely generated json file with the input csv file. file.json
####b) The generated empty json file with no data in input csv file. fileempty.json
####c) The  generated json file with one record in the input csv file. fileonerec.json
