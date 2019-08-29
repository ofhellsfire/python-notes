def sort_by_count(coll):
    d = dict()
    def by_count(item):
        return d[item], item
    for item in coll:
        d[item] = d.get(item, 0) + 1
    return sorted(d, key=by_count)

coll = ['uno', 'uno', 'dos', 'tres', 'tres', 'uno', 'tres', 'dos', 'tres', 'tres', 'das', 'das', 'das', 'dos', 'tres']
print(sort_by_count(coll))
