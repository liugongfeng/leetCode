from collections import defaultdict

class Solution:
    # Hash table
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        d = defaultdict(int)

        for domain in cpdomains:
            count, names = domain.split()
            count, list_names = int(count), names.split('.')

            for i in range(len(list_names)):
                d['.'.join(list_names[i:])] += count
        
        return [f"{cnt} {name}" for name, cnt in d.items()]

