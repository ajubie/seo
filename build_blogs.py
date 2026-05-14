import os
import re
from datetime import datetime

KEYWORDS = [
    "Analyzing Darknet State-Sponsored Hidden Services",
    "Privacy-Preserving Ad Networks for the Deep Web",
    "Secure Micro-SaaS Deployment on Hidden Services",
    "The Impact of 6G on Mobile Anonymity Networks",
    "Hardware-Level Backdoors and the Search for Clean Silicon",
    "Anonymous Dispute Resolution in Decentralized Markets",
    "Securing Supply Chains for Privacy-Focus Hardware",
    "The Rise of Privacy-First Content Delivery Networks (CDNs)",
    "Understanding Data Poisoning Attacks on Surveillance AI",
    "Anonymous Academic Publishing and Censorship Resistance"
]

CONTENT_DATA = {
    "Analyzing Darknet State-Sponsored Hidden Services": {
        "title": "Analyzing Darknet State-Sponsored Hidden Services in 2026",
        "description": "Deep dive into state-sponsored hidden services on the darknet. Discover how advanced adversaries utilize .onion services for covert operations.",
        "html": """
        <h2>The Evolution of State-Sponsored Operations</h2>
        <p>State-sponsored actors have increasingly turned to the darknet to conduct highly covert operations. <strong>Analyzing Darknet State-Sponsored Hidden Services</strong> requires a nuanced understanding of advanced persistence, OPSEC, and complex network infrastructures. Unlike traditional <a href="../../index.html#cat-marketplaces">marketplaces</a>, these state-backed domains are engineered for espionage, disinformation, and untraceable communication.</p>
        <p>These entities operate with near-limitless resources. They deploy custom `.onion` implementations to evade detection and utilize sophisticated encryption to protect their command-and-control (C2) servers. To fully comprehend these operations, one must look past simple anonymity and into the realm of hardware-level isolation.</p>

        <h2>Infrastructure and Tactics</h2>
        <p>The architecture of a state-sponsored service drastically differs from civilian deployments:</p>
        <ul>
            <li><strong>Isolated Sub-networks:</strong> Dedicated darknet nodes that intentionally route traffic through compromised but legitimate-looking relays.</li>
            <li><strong>Zero-Day Exploitation:</strong> Use of unknown vulnerabilities to compromise systems interacting with their hidden services.</li>
            <li><strong>Disinformation Distribution:</strong> Secure channels designed to leak manipulated data securely to journalists without revealing the source.</li>
        </ul>
        <img src="../../img/state-sponsored-architecture.webp" alt="Diagram showing the architecture of state-sponsored darknet hidden services" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

        <h2>Defensive Posture for Analysts</h2>
        <p>Security researchers engaging with these services face immense risk. State actors actively attempt to de-anonymize visitors using advanced browser exploitation and timing attacks. To protect yourself, always route analysis through multiple nested VPNs before entering the Tor network and use heavily sandboxed virtual environments.</p>
        <p>Researchers should constantly refer to established threat intelligence feeds. The <a href="https://www.cisa.gov/topics/cyber-threats-and-advisories" target="_blank" rel="noopener noreferrer nofollow">CISA Cyber Threats</a> portal provides invaluable baseline data for identifying known state-sponsored TTPs (Tactics, Techniques, and Procedures).</p>
        """
    },
    "Privacy-Preserving Ad Networks for the Deep Web": {
        "title": "Privacy-Preserving Ad Networks for the Deep Web",
        "description": "Explore the emergence of privacy-preserving ad networks tailored for the deep web. Learn how anonymity and monetization coexist.",
        "html": """
        <h2>Monetizing Anonymity</h2>
        <p>The deep web is transitioning from a purely chaotic environment to a structured digital economy. <strong>Privacy-Preserving Ad Networks for the Deep Web</strong> represent the next frontier in anonymous monetization. Administrators of <a href="../../index.html#cat-forums">darknet forums</a> and informational wikis need revenue streams that do not compromise their users' privacy.</p>
        <p>Traditional ad networks rely on invasive tracking scripts, cookies, and behavioral profiling. In the deep web, these techniques are not only ineffective (due to the use of privacy browsers) but actively dangerous, potentially de-anonymizing operators and visitors alike.</p>

        <h2>Zero-Knowledge Advertising</h2>
        <p>The solution lies in zero-knowledge advertising mechanisms:</p>
        <ul>
            <li><strong>Contextual Targeting:</strong> Ads are served based strictly on the content of the page, not the identity or history of the user.</li>
            <li><strong>Cryptographic Proof of View:</strong> Utilizing zero-knowledge proofs (ZKPs) to verify ad impressions without revealing the viewer's IP address or browser fingerprint.</li>
            <li><strong>Crypto-Native Payouts:</strong> Revenue is distributed automatically via smart contracts to <a href="../../index.html#cat-crypto">Monero (XMR)</a> or similar privacy coins, ensuring the financial trail remains dark.</li>
        </ul>
        <img src="../../img/privacy-ad-network.webp" alt="Flowchart explaining zero-knowledge advertising on the deep web" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

        <h2>The Future of Deep Web Commerce</h2>
        <p>As these networks mature, we expect to see a stabilization of the deep web economy. By aligning financial incentives with strict privacy protocols, developers can build sustainable, resilient hidden services. For insights into the underlying cryptographic primitives making this possible, read the <a href="https://zcash.github.io/halo2/" target="_blank" rel="noopener noreferrer nofollow">Halo 2 Documentation</a> on zero-knowledge proving systems.</p>
        """
    },
    "Secure Micro-SaaS Deployment on Hidden Services": {
        "title": "Secure Micro-SaaS Deployment on Hidden Services",
        "description": "A comprehensive guide to deploying secure Micro-SaaS applications as darknet hidden services. Learn architecture, OPSEC, and monetization.",
        "html": """
        <h2>The Rise of Darknet Micro-SaaS</h2>
        <p>Software as a Service (SaaS) has conquered the clearnet, and now it is expanding into the shadows. <strong>Secure Micro-SaaS Deployment on Hidden Services</strong> allows developers to offer specialized tools—such as secure messaging, encrypted file drops, or automated OPSEC auditing—directly to anonymous users.</p>
        <p>Unlike massive <a href="../../index.html#cat-marketplaces">marketplaces</a>, a Micro-SaaS is highly focused. However, the operational security requirements remain identically stringent. A single vulnerability can expose the entire customer base.</p>

        <h2>Architectural Considerations</h2>
        <p>Deploying a SaaS on an `.onion` address requires rethinking standard web development paradigms:</p>
        <ul>
            <li><strong>Stateless Design:</strong> Minimize server-side storage. Whenever possible, encrypt data client-side before it ever reaches the server.</li>
            <li><strong>Tor-Native Authentication:</strong> Implement authentication mechanisms that do not rely on email addresses. Use PGP keys or deterministic Tor-based identities.</li>
            <li><strong>Containerized Isolation:</strong> Every component (web server, database, worker queues) must run in strictly isolated containers, unable to access the external internet.</li>
        </ul>
        <img src="../../img/micro-saas-architecture.webp" alt="Secure Micro-SaaS deployment architecture for Tor hidden services" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

        <h2>Handling Payments Securely</h2>
        <p>Monetization is the primary challenge. Integrating clearnet payment processors is impossible. Instead, Micro-SaaS operators must rely on native <a href="../../index.html#cat-crypto">cryptocurrency</a> integrations. Implementing automated, non-custodial payment gateways using Monero or Lightning Network is essential. For best practices on secure coding, always consult the <a href="https://owasp.org/www-project-top-ten/" target="_blank" rel="noopener noreferrer nofollow">OWASP Top 10</a> guidelines, adapting them for the unique threat model of the darknet.</p>
        """
    },
    "The Impact of 6G on Mobile Anonymity Networks": {
         "title": "The Impact of 6G on Mobile Anonymity Networks",
         "description": "Analyze how the upcoming 6G technology will disrupt and enhance mobile anonymity networks and darknet access on cellular devices.",
         "html": """
         <h2>6G: A Paradigm Shift for Mobile Privacy</h2>
         <p>As the telecommunications industry prepares for the rollout of sixth-generation cellular networks, privacy advocates are bracing for impact. <strong>The Impact of 6G on Mobile Anonymity Networks</strong> will be profound. While 6G promises unprecedented speeds and hyper-connectivity, its reliance on AI-driven network management and pervasive sensing technologies poses severe risks to user anonymity.</p>
         <p>Accessing <a href="../../index.html#cat-privacy">privacy networks</a> via mobile devices has always been challenging due to baseband processor vulnerabilities. 6G exacerbates these issues by integrating precise spatial tracking directly into the signal infrastructure.</p>

         <h2>Threats to Mobile Tor and I2P</h2>
         <p>The core mechanisms of 6G introduce new attack vectors against anonymous routing:</p>
         <ul>
             <li><strong>AI Traffic Analysis:</strong> 6G networks use machine learning to optimize routing. These same algorithms can trivially identify the distinct traffic patterns of Tor or I2P, even when obfuscated.</li>
             <li><strong>Sub-Millimeter Tracking:</strong> The high frequencies used in 6G allow the network to act as high-resolution radar, pinpointing a user's physical location with terrifying accuracy.</li>
             <li><strong>Edge Computing Interception:</strong> The shift towards Mobile Edge Computing (MEC) means data is processed closer to the user, providing more opportunities for localized interception before traffic enters an encrypted tunnel.</li>
         </ul>
         <img src="../../img/6g-anonymity-threats.webp" alt="Diagram illustrating the threats 6G networks pose to mobile anonymity" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

         <h2>Adapting Anonymity for the 6G Era</h2>
         <p>To survive in a 6G world, anonymity networks must evolve. We will likely see the development of hardware-level noise generators to disrupt spatial tracking, and the integration of advanced polymorphic traffic obfuscation to defeat AI analysis. Staying informed is critical; researchers should follow developments from the <a href="https://www.eff.org/" target="_blank" rel="noopener noreferrer nofollow">Electronic Frontier Foundation (EFF)</a> regarding mobile surveillance legislation and technology.</p>
         """
    },
    "Hardware-Level Backdoors and the Search for Clean Silicon": {
        "title": "Hardware-Level Backdoors and the Search for Clean Silicon",
        "description": "Discover the insidious threat of hardware-level backdoors in modern processors and the ongoing quest to source secure, clean silicon for darknet operations.",
        "html": """
        <h2>The Foundation of Mistrust</h2>
        <p>Software security is irrelevant if the underlying hardware is compromised. <strong>Hardware-Level Backdoors and the Search for Clean Silicon</strong> is the most critical issue facing high-security operations today. Whether you are running a <a href="../../index.html#cat-marketplaces">secure marketplace</a> or communicating via encrypted channels, compromised silicon renders all software encryption moot.</p>
        <p>State actors and advanced persistent threats (APTs) have demonstrated the capability to implant backdoors directly into the silicon fabric during the manufacturing process, making them virtually undetectable by conventional software analysis.</p>

        <h2>The Anatomy of a Silicon Backdoor</h2>
        <p>These implants operate at Ring -3, deeper than the operating system or even the hypervisor. They can:</p>
        <ul>
            <li><strong>Extract Cryptographic Keys:</strong> Silently monitor memory buses and exfiltrate PGP or SSL keys before they are used.</li>
            <li><strong>Bypass OS Security:</strong> Grant remote attackers direct memory access (DMA) to the entire system.</li>
            <li><strong>Survive Reinstalls:</strong> Because the backdoor is etched into the physical chip, no amount of wiping the hard drive or flashing the BIOS will remove it.</li>
        </ul>
        <img src="../../img/clean-silicon-search.webp" alt="Illustration of microchip analysis in the search for hardware backdoors" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

        <h2>Sourcing Verifiable Hardware</h2>
        <p>The search for "clean" silicon has led to the rise of open-source hardware initiatives. Projects focusing on the RISC-V architecture offer the promise of auditable processor designs. However, the physical fabrication process remains a black box. For those requiring absolute security, extreme measures such as using decades-old, pre-Intel Management Engine (ME) processors, or building custom logic on FPGAs, are necessary. For further reading on processor vulnerabilities, see the <a href="https://meltdownattack.com/" target="_blank" rel="noopener noreferrer nofollow">Meltdown and Spectre</a> documentation.</p>
        """
    },
    "Anonymous Dispute Resolution in Decentralized Markets": {
        "title": "Anonymous Dispute Resolution in Decentralized Markets",
        "description": "Learn how decentralized darknet markets handle anonymous dispute resolution through cryptographic escrow and distributed jury systems.",
        "html": """
        <h2>Trust in a Trustless Environment</h2>
        <p>The core challenge of any darknet economy is establishing trust between pseudonymous actors. <strong>Anonymous Dispute Resolution in Decentralized Markets</strong> is the mechanism that prevents total systemic collapse due to exit scams and fraud. In modern <a href="../../index.html#cat-marketplaces">marketplaces</a>, traditional centralized moderation is being replaced by decentralized protocols.</p>
        <p>When a buyer claims a product was never delivered, and the vendor claims it was, how do you resolve the conflict without revealing the identity of either party?</p>

        <h2>Mechanisms of Resolution</h2>
        <p>Decentralized markets employ complex cryptographic and game-theoretic models to solve this:</p>
        <ul>
            <li><strong>Multisig Escrow:</strong> Transactions utilize 2-of-3 multisignature wallets (often using <a href="../../index.html#cat-crypto">Bitcoin or Monero</a>). The buyer, the seller, and a neutral arbitrator hold the keys. Funds only move when two parties agree.</li>
            <li><strong>Distributed Juries:</strong> In fully decentralized platforms, disputes are escalated to a randomly selected pool of anonymous users who review the encrypted evidence and vote on the outcome.</li>
            <li><strong>Reputation Staking:</strong> Arbitrators must lock up cryptocurrency as collateral. If they vote against the majority consistently (indicating malicious intent), their stake is slashed.</li>
        </ul>
        <img src="../../img/decentralized-dispute-resolution.webp" alt="Flowchart showing anonymous dispute resolution in decentralized markets" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

        <h2>The Future of Anonymous Commerce</h2>
        <p>These systems are pioneering new forms of digital jurisprudence. By removing the central point of failure (the market admin), decentralized platforms become significantly more resilient to law enforcement takedowns. For a deep dive into the foundational concepts of decentralized arbitration, review the <a href="https://kleros.io/" target="_blank" rel="noopener noreferrer nofollow">Kleros Protocol</a>, which models similar game-theoretic dispute systems.</p>
        """
    },
    "Securing Supply Chains for Privacy-Focus Hardware": {
         "title": "Securing Supply Chains for Privacy-Focus Hardware",
         "description": "Understand the critical importance of supply chain security for privacy-focused hardware and how to mitigate interdiction risks.",
         "html": """
         <h2>The Interdiction Threat</h2>
         <p>You can purchase the most secure laptop in the world, but if it is intercepted in transit and physically modified, your security is compromised before you even open the box. <strong>Securing Supply Chains for Privacy-Focus Hardware</strong> is a logistical nightmare for activists, journalists, and security professionals operating on the <a href="../../index.html#cat-privacy">deep web</a>.</p>
         <p>Supply chain interdiction involves intelligence agencies or organized crime syndicates intercepting packages, carefully opening them, installing hardware keyloggers or malicious firmware, and resealing them perfectly.</p>

         <h2>Strategies for Mitigation</h2>
         <p>Defeating interdiction requires paranoia and meticulous verification:</p>
         <ul>
             <li><strong>Anti-Tamper Packaging:</strong> Vendors use custom, serialized holographic seals and specialized tape that demonstrates clear evidence if removed or bypassed.</li>
             <li><strong>Glitter Nail Polish Verification:</strong> Applying unique patterns of glitter nail polish to screws and photographing them. The recipient compares the pattern upon arrival; it is mathematically impossible to recreate the exact pattern.</li>
             <li><strong>In-Person Procurement:</strong> The ultimate defense. Purchasing hardware in cash from anonymous retail locations, ensuring the device has no pre-associated connection to the buyer.</li>
         </ul>
         <img src="../../img/supply-chain-security.webp" alt="Methods for securing hardware supply chains against interdiction" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

         <h2>The Role of Trusted Vendors</h2>
         <p>A cottage industry of highly trusted hardware vendors has emerged, catering exclusively to extreme privacy needs. They handle the complex logistics of anonymous shipping and verifiable firmware flashing. To understand the scale of supply chain vulnerabilities, review the historical documentation on the <a href="https://arstechnica.com/information-technology/2014/05/photos-of-an-nsa-upgrade-factory-show-cisco-router-getting-implant/" target="_blank" rel="noopener noreferrer nofollow">NSA Tailored Access Operations (TAO)</a> catalog.</p>
         """
    },
    "The Rise of Privacy-First Content Delivery Networks (CDNs)": {
         "title": "The Rise of Privacy-First Content Delivery Networks (CDNs)",
         "description": "Explore how privacy-first CDNs are revolutionizing content delivery on the darknet, offering speed without compromising anonymity.",
         "html": """
         <h2>The CDN Dilemma on the Darknet</h2>
         <p>Traditional Content Delivery Networks (CDNs) are fundamentally incompatible with anonymity. They rely on tracking IP addresses, injecting caching headers, and maintaining massive centralized logs. However, the darknet is notoriously slow. <strong>The Rise of Privacy-First Content Delivery Networks (CDNs)</strong> is an attempt to solve this performance bottleneck without sacrificing OPSEC for <a href="../../index.html#cat-forums">forums</a> and image boards.</p>

         <h2>How Anonymous CDNs Work</h2>
         <p>Privacy-first CDNs operate entirely differently from their clearnet counterparts:</p>
         <ul>
             <li><strong>Distributed Onion Caching:</strong> Utilizing a network of decentralized `.onion` nodes to cache static assets close to the user within the Tor network, eliminating the need to exit to the clearnet.</li>
             <li><strong>Logless Edge Nodes:</strong> Edge nodes are configured to run entirely in RAM, with logging strictly disabled. Even if a node is seized, no user data exists.</li>
             <li><strong>Encrypted Asset Delivery:</strong> Assets are end-to-end encrypted; the CDN nodes cache ciphertext and cannot read the content they are serving.</li>
         </ul>
         <img src="../../img/privacy-cdn-architecture.webp" alt="Architecture diagram of a privacy-first, decentralized CDN" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

         <h2>Performance vs. Privacy</h2>
         <p>While they will never match the latency of a massive clearnet CDN, these privacy-first networks drastically reduce load times for heavy darknet sites. This improves user experience while maintaining the vital decoupling of identity and network activity. For more technical details on distributed caching algorithms, refer to research on <a href="https://ipfs.tech/" target="_blank" rel="noopener noreferrer nofollow">IPFS (InterPlanetary File System)</a> and related decentralized storage protocols.</p>
         """
    },
    "Understanding Data Poisoning Attacks on Surveillance AI": {
         "title": "Understanding Data Poisoning Attacks on Surveillance AI",
         "description": "A technical overview of data poisoning attacks designed to blind surveillance AI and protect privacy in an era of mass data collection.",
         "html": """
         <h2>Fighting Back Against Mass Surveillance</h2>
         <p>As state and corporate entities deploy massive AI systems for facial recognition, gait analysis, and behavioral profiling, traditional <a href="../../index.html#cat-privacy">privacy techniques</a> are becoming insufficient. <strong>Understanding Data Poisoning Attacks on Surveillance AI</strong> provides a proactive method for individuals to protect their digital and physical anonymity.</p>
         <p>Rather than simply hiding from the cameras, data poisoning actively degrades the accuracy of the underlying machine learning models.</p>

         <h2>Mechanisms of Poisoning</h2>
         <p>Data poisoning involves injecting carefully crafted, malicious data into the training sets used by surveillance AIs:</p>
         <ul>
             <li><strong>Adversarial Clothing:</strong> Wearing patterns designed specifically to confuse object detection algorithms, causing the AI to classify a person as a vehicle or ignore them entirely.</li>
             <li><strong>Digital Noise Injection:</strong> Submitting altered images to social media and public databases. These images look normal to humans but contain imperceptible noise that completely corrupts the AI's facial recognition matrix.</li>
             <li><strong>Behavioral Spoofing:</strong> Intentionally generating erratic and randomized digital footprints (search queries, location data) to render behavioral profiling models useless.</li>
         </ul>
         <img src="../../img/data-poisoning-ai.webp" alt="Example of adversarial noise used in data poisoning against AI recognition" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

         <h2>The Arms Race</h2>
         <p>This is an ongoing cryptographic arms race. As AI models become more robust against poisoning, researchers develop more sophisticated adversarial techniques. To understand the mathematical foundations of these vulnerabilities, study the research papers on <a href="https://arxiv.org/abs/1412.6572" target="_blank" rel="noopener noreferrer nofollow">Adversarial Examples in Deep Learning</a>.</p>
         """
    },
    "Anonymous Academic Publishing and Censorship Resistance": {
         "title": "Anonymous Academic Publishing and Censorship Resistance",
         "description": "How anonymous academic publishing on the darknet provides a critical lifeline for researchers facing severe censorship and persecution.",
         "html": """
         <h2>Science in the Shadows</h2>
         <p>In authoritarian regimes, publishing research that contradicts the state narrative can lead to imprisonment or death. <strong>Anonymous Academic Publishing and Censorship Resistance</strong> platforms on the darknet provide a secure haven for suppressed science, historical truths, and political analysis.</p>
         <p>These platforms operate similarly to secure <a href="../../index.html#cat-forums">forums</a>, but prioritize rigorous peer review while maintaining the absolute anonymity of both the authors and the reviewers.</p>

         <h2>Technical Requirements for Safe Publishing</h2>
         <p>Operating a censorship-resistant academic archive requires specialized OPSEC:</p>
         <ul>
             <li><strong>Metadata Scrubbing:</strong> Every submitted document (PDF, LaTeX) is automatically stripped of all identifying metadata, including author tags, software versions, and printer steganography.</li>
             <li><strong>Decentralized Hosting:</strong> The archives are mirrored across multiple Tor and I2P nodes, ensuring that a targeted attack on a single server cannot take down the repository.</li>
             <li><strong>Cryptographic Verification:</strong> Authors can sign their work using anonymous PGP keys, allowing them to prove authorship later without revealing their real-world identity.</li>
         </ul>
         <img src="../../img/anonymous-publishing.webp" alt="Diagram illustrating the anonymous academic publishing and metadata scrubbing process" width="800" height="400" loading="lazy" decoding="async" style="max-width:100%; height:auto; border-radius:8px; margin: 20px 0;">

         <h2>The Vital Importance of Uncensored Data</h2>
         <p>These platforms are essential for human progress, ensuring that critical data regarding public health, human rights violations, and environmental disaster cannot be permanently erased by hostile governments. For historical context on the importance of free access to information, look to the mission of the <a href="https://archive.org/" target="_blank" rel="noopener noreferrer nofollow">Internet Archive</a>.</p>
         """
    }
}

