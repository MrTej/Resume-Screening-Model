from flask import Flask, request, render_template
from resumescreeningmodelcvs import compute_fit_score, read_resume, extract_entities, flag_bias_indicators

app = Flask(__name__)

# ============================
# DEFINE JOB DESCRIPTIONS
# ============================
job_descriptions = {
    "HR": "Responsible for recruitment, onboarding, employee relations, payroll coordination, performance management, HR policy development, and maintaining compliance with labour regulations.",
    "DESIGNER": "Creates visual concepts, graphics, and layouts for digital and print media, using tools like Photoshop, Illustrator, and Figma. Collaborates with teams to create brand-consistent designs.",
    "INFORMATION-TECHNOLOGY": "Develops, maintains, and troubleshoots software systems, networks, databases, and cloud applications. Requires strong programming, systems analysis, and IT infrastructure knowledge.",
    "TEACHER": "Plans and delivers lessons, assesses student progress, manages classroom activities, and develops curriculum materials to support learning outcomes.",
    "ADVOCATE": "Provides legal advice, prepares cases, drafts legal documents, represents clients in court, and interprets laws and regulations.",
    "BUSINESS-DEVELOPMENT": "Identifies new business opportunities, builds client relationships, develops growth strategies, conducts market research, and manages sales pipelines.",
    "HEALTHCARE": "Provides clinical care, manages patient records, assists in diagnosis, monitors patient health, follows healthcare protocols, and collaborates with medical teams.",
    "FITNESS": "Develops workout programs, trains clients, provides nutrition advice, demonstrates exercises, ensures safety, and tracks fitness progress.",
    "AGRICULTURE": "Works on farming operations, including planting, harvesting, irrigation, crop management, soil analysis, and use of agricultural machinery.",
    "BPO": "Handles customer support, technical support, or back-office operations through calls, chats, or emails in a high-volume outsourcing environment.",
    "SALES": "Generates leads, pitches products, negotiates deals, closes sales, manages customer relationships, and meets revenue targets.",
    "CONSULTANT": "Analyzes business challenges, provides strategic recommendations, develops reports, and supports clients in implementing solutions to improve performance.",
    "DIGITAL-MEDIA": "Manages social media content, digital campaigns, analytics, SEO, online branding, and audience engagement across digital platforms.",
    "AUTOMOBILE": "Performs vehicle diagnostics, repairs, maintenance, quality inspections, and uses automotive tools and systems.",
    "CHEF": "Prepares meals, designs menus, oversees kitchen staff, maintains food quality standards, and manages kitchen operations.",
    "FINANCE": "Handles financial reporting, budgeting, auditing, investment analysis, forecasting, accounting, and compliance with financial regulations.",
    "APPAREL": "Manages clothing production, pattern making, garment design, fashion merchandising, textile selection, and quality control.",
    "ENGINEERING": "Designs and develops technical systems, performs CAD modelling, conducts tests, troubleshoots machinery, and improves engineering processes.",
    "ACCOUNTANT": "Manages financial statements, bookkeeping, tax filing, audits, reconciliations, and compliance with accounting standards.",
    "CONSTRUCTION": "Works on building projects, site management, surveying, blueprint interpretation, material coordination, and safety compliance.",
    "PUBLIC-RELATIONS": "Handles media communications, press releases, brand image management, public statements, event coordination, and crisis communication.",
    "BANKING": "Manages customer accounts, loans, transactions, financial advisory, risk assessment, and regulatory compliance within banking systems.",
    "ARTS": "Creates artistic works in mediums such as painting, music, theatre, or writing. Collaborates on creative projects and exhibits work.",
    "AVIATION": "Supports aircraft operations, maintenance, navigation systems, safety checks, flight coordination, and aviation compliance."
}


# ============================
# ROUTES
# ============================
@app.route("/")
def upload_form():
    return render_template("upload.html")


@app.route("/screen", methods=["POST"])
def screen_resume():
    if "resume" not in request.files:
        return "No resume uploaded", 400

    file = request.files["resume"]
    save_path = "uploaded_resume.pdf"
    file.save(save_path)

    # Extract text
    resume_text = read_resume(save_path)

    # Compute fit scores
    fit_scores = compute_fit_score(resume_text, job_descriptions)

    # Extract entities and bias flags
    entities = extract_entities(resume_text)
    bias_flags = flag_bias_indicators(resume_text)

    # Prepare top match and full ranking
    top_match = {"category": fit_scores[0][0], "score": fit_scores[0][1]}
    full_ranking = [{"category": job, "score": score} for job, score in fit_scores]

    return render_template(
        "results.html",
        top_match=top_match,
        full_ranking=full_ranking,
        entities=entities,
        bias_flags=bias_flags
    )


# ============================
# START SERVER
# ============================
if __name__ == "__main__":
    app.run(debug=True)
