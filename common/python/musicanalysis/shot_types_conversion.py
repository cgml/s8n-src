NN_SHOT_TYPES = ['CU','MS','FS','XLS']

SHOT_TYPES = {
    'XCU':{'nn_match':'CU','scale':1, 'name':'extreme close up'},
    'MCU':{'nn_match':'CU','scale':2},
    'WCU':{'nn_match':'CU','scale':3, 'name':'wide close up'},
    'CU':{'nn_match':'CU','scale':5},
    'MCS':{'nn_match':'MS','scale':20},
    'MS':{'nn_match':'MS','scale':30},
    'COWS':{'nn_match':'MS','scale':35},
    'MFS':{'nn_match':'FS','scale':40},
    'FS':{'nn_match':'FS','scale':50},
    'WS':{'nn_match':'FS','scale':100,'name':'wide shot', 'syn':['LS']},
    'XWS':{'nn_match':'XLS','scale':200,'name':'extreme wide shot', 'syn':['XLS']},
    'CI':{'nn_match':'XLS','scale':10, 'name':'cut in'},
    'CA':{'nn_match':'XLS','scale':100,'name':'cut out'}
}

def convert_to_nn_types(original_shot_types):
    result = []
    for st in original_shot_types:
        if SHOT_TYPES.get(st) != None:
            result.append(SHOT_TYPES.get(st)['nn_match'])
        else:
            print ('Not found',st)
    return result

def extract_sequence_from_manual_analysis(manual_analysis_csv_path):
    st = []
    with open(manual_analysis_csv_path) as f:
        lines = f.read().split('\n')
    for line in lines:
        st.append(line.split(',')[2])
    result = convert_to_nn_types(st)
    return result

# nn_st = convert_to_nn_types(st)
# print nn_st