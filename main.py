from collections import defaultdict


def gets_fragments(filename):
    with open(filename, "r") as file:
        fragments = [line.strip() for line in file.readlines()]
    return fragments


def build_graph(fragments):
    graph = defaultdict(list)
    for frag in fragments:
        prefix = frag[:2]  # перші дві цифри фрагмента
        graph[prefix].append(frag)
    print(graph)
    return graph


def find_longest_sequence(graph, fragments):
    def dfs(current, visited):
        nonlocal best_path, best_length
        sequence = assemble_sequence(current)
        if len(sequence) > best_length:
            best_length = len(sequence)
            best_path = current[:]

        last_prefix = current[-1][-2:]  # останні дві цифри поточного фрагмента
        for next_frag in graph[last_prefix]:
            if next_frag not in visited:
                visited.add(next_frag)
                dfs(current + [next_frag], visited)
                visited.remove(next_frag)

    best_path = []
    best_length = 0
    for fragment in fragments:
        dfs([fragment], set([fragment]))

    return best_path


def assemble_sequence(path):
    sequence = path[0]
    for frag in path[1:]:
        sequence += frag[2:]  # додаємо лише останні цифри фрагментів
    return sequence


if __name__ == "__main__":
    fragments = gets_fragments("source.txt")
    graph = build_graph(fragments)
    longest_path = find_longest_sequence(graph, fragments)
    longest_sequence = assemble_sequence(longest_path)

    print(longest_sequence)
