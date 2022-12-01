"""
Compute rating statistics.

Usage:
    rating-stats.py ML_DIR

Options:
    ML_DIR
        The directory to read. Must contain 'ratings.csv'.
"""

from docopt import docopt
import pandas as pd

# We are going to *import-protect* this script file, by using a function to encapsulate
# the logic, and then running it at the end of the script.  The function will take our
# command-line arguments, as parsed by docopt.
def main(options):
    ml_dir = options['ML_DIR']

    rating_file = f'{ml_dir}/ratings.csv'

    print('reading input file', rating_file)
    ratings = pd.read_csv(rating_file)

    print('computing user statistics')
    user_stats = ratings.groupby('userId')['rating'].agg(['count', 'mean'])

    print('saving user statistics')
    # we save without options, which *includes* the index as a column in the CSV file
    user_stats.to_csv(f'{ml_dir}/user-stats.csv')

    print('computing item statistics')
    item_stats = ratings.groupby('movieId')['rating'].agg(['count', 'mean'])

    print('saving item statistics')
    # same as before
    item_stats.to_csv(f'{ml_dir}/item-stats.csv')

# Now we run our main function when the file is run as a script.
if __name__ == '__main__':
    options = docopt(__doc__)
    main(options)