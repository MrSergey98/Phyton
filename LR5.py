import re


def validatehtml(string):

    pattern = r'<img src=".*"(alt=".*")?>'
    if re.fullmatch(pattern=pattern, string=string):
        return True
    else:
        return False


class ImgException(Exception):
    pass


def strictvalidatehtml(string):

    pattern = r'<img src=".*"(alt=".*")?>'
    if re.fullmatch(pattern=pattern, string=string):
        return string
    else:
        raise ImgException("Строка не прошла валидацию на код изображения HTML.")


if __name__ == "__main__":
    string = '<img src="dinosaur.jpg"q>'
    print(validatehtml(string))
    print(strictvalidatehtml(string))


