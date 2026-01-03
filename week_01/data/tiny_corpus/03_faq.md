# Frequently Asked Questions (FAQ)

## General Questions

### What is CloudSync Pro?
CloudSync Pro is an enterprise file synchronization and collaboration platform. It allows teams to securely share, sync, and collaborate on files across devices with real-time updates and version control.

### How is CloudSync Pro different from other services?
- **Security First:** AES-256 encryption with HIPAA/GDPR compliance
- **True Real-Time:** Sub-500ms sync for most files
- **Advanced Versioning:** Unlimited history for enterprise accounts
- **Flexible Deployment:** Cloud, on-premise, or hybrid options

### What platforms are supported?
- **Desktop:** Windows, macOS, Linux
- **Mobile:** iOS and Android
- **Web:** All modern browsers
- **API:** REST API with SDKs for Python, Node.js, and Go

## Pricing & Plans

### How much does it cost?
- **Free:** $0/month - 5GB storage, 1 user
- **Pro:** $12/user/month - 1TB storage, up to 10 users
- **Business:** $20/user/month - 10TB shared, up to 100 users
- **Enterprise:** Custom pricing - Unlimited storage and users

### Is there a free trial?
Yes! Pro and Business plans include a 14-day free trial. No credit card required.

### Can I upgrade or downgrade anytime?
Yes. Changes take effect immediately. Upgrades are prorated; downgrades apply at next billing cycle.

### Do you offer educational or non-profit discounts?
Yes! Verified educational institutions and registered non-profits receive 50% off Business plans.

## Technical Questions

### How does sync actually work?
CloudSync Pro uses delta-sync technology:
1. Monitors file changes in real-time
2. Calculates only the changed bytes (delta)
3. Encrypts and transmits just the delta
4. Merges changes on receiving devices
5. Resolves conflicts automatically or prompts user

### What happens if I edit a file offline?
Changes are queued locally and automatically synced when you reconnect. If someone else edited the same file, you'll see a conflict resolution dialog.

### How are conflicts resolved?
- **Automatic:** For non-overlapping changes in text files
- **Manual:** You choose to keep your version, their version, or merge
- **Version Branching:** Create separate versions instead of merging

### Is there a file size limit?
- Free: 100 MB per file
- Pro: 5 GB per file
- Business: 50 GB per file
- Enterprise: No limit

### How long are deleted files retained?
Deleted files remain in trash for 30 days before permanent deletion. Enterprise accounts can configure custom retention policies.

## Security & Privacy

### Where is my data stored?
Data centers in US (Virginia), EU (Ireland), and Asia (Singapore). You choose your primary region. Enterprise customers can use on-premise storage.

### Who can access my files?
Only you and people you explicitly share with. CloudSync Pro uses zero-knowledge encryption for enterprise accounts, meaning even we cannot access your data.

### What encryption do you use?
- **At Rest:** AES-256 bit encryption
- **In Transit:** TLS 1.3
- **Zero-Knowledge:** Optional for enterprise (client-side encryption)

### Are you GDPR/HIPAA compliant?
Yes. We are SOC 2 Type II certified and fully compliant with GDPR, HIPAA, and CCPA regulations.

### What happens if there's a data breach?
We monitor 24/7 for security threats. In the unlikely event of a breach:
1. Affected users notified within 24 hours
2. Detailed incident report provided
3. Free credit monitoring for 1 year
4. Third-party security audit results published

## Account & Billing

### How do I reset my password?
Click "Forgot Password" on the login page. You'll receive a reset link via email within 5 minutes.

### Can I have multiple accounts?
Yes, but we recommend using one account with our organizational features for easier management.

### How do I cancel my subscription?
Go to Account Settings > Billing > Cancel Subscription. Your account downgrades to Free at the end of the billing period.

### What payment methods do you accept?
Credit cards (Visa, Mastercard, Amex, Discover), PayPal, wire transfer (Enterprise only), and purchase orders (Business/Enterprise).

### Do you offer refunds?
Yes. If you're not satisfied within the first 30 days, we offer a full refund, no questions asked.

## Collaboration

### How many people can I share with?
- Free: Up to 3 external collaborators
- Pro: Unlimited within your 10 users
- Business/Enterprise: Unlimited

### Can I set different permission levels?
Yes. Choose from: View Only, Comment, Edit, Upload Only, or Full Access (including sharing).

### Can I share files with people who don't have accounts?
Yes. Create a share link that works without login. You can add password protection and expiration dates.

### How do notifications work?
Configure per-folder or per-file notifications via:
- Email (instant, hourly digest, or daily digest)
- Slack/Teams integration
- Mobile push notifications
- In-app notifications

## Troubleshooting

### Sync is slow. What should I do?
1. Check your internet connection speed
2. Pause and resume sync
3. Close bandwidth-heavy applications
4. Check bandwidth throttling settings
5. Contact support if issue persists

### I can't log in. Help!
- Verify you're using the correct email
- Check Caps Lock is off
- Try password reset
- Clear browser cache/cookies
- Try incognito/private mode
- Contact support@cloudsync.pro

### Files aren't syncing. Why?
Common causes:
- No internet connection
- Sync is paused
- Storage quota exceeded
- File name contains invalid characters (`/ \ : * ? " < > |`)
- File is locked by another application

### How do I contact support?
- **Email:** support@cloudsync.pro (response within 24 hours)
- **Live Chat:** Available 9am-6pm EST weekdays (Pro and above)
- **Phone:** 1-800-CLOUDSYNC (Enterprise only)
- **Community Forum:** community.cloudsync.pro

