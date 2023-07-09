# euler_tools

def permute_down(pattern: list) -> bool:
    """Permutes the pattern in place, from high to low.

    Args:
        pattern (list): a list of items that can be compared ordinally

    Returns:
        bool: True if permutation is possible, False if it is not
    """
    if len(pattern) == 1:
        return False
    else:
        changed = False
        # new_pattern = pattern.copy()
        for d in range(1, len(pattern)):
            i = - (d)
            j = - (d + 1)

            if pattern[i] < pattern[j]:
                # pattern[j] is higher than next digit, so switch 
                tail = pattern[j:]
                repl = max(x for x in tail if x < pattern[j])
                tail.remove(repl)
                tail.sort(reverse=True)
                tail.insert(0, repl)
                pattern[j:] = tail
                changed = True
                break
        
        return changed