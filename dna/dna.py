import csv
import sys


def main():
    #list to store dna sequence
    dna = []

    #Check for command-line usage
    if len(sys.argv)!=3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
    #Read database file into a variable
    file = sys.argv[1]
    with open(file, 'r') as db:
        reader = csv.DictReader(db)
        for row in reader:
            dna.append(row) #list of dicts
    #Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as seq:
        sequence = seq.read()
    #get list of STRs
    subseq = list(dna[0].keys())[1: ]
    #dict for storing frequency of each str
    results={}
    #Find longest match of each STR in DNA sequence
    for str in subseq:
        results[str] = longest_match(sequence, str)

    #Check database for matching profiles
    for person in dna:
        match = 0
        for str in subseq:
            if int(person[str]) == results[str]:
                match +=1
        if match == len(subseq):
            return print(person['name'])
    print('no match')
    return 0



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
