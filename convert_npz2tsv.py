#!/usr/bin/env python3

import numpy as np
import argparse
import os
import sys

def convert_npz_to_tsv(npz_file, output_dir=None, prefix=None):
    """
    Convert NumPy NPZ file(s) to TSV format
    
    Parameters:
    -----------
    npz_file : str
        Path to the NPZ file
    output_dir : str, optional
        Directory to save the TSV files, defaults to same directory as NPZ
    prefix : str, optional
        Prefix to add to the output filenames
    """
    try:
        # Load the NPZ file
        data = np.load(npz_file, allow_pickle=True)
        
        # Create output directory if specified and doesn't exist
        if output_dir is not None:
            os.makedirs(output_dir, exist_ok=True)
        else:
            output_dir = os.path.dirname(npz_file) or '.'
            
        # Set prefix if not specified
        if prefix is None:
            prefix = os.path.splitext(os.path.basename(npz_file))[0]
            
        print(f"Converting {npz_file}...")
        print(f"Found {len(data.files)} arrays: {', '.join(data.files)}")
        
        # Process each array in the NPZ file
        for i, array_name in enumerate(data.files):
            array = data[array_name]
            
            # Handle different array shapes
            if len(array.shape) == 0:  # Scalar
                print(f"Warning: Array '{array_name}' is scalar. Saving as single value.")
                with open(f"{output_dir}/{prefix}_{array_name}.tsv", 'w') as f:
                    f.write(str(array.item()))
                    
            elif len(array.shape) == 1:  # 1D array
                print(f"Converting 1D array '{array_name}' (length: {array.shape[0]})")
                np.savetxt(
                    f"{output_dir}/{prefix}_{array_name}.tsv",
                    array.reshape(-1, 1),
                    delimiter='\t',
                    fmt='%s'
                )
                
            else:  # 2D+ array
                print(f"Converting array '{array_name}' (shape: {array.shape})")
                if len(array.shape) > 2:
                    print(f"Warning: Array '{array_name}' has >2 dimensions. Flattening to 2D.")
                    # Flatten all but the first dimension
                    reshaped = array.reshape(array.shape[0], -1)
                    np.savetxt(
                        f"{output_dir}/{prefix}_{array_name}.tsv",
                        reshaped,
                        delimiter='\t',
                        fmt='%s'
                    )
                else:
                    np.savetxt(
                        f"{output_dir}/{prefix}_{array_name}.tsv",
                        array,
                        delimiter='\t',
                        fmt='%s'
                    )
                    
            print(f"Saved as {output_dir}/{prefix}_{array_name}.tsv")
            
        print(f"Conversion completed: {len(data.files)} arrays saved to TSV files.")
        return True
            
    except Exception as e:
        print(f"Error converting {npz_file}: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description='Convert NPZ files to TSV format')
    parser.add_argument('npz_files', nargs='+', help='NPZ file(s) to convert')
    parser.add_argument('-o', '--output-dir', help='Directory to save TSV files')
    parser.add_argument('-p', '--prefix', help='Prefix for output filenames')
    parser.add_argument('-r', '--recursive', action='store_true', help='Process directories recursively')
    
    args = parser.parse_args()
    
    # Process each input NPZ file
    success = 0
    failed = 0
    
    for npz_path in args.npz_files:
        if os.path.isdir(npz_path) and args.recursive:
            # If input is a directory and recursive flag is set
            for root, dirs, files in os.walk(npz_path):
                for file in files:
                    if file.endswith('.npz'):
                        file_path = os.path.join(root, file)
                        if convert_npz_to_tsv(file_path, args.output_dir, args.prefix):
                            success += 1
                        else:
                            failed += 1
        elif os.path.isfile(npz_path) and npz_path.endswith('.npz'):
            # If input is a file and has .npz extension
            if convert_npz_to_tsv(npz_path, args.output_dir, args.prefix):
                success += 1
            else:
                failed += 1
        else:
            if os.path.isdir(npz_path) and not args.recursive:
                print(f"Warning: {npz_path} is a directory. Use -r/--recursive to process directories.")
            elif not npz_path.endswith('.npz'):
                print(f"Warning: {npz_path} is not an NPZ file. Skipping.")
            else:
                print(f"Warning: {npz_path} does not exist or cannot be accessed.")
            failed += 1
    
    print(f"\nSummary: {success} files converted successfully, {failed} files failed or skipped.")
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    main()
