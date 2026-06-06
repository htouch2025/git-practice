def print_readme_lines():
    with open('README.md', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.rstrip())