import os

file_path = r'c:\Users\siddh\Desktop\Redesign\Jwellery\style.css'

# CSS to append
new_css = """
/* --- MOBILE SPECIFIC UTILITIES --- */
.mobile-only-item {
  display: none;
}

@media (max-width: 768px) {
  .mobile-only-item {
    display: block;
    width: 100%;
    margin-top: 10px;
  }
  .mobile-only-item a {
     font-weight: 700;
     color: var(--color-accent);
  }
}

@media (max-width: 480px) {
  .header-right {
    gap: 8px;
  }
  .header-logo {
    font-size: 18px;
  }
  
  /* 2-Column Feature Grid Fix */
  .feature-grid {
    gap: 15px;
    justify-content: center;
  }
  .feature-item {
    flex: 0 0 calc(50% - 15px) !important;
    min-width: auto !important;
    margin-bottom: 20px;
  }
}
"""

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Truncate at line 1451 (keep 1451 lines). 
# Note: The file might have extra lines due to the corruption, so we just take the first 1451.
# 1-indexed line 1451 is index 1450. One more included means slicing up to 1451.
valid_lines = lines[:1451]

# Double check the last line is the closing brace
print(f"Last valid line content: {valid_lines[-1]}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(valid_lines)
    f.write("\n")
    f.write(new_css)

print("Fixed style.css")
