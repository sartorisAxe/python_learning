#open an input file for further analysis
def unfold(path_name):
    try:
        with open(path_name) as f:
            for line in f:
                dist, amp = line.split(';')
                try:                
                    amp = '.'.join(amp.split(','))                
                except:
                    pass
                distance.append(int(dist))
                amplitude.append(float(amp)) 
    except:
        print("there was an error")

def show_ldf_nums(distance, amplitude):
    for num in range(len(distance)):
        print(f'{distance[num]} {amplitude[num]}')   

def calculate_depth_one(ratio):
    result = 655 + 100*(ratio - 3.01)/0.46
    return result

def calculate_depth_two(ratio):
    return 660 + 100(ratio-11.5)/3

def MNK(amp, dist):
#there should be an algorithm of MNK to get coefficients
#maybe it should return a list? or only coefficients?
    pass


distance = []
amplitude = []

unfold('C:\\python\\input_files\\input_ldf_01.txt')

show_ldf_nums(distance, amplitude)

