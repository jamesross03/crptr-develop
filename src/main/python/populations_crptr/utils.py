import csv
import random
import time

def readInFile(inputFile):
    recordsDict = {}
    with open(inputFile, "r") as f:
        dataset = csv.reader(f, delimiter=",")

        for row in dataset:
            if not row[0] in recordsDict:
                recordsDict[row[0]] = []

            for value in row[1:]:
                recordsDict[row[0]].append(value)

    return recordsDict

def readInFileAsDict(inputFile):
    with open(inputFile, 'r', newline='', encoding='utf-8') as f:
        dataset_file = csv.DictReader(f)
    return list(dataset_file)

def extractLabels(data, idColumnLabel = "rec-id"):
    #print data[idColumnLabel]
    labels = data[idColumnLabel]
    del data[idColumnLabel]
    #del labels[idColumnLabel]

    return labels

def convertFromListOfDictsToDictOfLists(dataset, idColumnLabel = "rec-id"):
    convertedDataset = dict()

    keys = list(dataset[0].keys())
    keys.remove(idColumnLabel)
    convertedDataset[idColumnLabel] = keys

    for d in dataset:
        r = d[idColumnLabel]
        del d[idColumnLabel]
        convertedDataset[r] = [v for v in list(d.values())]

    return convertedDataset


def removeCommas(dataset):
    for d in dataset:
        for key, value in d.items():
            if "," in d[key]:
                d[key] = d[key].replace(",", "-")
                print(d[key])

    return dataset


def removeCommasInFiles(inputFile, outputFile):

    with open(inputFile, 'r', newline='', encoding='utf-8') as f:
        dataset_file = csv.DictReader(f)

    dataset = list(dataset_file)

    dataset = removeCommas(dataset)

    fieldnames = list(dataset[0].keys())
    csvfile = open(outputFile, 'w', newline='', encoding='utf-8')
    csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn, fn) for fn in fieldnames))

    for r in dataset:
        csvwriter.writerow(r)
    csvfile.close()

    print("Removed commas in strings")

    return outputFile

def addCryptIDs(dataset):
    count = 0

    for r in dataset:
        r["rec-id"] = "rec-" + str(count) + "-org"
        count += 1
        r["crptr-record"] = "original"

    return dataset


def addCryptIDsInFiles(inputFile, outputFile):

    with open(inputFile, 'r', newline='', encoding='utf-8') as f:
        dataset_file = csv.DictReader(f)

    dataset = list(dataset_file)

    dataset = addCryptIDs(dataset)

    fieldnames = list(dataset[0].keys())
    csvfile = open(outputFile, 'w', newline='', encoding='utf-8')
    csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn, fn) for fn in fieldnames))

    for r in dataset:
        csvwriter.writerow(r)

    csvfile.close()

    print("Added Crptr IDs")


def writeToFile(dataset, outputFile):
    fieldnames = list(dataset[0].keys())
    csvfile = open(outputFile, 'w', newline='', encoding='utf-8')
    csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn, fn) for fn in fieldnames))

    for r in dataset:
        csvwriter.writerow(r)

    csvfile.close()

def removeCryptIDs(dataset, labels):

    # for i in dataset:
    #     if None in i:
    #         print i

    for r in list(dataset.values()):
        del r[labels.index('crptr-record')]

    del labels[labels.index('crptr-record')]

    return dataset


def removeCryptIDsInFiles(inputFile, outputFile):

    with open(inputFile, 'r', newline='', encoding='utf-8') as f:
        dataset_file = csv.DictReader(f)

    dataset = list(dataset_file)
    dataset_len = str(len(dataset))

    dataset = removeCryptIDs(dataset)

    fieldnames = list(dataset[0].keys())
    csvfile = open(outputFile, 'w', newline='', encoding='utf-8')
    csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn, fn) for fn in fieldnames))

    for r in dataset:
        csvwriter.writerow(r)

    csvfile.close()

    print("Removed Crptr IDs")

def removeOrigonalRecordsForWhichDuplicateExists(dataset, labels):
    # for i in dataset:
    #     if None in i:
    #         print i

    delete = []

    for r in dataset:
        # index = labels.index('rec-id')
        if "dup" in r:
            rec, recid, dup, dupid = r.split('-')
            org_of_dup = rec + "-" + recid + "-org"

            delete.append(org_of_dup)

            # for r2 in dataset:
            #     if org_of_dup == r2:
            #         dataset.remove(r2)

    for d in delete:
        del dataset[d]

    return dataset

def removeOrigonalRecordsForWhichDuplicateExistsInFiles(inputFile, outputFile):

    with open(inputFile, 'r', newline='', encoding='utf-8') as f:
        dataset_file = csv.DictReader(f)

    dataset = list(dataset_file)
    dataset_len = str(len(dataset))

    dataset = removeOrigonalRecordsForWhichDuplicateExists(dataset)

    fieldnames = list(dataset[0].keys())
    csvfile = open(outputFile, 'w', newline='', encoding='utf-8')
    csvwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
    csvwriter.writerow(dict((fn, fn) for fn in fieldnames))

    for r in dataset:
        csvwriter.writerow(r)

    csvfile.close()

    print("Removed origonals of corrupted records")


def outputDictToCSV(labels, dict, outputFile, encoding = 'utf-8'):
    rec_id_list = list(dict.keys())
    rec_id_list.sort()

    with open(outputFile, 'w', newline='', encoding=encoding) as csvfile:
        outputWriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        outputWriter.writerow(labels)

        for rec_id in rec_id_list:
            outputWriter.writerow(dict[rec_id])
            # row = [unicode(cell, 'utf-8') for cell in dict[rec_id]]
            # row = [s.decode('utf-8') for s in dict[rec_id]]
            # outputWriter.writerow(row)

            # outputWriter.writerow(dict[rec_id])


                # yield [unicode(cell, 'utf-8') for cell in row]



def setDeterminism(deterministic, seed = None):
    if deterministic:
        random.seed(seed)
    else:
        seed = time.time()
        random.seed(seed)

    print("Used seed: " + str(seed))
