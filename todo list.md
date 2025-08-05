# Internship Tasks - Complete To-Do List & Explanation

## 📅 **Timeline: 2 Days (Deadline: August 10, 2025)**

---

## **TASK 1: Court Data Fetcher & Mini-Dashboard** 
### ⏰ **Day 1 Schedule**

### **What You're Building:**
A web application that:
- Takes court case details as input (Case Type, Number, Year)
- Scrapes data from Indian court websites
- Shows case information like parties, dates, orders
- Stores all queries in a database
- Allows PDF downloads of court orders

### **📋 Day 1 To-Do List:**

#### **Morning (4 hours):**
- [ ] **Setup Environment** (30 min)
  - Install Python, pip, Git
  - Create project folder
  - Install required libraries
  
- [ ] **Choose Target Court** (15 min)
  - Pick Delhi High Court OR any District Court
  - Inspect website structure
  - Document choice in README

- [ ] **Database Design** (45 min)
  - Create SQLite database
  - Design tables for queries and case data
  - Test database connections

- [ ] **Web Scraper Foundation** (2.5 hours)
  - Study court website structure
  - Handle CAPTCHA/security measures
  - Create scraping functions
  - Test data extraction

#### **Afternoon (4 hours):**
- [ ] **Flask Web App** (2 hours)
  - Create main app.py
  - Build search form
  - Handle form submissions
  - Connect scraper to web interface

- [ ] **Frontend Templates** (1 hour)
  - Design search form (HTML/CSS)
  - Create results display page
  - Make it user-friendly

- [ ] **Testing & Error Handling** (1 hour)
  - Test with real case numbers
  - Handle invalid inputs
  - Add user-friendly error messages

#### **Evening (2 hours):**
- [ ] **Documentation** (30 min)
  - Write comprehensive README
  - Document CAPTCHA strategy
  - Add setup instructions

- [ ] **Demo Video** (30 min)
  - Record 5-minute screen capture
  - Show complete workflow
  - Upload to YouTube/Loom

- [ ] **Final Polish** (1 hour)
  - Code cleanup
  - Add comments
  - Push to GitHub
  - Test final deployment

---

## **TASK 2: WhatsApp-Driven Google Drive Assistant**
### ⏰ **Day 2 Schedule**

### **What You're Building:**
An n8n workflow that:
- Receives WhatsApp messages via Twilio
- Understands commands like "LIST /folder", "DELETE file.pdf"
- Performs Google Drive operations
- Uses AI to summarize documents
- Sends results back to WhatsApp

### **📋 Day 2 To-Do List:**

#### **Morning (4 hours):**
- [ ] **Setup Services** (1.5 hours)
  - Create Twilio WhatsApp Sandbox account
  - Setup Google Drive API credentials
  - Get OpenAI API key
  - Install n8n via Docker

- [ ] **n8n Workflow Design** (1 hour)
  - Plan workflow structure
  - Create webhook endpoint
  - Design command parsing logic

- [ ] **WhatsApp Integration** (1.5 hours)
  - Connect Twilio webhook to n8n
  - Parse incoming messages
  - Test message reception

#### **Afternoon (4 hours):**
- [ ] **Google Drive Operations** (2 hours)
  - Implement LIST command
  - Implement DELETE command
  - Implement MOVE command
  - Test each operation

- [ ] **AI Summarization** (1 hour)
  - Connect to OpenAI/Claude API
  - Create summary prompts
  - Handle different file types (PDF, DOCX, TXT)

- [ ] **Command Processing** (1 hour)
  - Parse text commands
  - Add error handling
  - Implement safety confirmations

#### **Evening (2 hours):**
- [ ] **Testing & Safety** (1 hour)
  - Test all commands
  - Add deletion confirmations
  - Create audit logging

- [ ] **Documentation & Demo** (1 hour)
  - Export workflow.json
  - Write setup instructions
  - Record demo video
  - Push to GitHub

---

## **🛠️ What You Need to Install/Setup:**

### **For Task 1:**
```bash
# Python libraries
pip install flask requests beautifulsoup4 selenium webdriver-manager python-dotenv

# System requirements
- Python 3.8+
- Chrome browser (for Selenium)
- Git
```

### **For Task 2:**
```bash
# Docker for n8n
docker pull n8nio/n8n

# API Accounts needed:
- Twilio account (free sandbox)
- Google Cloud Console account
- OpenAI account (or Claude API)
```

---

## **🎯 Key Success Factors:**

### **Task 1 Priorities:**
1. **Choose simple court website** - Don't pick overly complex sites
2. **Handle CAPTCHA smartly** - Document your approach clearly
3. **Robust error handling** - Website might be down
4. **Clean code structure** - Make it readable

### **Task 2 Priorities:**
1. **Start with basic commands** - GET, LIST working first
2. **Safety first** - Prevent accidental deletions
3. **Clear documentation** - n8n workflows can be complex
4. **Test thoroughly** - WhatsApp integration can be tricky

---

## **📊 Evaluation Criteria (What They're Looking For):**

### **Technical Skills:**
- [ ] Code quality and structure
- [ ] Error handling and robustness
- [ ] Security practices (no hardcoded keys)
- [ ] Database design

### **Problem Solving:**
- [ ] CAPTCHA/security bypass creativity
- [ ] Workflow logic and efficiency
- [ ] Integration challenges handling

### **Documentation:**
- [ ] Clear README files
- [ ] Setup instructions
- [ ] Video demonstrations
- [ ] Code comments

### **Bonus Points:**
- [ ] Docker containers
- [ ] Unit tests
- [ ] CI/CD workflows
- [ ] Creative features

---

## **🚨 Important Notes:**

1. **Partial Credit Available** - Even incomplete solutions are valued
2. **Document Blockers** - If stuck, explain what you tried
3. **Use AI Tools** - You can use Claude/GPT for help (mention in README)
4. **Work Solo** - Individual work only
5. **Deadline Firm** - August 10, 2025, 23:59 IST

---

## **📝 Submission Requirements:**
- [ ] Public GitHub repositories
- [ ] MIT or Apache-2.0 license
- [ ] Demo videos (≤5 minutes each)
- [ ] Comprehensive README files
- [ ] Google Form submission (will be shared later)

---

**Ready to start coding? Let me know when you want to begin with Task 1, and I'll provide the detailed code implementation!**