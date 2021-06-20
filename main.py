# This is a sample Python script.
import xml.etree.ElementTree as Xet
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Importing the required libraries


    cols = ["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"]
    rows = []

    # Parsing the XML file
    xmlparse = Xet.parse('mergedAnnotations.xml')
    root = xmlparse.getroot()
    fileLength = len(root)

    for i in root:
        filename = i.find("filename").text
        width = i.find("size").find("width").text
        height = i.find("size").find("height").text
        annotation = i.find("object").find("name").text
        xmin = i.find("object").find("bndbox").find("xmin").text
        ymin = i.find("object").find("bndbox").find("ymin").text
        xmax = i.find("object").find("bndbox").find("xmax").text
        ymax = i.find("object").find("bndbox").find("ymax").text

        rows.append({"filename": filename,
                     "width": width,
                     "height": height,
                     "class": annotation,
                     "xmin": xmin,
                     "ymin": ymin,
                     "xmax": xmax,
                     "ymax": ymax})

    df = pd.DataFrame(rows, columns=cols)
    df = df.sample(frac=1)
    # shuffle the dataframe
    # calculate how many items need to be put in the test csv file
    amountForTest = int((20 / 100) * fileLength)

    # split dataframe in train and test
    dfTrain = df.iloc[amountForTest + 1:, :]
    dfTest = df.iloc[:amountForTest, :]


    # Writing dataframe to csv
    dfTest.to_csv('test_labels.csv', index=False)
    dfTrain.to_csv('train_labels.csv', index=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
