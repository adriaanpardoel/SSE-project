import pandas as pd
import sys
import os
import argparse
import pathlib
import datetime as dt


def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [<path-to-data>] [--csv <location>]',
        description='Analyse power data.'
    )

    parser.add_argument('data',
                        type=pathlib.Path,
                        help='path to data',
                        default=['.'],
                        nargs='+')

    parser.add_argument('--csv',
                        type=pathlib.Path,
                        default='./out.csv',
                        help='file to log measurements to')

    return parser


def sort_pwrdata(data):
    n = len(data)
    times = list()
    pwrdata = list()

    for key in data:
        times.append(key)

    for i in range(n):
        for j in range(0, n - i - 1):
            if times[j] > times[j + 1]:
                times[j], times[j + 1] = times[j + 1], times[j]

    for key in times:
        pwrdata.append(data[key])

    return pwrdata


def read_PwrData(path):
    data = dict()
    for file in os.listdir(path):
        if file.endswith('.csv'):
            filepath = os.path.join(path, file)
            with open(filepath, 'r') as f:
                text = f.read().split('\n')
                time = text[1].split(',')[0].split(':')
                time = dt.time(int(time[0]), int(time[1]), int(time[2]))
                for line in text:
                    if line.startswith('Cumulative Processor Energy_0 (Joules)'):
                        data[time] = float(line.split('=')[1])

    return sort_pwrdata(data)


def read_results(path):
    results = pd.read_csv(path)
    return results


def split_hidden_layers_sizes(df):
    layers = list()
    layer_size = list()

    hidden_layer_sizes = list(df['hidden_layer_sizes'])

    for item in hidden_layer_sizes:
        layer_size.append(int(item[1:4]))
        if len(item) == 6:
            layers.append(1)
        elif len(item) == 10:
            layers.append(2)
        elif len(item) == 15:
            layers.append(3)
        else:
            print(item, "input error")
            sys.exit()

    del df['hidden_layer_sizes']
    df['layers'] = layers
    df['layer_size'] = layer_size

    return df


def add_cost(df):
    min_samples = df['n_samples'].min()
    min_features = df['n_features'].min()
    min_classes = df['classes'].min()
    min_layers = df['layers'].min()
    min_layer_size = df['layer_size'].min()

    simplest_model = df[(df['n_samples'] == min_samples) &
                        (df['n_features'] == min_features) &
                        (df['classes'] == min_classes) &
                        (df['layers'] == min_layers) &
                        (df['layer_size'] == min_layer_size)]

    baseline_cost = simplest_model['energy'][0]
    df['cost'] = df['energy'] / baseline_cost
    return df

def add_avg_iteration_cost(df):
    df['avg_iteration_energy'] = df['energy']/df['iterations']
    return df

if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()
    data = list()

    for path in args.data:
        results_path = os.path.join(path, 'result.csv')
        pwrdata_path = os.path.join(path, 'PwrData')

        if os.path.exists(results_path) == False:
            print("could not find result.csv")
            os.exit()
        elif os.path.isdir(pwrdata_path) == False:
            print("could not find PwrData folder")
            os.exit()

        results = read_results(results_path)
        results['system'] = os.path.basename(path)
        results = split_hidden_layers_sizes(results)
        results['energy'] = read_PwrData(pwrdata_path)
        results = add_avg_iteration_cost(results)
        results = add_cost(results)
        data.append(results)

    all_data = data[0]
    for df in data[1:]:
        all_data = pd.concat([all_data, df], axis=0)

    all_data.to_csv(args.csv, index=False)
