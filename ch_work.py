import ma_check
import sys


def open_dic(txt):
    get_list = list()
    with open(txt,'r') as txt_dict:
        lines = txt_dict.readlines()
    for line in lines:
        line = line.strip('\n')
        get_list.append(line)
    return get_list

def work(i,dict_list):
    ###############################################
    raw_word = '' #The failure mnemonic word string
    target_address = '' #The target wallet address
    ###############################################
    words = raw_word.split(" ")
    j=0
    for inject in dict_list:
        words.insert(i,inject)
        cooked_words = " ".join(words)
        if ma_check.ma_check(cooked_words,target_address):
            print("The right mnemonic is found!!!\n"+cooked_words)
            sys.exit(0)
        else:
            j=j+1
            print(i,"posiont insert",j,"times")
        del words[i]
    print("The mnemonic at",i,"position is not found! Sorry!")
        
    
if __name__ == '__main__':
    dict_list = open_dic('english.txt')
    for x in range(int(sys.argv[1]),int(sys.argv[2])):
        work(x,dict_list)
