import tour

def make_rules(data):
    rules = [tour.Rule(ordering = r[0], switch_square = r[1], next_rule = None) for r in data]
    for i in range(0, len(rules)-1):
        rules[i].next_rule = rules[i+1]
    return rules

def get_rules(m, board):
    if 0 == m%8:
        return make_rules([["34261578", board.get_square_at(m-1,     m-2     )], \
                           ["87642135", board.get_square_at(2,       2       )], \
                           ["51867342", board.get_square_at(m-8,     1       )], \
                           ["51342678", board.get_square_at(7,       m-3     )], \
                           ["21435678", None]])
    elif 1 == m%8:
        return make_rules([["34261578", board.get_square_at(m-1,     m-2     )], \
                           ["87642135", board.get_square_at(2,       2       )], \
                           ["51324678", board.get_square_at(m-6,     (m+9)/2 )], \
                           ["32481765", None]])
    elif 2 == m%8:
        return make_rules([["34261578", board.get_square_at(6,       1       )], \
                           ["87642135", board.get_square_at(3,       1       )], \
                           ["54132678", board.get_square_at(m-15,    4       )], \
                           ["52431678", board.get_square_at(10,      m-2     )], \
                           ["85647123", board.get_square_at(5,       (m-6)/2 )], \
                           ["15746823", None]])
    elif 3 == m%8:
        return make_rules([["34625718", board.get_square_at(m-1,     m-2     )], \
                           ["42681357", board.get_square_at(m-6,     m       )], \
                           ["86512347", board.get_square_at(2,       5       )], \
                           ["51867342", board.get_square_at(m-10,    3       )], \
                           ["61825437", board.get_square_at((m+1)/2, m-2     )], \
                           ["71642538", None]])
    elif 4 == m%8:
        return make_rules([["34261578", board.get_square_at(m-1,     m-2     )], \
                           ["87642135", board.get_square_at(2,       2       )], \
                           ["51867342", board.get_square_at(m-8,     1       )], \
                           ["51342678", board.get_square_at(10,      m-5     )], \
                           ["86753421", board.get_square_at(13,      (m+2)/2 )], \
                           ["78563421", None]])
    elif 5 == m%16: 
        return make_rules([["34261578", board.get_square_at(m-1,     m-2     )], \
                           ["87642135", board.get_square_at(2,       2       )], \
                           ["51324678", board.get_square_at(m-2,     (m-5)/2 )], \
                           ["15234678", None]])
    elif 13 == m%16: 
        return make_rules([["34261578", board.get_square_at(m-1,     m-2     )], \
                           ["87642135", board.get_square_at(2,       2       )], \
                           ["51324678", board.get_square_at(m-2,     (m-13)/2)], \
                           ["15234678", None]])
    elif 6 == m%8:
        return make_rules([["34261578", board.get_square_at(6,       1       )], \
                           ["87642135", board.get_square_at(3,       1       )], \
                           ["54132678", board.get_square_at(m-10,    1       )], \
                           ["52431678", board.get_square_at(10,      m-2     )], \
                           ["85647123", board.get_square_at(3,       (m+8)/2 )], \
                           ["12453678", None]])
    elif 7 == m%8:
        return make_rules([["34625718", board.get_square_at(m-1,     m-2     )], \
                           ["42681357", board.get_square_at(m-6,     m       )], \
                           ["86512347", board.get_square_at(2,       5       )], \
                           ["51867342", board.get_square_at(m-6,     3       )], \
                           ["61825437", board.get_square_at((m+1)/2, m-2     )], \
                           ["61357284", None]])


