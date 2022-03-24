import pandas as pd
import os
import argparse
import pathlib
import datetime as dt

def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [--data <path-to-data>] [--csv <location>]',
        description='Analyse power data.'
    )

    parser.add_argument('data',
                        type=pathlib.Path,
                        help='path to data',
                        default=['.'],
                        nargs='+')  

    parser.add_argument('--csv', 
                        type=pathlib.Path, 
                        default=['./out.csv'],
                        help='file to log measurements to')                        

    return parser
    
def sort_pwrdata(data):

    n = len(data)
    times = list()
    pwrdata = list()
    
    for key in data:
        times.append(key)
        
    for i in range(n):
        for j in range(0, n-i-1):
            if times[j]> times[j+1]:
                times[j], times[j+1] = times[j+1], times[j]
                
    for key in times:
        pwrdata.append(data[key])
        
    return pwrdata
        
    
    
def read_PwrData(path):
    pwrdata = list()
    data = dict()
    for file in os.listdir(path):
        if file.endswith('.csv'):
            filepath = os.path.join(path, file)
            with open(filepath, 'r') as f:
                text = f.read().split('\n')
                time = text[1].split(',')[0].split(':')
                time = dt.time(int(time[0]), int(time[1]), int(time[2]))
                for line in text:
                    if line.startswith('Average Processor Power'):
                        APP = line.split('=')[1]
                        data[time] = APP
                        pwrdata.append(APP)
                        
    pwrdata = sort_pwrdata(data)
                        
    return pwrdata                        
                
            
def read_results(path):
    results = pd.read_csv(path)
    return results
    
def split_hidden_layers_sizes(df):
    layers = list()
    layer_size = list()
        
    hidden_layer_sizes = list(df['hidden_layer_sizes'])
    
    for item in hidden_layer_sizes:
        layer_size.append(int(item[1:4]))
        if len(item)==6:
            layers.append(1)
        elif len(item)==10:
            layers.append(2)
        elif len(item)==15:
            layers.append(3)
        else:
            print(item, "input error")
            sys.exit()
            
    del df['hidden_layer_sizes']
    df['layers']= layers
    df['layer_size'] = layer_size
    
    return df
    
if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()  
    data  = list()
    
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
        results = split_hidden_layers_sizes(results)
        results['pwrdata'] = read_PwrData(pwrdata_path)
        data.append(results)
        
    all_data = data[0]
    for df in data[1:]:
        all_data = pd.concat([all_data, df],axis=0)
        
    all_data.to_csv(args.csv[0], index=False)
        
        
        
        