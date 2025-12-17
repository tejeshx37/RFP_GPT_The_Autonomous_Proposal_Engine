from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.cell(0, 10, 'Request for Proposal - Industrial Coating Services', new_x="LMARGIN", new_y="NEXT", align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', align='C')

def create_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    
    # Page 1
    pdf.add_page()
    pdf.set_font('Helvetica', '', 12)
    
    content_p1 = """
    Date: October 25, 2024
    Company: Apex Manufacturing Solutions
    Attention: Vendor Partners
    
    Overview:
    Apex Manufacturing Solution is seeking a qualified supplier for high-performance industrial coatings. 
    We specialize in heavy machinary and automotive component manufacturing. 
    Our upcoming project requires a reliable coating solution that ensures durability and safety under extreme conditions.
    
    We are looking for a partner who can provide a product that meets our specific technical requirements 
    and can deliver within a tight timeline.
    
    This RFP outlines our needs. Please review the technical specifications on the following page.
    """
    pdf.multi_cell(0, 10, content_p1)
    
    # Page 2
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, 'Technical Requirements & Commercial Terms', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', '', 12)
    
    content_p2 = """
    1. Temperature Resistance:
    The coating must be able to withstand temperatures of at least 200 degrees Celsius without degrading. 
    This is critical for our heat-treating process.
    
    2. Viscosity and Application:
    We require a viscosity of approximately 90-95 KU (Krebs Units) or similar standard to ensure proper flow 
    during our automated spray application. Ease of application is key.
    
    3. Industry Suitability:
    The product should be suitable for automotive and high-stress industrial environments. 
    Resistance to oil and chemicals is a plus.
    
    Budget:
    Our allocated budget for the initial batch is approximately $50,000 - $60,000.
    
    Submission Criteria:
    Please provide your proposal, including specific product recommendations and pricing, within 48 hours.
    """
    pdf.multi_cell(0, 10, content_p2)
    
    output_path = "data/sample_rfp.pdf"
    # fpdf2 output
    pdf.output(output_path)
    print(f"PDF generated at {output_path}")

if __name__ == "__main__":
    create_pdf()
