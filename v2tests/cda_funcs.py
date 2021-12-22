import pandas as pd

def qResultsToDF(query_results):
    ''' convert a set of Q results to a DataFrame '''
    resList = []
    for row in query_results:
        resList.append(row)
    df = pd.DataFrame(resList)
    return df

