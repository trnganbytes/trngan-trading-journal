# Mình sẽ tạo file zip web mẫu TrNgan Trading Journal với cấu trúc chuẩn
import zipfile
import os

# Tạo thư mục tạm
os.makedirs('/mnt/data/TrNgan-Trading-Journal/posts', exist_ok=True)
os.makedirs('/mnt/data/TrNgan-Trading-Journal/assets/images', exist_ok=True)

# index.html
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TrNgan Trading Journal</title>
  <link rel="stylesheet" href="assets/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
</head>
<body>
  <header>
    <h1>TrNgan Trading Journal</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="analysis.html">Daily Analysis</a>
      <a href="about.html">About Me</a>
    </nav>
  </header>
  <main>
    <section class="intro">
      <h2>Welcome!</h2>
      <p>Your daily insight into stock market trends and trading reflections.</p>
    </section>
    <section class="featured">
      <h2>Latest Analysis</h2>
      <div class="card">
        <a href="posts/sample-post.html">VNM Daily Analysis - 11/11/2025</a>
      </div>
    </section>
  </main>
  <footer>
    <p>© 2025 TrNgan Trading Journal</p>
  </footer>
</body>
</html>'''

# about.html
about_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>About Me - TrNgan Trading Journal</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header>
  <h1>TrNgan Trading Journal</h1>
  <nav>
    <a href="index.html">Home</a>
    <a href="analysis.html">Daily Analysis</a>
    <a href="about.html">About Me</a>
  </nav>
</header>
<main>
  <section class="about">
    <h2>About Me</h2>
    <p>Hi, I'm TrNgan — a passionate trader and data analyst sharing daily stock insights.</p>
    <p>GitHub: <a href="https://github.com/TrNganBytes" target="_blank">TrNganBytes</a></p>
  </section>
</main>
<footer>
  <p>© 2025 TrNgan Trading Journal</p>
</footer>
</body>
</html>'''

# analysis.html
analysis_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Daily Analysis - TrNgan Trading Journal</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header>
  <h1>TrNgan Trading Journal</h1>
  <nav>
    <a href="index.html">Home</a>
    <a href="analysis.html">Daily Analysis</a>
    <a href="about.html">About Me</a>
  </nav>
</header>
<main>
  <section class="post">
    <h2>VNM Analysis - 11/11/2025</h2>
    <p>Today VNM increased by 2.3% with higher-than-average volume...</p>
    <iframe src="https://s.tradingview.com/widgetembed/?symbol=VNM&interval=D&hidesidetoolbar=1" width="600" height="400" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
  </section>
</main>
<footer>
  <p>© 2025 TrNgan Trading Journal</p>
</footer>
</body>
</html>'''

# sample post
sample_post = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>VNM Daily Analysis - 11/11/2025</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header>
  <h1>TrNgan Trading Journal</h1>
  <nav>
    <a href="../index.html">Home</a>
    <a href="../analysis.html">Daily Analysis</a>
    <a href="../about.html">About Me</a>
  </nav>
</header>
<main>
  <section class="post">
    <h2>VNM Analysis - 11/11/2025</h2>
    <p>Today VNM increased by 2.3% with higher-than-average volume...</p>
    <iframe src="https://s.tradingview.com/widgetembed/?symbol=VNM&interval=D&hidesidetoolbar=1" width="600" height="400" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
  </section>
</main>
<footer>
  <p>© 2025 TrNgan Trading Journal</p>
</footer>
</body>
</html>'''

# style.css
style_css = '''body {
  margin: 0;
  font-family: 'Poppins', sans-serif;
  background-color: #0e0e10;
  color: #f0f0f0;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 30px;
  background-color: #1a1a1a;
}
header h1 {
  margin: 0;
  font-size: 24px;
  color: #00bcd4;
}
nav a {
  margin-left: 20px;
  text-decoration: none;
  color: #f0f0f0;
}
nav a:hover {
  color: #00bcd4;
}
main {
  padding: 20px 30px;
}
.card {
  background-color: #1a1a1a;
  padding: 15px;
  border-radius: 10px;
  margin-bottom: 10px;
}
footer {
  text-align: center;
  padding: 10px;
  background-color: #1a1a1a;
}'''

# Ghi file vào thư mục tạm
with open('/mnt/data/TrNgan-Trading-Journal/index.html', 'w') as f:
    f.write(index_html)
with open('/mnt/data/TrNgan-Trading-Journal/about.html', 'w') as f:
    f.write(about_html)
with open('/mnt/data/TrNgan-Trading-Journal/analysis.html', 'w') as f:
    f.write(analysis_html)
with open('/mnt/data/TrNgan-Trading-Journal/posts/sample-post.html', 'w') as f:
    f.write(sample_post)
with open('/mnt/data/TrNgan-Trading-Journal/assets/style.css', 'w') as f:
    f.write(style_css)

# Tạo file zip
zipf = zipfile.ZipFile('/mnt/data/TrNgan-Trading-Journal.zip','w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk('/mnt/data/TrNgan-Trading-Journal'):
    for file in files:
        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), '/mnt/data/TrNgan-Trading-Journal'))
zipf.close()

'/mnt/data/TrNgan-Trading-Journal.zip'
