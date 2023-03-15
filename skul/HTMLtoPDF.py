import pdfkit as pdf

pdf.from_string('Hello','string.pdf')

pdf.from_file('admit.html','file.pdf')

url='https://bd.linkedin.com/in/syedzakirhossain?original_referer=https%3A%2F%2Fwww.google.com%2F'

pdf.from_url(url,'website.pdf')