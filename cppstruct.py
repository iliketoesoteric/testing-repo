# python linters don't like this

class struct(type):
    def __new__(cls, name, bases, dict):
        annotations = dict.pop('__annotations__')
        for key in annotations:
            globals()[key] = key

        def __getitem__(self, other):
            if other in annotations:
                return annotations[other]
        
        dict.update(annotations)
        dict['__getitem__'] = __getitem__

        return type(name, bases, dict)

@lambda x: x()
class person(metaclass=struct):
    name: 'BRUH';
    age: 10;

print(
    person[name],
    person[age]
)
