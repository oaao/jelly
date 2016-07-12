from functools import reduce


def jam_calc(strength, sen, qty):
    c = (1 - (strength / sen) ** qty)
    jams_list.append(c)


def jam_inputs():
    next_calc = ''
    while next_calc is not 'n':
        jam_str = float(input('What is the jam strength of the current jammer?\n'))
        jam_n = int(input('How many of this exact jam are you applying to the target?\n'))
        jam_calc(jam_str, jam_sen, jam_n)
        next_calc = input('Do you want to add another type of jam for this target? [y, n]\n')
        if next_calc is 'y':
            continue
        elif next_calc is 'n':
            break
        else:
            print('Something went wrong; please be careful of your inputs and try again.')
            break


def jam_main():
    iter_jams = reduce(lambda x, y: x*y, jams_list)
    jams_total = 1 - iter_jams
    print('You have a %s overall chance of jamming your target. Fuck you.'
          % '{:.1%}'.format(jams_total))

jams_list = []
jam_sen = float(input('What is the target\'s sensor strength?\n'))

jam_inputs()
jam_main()
