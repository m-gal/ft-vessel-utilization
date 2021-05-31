"""
    Helps to reload project's module and get its inspections
    w\o reloading working space

    @author: mikhail.galkin
"""

#%% Import libs
import sys
import inspect
import importlib

sys.path.extend(["..", "../..", "../../.."])
import vessel_utilize

#%% CONFIG: Reload -------------------------------------------------------------
import vessel_utilize.config

importlib.reload(vessel_utilize.config)
from vessel_utilize.config import project_dir

print(project_dir)

#%% UTILS: Reload --------------------------------------------------------------
import vessel_utilize.utils

importlib.reload(vessel_utilize.utils)
print(inspect.getsource(vessel_utilize.utils.set_pd_options))

#%% CLASSES: Reload ------------------------------------------------------------
# import vessel_utilize.classes

# importlib.reload(vessel_utilize.classes)

#%% PLOTS: Reload --------------------------------------------------------------
import vessel_utilize.plots

importlib.reload(vessel_utilize.plots)
print(inspect.getsource(vessel_utilize.plots.plot_residuals_errors))

#%% MODEL: RandomForestRegressor -----------------------------------------------
import vessel_utilize.model._rf

importlib.reload(vessel_utilize.model._rf)
print(inspect.getsource(vessel_utilize.model._rf.model))
print(inspect.getsource(vessel_utilize.model._rf.param_search))


#%% MODEL: XGBRegressor --------------------------------------------------------
import vessel_utilize.model._xgb

importlib.reload(vessel_utilize.model._xgb)
print(inspect.getsource(vessel_utilize.model._xgb.model))
print(inspect.getsource(vessel_utilize.model._xgb.param_search))

#%% shipdb_train_model_enrich -------------------------------------------------------=
import vessel_utilize.data.shipdb_train_model_enrich

importlib.reload(vessel_utilize.data.shipdb_train_model_enrich)
print(inspect.getsource(vessel_utilize.data.shipdb_train_model_enrich.train_model))

#%%
