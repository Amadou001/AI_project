import pandas as pd

# Create a dictionary with sample emails and their labels
data = {
    'text': [
        "Dear user, your account has been compromised. Click here to reset your password.",
        "Hi John, Can you send me the report by EOD today?",
        "Your package is out for delivery. Track your shipment here.",
        "Your bank account needs immediate verification to avoid suspension. Log in here.",
        "Meeting scheduled for tomorrow at 10 AM. Please confirm your availability.",
        "Congratulations! You've won a $1000 gift card. Claim your prize now.",
        "Reminder: Your subscription is due for renewal next week.",
        "Urgent: Update your billing information to avoid service disruption.",
        "Let's catch up for lunch tomorrow at our usual place.",
        "We have detected unusual activity on your account. Verify now to secure your account."
    ],
    'label': [
        "phishing",
        "legitimate",
        "legitimate",
        "phishing",
        "legitimate",
        "phishing",
        "legitimate",
        "phishing",
        "legitimate",
        "phishing"
    ]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('emails.csv', index=False)
