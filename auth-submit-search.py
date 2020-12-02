#! python3
# auth-submit-search.py - searches a subreddit for the top posts based on if they include
# the defined keywords.
# Returns a dictionary of the authors of the posts, the number
# of posts the author has and the date their account was created.

import praw
import string
import pprint
from datetime import datetime
from collections import Counter
import sys


def main():
    # Creates an authorized reddit instance using worldn_counter to log into Reddit
    reddit = praw.Reddit(client_id='', client_secret='',user_agent='')

    print('Read Only mode: ' + str(reddit.read_only) + '\n')
    
    # assign subreddit to search
    subred = reddit.subreddit(sys.argv[1])

    # defines the max amount of submissions to search
    lim = int(sys.argv[2])
    
    # objects representing key words to find in submission titles and caches for found results
    key_words = sys.argv[3:]
    key_words = [word.lower() for word in key_words]
    print('Keywords provided: {}'.format(key_words))
    
    posts_cache_id = []
    posts_authors = []

    # displays subreddit information
    print(' Current Subreddit Information '.center(39, '='))
    print(subred.display_name)
    print(subred.title)
    print(''.center(39, '='))

    print('Collecting top {} posts of the year...'.format(str(lim)))
    # Loops through the top submissions of selected subreddit and parses
    # the titles to see if any words match the defined key words in key_words
    for submission in subred.top(time_filter='year', limit=lim):
        title = ''.join([l for l in submission.title if l not in string.punctuation])
        words = title.split()
        words = [word.lower() for word in words]
        # Conditional that returns True if an item in key_words matches an item in words
        if bool(set(key_words) & set(words)):
            posts_authors.append(submission.author)
            posts_cache_id.append(submission.id)

    # Creates a dictonary of authors and number of posts by an author in the returned list of posts
    author_count = Counter(posts_authors)
    author_submission_count = []

    # Creates a list of dictionaries with information about the author, the date the account
    # was created and the number of posts the author created
    # Loop through each unique redditor in posts_authors and add the needed data to
    # author_submission_count
    print('Obtaining author count...')
    for author in set(posts_authors):
        try:
            auth_inst = {'name': author.name,'creation': author.created_utc, 'posts': author_count[author]}
            author_submission_count.append(auth_inst)
        except AttributeError:
            print('NOTE: Data on Author {} does not exist. Skipping...'.format(author))
            continue
    
    # Print results to screen
    # pprint.pprint(sorted(author_submission_count, key = lambda i: i['posts'], reverse=True))

    return author_submission_count

if __name__ == '__main__':
    main()
