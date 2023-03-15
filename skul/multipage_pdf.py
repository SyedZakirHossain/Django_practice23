from django.http import HttpResponse

def Print_PDF(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="rayhan.pdf"'

        p = canvas.Canvas(response)

        p.drawString(100, 100, "Some text in first page.")
        p.showPage()

        p.drawString(200, 100, "Some text in second page.")
        p.showPage()

        p.drawString(300, 100, "Some text in third page")
        p.showPage()

        p.save()
        return response (p)