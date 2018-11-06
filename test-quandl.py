# -*- coding : utf8 -*-
import quandl

petr4 = quandl.get("SGE/BVMF_PETR4")
print(petr4.index)
print(petr4.head())