import sys

def parse_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.strip().split()
            for word in words:
                outfile.write(f"__Label__{word} {word}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    parse_file(input_file, output_file)
    print(f"Parsing complete. Results written to {output_file}")