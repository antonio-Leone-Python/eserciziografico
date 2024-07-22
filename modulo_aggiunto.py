def calcolo_media_mensile(df):
    media= df.resample('ME').mean()
    return media

def calcolo_deviazione_mensile(df):
    standard=df.resample('ME').std()
    return standard  

def set_indice(df):
    df=df.set_index('data', inplace=True)
    return df
    

    