def detect_allergy(text):
    keywords = ["allergy", "allergic", "sensitive to"]
    allergies_found = []

    for word in keywords:
        if word.lower() in text.lower():
            allergies_found.append(word)

    if allergies_found:
        return "⚠️ Allergy Alert: Patient may have allergies mentioned."
    else:
        return "✅ No allergies detected."
