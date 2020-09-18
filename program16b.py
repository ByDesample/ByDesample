def Gather(processParam: str) -> int:
    index = processParam[:processParam.find("+")]
    index2 = processParam[processParam.rfind("+"):]
    return int(index) + int(index2)


def Extraction(processParam: str) -> int:
    index = processParam[:processParam.find("-")]
    index2 = processParam[processParam.rfind("-"):]
    return int(index) - int(index2)


def Impact(processParam: str) -> int:
    index = processParam[:processParam.find("*")]
    index2 = processParam[processParam.rfind("*"):]
    return int(index) * int(index2)


def Chamber(processParam: str) -> int:
    index = processParam[:processParam.find("/")]
    index2 = processParam[processParam.rfind("/"):]
    return int(index) // int(index2)


while True:
    process = input("Enter Process: ")
    if process in process.find("+"):
        Gather(process)