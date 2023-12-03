import chardet

with open('test.log','rt') as file:
    raw_data = file.read()

    result = chardet.detect((raw_data))
    print(result)
    encoding = result['encoding']
    print(encoding)
    print(raw_data.decode(encoding=encoding))