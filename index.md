---
layout: default
title: Home
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Waste Reverse Engineering Clinic - Charlotte DIY Electronics & Lifelong Learning Collective</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #008080;
            font-family: "MS Sans Serif", "Microsoft Sans Serif", sans-serif;
            color: #000;
            padding: 20px;
            line-height: 1.4;
        }

        .desktop-icon {
            position: fixed;
            top: 20px;
            left: 20px;
            text-align: center;
            width: 80px;
            cursor: pointer;
        }

        .desktop-icon img {
            width: 48px;
            height: 48px;
            image-rendering: pixelated;
        }

        .desktop-icon-text {
            background: #008080;
            color: white;
            padding: 2px 4px;
            font-size: 11px;
            margin-top: 4px;
            text-shadow: 1px 1px 0 #000;
        }

        .window {
            background: #c0c0c0;
            border: 2px outset #fff;
            box-shadow: 2px 2px 0 #000;
            max-width: 900px;
            margin: 40px auto;
            position: relative;
        }

        .title-bar {
            background: linear-gradient(90deg, #000080, #1084d0);
            padding: 3px 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .title-text {
            color: white;
            font-weight: bold;
            font-size: 12px;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .title-icon {
            width: 16px;
            height: 16px;
            background: #c0c0c0;
            border: 1px solid #fff;
            image-rendering: pixelated;
        }

        .window-controls {
            display: flex;
            gap: 2px;
        }

        .window-button {
            width: 16px;
            height: 14px;
            background: #c0c0c0;
            border: 1px outset #fff;
            font-size: 10px;
            line-height: 12px;
            text-align: center;
            cursor: pointer;
            font-weight: bold;
        }

        .window-button:active {
            border-style: inset;
        }

        .menu-bar {
            background: #c0c0c0;
            border-bottom: 1px solid #808080;
            padding: 2px 5px;
            font-size: 11px;
        }

        .menu-item {
            display: inline-block;
            padding: 2px 8px;
            cursor: pointer;
        }

        .menu-item:hover {
            background: #000080;
            color: white;
        }

        .window-content {
            padding: 15px;
            background: #c0c0c0;
            min-height: 400px;
        }

        .content-frame {
            background: white;
            border: 2px inset #808080;
            padding: 20px;
            margin-bottom: 15px;
        }

        h1 {
            font-size: 24px;
            color: #000080;
            margin-bottom: 15px;
            font-weight: bold;
        }

        h2 {
            font-size: 18px;
            color: #000080;
            margin: 20px 0 10px 0;
            padding-bottom: 3px;
            border-bottom: 2px solid #000080;
        }

        h3 {
            font-size: 14px;
            color: #800000;
            margin: 15px 0 8px 0;
        }

        p {
            margin-bottom: 12px;
            font-size: 13px;
        }

        .button {
            background: #c0c0c0;
            border: 2px outset #fff;
            padding: 5px 15px;
            font-family: "MS Sans Serif", sans-serif;
            font-size: 11px;
            cursor: pointer;
            display: inline-block;
            margin: 5px 5px 5px 0;
            text-decoration: none;
            color: #000;
        }

        .button:active {
            border-style: inset;
        }

        .button:hover {
            background: #d0d0d0;
        }

        .status-bar {
            background: #c0c0c0;
            border-top: 1px solid #fff;
            padding: 3px 5px;
            font-size: 11px;
            display: flex;
            gap: 10px;
        }

        .status-section {
            border: 1px inset #808080;
            padding: 2px 8px;
            flex: 1;
        }

        .scrollbox {
            border: 2px inset #808080;
            background: white;
            padding: 10px;
            max-height: 200px;
            overflow-y: scroll;
            margin: 10px 0;
            font-size: 12px;
        }

        .info-box {
            background: #ffffc0;
            border: 1px solid #808080;
            padding: 10px;
            margin: 15px 0;
            font-size: 12px;
        }

        .warning-box {
            background: #ffc0c0;
            border: 2px solid #800000;
            padding: 10px;
            margin: 15px 0;
            font-size: 12px;
        }

        ul {
            margin-left: 25px;
            margin-bottom: 12px;
        }

        li {
            margin-bottom: 6px;
            font-size: 13px;
        }

        a {
            color: #0000ff;
            text-decoration: underline;
        }

        a:visited {
            color: #800080;
        }

        a:hover {
            color: #ff0000;
        }

        .image-placeholder {
            border: 2px inset #808080;
            background: #808080;
            padding: 40px;
            text-align: center;
            color: white;
            font-size: 12px;
            margin: 15px 0;
        }

        .tab-container {
            margin: 20px 0;
        }

        .tabs {
            display: flex;
            gap: 2px;
            margin-bottom: -2px;
        }

        .tab {
            background: #c0c0c0;
            border: 2px outset #fff;
            border-bottom: none;
            padding: 5px 15px;
            cursor: pointer;
            font-size: 11px;
            position: relative;
            z-index: 1;
        }

        .tab.active {
            background: white;
            border-bottom: 2px solid white;
            z-index: 2;
        }

        .tab-content {
            border: 2px inset #808080;
            background: white;
            padding: 15px;
            display: none;
        }

        .tab-content.active {
            display: block;
        }

        .grid-2col {
            display: flex;
            gap: 15px;
            margin: 15px 0;
        }

        .grid-2col > div {
            flex: 1;
        }

        @media (max-width: 768px) {
            body {
                padding: 10px;
            }

            .window {
                margin: 20px 0;
            }

            .grid-2col {
                flex-direction: column;
            }

            .desktop-icon {
                position: static;
                margin: 0 auto 20px;
            }
        }

        .blink {
            animation: blink-animation 1s steps(2, start) infinite;
        }

        @keyframes blink-animation {
            to {
                visibility: hidden;
            }
        }

        .marquee-container {
            background: #000;
            color: #00ff00;
            padding: 8px;
            border: 2px inset #808080;
            margin: 15px 0;
            font-family: "Courier New", monospace;
            font-size: 12px;
            overflow: hidden;
        }

        .ascii-art {
            font-family: "Courier New", monospace;
            font-size: 10px;
            line-height: 1.2;
            white-space: pre;
            background: #000;
            color: #00ff00;
            padding: 10px;
            border: 2px inset #808080;
            margin: 15px 0;
        }
    </style>
</head>
<body>

<div class="window">
    <div class="title-bar">
        <div class="title-text">
            <span class="title-icon">[C]</span>
            E-Waste Reverse Engineering Clinic - Charlotte, NC
        </div>
        <div class="window-controls">
            <div class="window-button">_</div>
            <div class="window-button">□</div>
            <div class="window-button">X</div>
        </div>
    </div>

    <div class="menu-bar">
        <span class="menu-item">File</span>
        <span class="menu-item">Edit</span>
        <span class="menu-item">View</span>
        <span class="menu-item">Resources</span>
        <span class="menu-item">Help</span>
    </div>

    <div class="window-content">
        <div class="content-frame">
            <h1>E-Waste Reverse Engineering Clinic</h1>
            
            <div class="info-box">
                <strong>Status:</strong> <span class="blink">>>> ACTIVE PROJECT <<<</span><br>
                <strong>Location:</strong> Charlotte, North Carolina<br>
                <strong>Mission:</strong> Teaching electronics through hands-on hardware exploration
            </div>

            <p>We are rebuilding a public hackerspace culture in Charlotte by teaching digital communication and electronics using discarded circuit boards and open hardware tools. Our workshops focus on practical reverse engineering skills that anyone can learn, using tools like the GreatFET One to probe chips and understand how modern electronics actually work.</p>

            <p>This is not about professional engineering credentials or expensive equipment. This is about curiosity, community learning, and rescuing knowledge from the landfill. We believe hardware literacy should be accessible to everyone, and that every city deserves a space where people can learn by taking things apart.</p>

            <div class="marquee-container">
                <marquee>*** NO GATEKEEPING *** EVERYONE WELCOME *** BRING YOUR QUESTIONS *** MISTAKES ARE HOW WE LEARN *** FREE WORKSHOPS *** RIGHT TO REPAIR ***</marquee>
            </div>

            <h2>What We Do</h2>
            
            <div class="grid-2col">
                <div>
                    <h3>Workshop Activities</h3>
                    <ul>
                        <li>Identify chips on discarded circuit boards</li>
                        <li>Use I²C and SPI probes to read chip addresses</li>
                        <li>Document findings in a shared database</li>
                        <li>Learn to read datasheets and pinouts</li>
                        <li>Practice basic soldering and desoldering</li>
                        <li>Understand USB enumeration and device protocols</li>
                    </ul>
                </div>
                <div>
                    <h3>Tools We Use</h3>
                    <ul>
                        <li>GreatFET One (open hardware USB tool)</li>
                        <li>Basic multimeters and logic analyzers</li>
                        <li>Magnification and lighting equipment</li>
                        <li>Python scripts for data collection</li>
                        <li>Datasheets and chip documentation</li>
                        <li>Your own curiosity and patience</li>
                    </ul>
                </div>
            </div>

            <div class="ascii-art">
███████╗ ██╗██╗   ██╗    ███████╗████████╗██╗  ██╗ ██████╗ ███████╗       ███╗   ██╗███████╗██╗   ██╗███████╗██████╗     ███████╗████████╗ ██████╗ ██████╗ 
██╔══██╗██║╚██╗ ██╔╝    ██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔════╝       ████╗  ██║██╔════╝██║   ██║██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║  ██║██║ ╚████╔╝     █████╗     ██║   ███████║██║   ██║███████╗       ██╔██╗ ██║█████╗  ██║   ██║█████╗  ██████╔╝    ███████╗   ██║   ██║   ██║██████╔╝
██║  ██║██║  ╚██╔╝      ██╔══╝     ██║   ██╔══██║██║   ██║╚════██║       ██║╚██╗██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗    ╚════██║   ██║   ██║   ██║██╔═══╝ 
██████╔╝██║   ██║       ███████╗   ██║   ██║  ██║╚██████╔╝███████║▄█╗    ██║ ╚████║███████╗ ╚████╔╝ ███████╗██║  ██║    ███████║   ██║   ╚██████╔╝██║     
╚═════╝ ╚═╝   ╚═╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═╝  ╚═══╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
                                                                                                                                                          
██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗                                                                                           
██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝                                                                                           
██║     █████╗  ███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗                                                                                          
██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║                                                                                          
███████╗███████╗██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝                                                                                          
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝                                                                                           
            </div>

            <h2>How It Works</h2>

            <div class="scrollbox">
                <p><strong>Step 1: Source E-Waste</strong></p>
                <p>We collect discarded electronics from donation centers, repair shops, and community members. Old modems, routers, printers, and computer peripherals are perfect candidates.</p>
                
                <p><strong>Step 2: Visual Inspection</strong></p>
                <p>Participants learn to identify chip types by their physical characteristics: package style, pin count, manufacturer markings, and context clues from surrounding components.</p>
                
                <p><strong>Step 3: Protocol Probing</strong></p>
                <p>Using the GreatFET One, we probe I²C and SPI buses to discover chip addresses and communication patterns. This teaches fundamental concepts about how devices talk to each other.</p>
                
                <p><strong>Step 4: Documentation</strong></p>
                <p>All findings go into our shared database. Board type, chip identification, interface protocols, and working condition are logged for future reference and educational use.</p>
                
                <p><strong>Step 5: Share Knowledge</strong></p>
                <p>Workshop materials, scripts, and documentation are published openly so other communities can replicate the clinic in their own cities.</p>
            </div>

            <div class="tab-container">
                <div class="tabs">
                    <div class="tab active" onclick="openTab(event, 'community')">Community Goals</div>
                    <div class="tab" onclick="openTab(event, 'status')">Current Status</div>
                    <div class="tab" onclick="openTab(event, 'involved')">Get Involved</div>
                </div>

                <div id="community" class="tab-content active">
                    <h3>Building a Hardware Community</h3>
                    <p>Our long-term goal is to establish a permanent hackerspace in Charlotte where people can access tools, learn skills, and work on projects together. We want to create a culture where hardware knowledge is shared freely and where making things is valued over buying things.</p>
                    
                    <p><strong>Core Values:</strong></p>
                    <ul>
                        <li>Open learning with no prerequisites or gatekeeping</li>
                        <li>Practical skills over theoretical credentials</li>
                        <li>Community ownership of knowledge and tools</li>
                        <li>Environmental consciousness through repair and reuse</li>
                        <li>Documentation that others can actually use</li>
                    </ul>

                    <p>We are creating educational materials that any city can adapt. The scripts, workshop formats, and documentation templates in this repository are designed to be copied, modified, and improved by other communities.</p>
                </div>

                <div id="status" class="tab-content">
                    <h3>Project Timeline</h3>
                    <p><strong>Phase 1 (Current):</strong> Initial workshops and tool development</p>
                    <ul>
                        <li>Testing workshop formats with small groups</li>
                        <li>Building Python scripts for data collection</li>
                        <li>Creating documentation templates and guides</li>
                        <li>Establishing relationships with e-waste sources</li>
                    </ul>

                    <p><strong>Phase 2 (Next 6 months):</strong> Regular public workshops</p>
                    <ul>
                        <li>Monthly hands-on sessions open to all skill levels</li>
                        <li>Growing the chip identification database</li>
                        <li>Developing repair-focused curriculum tracks</li>
                        <li>Building partnerships with local schools and libraries</li>
                    </ul>

                    <p><strong>Phase 3 (Long-term):</strong> Permanent hackerspace</p>
                    <ul>
                        <li>Secure dedicated space for tools and storage</li>
                        <li>Establish regular open hours and project nights</li>
                        <li>Create advanced curriculum for specific skills</li>
                        <li>Support other cities starting similar clinics</li>
                    </ul>

                    <div class="warning-box">
                        <strong>Note:</strong> This is a grassroots project with no corporate funding. Progress depends on volunteer effort and community participation. If you want this to happen faster, join us and help make it real.
                    </div>
                </div>

                <div id="involved" class="tab-content">
                    <h3>How to Participate</h3>
                    
                    <p><strong>Join a Workshop:</strong></p>
                    <p>Workshop signup information will be posted here as sessions are scheduled. Follow the GitHub repository for announcements or email splicer@hiddenlayermedia.com to be added to the notification list.</p>

                    <p><strong>Contribute to the Repository:</strong></p>
                    <ul>
                        <li>Add your own chip identification logs</li>
                        <li>Improve documentation and scripts</li>
                        <li>Share workshop format ideas</li>
                        <li>Report issues or suggest features</li>
                    </ul>

                    <p><strong>Start Your Own Clinic:</strong></p>
                    <p>Everything in this repository is freely licensed for reuse. Fork it, adapt it to your city, and let us know how it goes. We want to see this model spread.</p>

                    <p><strong>Donate Equipment:</strong></p>
                    <p>We accept donations of working or broken electronics, test equipment, and tools. Contact us for drop-off details.</p>

                    <a href="https://github.com/numbpill3d/e-waste-clinic" class="button">View on GitHub</a>
                    <a href="#" class="button">Workshop Signup (Coming Soon)</a>
                    <a href="docs/setup-instructions.html" class="button">Setup Guide</a>
                    <a href="CONTRIBUTING.html" class="button">Contribute</a>
                </div>
            </div>

            <div class="image-placeholder">
                <p>[IMAGE: JTAG Anatomy]</p>
                <p>/resources/images/06.jpg</p>
                <p>(Field reference for identifying chip types and reading pinouts)</p>
            </div>

            <h2>Resources</h2>
            
            <div class="grid-2col">
                <div>
                    <h3>Documentation</h3>
                    <ul>
                        <li><a href="https://greatscottgadgets.github.io/greatfet-tutorials/getting-started.html">GreatFET Setup Instructions</a></li>
                        <li><a href="docs/data-format.html">Data Logging Format Guide</a></li>
                        <li><a href="CONTRIBUTING.html">How to Contribute</a></li>
                        <li><a href="CODE_OF_CONDUCT.html">Code of Conduct</a></li>
                    </ul>
                </div>
                <div>
                    <h3>Scripts and Tools</h3>
                    <ul>
                        <li>i2c_probe.py (I²C address scanner)</li>
                        <li>usb_enum.py (USB device enumerator)</li>
                        <li>log_to_csv.py (Data formatter)</li>
                        <li>chip_lookup.py (Datasheet finder)</li>
                    </ul>
                </div>
            </div>

            <div class="info-box">
                <strong>Licenses:</strong><br>
                Code: MIT License (see LICENSE)<br>
                Documentation: CC-BY-SA 4.0 (see LICENSE.docs)<br>
                All materials are free to use, modify, and redistribute.
            </div>

            <hr style="border: 1px inset #808080; margin: 20px 0;">

            <p style="font-size: 11px; color: #808080;">
                <strong>Created by:</strong> v. Splicer, Hidden Layer Media, and the Charlotte Hardware Collective (in progress)<br>
                <strong>Contact:</strong> voidrane@proton.me<br>
                <strong>Website:</strong> voidrane.nekoweb.org<br>
                <strong>Last Updated:</strong> October 20, 2025<br>
                <strong>Best Viewed:</strong> With an open mind and a soldering iron nearby
            </p>
        </div>
    </div>

    <div class="status-bar">
        <div class="status-section">Ready</div>
        <div class="status-section">Community Project</div>
        <div class="status-section">Open Source</div>
        <div class="status-section">Right to Repair</div>
        <div class="status-section">DIY</div>
        <div class="status-section">Neon Maxima 2133</div>
    </div>
</div>

<script>
    function openTab(evt, tabName) {
        var i, tabcontent, tabs;
        
        tabcontent = document.getElementsByClassName("tab-content");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].classList.remove("active");
        }
        
        tabs = document.getElementsByClassName("tab");
        for (i = 0; i < tabs.length; i++) {
            tabs[i].classList.remove("active");
        }
        
        document.getElementById(tabName).classList.add("active");
        evt.currentTarget.classList.add("active");
    }
</script>

</body>
</html>
