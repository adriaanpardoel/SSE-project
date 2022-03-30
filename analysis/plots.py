import pandas as pd
import argparse
import pathlib
import matplotlib.pyplot as plt


def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [--data <path-to-data>]',
        description='Plot data.'
    )

    parser.add_argument('--data',
                        type=pathlib.Path,
                        help='path to data',
                        default='./out.csv')

    return parser


if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()

    df = pd.read_csv(args.data)

    # system = 'Sam'
    # df = df[df['system'] == system]

    # plt.scatter(df['n_samples'] * df['n_features'] * df['classes'] * df['layers'] * df['layer_size'] / df['iterations'], df['cost'])

    plt.hist(df['cost'], bins=24, rwidth=0.85)
    plt.show()
