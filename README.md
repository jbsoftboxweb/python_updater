# Python Updating System

## Desciption
Here is a complete, improved Python Updater App with the following features:
<ul>
  <li>✅ Closes the main app before updating</li>
  <li>✅ Downloads ZIP from GitHub</li>
  <li>✅ Shows a Progress Bar</li>
  <li>✅ Extracts and replaces all files, including inside folders</li>
</ul>

## 🧠 How It Works
<ol>
  <li>Your main app runs this updater.</li>
  <li>The updater closes the main app (via PID or known method).</li>
  <li>It shows a progress bar during download.</li>
  <li>It extracts and replaces files.</li>
  <li>It cleans up temp files and closes.</li>
</ol>

## 🧩 Requirements
Install these packages if you haven't:
`pip install requests tqdm`

## Updater.py file

Check `Updater.py` file for Source Code

## 🧪 To Use It:
<ol>
  <li>Replace GITHUB_ZIP_URL with your actual download URL.</li>
    If Your use ower testing zip this is the url for it
        https://github.com/jbsoftboxweb/python_updater/releases/download/tesing/updater.zip
  <li>Put this script in an updates/ folder next to your main app.</li>
  <li>From your main app, run this updater script using:</li>
</ol>

## Main.py file
In your main app (e.g., main.py), call the updater before quitting:

Check `Main.py` file for Source Code
