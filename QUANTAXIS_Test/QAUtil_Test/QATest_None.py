import unittest

import sys
import time

#from QUANTAXIS.QAFetch import (QATdx );
from QUANTAXIS.QAUtil import (QADate, QADate_trade );

#from pandas import Series
import pandas as pd


class Test_QA_None(unittest.TestCase):

    def test_None(self):


        obj = pd.Series([3,4,-2,2])
        print(obj)

        #now = QADate.QA_util_time_now()
        #print( type(now) )

        #today = QADate.QA_util_date_today()
        #print( type(today))

        #print("okok---> do the task")

        # for i in range(101):
        #     s1 = "\r%d%%[%s%s]" % (i, "*" * i, " " * (100 - i))
        #     time.sleep(1)
        #     sys.stdout.write(s1)
        #     sys.stdout.flush()
        # pass


