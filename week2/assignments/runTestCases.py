import os
import zipfile
import shutil


def runTestCases(processingFunction, zip_filename):
    # Step 1: Unzip the folder
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall("tmp")

    # Step 2: Locate the unknown folder (the one directly inside the unzipped 'grpa' folder)
    root_folder = 'tmp'
    extracted_folder = os.path.join(root_folder, os.listdir(root_folder)[0])
    total_testcase_count = 0
    testcase_passed_count = 0
    for category in ['public','private']:
        
        category_folder = os.path.join(extracted_folder,category)
        
        for testcase in os.listdir(category_folder):
            testcase_folder = os.path.join(category_folder,testcase)
            
            if os.path.isdir(testcase_folder):
                input_file = os.path.join(testcase_folder,'input.txt')
                output_file = os.path.join(testcase_folder,'output.txt')
                
                with open(input_file, 'r') as inFile:
                    input_array = list(map(int,inFile.read().strip().split()))
                
                with open(output_file,'r') as outFile:
                    output_array = list(map(int,outFile.read().strip().split()))
                
                result = processingFunction(input_array)
                # print("input_array",input_array)
                # print("output_array",output_array)
                # print("result",result)
                total_testcase_count = total_testcase_count + 1
                if result == output_array:
                    testcase_passed_count = testcase_passed_count + 1
                    print(f"{category} {testcase}: test case passed")
                else:
                    print(f"{category} {testcase}: test case failed")
    print(f"{testcase_passed_count} testcases passed out of {total_testcase_count}")
    shutil.rmtree(extracted_folder)