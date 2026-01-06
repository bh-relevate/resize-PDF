import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading

class PDFMarginToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Margin Tool - MLR Submission Prep")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # Variables
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.margin_type = tk.StringVar(value="tpp_default")
        self.custom_value = tk.StringVar(value="375")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="PDF Margin Tool", 
                               font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        subtitle_label = ttk.Label(main_frame, text="Add annotation space for MLR submissions", 
                                   font=('Helvetica', 9))
        subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # Input File Section
        ttk.Label(main_frame, text="Input PDF:", font=('Helvetica', 10, 'bold')).grid(
            row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        ttk.Entry(main_frame, textvariable=self.input_file, width=50, state='readonly').grid(
            row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Button(main_frame, text="Browse...", command=self.browse_input).grid(
            row=3, column=2, padx=(5, 0), pady=(0, 5))
        
        # Output File Section
        ttk.Label(main_frame, text="Save As:", font=('Helvetica', 10, 'bold')).grid(
            row=4, column=0, sticky=tk.W, pady=(15, 5))
        
        ttk.Entry(main_frame, textvariable=self.output_file, width=50, state='readonly').grid(
            row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 5))
        
        ttk.Button(main_frame, text="Browse...", command=self.browse_output).grid(
            row=5, column=2, padx=(5, 0), pady=(0, 5))
        
        # Margin Settings Section
        ttk.Label(main_frame, text="Margin Settings:", font=('Helvetica', 10, 'bold')).grid(
            row=6, column=0, sticky=tk.W, pady=(15, 10))
        
        # Radio buttons for margin type
        radio_frame = ttk.Frame(main_frame)
        radio_frame.grid(row=7, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
        
        ttk.Radiobutton(radio_frame, text="TPP/SPP Default (30% of page width)", 
                       variable=self.margin_type, value="tpp_default",
                       command=self.update_custom_state).pack(anchor=tk.W, pady=2)
        
        ttk.Radiobutton(radio_frame, text="Custom pixels:", 
                       variable=self.margin_type, value="custom_pixels",
                       command=self.update_custom_state).pack(anchor=tk.W, pady=2)
        
        ttk.Radiobutton(radio_frame, text="Custom percentage:", 
                       variable=self.margin_type, value="custom_percentage",
                       command=self.update_custom_state).pack(anchor=tk.W, pady=2)
        
        # Custom value entry
        custom_frame = ttk.Frame(main_frame)
        custom_frame.grid(row=8, column=0, columnspan=3, sticky=tk.W, padx=(20, 0))
        
        self.custom_entry = ttk.Entry(custom_frame, textvariable=self.custom_value, width=15)
        self.custom_entry.pack(side=tk.LEFT, padx=(0, 5))
        self.custom_entry.config(state='disabled')
        
        self.custom_label = ttk.Label(custom_frame, text="px")
        self.custom_label.pack(side=tk.LEFT)
        
        # Process Button
        self.process_btn = ttk.Button(main_frame, text="Process PDF", 
                                      command=self.process_pdf, style='Accent.TButton')
        self.process_btn.grid(row=9, column=0, columnspan=3, pady=(20, 10), 
                             sticky=(tk.W, tk.E))
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=10, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready to process", 
                                     font=('Helvetica', 9))
        self.status_label.grid(row=11, column=0, columnspan=3)
        
        # Info section
        info_frame = ttk.LabelFrame(main_frame, text="Quick Guide", padding="10")
        info_frame.grid(row=12, column=0, columnspan=3, pady=(15, 0), sticky=(tk.W, tk.E))
        
        info_text = """1. Select your PDF screenshot file
2. Choose where to save the processed file
3. Select margin setting (TPP/SPP Default recommended)
4. Click 'Process PDF' to add annotation space"""
        
        ttk.Label(info_frame, text=info_text, justify=tk.LEFT, 
                 font=('Helvetica', 8)).pack(anchor=tk.W)
        
    def update_custom_state(self):
        """Enable/disable custom entry based on selection"""
        if self.margin_type.get() in ["custom_pixels", "custom_percentage"]:
            self.custom_entry.config(state='normal')
            if self.margin_type.get() == "custom_percentage":
                self.custom_label.config(text="%")
            else:
                self.custom_label.config(text="px")
        else:
            self.custom_entry.config(state='disabled')
    
    def browse_input(self):
        """Open file dialog for input file"""
        filename = filedialog.askopenfilename(
            title="Select PDF to Process",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.input_file.set(filename)
            # Auto-suggest output filename
            if not self.output_file.get():
                input_path = Path(filename)
                suggested_output = input_path.parent / f"{input_path.stem}_annotated{input_path.suffix}"
                self.output_file.set(str(suggested_output))
    
    def browse_output(self):
        """Open file dialog for output file"""
        initial_file = "output.pdf"
        if self.input_file.get():
            input_path = Path(self.input_file.get())
            initial_file = f"{input_path.stem}_annotated{input_path.suffix}"
            
        filename = filedialog.asksaveasfilename(
            title="Save Processed PDF As",
            initialfile=initial_file,
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.output_file.set(filename)
    
    def calculate_margin(self, page_width):
        """Calculate margin based on selected type"""
        margin_type = self.margin_type.get()
        
        if margin_type == "tpp_default":
            # 30% of page width
            return int(page_width * 0.3)
        elif margin_type == "custom_pixels":
            try:
                return int(float(self.custom_value.get()))
            except ValueError:
                raise ValueError("Please enter a valid number for pixels")
        elif margin_type == "custom_percentage":
            try:
                percentage = float(self.custom_value.get())
                if percentage < 0 or percentage > 100:
                    raise ValueError("Percentage must be between 0 and 100")
                return int(page_width * (percentage / 100))
            except ValueError:
                raise ValueError("Please enter a valid percentage (0-100)")
        
        return 0
    
    def add_margin_to_pdf(self, input_file, output_file, margin_pixels):
        """Process the PDF with margin"""
        try:
            doc = fitz.open(input_file)
            new_doc = fitz.open()
            
            total_pages = len(doc)
            
            for page_number in range(total_pages):
                page = doc.load_page(page_number)
                original_width = page.rect.width
                original_height = page.rect.height
                new_width = original_width + margin_pixels
                
                new_page = new_doc.new_page(width=new_width, height=original_height)
                target_rect = fitz.Rect(0, 0, original_width, original_height)
                new_page.show_pdf_page(target_rect, doc, page_number)
                
                # Update status periodically
                if page_number % 5 == 0:
                    self.status_label.config(
                        text=f"Processing page {page_number + 1} of {total_pages}..."
                    )
                    self.root.update()
            
            new_doc.save(output_file)
            new_doc.close()
            doc.close()
            
            return True, total_pages, margin_pixels
            
        except Exception as e:
            return False, str(e), 0
    
    def process_pdf_thread(self):
        """Process PDF in separate thread to keep UI responsive"""
        try:
            # Validation
            if not self.input_file.get():
                messagebox.showerror("Error", "Please select an input PDF file")
                return
            
            if not self.output_file.get():
                messagebox.showerror("Error", "Please select an output location")
                return
            
            if not Path(self.input_file.get()).exists():
                messagebox.showerror("Error", "Input file does not exist")
                return
            
            # Calculate margin
            doc = fitz.open(self.input_file.get())
            first_page_width = doc[0].rect.width
            doc.close()
            
            try:
                margin_pixels = self.calculate_margin(first_page_width)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return
            
            # Update UI
            self.process_btn.config(state='disabled')
            self.progress.start(10)
            self.status_label.config(text="Processing PDF...")
            
            # Process
            success, result, actual_margin = self.add_margin_to_pdf(
                self.input_file.get(),
                self.output_file.get(),
                margin_pixels
            )
            
            # Stop progress
            self.progress.stop()
            self.process_btn.config(state='normal')
            
            if success:
                total_pages = result
                self.status_label.config(text="✓ Processing complete!")
                messagebox.showinfo(
                    "Success",
                    f"PDF processed successfully!\n\n"
                    f"Pages processed: {total_pages}\n"
                    f"Right margin added: {actual_margin}px\n"
                    f"New width: {first_page_width + actual_margin:.0f}px\n\n"
                    f"Saved to:\n{self.output_file.get()}"
                )
            else:
                error_msg = result
                self.status_label.config(text="✗ Processing failed")
                messagebox.showerror("Error", f"Failed to process PDF:\n{error_msg}")
                
        except Exception as e:
            self.progress.stop()
            self.process_btn.config(state='normal')
            self.status_label.config(text="✗ Error occurred")
            messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")
    
    def process_pdf(self):
        """Start processing in a separate thread"""
        thread = threading.Thread(target=self.process_pdf_thread)
        thread.daemon = True
        thread.start()

def main():
    root = tk.Tk()
    app = PDFMarginToolGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()