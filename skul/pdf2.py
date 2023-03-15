from fpdf import FPDF

from .models import students
pdf=FPDF('P', 'mm' , 'A4')

pdf.add_page()

pdf.set_font('helvetica', '',16)

pdf.cell(40,10,{{students}})

pdf.output('pdf11.pdf')