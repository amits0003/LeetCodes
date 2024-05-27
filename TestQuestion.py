"""
Write a program to remove elements that have duplicates from a string in any language.
input : aabcdc??/
output: bd/
"""

stringA = "aabcdc??"

ds = [1, 2, 3, 1, 2, 3, 4]
ds1 = []
for ele in ds:
    if ds.count(ele) == 1:
        ds1.append(ele)

newStr = ""

uniqueDict = {}

for idx in range(len(stringA)):
    # print(stringA[idx])

    if stringA.count(stringA[idx]) ==1:
        newStr = newStr + stringA[idx]


print(newStr)

"""Given an upload file button and submit button in a form, what would your test scenarios be."""

""" positive flow"""
"""1.  presence of upload file button and presence of submit file button """
"""2.  Testing Upload File Button : suppose acceptable formats are : .PDF, .CSV, .JPEG, .PNG = in recursive
 way , sample file of all formats will be uploaded to see, if Form is generating success response """
"""3. Testing Upload File Button : the upload file size limit for all formats : example 5 MB : in recursive way
 , user will upload the files for all above formats to see the whether postal is allowing the upload"""
"""4. Negative scenario for Testing Upload File Button  : user uploads the file other than the format mentioned above 
to test if the form is returning any error post upload"""
"""5.Negative scenario for Testing Upload File Button : user uploads the file size more than allowed file size to observe 
the form is generating any error response """
""" 6. extend test 2  : next -> submit button will be pressed : form should generate a sucess response on UI"""
""" 7. extend test 2  : next -> submit button will be pressed : a new entry in DB with the file details should be validated"""
""" 8 extend test 3 : next - > submit button will be pressed form should generate a nsucess resposne ,a nd new entry in db . """
""" 9 extend 4 : next - > press the submit button > error message (for file format) should be displayed and form should not allow upload"""
""" 10 : extend 5 - next -> press the sub,it button > error message (for exceeding file size) should be displayed at the UI """
""" 11: user uploads a invalid file format > no new entry should be viusible in db with this file details"""
""" 12: user uploads a large fixe size exceeding limit  > no new entry should be viusible in db with this file details"""
""" 13: user uploads the same file (with right size and valid format) > if user req says that file upload should be allowed
two entrie in db with different time stamps / if older file entry gets over-ridden with new time stamp"""


