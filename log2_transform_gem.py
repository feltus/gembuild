#!/usr/bin/env python3

import numpy as np
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description='Transform gene expression matrix to log2 scale')
    parser.add_argument('--input', '-i', help='Input gene expression matrix file (default: stdin)')
    parser.add_argument('--output', '-o', help='Output file for transformed matrix (default: stdout)')
    parser.add_argument('--pseudocount', '-p', type=float, default=0.01, 
                        help='Pseudocount added before log transformation to handle zeros (default: 0.01)')
    return parser.parse_args()

def log2_transform_matrix(input_file, output_file, pseudocount=1.0):
    """
    Read gene expression matrix, apply log2 transformation, and write output
    
    Args:
        input_file: File handle for input matrix
        output_file: File handle for output matrix
        pseudocount: Value to add to expression values before log transformation
    """
    # Read header line
    header = input_file.readline().strip()
    output_file.write(header + '\n')
    
    # Process each sample line
    for line in input_file:
        line = line.strip()
        if not line:
            continue
            
        fields = line.split('\t')
        sample_id = fields[0]
        expression_values = fields[1:]
        
        # Apply log2 transformation to each expression value
        transformed_values = []
        for value in expression_values:
            try:
                # Convert to float, add pseudocount, and transform
                expr = float(value)
                log2_expr = np.log2(expr + pseudocount)
                transformed_values.append(f"{log2_expr:.6f}")
            except ValueError:
                # Handle any non-numeric values by keeping them unchanged
                transformed_values.append(value)
        
        # Write transformed line to output
        output_line = sample_id + '\t' + '\t'.join(transformed_values)
        output_file.write(output_line + '\n')

def main():
    args = parse_arguments()
    
    # Set up input file
    if args.input:
        try:
            input_file = open(args.input, 'r')
        except IOError:
            print(f"Error: Could not open input file '{args.input}'", file=sys.stderr)
            sys.exit(1)
    else:
        input_file = sys.stdin
    
    # Set up output file
    if args.output:
        try:
            output_file = open(args.output, 'w')
        except IOError:
            print(f"Error: Could not open output file '{args.output}'", file=sys.stderr)
            if args.input and input_file != sys.stdin:
                input_file.close()
            sys.exit(1)
    else:
        output_file = sys.stdout
    
    # Process the matrix
    try:
        log2_transform_matrix(input_file, output_file, args.pseudocount)
    except Exception as e:
        print(f"Error processing matrix: {e}", file=sys.stderr)
    finally:
        # Close files if they're not stdin/stdout
        if args.input and input_file != sys.stdin:
            input_file.close()
        if args.output and output_file != sys.stdout:
            output_file.close()

if __name__ == "__main__":
    main()
