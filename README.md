# pyView
This is to give Rstudio equivalent View Function to pandas DataFrame using the pyQT framework. (If you have [Anaconda] (https://www.continuum.io/downloads) full package installed then it will do)
This is tested for python 3+ version.

To use this you need to have pyQT,pandas installed. 
A small example will be

````python
from helper import View
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,5))
View(df)

````
That's all. 

####Warning : This  process is resource intensive compared to Rstudio View function as it creates lot of pyQt objects where as Rstudio makes html page
####Now selecting a column will sort it. 



