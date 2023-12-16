def upper_dekor(funk):
    def wew():
        # print(upper(funk))
        result = funk()
        return result.upper()

    return wew
@upper_dekor
def funk():
    return ("tekst")


print(funk())
