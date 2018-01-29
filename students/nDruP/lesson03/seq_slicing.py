def swap_first_last(seq):
    first = seq[0]
    seq[0]=seq[len(seq)-1]
    seq[len(seq)-1]=first
    return seq


one_element = [51]
string_a = 'Love Galore'
seq_a = [5,3,1,2,4,6]

assert swap_first_last(one_element) == one_element
assert swap_first_last(string_a) == 'eove GaloL'
assert swap_first_last(seq_a) == [6,3,1,2,4,5]