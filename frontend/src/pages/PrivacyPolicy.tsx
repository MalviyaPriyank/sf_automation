const PrivacyPolicy = () => {
  return (
    <div className="bg-background text-foreground">
      <div className="max-w-4xl mx-auto px-6 py-12 space-y-12">
        <header className="space-y-3">
          <p className="text-xs uppercase tracking-[0.2em] text-muted-foreground">
            Gyrus Inc.
          </p>
          <h1 className="text-4xl font-semibold tracking-tight">Privacy Policy</h1>
          <p className="text-sm text-muted-foreground">
            For individuals in the European Economic Area, United Kingdom, and Switzerland,
            you can read this version of our Privacy Policy.
          </p>
        </header>

        <section className="space-y-4 text-sm text-muted-foreground leading-relaxed">
          <p>
            We at Gyrus Inc. (&ldquo;Gyrus,&rdquo; &ldquo;we,&rdquo; &ldquo;our,&rdquo; or
            &ldquo;us&rdquo;) respect your privacy and are committed to keeping secure any
            information we obtain from or about you. This Privacy Policy describes how we
            handle personal data when you use our websites, applications, and services
            (collectively, the &ldquo;Services&rdquo;).
          </p>
          <p>
            This Privacy Policy does not apply to content that we process on behalf of
            customers of our business offerings (for example, the Gyrus API). Our use of
            that data is governed by the customer agreements covering access to and use of
            those offerings.
          </p>
          <p>
            For information about how we collect and use data to improve our models and
            products, and your choices with respect to that data, please see our help center
            guidance on training data.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">1. Personal data we collect</h2>
          <div className="space-y-3 text-sm text-muted-foreground leading-relaxed">
            <p>
              We collect personal data relating to you (&ldquo;Personal Data&rdquo;) as follows:
            </p>
            <div className="space-y-2">
              <p className="font-semibold text-foreground">Personal Data you provide:</p>
              <ul className="list-disc pl-6 space-y-2">
                <li>
                  <span className="font-medium text-foreground">Account Information:</span>{" "}
                  Name, contact details, account credentials, payment information, and
                  transaction history when you create or manage an account.
                </li>
                <li>
                  <span className="font-medium text-foreground">User Content:</span>{" "}
                  Prompts and other content you upload or submit (e.g., files, images, audio),
                  depending on the features you use.
                </li>
                <li>
                  <span className="font-medium text-foreground">Communication Information:</span>{" "}
                  Messages you send to us (for example, via email or social channels),
                  including your contact details and the contents of your communications.
                </li>
                <li>
                  <span className="font-medium text-foreground">Other Information You Provide:</span>{" "}
                  Responses to surveys or events, and information you give us to verify your
                  identity or age.
                </li>
              </ul>
            </div>
            <div className="space-y-2">
              <p className="font-semibold text-foreground">Personal Data from your use of the Services:</p>
              <ul className="list-disc pl-6 space-y-2">
                <li>
                  <span className="font-medium text-foreground">Log Data:</span>{" "}
                  IP address, browser type and settings, timestamps, and how you interact with
                  the Services.
                </li>
                <li>
                  <span className="font-medium text-foreground">Usage Data:</span>{" "}
                  Features you use, content you view or engage with, time zone, device type,
                  and activity in the Services.
                </li>
                <li>
                  <span className="font-medium text-foreground">Device Information:</span>{" "}
                  Device name, operating system, identifiers, and browser details.
                </li>
                <li>
                  <span className="font-medium text-foreground">Location Information:</span>{" "}
                  General location derived from your IP address for security and product
                  experience. Some features may allow you to share more precise location
                  information.
                </li>
                <li>
                  <span className="font-medium text-foreground">Cookies and Similar Technologies:</span>{" "}
                  We use cookies to operate and improve the Services and remember your
                  preferences. See our Cookie Notice for details.
                </li>
              </ul>
            </div>
            <p>
              We may also receive information from trusted partners (for example, security and
              fraud prevention providers) and publicly available sources to protect and improve
              the Services.
            </p>
          </div>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">2. How we use Personal Data</h2>
          <ul className="list-disc pl-6 space-y-2 text-sm text-muted-foreground leading-relaxed">
            <li>Provide, maintain, and improve the Services (for example, responding to your prompts).</li>
            <li>Develop new features and conduct research.</li>
            <li>Communicate with you about the Services, including updates and events.</li>
            <li>Prevent fraud, misuse, or illegal activity and protect the security of our systems.</li>
            <li>Comply with legal obligations and protect the rights, privacy, safety, or property of users, Gyrus, or others.</li>
          </ul>
          <p className="text-sm text-muted-foreground leading-relaxed">
            We may aggregate or de-identify Personal Data so it no longer identifies you and use
            that information to analyze and improve the Services.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">3. Disclosure of Personal Data</h2>
          <ul className="list-disc pl-6 space-y-2 text-sm text-muted-foreground leading-relaxed">
            <li><span className="font-medium text-foreground">Vendors and Service Providers:</span> Hosting, cloud, analytics, customer support, payments, and security partners acting under our instructions.</li>
            <li><span className="font-medium text-foreground">Business Transfers:</span> In connection with a merger, acquisition, or similar transaction.</li>
            <li><span className="font-medium text-foreground">Legal and Safety:</span> To comply with law, protect rights and safety, prevent fraud, or respond to lawful requests.</li>
            <li><span className="font-medium text-foreground">Affiliates:</span> Entities under common control with Gyrus, consistent with this Privacy Policy.</li>
            <li><span className="font-medium text-foreground">Business Account Administrators:</span> If you join an organization account, administrators may access your Gyrus account and Content.</li>
            <li><span className="font-medium text-foreground">Other Users or Third Parties:</span> When you choose to share or connect to third-party applications, subject to their terms.</li>
          </ul>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">4. Retention</h2>
          <p className="text-sm text-muted-foreground leading-relaxed">
            We retain Personal Data only as long as needed to provide the Services, for
            legitimate business purposes (such as security, compliance, and dispute resolution),
            or as required by law. Retention periods depend on factors like the nature of the
            data, why it was collected, legal requirements, and your settings.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">5. Your rights</h2>
          <p className="text-sm text-muted-foreground leading-relaxed">
            Depending on where you live, you may have rights over your Personal Data, such as
            access, deletion, correction, restriction, portability, or objection, and the right
            to withdraw consent where applicable. You may also have the right to lodge a
            complaint with your local data protection authority.
          </p>
          <p className="text-sm text-muted-foreground leading-relaxed">
            To exercise rights you cannot manage in your account, contact us at
            {" "}<a className="underline hover:text-primary" href="mailto:privacy@gyrus.com">privacy@gyrus.com</a>.
            We may need to verify your identity before fulfilling a request.
          </p>
          <p className="text-sm text-muted-foreground leading-relaxed">
            AI systems can generate outputs that are not always factually accurate. If output
            includes information about you that is incorrect and you want it corrected or
            removed, contact us and we will consider your request based on applicable law and
            technical feasibility.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">6. Children</h2>
          <p className="text-sm text-muted-foreground leading-relaxed">
            Our Services are not directed to children under 13, and we do not knowingly collect
            Personal Data from children under 13. Users under 18 must have permission from a
            parent or guardian.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">7. Security</h2>
          <p className="text-sm text-muted-foreground leading-relaxed">
            We implement commercially reasonable technical, administrative, and organizational
            measures to protect Personal Data. No Internet or email transmission is ever fully
            secure, so please use caution when sharing information online.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">8. Changes to this Privacy Policy</h2>
          <p className="text-sm text-muted-foreground leading-relaxed">
            We may update this Privacy Policy from time to time. When we do, we will update the
            effective date and, where required, provide additional notice.
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-semibold">9. Contact us</h2>
          <p className="text-sm text-muted-foreground leading-relaxed">
            If you have questions or concerns about this Privacy Policy, contact us at{" "}
            <a className="underline hover:text-primary" href="mailto:privacy@gyrus.com">privacy@gyrus.com</a>.
          </p>
        </section>
      </div>
    </div>
  );
};

export default PrivacyPolicy;
