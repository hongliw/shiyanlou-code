import sys

def Hours(minutes):
    if minutes < 0:
        raise ValueError('Input number cannnot be negative')
    else:
        hours = minutes // 60
        minute = minutes % 60
        print('{} H, {} M'.format(hours, minute))

    

if __name__ == '__main__':
    try:
        Hours(int(sys.argv[1]))
    except:
        print('Parameter Error.')
