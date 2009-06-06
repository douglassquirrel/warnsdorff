import tour

def make_rules(data):
    rules = [tour.Rule(ordering = r[0], switch_square = r[1], next_rule = None) for r in data]
    for i in range(0, len(rules)-1):
        rules[i].next_rule = rules[i+1]
    return rules

def get_rules(m, board):
    if 0 == m%8:
        return make_rules([["34261578", board.get_square_at(m-1, m-2)], \
                           ["87642135", board.get_square_at(2,   2  )], \
                           ["51867342", board.get_square_at(m-8, 1  )], \
                           ["51342678", board.get_square_at(7,   m-3)], \
                           ["21435678", None]])
    return None

