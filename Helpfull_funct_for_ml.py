
#Find correlation in data set between all collumns. It finds ONLE linear corellation
def find_correlation(data, min_cor,max_cor = 1.1 )
    columns = data.columns
    strong_correlation = []
    for i in columns:
        for j in columns:
            subtle_cor = abs(data.corr()[i][j])
            if subtle_cor > min_cor and i != j and subtle_cor < max_cor:
                strong_correlation.append(f"{i} and {j} correlates in {subtle_cor}")
    return strong_correlation

#Mutual correlation find ALL types of correlation between feuture and target

