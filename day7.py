def removeCarriage(line):
    return line.strip('\n')

def run1():
    f = open("day7.txt", "r")  
    bag_type = ["shiny gold bags", "shiny gold bag"]
    previous_check = 0
    while (True):
        for line in f:
            line = removeCarriage(line)
            found = any(bag in line for bag in bag_type)
            if found and line.split("bags")[0]+'bag' not in bag_type: 
                bag_type += [line.split("bags")[0] + 'bag', line.split("bags")[0] + 'bags']
        f.seek(0) 
        if previous_check != len(bag_type)/2 - 1: previous_check = len(bag_type)/2 - 1
        else: break
    print(len(bag_type)/2 - 1)
    f.close()

def count_bags_in_tree(tree, start, number_of_parents):
    total_count = 0
    for bag in tree[start]:
        if bag[0] == '0':
            return 1
        total_count += 1 + int(bag[1]) * int(count_bags_in_tree(tree, bag[0], bag[1]))
    return total_count

def run2():
    f = open("day7.txt", "r")  
    bag_dictionary = {}
    previous_check = 0
    while (True):
        for line in f:
            line = removeCarriage(line)
            if 'no' in line:
                bag_dictionary[line.split('bags')[0] + 'bag'] = [('0', '0')]
                bag_dictionary[line.split('bags')[0] + 'bags'] = [('0', '0')]
                continue
            # Add values to the dictionary
            parent_bag = line.split('bags')[0]
            bag_dictionary[parent_bag + 'bag'] = []
            bag_dictionary[parent_bag + 'bags'] = []
            # Split each section
            list_of_bags = line.split('contain')[1].split(',')
            for bag in list_of_bags:
                bag_attributes = bag.split(' ')
                bag_dictionary[parent_bag + 'bag'] += [(bag_attributes[2] + ' ' + bag_attributes[3] + ' bag', bag_attributes[1])]
                bag_dictionary[parent_bag + 'bags'] += [(bag_attributes[2] + ' ' + bag_attributes[3] + ' bag', bag_attributes[1])]
        if previous_check != len(bag_dictionary.keys()): previous_check = len(bag_dictionary.keys())
        else: break
    print(count_bags_in_tree(bag_dictionary, 'shiny gold bag', 1))


def main():
    #run1()
    run2()

if __name__ == "__main__":
    main()