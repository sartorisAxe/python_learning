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
            return [distance, amplitude]
                 
    except:
        print("there was an error")
