from sem_pipeline import df, semantic_match
import pandas as pd

rows = []

for i, row in df.iterrows():
    text = row["Skill"]
    if not isinstance(text, str) or not text.strip():
        continue
    matched, count, total, rate, avg = semantic_match(text)
    rows.append({
        "Tên MH": row["Tên MH"],
        "Original Skill": text,
        "Matched Skills": matched,
        "Matched Count": count,
        "Total Skills": total,
        "Match Rate (%)": rate,
        "Average Cosine Score": avg
    })

# ✅ Xuất file kết quả
df_out = pd.DataFrame(rows)
df_out.to_excel("output/semantic_skill_matching.xlsx", index=False)

# ✅ TÍNH TỔNG KẾT TẠI ĐÂY
total_matched = df_out["Matched Count"].sum()
total_skills = df_out["Total Skills"].sum()
avg_match_rate = round((total_matched / total_skills) * 100, 2) if total_skills else 0.0
avg_cosine_score = round(df_out["Average Cosine Score"].mean(), 4)

# ✅ In kết quả ra terminal
print("\n📊 Semantic Matching Summary:")
print(f"- Tổng kỹ năng: {total_skills}")
print(f"- Số kỹ năng match được: {total_matched}")
print(f"- Match rate: {avg_match_rate}%")
print(f"- Avg Cosine Score: {avg_cosine_score}")
