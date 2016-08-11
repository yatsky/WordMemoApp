import  cfg


def is_number():
    while True:
        try:
            cfg.target = int(raw_input('Please set your target today.\n'))
            break
        except ValueError:
            print 'You typed a wrong number!\nPlease give another one!\n'


def is_big():
    while True:
        if cfg.target > min(cfg.records):
            break
        else:
            print 'This target is too small, you could do better!\n'
            print 'Give me another one!'
            is_number()