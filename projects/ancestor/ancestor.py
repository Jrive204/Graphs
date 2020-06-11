from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    parent_dict = defaultdict(list)
    for pair in ancestors:
        parent_dict[pair[1]].append(pair[0])
        print(pair[0], pair[1], "PAIR", pair, dict.__repr__(parent_dict))

    if starting_node not in parent_dict:
        return -1

    def recursive_ancestor(child, level=0):
        print(f"\n recurs -- child: {child} {parent_dict}")
        if child not in parent_dict:
            print("\n child not in parent dict, appends to list",
                  (child, level), "\n")
            return (child, level)
        else:
            candidates = []
            for parent in parent_dict[child]:
                print(
                    candidates,
                    level,
                    child,
                    "< -- Child Parent -->",
                    parent,
                    parent_dict[child],
                    "CANDIDATES")
                # This will eventually Append if it returns (child,Level) from
                # child non in parent dict
                candidates.append(recursive_ancestor(parent, level + 1))

            print("Return Sorted", child, "<-Child level ->", level, candidates)
            return sorted(candidates, key=lambda x: (x[1]), reverse=True)[0]

    return recursive_ancestor(starting_node)[0]


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 9))
