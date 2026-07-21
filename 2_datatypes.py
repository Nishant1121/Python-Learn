type(42)                # <class 'int'>
type(3.14)              # <class 'float'>
type("Hello")           # <class 'str'>
type(True)              # <class 'bool'>
print(type(None))              # <class 'NoneType'>

isinstance(3.14, float)  # True
issubclass(int, object)  # True - everything inherits from object

int("42")                # 42
float("3.14")            # 3.14
str(42)                  # "42"
bool(1)                  # True
bool(0)                # False
bool("")               # False — empty string is falsy
bool([])               # False — empty list is falsy
list("abc")              # ["a", "b", "c"]
list((1, 2, 3))        # [1, 2, 3]
set([1, 1, 2, 3])      # {1, 2, 3} — deduplicates

#0, 0.0, "", [], {}, set(), and None are all falsy.Everything else is truthy.