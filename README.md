# altagram-starships

### Requirements
- **Python** >= **3.6.8**
- **Pip** >= **19.0.3**

## Installation

``pip install -r requirements.txt``

## Usage 

To run the API:
``
python <project_path>/app.py
``

## Endpoints: 

### /starships - GET Method

#### Description
To get all the starships simply call:

#### URL Params:
None

##### Response example:

```json
{
        "starships":[
            {"name": "starship 4", "hyperdrive" : 0.1},
            {"name": "starship 1", "hyperdrive" : 0.3},
            {"name": "starship 6", "hyperdrive" : 0.5},
            {"name": "starship 2", "hyperdrive" : 3.0},
            {"name": "starship 5", "hyperdrive" : 4.9}
        ],
        "starships_unknown_hyperdrive": [
            {"name": "starship 8"},
            {"name": "starship 3"} 
        ]
}
```
