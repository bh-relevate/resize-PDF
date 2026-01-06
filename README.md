# PDF Margin Tool - User Guide

## Overview

The PDF Margin Tool automates the process of adding right-side annotation space to PDF screenshots for MLR/Regulatory submission. This tool eliminates the manual work of resizing PDFs and ensures consistent margins across all submission materials.

**What it does:** Adds white space to the right side of your PDF pages, creating room for account team annotations during the review process.

---

## Installation

### First-Time Setup (Mac)

1. **Download the tool:**
   - Locate `PDF Margin Tool` application in your SharePoint project folder or shared drive
   - Copy it to your computer (suggested location: Applications folder or Desktop)

2. **First launch:**
   - Right-click (or Control + click) on `PDF Margin Tool`
   - Select **"Open"** from the menu
   - Click **"Open"** in the security dialog that appears
   - ⚠️ This step is only needed the first time you run the tool

3. **Subsequent launches:**
   - Simply double-click `PDF Margin Tool` to open

---

## How to Use

### Step 1: Select Your Input PDF
1. Click the **"Browse..."** button next to "Input PDF"
2. Navigate to your screenshot PDF file
3. Select the file and click **"Open"**

### Step 2: Choose Save Location
1. Click the **"Browse..."** button next to "Save As"
2. Choose where to save your processed file
3. The tool automatically suggests a filename with "_annotated" suffix
4. Click **"Save"**

### Step 3: Select Margin Settings

Choose one of three options:

#### **TPP/SPP Default (Recommended)**
- Automatically adds 30% margin (right-aligned annotation space)
- Follows standard TPP/SPP submission guidelines
- **Use this for standard projects**

#### **Custom Pixels**
- Enter a specific pixel width (e.g., `375`)
- Use when you have exact dimension requirements
- Common values: 300-500px

#### **Custom Percentage**
- Enter a percentage of the page width (e.g., `25`)
- Useful for maintaining proportional margins across different page sizes
- Valid range: 0-100%

### Step 4: Process
1. Click **"Process PDF"**
2. Wait for the progress bar to complete
3. A success message will display the details of your processed file

---

## Use Cases & Examples

### Standard TPP/SPP Submission
**Scenario:** Desktop screenshots for regulatory review  
**Settings:** TPP/SPP Default (30%)  
**Result:** ~432px margin on 1440px pages

### Custom Client Requirements
**Scenario:** Client requests specific margin width  
**Settings:** Custom Pixels - enter exact width  
**Result:** Exact pixel margin as specified

### Mobile Screenshots
**Scenario:** 390px mobile screenshots need annotation space  
**Settings:** TPP/SPP Default OR Custom Percentage (30%)  
**Result:** ~117px margin maintaining proportion

---

## Tips & Best Practices

✓ **Use TPP/SPP Default** for standard submissions (matches the 70/30 layout guideline)

✓ **Keep original files** - The tool creates a new file and doesn't modify your original

✓ **Naming convention** - Tool auto-adds "_annotated" to filenames for easy identification

✓ **Batch processing** - Process one file at a time, but you can queue multiple files by repeating the process

✓ **File organization** - Organize processed files in a "MLR_Ready" folder for easy SharePoint upload

---

## Troubleshooting

### Tool won't open
**Issue:** "PDF Margin Tool can't be opened because it is from an unidentified developer"  
**Solution:** Right-click the app → Select "Open" → Click "Open" in the dialog

### Invalid number error
**Issue:** Error message when processing  
**Solution:** Ensure custom values are numbers only (no letters or special characters)

### File not found
**Issue:** Input file can't be located  
**Solution:** Verify the PDF file still exists in the selected location

### Processing fails
**Issue:** Error during processing  
**Solution:** 
- Ensure the input PDF is not corrupted
- Check that you have write permissions for the output location
- Try a different output location

### Application freezes
**Issue:** Tool becomes unresponsive during processing  
**Solution:** Wait - large PDFs (50+ pages) may take 30-60 seconds to process

---

## Technical Details

**Supported formats:** PDF only  
**Input requirements:** Valid PDF file (any size)  
**Output format:** PDF (same quality as input)  
**Page orientation:** Works with portrait and landscape  
**File size:** No limit, but larger files take longer to process

---

## Workflow Integration

### Recommended Process:

1. **Capture screenshots** using GoFullPage or standard tools
2. **Combine into PDF** (if multiple screenshots)
3. **Run PDF Margin Tool** to add annotation space
4. **Review output** to ensure proper margins
5. **Upload to SharePoint** project folder
6. **Submit for MLR review**

### Folder Structure:
Project_Folder/
├── original_screenshots/
│   └── homepage_desktop.pdf
├── mlr_ready/
│   └── homepage_desktop_annotated.pdf
└── PDF Margin Tool (application)

---

## Support & Feedback

**Questions or issues?**  
Contact: [Your Name] - [Your Email]

**Feature requests:**  
We're continuously improving this tool. Suggestions for automation or additional features are welcome!

**AI Center of Excellence:**  
This tool is part of Relevate Health's AI COE initiative to streamline repetitive tasks and improve workflow efficiency.

---

## Version History

**v1.0** - Initial release
- TPP/SPP default margins (30%)
- Custom pixel margins
- Custom percentage margins
- Progress indicator
- Auto-suggested filenames

---

## Frequently Asked Questions

**Q: Can I process multiple PDFs at once?**  
A: Currently, the tool processes one PDF at a time. Batch processing may be added in future versions.

**Q: Does this modify my original PDF?**  
A: No, the tool creates a new file. Your original remains unchanged.

**Q: What happens to the PDF quality?**  
A: Quality is preserved. The tool doesn't compress or reduce resolution.

**Q: Can I use this for tablet screenshots?**  
A: Yes! Use TPP/SPP Default or Custom Percentage for proportional margins.

**Q: Will this work on Windows?**  
A: The current version is Mac-only. Contact support if you need a Windows version.

**Q: Can I undo the margin addition?**  
A: No, but you can always reprocess your original file with different settings.

---

**Last Updated:** [2026.01.06]  
**Maintained by:** UX & Studio Design Team  
**Part of:** AI Center of Excellence Initiative