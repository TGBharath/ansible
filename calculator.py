# calculator application for 2 numbers with + - / *
a = $value1
b = $value2

operation = $Choices

match operation:
        case add:
            return "a+b"
        case sub:
            return "a-b"
        case mul:
            return "a*b"
        case div:
            return "a/b"
