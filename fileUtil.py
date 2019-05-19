'''数据预处理，标注字的位置 '''
def generate_label(input_file,output_file):
    with open(input_file,'r',encoding='utf-8') as file:
        lines=file.readlines()

    with open(output_file,'w',encoding='utf-8') as out:
        for line in lines:
            word_list = line.strip().split()
            for word in word_list:
                if len(word) == 1:
                    out.write(word + "##S ")
                else:
                    out.write(word[0] + "##B ")
                    for w in word[1:len(word) - 1]:
                        out.write(w + "##M ")
                    out.write(word[len(word) - 1] + "##E ")


            out.write("\n")
        out.close()

def get_data(input_file):
    word_list=[]
    label_list=[]
    with open(input_file,'r',encoding='utf-8') as file:
        lines=file.readlines()
        for line in lines:
            words=line.split()
            word_list.append(list(map(lambda x:x.split("##")[0],words)))
            label_list.append(list(map(lambda x:x.split("##")[1],words)))
            # print(list(map(lambda x:x.split("##")[0],words)))
    return word_list,label_list


if __name__ == '__main__':
    generate_label('test_cws1.txt','test.txt')
    get_data('train.txt')