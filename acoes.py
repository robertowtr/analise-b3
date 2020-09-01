#https://medium.com/@cesar.vieira/analisando-a%C3%A7%C3%B5es-da-bovespa-parte-i-500107703688

import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['ABEV3.SA','AZUL4.SA','BTOW3.SA','B3SA3.SA','BBSE3.SA','BBDC4.SA','BBDC3.SA','BRAP4.SA','BBAS3.SA','BRKM5.SA','BRFS3.SA','CCRO3.SA','CMIG4.SA','CIEL3.SA','CSAN3.SA','CVCB3.SA','CYRE3.SA','ECOR3.SA','ELET3.SA','ELET6.SA','EMBR3.SA','ENBR3.SA','ENGIE3.SA','EQTL3.SA','YDUQ3.SA','FLRY3.SA','GGBR4.SA','GOAU4.SA','GOLL4.SA','HYPE3.SA','IGTA3.SA','IRBR3.SA','ITSA4.SA','ITUB4.SA','JBSS3.SA','KLBN11.SA','KROT3.SA','RENT3.SA','LAME4.SA','LREN3.SA','MGLU3.SA','MRFG3.SA','MRVE3.SA','MULT3.SA','NATU3.SA','PCAR4.SA','PETR4.SA','PETR3.SA','BRDT3.SA','QUAL3.SA','RADL3.SA','RAIL3.SA','SBSP3.SA','SANB11.SA','CSNA3.SA','SMLS3.SA','SUZB5.SA','TAEE11.SA','VIVT4.SA','TIMP3.SA','UGPA3.SA','USIM5.SA','VALE3.SA','VVAR3.SA','WEGE3.SA']

prices=pd.DataFrame()

#tickers = [TickerA, TickerB, TickerC]
for t in tickers:
   print(t)
   try:
      prices[t]=wb.DataReader(t, data_source='yahoo', start='2020-1-1')['Adj Close']
   except:
      continue  

prices.to_csv('/Users/roberto.walter/Desktop/prices.csv',index=True)