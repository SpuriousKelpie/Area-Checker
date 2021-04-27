# Area-Checker
A Python script that retrieves subreddit comments about a city area and then writes them to a CSV file.

The script first establishes an authorised read-only Reddit instance. It then retrieves the last thousand posts from the specified subreddit (this limit is set by the Reddit API). Comments from posts with the city area in their title are then written to a CSV file.

## Prerequisites
The script is written in Python 3 and uses the Python Reddit API Wrapper (PRAW). A Reddit account is required to access the Reddit API. The OAuth configuration variables on lines 12-14 need to be initialised (see [PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/authentication.html)).

## Usage
```
python3 area-checker.py [city subreddit] [city area]
```

## Contribute
If you would like to contribute to the project, then please contact me.

## License
This project is licensed under the GNU General Public License v3.0.
