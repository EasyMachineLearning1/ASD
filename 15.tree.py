class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_bracket_notation(s):
    index = 0

    def helper():
        nonlocal index
        if index >= len(s) or s[index] == ')':
            return None

        # Читаем значение узла
        value = ''
        while index < len(s) and s[index] not in '(),':
            value += s[index]
            index += 1
        
        if value == '':
            node = TreeNode(None)
        else:
            node = TreeNode(int(value))

        # Обрабатываем левое поддерево
        if index < len(s) and s[index] == '(':
            index += 1  # Пропускаем открывающую скобку
            node.left = helper()
            if index < len(s) and s[index] == ',':
                index += 1  # Пропускаем запятую
                node.right = helper()
            index += 1  # Пропускаем закрывающую скобку

        return node

    return helper()

# Пример использования
s = "8(3(1,6(4,7)),10(,14(13,)))"
root = parse_bracket_notation(s)

# Функция для печати дерева (для проверки)
def print_tree(node, level=0):
    if node:
        print("  " * level + str(node.value))
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)

print_tree(root)


# Прямой обход (Pre-order)
def pre_order(node):
    if node:
        print(node.value, end=" ")  # Посещаем корень
        pre_order(node.left)       # Рекурсивно обходим левое поддерево
        pre_order(node.right)      # Рекурсивно обходим правое поддерево

# Центральный обход (In-order)
def in_order(node):
    if node:
        in_order(node.left)        # Рекурсивно обходим левое поддерево
        print(node.value, end=" ") # Посещаем корень
        in_order(node.right)      # Рекурсивно обходим правое поддерево

# Концевой обход (Post-order)
def post_order(node):
    if node:
        post_order(node.left)      # Рекурсивно обходим левое поддерево
        post_order(node.right)     # Рекурсивно обходим правое поддерево
        print(node.value, end=" ") # Посещаем корень

# Создаем дерево из строки
s = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13,)))"
root = parse_bracket_notation(s)

# Выполняем обходы
print("Прямой обход (Pre-order):")
pre_order(root)
print("\n")

print("Центральный обход (In-order):")
in_order(root)
print("\n")

print("Концевой обход (Post-order):")
post_order(root)
print("\n")