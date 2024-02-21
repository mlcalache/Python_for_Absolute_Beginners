example = "hello world"  # global scope


def local_scope():
    example = "this is a string"  # local scope
    return example


print(example)
print(local_scope())
