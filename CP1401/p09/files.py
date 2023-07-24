def question_4():
    in_file = open("name.txt", 'r')
    text = in_file.read().strip()
    print(text)

# question_4()

def question_5():
    file_name = input("Filename :")
    threshold = float(input("Threshold:"))
    count = 0
    total_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            total_count += 1
            if float(line) > threshold:
                count += 1
    print(f'Processing...')
    print(f"{count} out of {total_count} ({count/total_count*100}%) values in {file_name} are greater than {threshold}.")

# question_5()

def question_6():
    input_file = input("please enter the input file name: ")
    output_file = input("please enter the output file name: ")
    search_string = input("Enter the search string: ")
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        for line in input_file:
            if search_string in line:
                output_file.write(line)
    print(f'Lines containing {search_string} from {input_file} written to {output_file}')

# question_6()