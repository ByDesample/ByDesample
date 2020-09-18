def Gather(processParam: str) -> int:
    index = processParam[:processParam.find("+")]
    index2 = processParam[processParam.rfind("+") + 1:]
    return int(index) + int(index2)


def Extraction(processParam: str) -> int:
    index = processParam[:processParam.find("-")]
    index2 = processParam[processParam.rfind("-") + 1:]
    extraction_process = int(index) - int(index2)
    return extraction_process


def Impact(processParam: str) -> int:
    index = processParam[:processParam.find("*")]
    index2 = processParam[processParam.rfind("*") + 1:]
    return int(index) * int(index2)


def Chamber(processParam: str) -> int:
    index = processParam[:processParam.find("/")]
    index2 = processParam[processParam.rfind("/") + 1:]
    return int(index) // int(index2)


while True:
    process = input("Enter Process: ")
    for mark in process:
        if mark == "+":
            gather_result = Gather(process)
            print(gather_result)
        elif mark == "-":
            extraction_result = Extraction(process)
            print(extraction_result)
        elif mark == "*":
            impact_result = Impact(process)
            print(impact_result)
        elif mark == "/":
            chamber_result = Chamber(process)
            print(chamber_result)
