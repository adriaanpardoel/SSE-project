import argparse
import pathlib
import pandas as pd
import numpy as np
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


def boxplot(ax, df, x_attr, y_attr):
    vals = np.sort(df[x_attr].unique())
    boxplot_data = [df[df[x_attr] == val][y_attr] for val in vals]

    ax.set_xticklabels(vals)
    ax.boxplot(boxplot_data)


if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()

    df = pd.read_csv(args.data)

    fig = plt.figure(figsize=[19.2, 9.6])

    ax_samples = plt.subplot2grid((2, 6), (0, 0), colspan=2)
    ax_samples.set_xlabel('number of samples')
    ax_samples.set_ylabel('cost')
    boxplot(ax_samples, df, 'n_samples', 'cost')

    ax_features = plt.subplot2grid((2, 6), (0, 2), colspan=2)
    ax_features.set_xlabel('number of features')
    ax_features.set_ylabel('cost')
    boxplot(ax_features, df, 'n_features', 'cost')

    ax_classes = plt.subplot2grid((2, 6), (0, 4), colspan=2)
    ax_classes.set_xlabel('number of classes')
    ax_classes.set_ylabel('cost')
    boxplot(ax_classes, df, 'classes', 'cost')

    ax_layers = plt.subplot2grid((2, 6), (1, 1), colspan=2)
    ax_layers.set_xlabel('number of hidden layers')
    ax_layers.set_ylabel('cost')
    boxplot(ax_layers, df, 'layers', 'cost')

    ax_layer_size = plt.subplot2grid((2, 6), (1, 3), colspan=2)
    ax_layer_size.set_xlabel('hidden layer size')
    ax_layer_size.set_ylabel('cost')
    boxplot(ax_layer_size, df, 'layer_size', 'cost')

    plt.show()
