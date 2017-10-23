class classic:
        def __getattr__(self,name):
            if name == 'age':
                return 40
            else:
                raise AttributeError


if __name__ == '__main__':
    x = classic()
    print(x.age)
    print(x.name)


