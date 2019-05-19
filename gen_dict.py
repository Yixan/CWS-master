import pickle
def gen_dict(filename,mode='pkl'):
    char2num_dict=dict()
    with open(filename,'r',encoding='utf-8') as file:
        chars=file.read()
        chars= ''.join(chars.split())
    # print(chars)
    i=1
    for char in chars:
        if not char in char2num_dict.keys():
            char2num_dict[char]=i
            i=i+1
    char2num_dict['<UNK>']=i
    print(char2num_dict)
    num2char_dict=dict(zip(char2num_dict.values(), char2num_dict.keys()))
    if mode=='pkl':
        with open('data\\char2num.pkl', 'wb') as f:
            pickle.dump(char2num_dict, f, pickle.HIGHEST_PROTOCOL)

    return char2num_dict,num2char_dict





if __name__ == '__main__':
    gen_dict('train_cws.txt')