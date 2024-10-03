print("Try programiz.pro")
"""write a function for getting frequency of each character"""
sample_string = "pythonnaturallanguageprocessing"


def cal_freq(str1):
    result = {}

    for ele in str1:
        if ele in result:
            result[ele] += 1
        else:
            result[ele] = 1
    return result
