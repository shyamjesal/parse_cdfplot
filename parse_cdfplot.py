import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import multiprocessing as mp
import sys

def generate_plots(filename):
    df = pd.read_csv(filename,names=['request_type','latency'])
    
    # plot cdf 
    sns.ecdfplot(df, x="latency",hue="request_type")

    # save them to their respective directory
    plt.savefig("{}//cdf_plot.png".format(os.path.dirname(filename)),format='png',dpi=150)
    
    # clear the plot 
    plt.clf()

def start_mp(root_path):
    # get list of stat files 
    file_list = glob.glob(str(os.path.join(root_path,'experiment'))+'*/stats.csv')

    # spawn multiprocess 
    for filepath in file_list:
        p = mp.Process(target=generate_plots, args=(filepath,))
        p.start()

if __name__ == "__main__": 
    start_mp(sys.argv[1])