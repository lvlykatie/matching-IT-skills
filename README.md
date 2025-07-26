# Course Skills Analysis Project

This project processes and analyzes course data with skills information using fuzzy string matching techniques to standardize and categorize skills across different courses.

## 📁 Project Structure

```
├── README.md                           # This file
├── raw-data.xlsx                       # Original raw course data
├── courses_flattened.xlsx              # Processed course data (flattened)
├── format-rows.ipynb                   # Data preprocessing notebook
└── fuzzy/
    ├── rapidfuzz.ipynb                 # Fuzzy matching analysis notebook
    └── courses_with_matched_skills.xlsx # Output with matched skills
```

## 🎯 Project Overview

This project consists of two main phases:

1. **Data Preprocessing**: Flattens and cleans raw course data from Excel
2. **Skills Analysis**: Uses fuzzy string matching to standardize and categorize skills

## 📊 Data Files

- **`raw-data.xlsx`**: Original course data with merged cells and multiple rows per course
- **`courses_flattened.xlsx`**: Cleaned data with one row per course and consolidated skills
- **`courses_with_matched_skills.xlsx`**: Final output with standardized skills and matching statistics

## 🔧 Setup and Dependencies

### Required Python Packages

```bash
pip install pandas
pip install openpyxl
pip install rapidfuzz
pip install jupyter
```

### Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure all Excel files are in the correct locations

## 📝 Usage Instructions

### Step 1: Data Preprocessing

Run the `format-rows.ipynb` notebook to process the raw data:

```python
# This notebook will:
# 1. Read raw-data.xlsx
# 2. Fill merged cells
# 3. Group by course and consolidate skills
# 4. Output courses_flattened.xlsx
```

### Step 2: Skills Analysis

Run the `fuzzy/rapidfuzz.ipynb` notebook to perform fuzzy matching:

```python
# This notebook will:
# 1. Load processed course data
# 2. Extract and clean unique skills
# 3. Apply fuzzy string matching
# 4. Calculate matching statistics
# 5. Output courses_with_matched_skills.xlsx
```

## 🔍 Key Features

### Data Preprocessing (`format-rows.ipynb`)

- Handles merged cells in Excel data
- Groups multiple rows per course into single entries
- Consolidates skills and course descriptions
- Outputs clean, flattened dataset

### Fuzzy Matching (`rapidfuzz.ipynb`)

- **Skill Standardization**: Uses fuzzy string matching to standardize skill names
- **Matching Functions**:
  - `match_skills()`: Matches raw skills to standard skills
  - `average_matching_score()`: Calculates average matching confidence
  - `matching_stats()`: Provides matching statistics
- **Quality Metrics**:
  - Precision, Recall, and F1 Score
  - Average matching score
  - Match rate percentage

## 📈 Output Analysis

The final output includes:

- **Original Skills**: Raw skill data from courses
- **Matched Skills**: Standardized skill names
- **Matching Score**: Confidence level of each match (0-100)
- **Match Rate**: Percentage of successfully matched skills
- **Statistics**: Overall matching performance metrics

## 🎛️ Configuration

### Fuzzy Matching Threshold

Default threshold is 80% - skills below this confidence level are marked as "[Unmatched]"

```python
# Adjust threshold in the notebook
threshold = 80  # Change this value as needed
```

### Skill Filtering

Skills are filtered based on:

- Length (minimum 3 characters)
- Word count (maximum 5 words)
- Special character removal

## 📋 Data Schema

### Input Schema (`raw-data.xlsx`)

- `STT`: Course number
- `Mã MH`: Course code
- `Tên MH`: Course name
- `Tóm tắt môn học`: Course description
- `Skill`: Skills (comma-separated)

### Output Schema (`courses_with_matched_skills.xlsx`)

- All original fields
- `Matched_Skills`: Standardized skill names
- `Matching_Score`: Average confidence score
- `Matched_Count`: Number of successfully matched skills
- `Total_Skills`: Total number of skills
- `Match_Rate(%)`: Percentage of matched skills

## 🚀 Quick Start

1. **Prepare Data**: Ensure `raw-data.xlsx` is in the root directory
2. **Run Preprocessing**: Execute `format-rows.ipynb`
3. **Run Analysis**: Execute `fuzzy/rapidfuzz.ipynb`
4. **Review Results**: Check `fuzzy/courses_with_matched_skills.xlsx`

## 🔧 Troubleshooting

### Common Issues

- **File Not Found**: Ensure all Excel files are in the correct directories
- **Path Issues**: The fuzzy matching notebook uses relative paths (`../courses_flattened.xlsx`)
- **Memory Issues**: For large datasets, consider processing in chunks

### Performance Tips

- Adjust the fuzzy matching threshold based on your data quality
- Consider preprocessing skills to remove common variations
- Use batch processing for large datasets

## 📊 Example Output

```
## 📊 Đánh giá độ chính xác fuzzy matching

- **Tổng kỹ năng**: 1500
- **Tổng kỹ năng match được**: 1350
- **Precision (approx)**: 90.00%
- **Recall (approx)**: 90.00%
- **F1 Score (approx)**: 90.00%
- **Điểm fuzzy trung bình**: 85.5/100
```

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

For questions or issues, please:

1. Check the troubleshooting section
2. Review the notebook comments (in Vietnamese)
3. Create an issue with detailed error information

---

**Note**: This project includes Vietnamese comments in the notebooks. The main functionality is language-agnostic and can be adapted for other languages.
