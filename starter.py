import os.path as osp
from kbc.cqd_beam import *


#model_path = "models/FB15k-model-rank-100-epoch-100-1602511249.pt"
model_paths = ["models/FB15k-model-rank-100-epoch-100-1602511249.pt",
			   "models/FB15k-model-rank-200-epoch-100-1602513660.pt",
			   "models/FB15k-model-rank-500-epoch-100-1602516425.pt",
			   "models/FB15k-model-rank-1000-epoch-100-1602520745.pt"]
path = "data/FB15k"
dataset = osp.basename(path)
mode = "test"
candidates = 64
t_norm = "product"
scores_normalize = 0

data_hard_path = osp.join(path, f'{dataset}_{mode}_hard.pkl')
data_complete_path = osp.join(path, f'{dataset}_{mode}_complete.pkl')

data_hard = pickle.load(open(data_hard_path, 'rb'))
data_complete = pickle.load(open(data_complete_path, 'rb'))

for model_path in model_paths:
	run(model_path, data_hard, data_complete,
		dataset, t_norm, candidates,
		scores_normalize,
		kg_path=path, explain=False)