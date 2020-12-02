# auth-submit-search
A Reddit tool to collect author post counts on a subreddit's top posts based on passed keywords

## Install
Requires Python 3 and the praw api wrapper
You must also manually add your own account key to the script in order to authenticate with Reddit and run the script

## Usage

./auth-submit-search.py <subreddit> <number of posts> <keyword 1> <keyword 2> ... <keyword n>

Example
./auth-submit-search.py lsat 1000 score gpa T14
