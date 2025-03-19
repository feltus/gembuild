#gem_histogram.py

#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate histogram of gene expression values for specific genes')
    parser.add_argument('--expression_file', '-e', required=True, help='Gene expression matrix file path')
    parser.add_argument('--gene_list_file', '-g', required=True, help='File containing genes of interest')
    parser.add_argument('--output', '-o', default='gene_expression_histogram.png', help='Output histogram file path')
    parser.add_argument('--bins', '-b', type=int, default=50, help='Number of bins for histogram')
    parser.add_argument('--log_scale', '-l', action='store_true', help='Use log scale for expression values')
    return parser.parse_args()

def read_gene_list(file_path):
    """Read gene list file and return list of genes (skipping first element)"""
    with open(file_path, 'r') as f:
        line = f.readline().strip()
        genes = line.split('\t')[1:]  # Skip first element
    return genes

def read_expression_matrix(file_path):
    """Read gene expression matrix file and return header and data"""
    with open(file_path, 'r') as f:
        header = f.readline().strip().split('\t')
        data = []
        for line in f:
            data.append(line.strip().split('\t'))
    return header, data

def main():
    args = parse_arguments()
    
    # Read gene list (skip first element)
    target_genes = read_gene_list(args.gene_list_file)
    print(f"Found {len(target_genes)} target genes")
    
    # Read expression matrix
    header, expression_data = read_expression_matrix(args.expression_file)
    print(f"Expression matrix has {len(header)} columns and {len(expression_data)} rows")
    
    # Find indices of target genes in header
    gene_indices = []
    found_genes = []
    for gene in target_genes:
        if gene in header:
            gene_indices.append(header.index(gene))
            found_genes.append(gene)
    
    print(f"Found {len(found_genes)} of {len(target_genes)} genes in expression matrix")
    
    if len(found_genes) == 0:
        print("No target genes found in expression matrix. Exiting.")
        return
    
    # Extract expression values for target genes
    all_values = []
    for row in expression_data:
        for idx in gene_indices:
            try:
                value = float(row[idx])
                if value > 0:  # Only include positive values
                    all_values.append(value)
            except (IndexError, ValueError):
                pass
    
    print(f"Extracted {len(all_values)} expression values")
    
    if len(all_values) == 0:
        print("No valid expression values found. Exiting.")
        return
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    
    if args.log_scale:
        all_values = [np.log10(x) for x in all_values if x > 0]
        plt.hist(all_values, bins=args.bins)
        plt.xlabel('Log10 Gene Expression')
        plt.title(f'Histogram of Log10 Gene Expression Values for {len(found_genes)} Genes')
    else:
        plt.hist(all_values, bins=args.bins)
        plt.xlabel('Gene Expression')
        plt.title(f'Histogram of Gene Expression Values for {len(found_genes)} Genes')
    
    plt.ylabel('Frequency')
    plt.grid(alpha=0.3)
    
    # Add summary statistics to plot
    stats_text = f"n = {len(all_values)}\n"
    stats_text += f"Mean: {np.mean(all_values):.2f}\n"
    stats_text += f"Median: {np.median(all_values):.2f}\n"
    stats_text += f"Min: {min(all_values):.2f}\n"
    stats_text += f"Max: {max(all_values):.2f}\n"
    stats_text += f"SD: {np.std(all_values):.2f}"
    
    plt.figtext(0.75, 0.70, stats_text, bbox=dict(facecolor='white', alpha=0.5))
    
    # Save the plot
    plt.savefig(args.output, dpi=300)
    print(f"Histogram saved to {args.output}")
    
    # Show the genes found
    print("\nGenes found in expression matrix:")
    for gene in found_genes:
        print(f"- {gene}")

if __name__ == "__main__":
    main()
