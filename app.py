from flask import Flask, render_template, request,send_from_directory
from db.db import get_company_list, get_job_roles, get_locations, get_industry_types, get_alumni_info, get_job_numbers_by_location, get_job_numbers_by_industry
import xlwt



app = Flask(__name__)
alumni_cols = ['Name','Ph No.','Email Id', 'Linkedin Profile','GPA','Company', 'Location', 'Title', 'Start Date', 'End Date' , 'Salary']

@app.route('/')
@app.route('/home')
def index():
    company_list = get_company_list()
    job_roles = get_job_roles()
    locations = get_locations()
    industry_types = get_industry_types()
    return render_template('index.html', company_list=company_list, job_roles=job_roles, locations=locations, industry_types=industry_types)

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/search', methods =['POST'])
def search():

    company_list = get_company_list()
    job_roles = get_job_roles()
    locations = get_locations()
    industry_types = get_industry_types()

    new_request = request.form.to_dict(flat=False)

    company_name = new_request.get('company', "")
    location = new_request.get('location', "")
    job_role = new_request.get('jobrole', "")
    industry_type = new_request.get('industry', "")

    if company_name == '' and  location == '' and job_role == '' and industry_type == '':
        return render_template('index.html', company_list=company_list, job_roles=job_roles, locations=locations, industry_types=industry_types)

    alumni_info = get_alumni_info(company_name, location, job_role, industry_type)
    job_loc_info = get_job_numbers_by_location()
    job_industry_info = get_job_numbers_by_industry()

    create_excel(alumni_info)

    return render_template('search.html', company_list=company_list, job_roles=job_roles,
                            locations=locations,industry_types=industry_types,alumni_info=alumni_info,
                            job_loc_info=job_loc_info, job_industry_info=job_industry_info)

@app.route('/download')
def download_alumni_info():

    return send_from_directory("files/", "Alumni_info.xls", as_attachment=True)


def create_excel(alumni_info):
    filename = "files/Alumni_info.xls"
    excel_file = xlwt.Workbook()
    sheet = excel_file.add_sheet('Alumni Info')
    col = 0
    for i in alumni_cols:
        sheet.write(0,col,i)
        col+=1
    row = 1
    col = 0
    for alumni in alumni_info:
        sheet.write(row, col, alumni[0] + " " + alumni[1])
        sheet.write(row, col + 1, alumni[2])
        sheet.write(row, col + 2, alumni[3])
        sheet.write(row, col + 3, alumni[4])
        sheet.write(row, col + 4, alumni[5])
        sheet.write(row, col + 5, alumni[6])
        sheet.write(row, col + 6, alumni[7])
        sheet.write(row, col + 7, alumni[8])
        sheet.write(row, col + 8, alumni[9])
        sheet.write(row, col + 9, alumni[10])
        sheet.write(row, col + 10, alumni[11])
        row += 1
    excel_file.save(filename)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8080"),
        debug=True,
        threaded=True
    )