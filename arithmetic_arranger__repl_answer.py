import operator

def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
      return 'Error: Too many problems.'
    top_list = []
    bottom_list = []
    divider_list = []
    answer_list = []
    for problem in problems:
        split = problem.split(' ')
        if split[1] == '*' or split[1] == '/':
          return 'Error: Operator must be \'+\' or \'-\'.'
        if split[0].isdigit() == False or split[2].isdigit() == False:
          return 'Error: Numbers must only contain digits.'
        num_one_len = len(split[0])
        num_two_len = len(split[2])
        if num_one_len > 4 or num_two_len > 4:
          return 'Error: Numbers cannot be more than four digits.'
        ops = { "+": operator.add, "-": operator.sub }
        if split[1] == '+':
          answer = ops['+'](int(split[0]),int(split[2]))
        else:
          answer = ops['-'](int(split[0]),int(split[2]))
        answer = str(answer)
        bigger_num = (num_one_len if num_one_len
                      > num_two_len else num_two_len)

        # need to figure out whitespace calculation for each line
        space_top_length = 0
        space_bottom_length = 0
        if num_one_len > num_two_len:
            space_bottom_length = num_one_len - num_two_len
        else:
            space_top_length = num_two_len - num_one_len

        count = 0
        spaces_top = ''
        while space_top_length > count:
            spaces_top += ' '
            count += 1

        count2 = 0
        spaces_bottom = ''
        while space_bottom_length > count2:
            spaces_bottom += ' '
            count2 += 1

        count3 = 0
        divider = '--'
        while bigger_num > count3:
            divider += '-'
            count3 += 1

        top_line = '  ' + spaces_top + split[0]
        bottom_line = split[1] + ' ' + spaces_bottom + split[2]

        top_list.append(top_line)
        bottom_list.append(bottom_line)
        divider_list.append(divider)
        
        if show_answer:
          if '-' in answer:
            answer_line = ' '+ answer
            answer_list.append(answer_line)
          else:
            answer_line = '  ' + answer
            answer_list.append(answer_line)
        else:
          answer_list = ''
        t = '    '.join(top_list)
        b = '    '.join(bottom_list)
        d = '    '.join(divider_list)
        a = '    '.join(answer_list)
    if not a:
      return """{}
{}
{}""".format(t,b,d)
    else:
      return """{}
{}
{}
{}""".format(t,b,d,a)


arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49','9999 + 9999'])
