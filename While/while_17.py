next_num = int(input())
previous_num = next_num
current_counter = 0
largest_counter = 1

while next_num != 0:
    if next_num == previous_num:
        current_counter += 1
    else:
        current_counter = 1
    if largest_counter <= current_counter:
        largest_counter = current_counter
    previous_num = next_num
    next_num = int(input())
print(largest_counter)


prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
