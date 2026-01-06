import fitz  # PyMuPDF
import argparse
import sys
from pathlib import Path

def add_right_margin_to_pdf(input_file, output_file, margin_pixels):
    """
    Adds white space to the right side of every page in a PDF.
    
    Args:
        input_file (str): Path to the input PDF file
        output_file (str): Path for the output PDF file
        margin_pixels (int): Width in pixels/points to add to the right
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Validate input file exists
        if not Path(input_file).exists():
            print(f"Error: Input file '{input_file}' not found.")
            return False
        
        # Open the original PDF
        print(f"Opening '{input_file}'...")
        doc = fitz.open(input_file)
        
        if len(doc) == 0:
            print("Error: PDF contains no pages.")
            return False
        
        # Create a new PDF for the output
        new_doc = fitz.open()
        
        print(f"Processing {len(doc)} page(s)...")
        
        # Iterate through every page
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            
            # Get original dimensions
            original_width = page.rect.width
            original_height = page.rect.height
            
            # Calculate new width (adding to the right)
            new_width = original_width + margin_pixels
            
            # Create a new page with increased width
            new_page = new_doc.new_page(width=new_width, height=original_height)
            
            # Define the rectangle where original content will be placed (left-aligned)
            target_rect = fitz.Rect(0, 0, original_width, original_height)
            
            # Draw the original page content onto the new page (left-aligned)
            # The remaining space on the right will be white
            new_page.show_pdf_page(target_rect, doc, page_number)
            
            if (page_number + 1) % 10 == 0:
                print(f"  Processed {page_number + 1} pages...")
        
        # Save the new PDF
        print(f"Saving output to '{output_file}'...")
        new_doc.save(output_file)
        new_doc.close()
        doc.close()
        
        print(f"✓ Success! PDF resized with {margin_pixels}px right margin.")
        print(f"  Original width: ~{original_width:.0f}px")
        print(f"  New width: ~{new_width:.0f}px")
        return True
        
    except Exception as e:
        print(f"✗ Error occurred: {str(e)}")
        return False

def calculate_percentage_margin(base_width, percentage):
    """
    Helper function to calculate margin based on percentage of page width.
    
    Args:
        base_width (int): Original page width
        percentage (float): Percentage of width to add (e.g., 30 for 30%)
    
    Returns:
        int: Calculated margin in pixels
    """
    return int(base_width * (percentage / 100))

def main():
    parser = argparse.ArgumentParser(
        description='Add right margin to PDF pages for MLR annotation space.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Add 375px margin to the right
  python pdf_margin_tool.py input.pdf output.pdf 375
  
  # Add 30% margin (relative to page width)
  python pdf_margin_tool.py input.pdf output.pdf 30 --percentage
  
  # Use default 30% margin for TPP/SPP submissions
  python pdf_margin_tool.py input.pdf output.pdf --default-tpp
        """
    )
    
    parser.add_argument('input_file', help='Input PDF file path')
    parser.add_argument('output_file', help='Output PDF file path')
    parser.add_argument('margin', nargs='?', type=float, default=None,
                       help='Margin size in pixels (or percentage if --percentage flag used)')
    parser.add_argument('--percentage', '-p', action='store_true',
                       help='Treat margin value as percentage of page width')
    parser.add_argument('--default-tpp', '-d', action='store_true',
                       help='Use default 30%% margin for TPP/SPP submissions')
    
    args = parser.parse_args()
    
    # Determine margin value
    if args.default_tpp:
        # For TPP/SPP: assuming 1440px base width, 30% = ~432px
        # But we'll calculate dynamically based on actual page width
        print("Using default TPP/SPP margin (30% of page width)...")
        doc = fitz.open(args.input_file)
        first_page_width = doc[0].rect.width
        doc.close()
        margin_pixels = calculate_percentage_margin(first_page_width, 30)
        print(f"Calculated margin: {margin_pixels}px (30% of {first_page_width:.0f}px)")
    elif args.margin is None:
        print("Error: Please specify margin value or use --default-tpp flag")
        parser.print_help()
        sys.exit(1)
    elif args.percentage:
        doc = fitz.open(args.input_file)
        first_page_width = doc[0].rect.width
        doc.close()
        margin_pixels = calculate_percentage_margin(first_page_width, args.margin)
        print(f"Calculated margin: {margin_pixels}px ({args.margin}% of {first_page_width:.0f}px)")
    else:
        margin_pixels = int(args.margin)
    
    # Execute the transformation
    success = add_right_margin_to_pdf(args.input_file, args.output_file, margin_pixels)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()