def kebab_case(string):
    string = string.lower()
    string = re.sub(r'[^a-z0-9 ]', '', string)
    return string.replace(' ', '-')

def build_blogs():
    with open('blog_template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    for keyword in KEYWORDS:
        if keyword not in CONTENT_DATA:
            continue

        data = CONTENT_DATA[keyword]
        title = data["title"]
        desc = data["description"]
        content_html = data["html"]
        slug = kebab_case(keyword)

        # Output directory
        out_dir = os.path.join('public', 'blog', slug)
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, 'index.html')

        html_out = template

        # Replace Title
        html_out = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html_out, flags=re.IGNORECASE)

        # Replace Meta Description
        html_out = re.sub(
            r'<meta name="description"\s+content="[^"]*"\s*/>',
            f'<meta name="description"\n    content="{desc}" />',
            html_out,
            flags=re.IGNORECASE | re.DOTALL
        )

        # Replace Canonical URL
        html_out = re.sub(
            r'<link rel="canonical" href="[^"]*"\s*/>',
            f'<link rel="canonical" href="https://darkdir.link/blog/{slug}/" />',
            html_out,
            flags=re.IGNORECASE
        )

        # Replace Open Graph Title
        html_out = re.sub(
            r'<meta property="og:title" content="[^"]*"\s*/>',
            f'<meta property="og:title" content="{title}" />',
            html_out,
            flags=re.IGNORECASE
        )

        # Replace Open Graph Description
        html_out = re.sub(
            r'<meta property="og:description"\s+content="[^"]*"\s*/>',
            f'<meta property="og:description"\n    content="{desc}" />',
            html_out,
            flags=re.IGNORECASE | re.DOTALL
        )

        # Replace Open Graph URL
        html_out = re.sub(
            r'<meta property="og:url" content="[^"]*"\s*/>',
            f'<meta property="og:url" content="https://darkdir.link/blog/{slug}/" />',
            html_out,
            flags=re.IGNORECASE
        )

        # Replace JSON-LD Schema Headline and Description
        html_out = re.sub(
            r'"headline":\s*"[^"]*"',
            f'"headline": "{title}"',
            html_out,
            flags=re.IGNORECASE
        )
        html_out = re.sub(
            r'"description":\s*"[^"]*"',
            f'"description": "{desc}"',
            html_out,
            flags=re.IGNORECASE
        )

        # Replace content inside <div class="static-content-wrap"> while keeping ad banners
        # We find the start and end of static-content-wrap, then carefully inject content
        # preserving the ads if possible.
        # Actually, let's just use regex to replace everything between the top ad and bottom ad.
        # Looking at the template, the structure is:
        # <div class="static-content-wrap">
        #   [TOP AD BANNER]
        #   <h2>...</h2>...<p>...</p>
        #   [MIDDLE AD BANNER (float right)]
        #   <h2>...</h2>...<p>...</p>
        #   [BOTTOM AD BANNER]
        # </div>

        # We will extract the ad banners from the original template to ensure they are untouched.
        # Top ad
        top_ad_match = re.search(r'(<div class="ad-banner-horizontal"[^>]*>.*?</div>)', template, re.DOTALL)
        top_ad = top_ad_match.group(1) if top_ad_match else ""

        # Middle ad
        mid_ad_match = re.search(r'(<div class="ad-banner-rect"[^>]*>.*?</div>)', template, re.DOTALL)
        mid_ad = mid_ad_match.group(1) if mid_ad_match else ""

        # Bottom ad (the last ad-banner-horizontal)
        ads = re.findall(r'(<div class="ad-banner-horizontal"[^>]*>.*?</div>)', template, re.DOTALL)
        bottom_ad = ads[-1] if len(ads) > 1 else ""

        # Now, split the generated content into top and bottom parts to insert the middle ad.
        # Assuming the generated content has multiple <h2> tags, we can insert the middle ad before the second <h2>.
        content_parts = content_html.split('<h2>', 2)
        if len(content_parts) == 3:
            final_content = content_parts[0] + '<h2>' + content_parts[1] + mid_ad + '<h2>' + content_parts[2]
        else:
            final_content = content_html + mid_ad

        new_wrap_content = f'\n        <div class="static-content-wrap">\n          {top_ad}\n          {final_content}\n          {bottom_ad}\n        </div>\n'

        html_out = re.sub(
            r'<div class="static-content-wrap">.*?</div>\s*</article>',
            f'{new_wrap_content}    </article>',
            html_out,
            flags=re.DOTALL
        )

        # Replace H1 title in static-header
        html_out = re.sub(
            r'<div class="static-header">\s*<h1>.*?</h1>',
            f'<div class="static-header">\n        <h1>{title}</h1>',
            html_out,
            flags=re.DOTALL
        )

        # Replace publish date
        current_date = datetime.now().strftime("%b %d, %Y")
        iso_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")

        html_out = re.sub(
            r'Published on [^•]*•',
            f'Published on {current_date} •',
            html_out
        )

        html_out = re.sub(
            r'"datePublished":\s*"[^"]*"',
            f'"datePublished": "{iso_date}"',
            html_out
        )
        html_out = re.sub(
            r'"dateModified":\s*"[^"]*"',
            f'"dateModified": "{iso_date}"',
            html_out
        )

        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(html_out)

        print(f"Generated {out_file}")

if __name__ == "__main__":
    build_blogs()
