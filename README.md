# Python Project Template


This is my template for Python projects. I have created many small projects, so this helps me to make the projects at the start.


## Repo Structure

```
.
├── .env
├── .git
│   ├── ...
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
├── start.sh
└── utils
    └── _global.py
└── venv
    └── ...
```

## Dir and File explanation
- .env
    - Can be used to define secrets or variables that are sensitive, like API keys, file locations outside of the project dir, or individual profiles.
- .git
    - Files defining the needed files to make this a git repo.
- .gitignore
    - Defines what files aren't committed. Default Python .gitignore structure, and here the .env is defined so it won't make it to commits.
- README.md
    - Look up the [Dir and File Explanation in here](README.md)
- main.py
    - Main Python file.
- requirements.txt
    - Defines the libraries that need to be installed within the venv.
- start.sh
    - Start script, when run will build the venv and install the libraries (might get bigger if needed).
- utils
    - Directory to store functions used with main.py
    - _global.py
        - Defines global variables, so they are easy to change. Name starts with `_`because it is not meant to be called from anywhere other than other functions.
- venv
    - Directory that stores the venv, or the Virtual Environment.
