print("🎓 Welcome to the College Enquiry Chatbot!")
print("Ask about: 'fees', 'courses', 'timings', 'contact', or type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if "bye" in user:
        print("🎓 Chatbot: Thank you! Feel free to ask anytime. Goodbye!")
        break

    elif "fees" in user or "fee" in user:
        print("\n💰 Fee Details:")
        print("- B.Tech: ₹2,00,000 per year")
        print("- M.Tech: ₹3,00,000 per year")
        print("- MBA: ₹1,50,000 per year\n")

    elif "college_name" in user:
        print("\n Nri institute of Technology")
    elif "courses" in user:
        print("\n📚 Courses Offered:")
        print("- B.Tech (CSE, ECE, EEE, Mechanical, Civil,Aiml,CSD,CSM)")
        print("- M.Tech (CSE, Structural Engineering)")
        print("- MBA (Finance, HR, Marketing)\n")

    elif "timings" in user or "timing" in user:
        print("\n⏰ College Timings:")
        print("- Monday to Saturday: 9:20 AM to 4:30 PM")
        print("- Sunday: Holiday\n")

    elif "contact" in user or "phone" in user or "email" in user:
        print("\n📞 Contact Information:")
        print("- Phone: +91 98765 43210")
        print("- Email: info@college.com")
        print("- Address: XYZ Road, Hyderabad, India\n")

    else:
        print("🎓 Chatbot: Sorry, I can answer only about fees, courses, timings, or contact info.\n")
