import random
import uuid
import csv

greetings = [
    "Hi All,", "Hii Everyone,", "Hello Connections,", "Hiring Alert ", "We’re hiring!"
]

referral_templates = [
    "Apply here: {link}", 
    "Drop your email for referral ", 
    "Click to apply: {link}", 
    "Use this link to apply  {link}"
]

salary_ranges = ["3–6 LPA", "5–10 LPA", "8–12 LPA", "10–15 LPA", "15–25 LPA"]
job_types = ["WFH", "WFO", "Hybrid", "Remote"]
locations = ["India", "PAN India", "Bangalore", "Mumbai", "Remote"]
eligibility_notes = [
    "Freshers welcome!", 
    "Final-year students can apply.", 
    "No prior experience needed.", 
    "Open to all graduates."
]
skills_required = [
    "Good Communication", 
    "Basic coding knowledge", 
    "Teamwork & collaboration", 
    "Analytical mindset"
]
roles_master = [
    "Frontend Developer", "Backend Developer", "Full Stack Developer", "UI/UX Designer",
    "Data Analyst", "Software Engineer", "QA Tester", "DevOps Intern", "Marketing Intern",
    "Cybersecurity Intern", "AI Engineer", "Business Analyst", "Java Developer", "Python Developer"
]

hashtags = [
    "#hiring", "#careers", "#jobsearch", "#techjobs", "#linkedinjobs", 
    "#applynow", "#fresherjobs", "#softwarejobs", "#internship"
]
companies = [
    "Google", "Microsoft", "Amazon", "Apple", "Meta", "Netflix", "Adobe", "Intel",

    "TCS", "Infosys", "Wipro", "Tech Mahindra", "HCL", "Cognizant", "L&T Infotech",

    "Accenture", "Capgemini", "Deloitte", "KPMG", "EY", "PwC", "Oracle", "Salesforce",

    "Swiggy", "Zomato", "Paytm", "PhonePe", "CRED", "Razorpay", "Meesho", "Groww",

    "Fractal", "Freshworks", "Postman", "BrowserStack", "Limechat", "Nanonets", "Zoho",

    "Barclays", "JPMorgan Chase", "Goldman Sachs", "HSBC", "ICICI Bank", "Axis Bank", "Kotak Mahindra Bank",

    "Flipkart", "Ola", "Uber", "Spotify", "LinkedIn", "Slack", "GitHub", "Notion"
]

def random_link():
    return f"https://lnkd.in/{uuid.uuid4().hex[:7]}"

def generate_job_post():
    greeting = random.choice(greetings)
    link = random_link()
    salary = random.choice(salary_ranges)
    job_type = random.choice(job_types)
    location = random.choice(locations)
    eligibility = random.choice(eligibility_notes)
    skills = random.choice(skills_required)
    company = random.choice(companies)
    role = random.choice(roles_master)
    open_roles = random.sample(roles_master, random.randint(5, 10))
    roles_list = "\n".join([f"{i+1}. {r}" for i, r in enumerate(open_roles)])
    tag_list = " ".join(random.sample(hashtags, random.randint(5, 8)))

    templates = [

                # 🔹 Template 1 – Classic LinkedIn Referral
                f"""{greeting}We are #hiring for multiple positions!

        Apply here: {link}

        Eligibility Criteria:
        * Salary Range: {salary}
        * Job Type: {job_type}
        * Location: {location}
        * {eligibility}
        * Skills: {skills}

        Open Positions:
        {roles_list}

        Please like or comment so I can review your profile.
        We'll check your LinkedIn and reach out if there's a match.

        Thank you 🙏

        {tag_list}""",

                # 🔹 Template 2 – Barclays Style
                f"""🚨 #{company} is Hiring – {role}!

        Looking to join a global leader in tech? Here’s your opportunity!

        ✅ Position: {role}
        ✅ Location: {location}
        ✅ Salary: {salary}
        ✅ Experience: 0–2 Years (Freshers Welcome!)
        ✅ Skills: {skills}

        Apply Now: {link}

        📢 Comment #Interested & tag a friend!

        Open Roles:
        {roles_list}

        Tags: {tag_list}""",

                # 🔹 Template 3 – Startup Hype
                f"""🚀 Hiring Alert!! Great Opportunity!

        #{company} is hiring {role} at {location}!

        💰 Salary: {salary}
        🛠 Skills: {skills}

        📩 Apply now: {link}
        📢 Like and comment #Interested!

        Roles Open:
        {roles_list}

        Tags: {tag_list}""",

                # 🔹 Template 4 – Mass Hiring (Virtual Interview)
                f"""🎯 We're Hiring at {company}!

        Virtual Interview on 18th & 19th July 2025 | 07:00 PM IST

        ✅ Work Mode: {job_type}
        ✅ Location: {location}
        ✅ Salary: {salary}

        Who Can Apply:
        - Freshers
        - Final Year Students

        📨 Comment your email to get the apply link!

        Open Positions:
        {roles_list}

        #JoinUs #FreshersWelcome #VirtualInterview {tag_list}"""
            ]

    return random.choice(templates).strip()

def generate_dataset(OUTPUT_FILE, NUM_POSTS):
    """
        args:
            OUTPUT_FILE: path of csv file to be created
            NUM_POSTS: number of fake posts to be generated

        Returns:
            null
    """

    # Write CSV
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["post_id", "description", "fraudulent"])
        for i in range(1, NUM_POSTS + 1):
            post = generate_job_post()
            writer.writerow([i, post, 1])