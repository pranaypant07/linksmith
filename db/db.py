from db_utils import rows_with_connection


def get_company_list():

    sql = '''
             SELECT 
             DISTINCT companyName 
             FROM 
             [LinkSmith.Company]
          '''

    results = rows_with_connection(sql)

    company_list = []

    for row in results:
        for company in row:
            company_list.append(company)

    return company_list

def get_locations():

    sql = '''
             SELECT 
             DISTINCT stateLocation 
             FROM [LinkSmith.Company]
          '''

    results = rows_with_connection(sql)

    locations = []

    for row in results:
        for location in row:
            locations.append(location)

    return locations

def get_job_roles():

    sql = '''
             SELECT 
             DISTINCT jobType 
             FROM [LinkSmith.JobRole]
          '''

    results = rows_with_connection(sql)

    job_roles = []

    for row in results:
        for job_role in row:
            job_roles.append(job_role)

    return job_roles

def get_industry_types():

    sql = '''
             SELECT
             DISTINCT industryType 
             FROM [LinkSmith.Company]
          '''

    results = rows_with_connection(sql)

    job_roles = []

    for row in results:
        for industry in row:
            job_roles.append(industry)

    return job_roles

def get_alumni_info(company_name, location,jobrole, industry_type):
    company_new_name = ""
    location_new = ""
    jobrole_new = ""
    industry_type_new = ""

    if company_name:
        for i in company_name:
            company_new_name += "'" + i.strip('[]') + "',"
    company_new_name = company_new_name[:-1]

    if location:
        for i in location:
            location_new += "'" + i.strip('[]') + "',"
    location_new = location_new[:-1]

    if jobrole:
        for i in jobrole:
            jobrole_new += "'" + i.strip('[]') + "',"
    jobrole_new = jobrole_new[:-1]

    if industry_type:
        for i in industry_type:
            industry_type_new += "'" + i.strip('[]') + "',"
    industry_type_new = industry_type_new[:-1]

    sql = '''
              SELECT 
                a.fName, 
                a.lName,
                a.pNumber, 
                a.emailId, 
                a.linkedinProfile, 
                a.gpa, 
                c.companyName, 
                c.stateLocation,
                jr.jobType,     
                wi.startDate, 
                wi.endDate, 
                jr.salary
              FROM 
                [LinkSmith.Alumni] a, 
                [LinkSmith.Company] c, 
                [LinkSmith.WorksIn] wi, 
                [LinkSmith.JobRole] jr
            WHERE
                a.alumniId = wi.alumniId AND 
                wi.companyId= c.companyId AND
                wi.jobId = jr.jobId AND
            '''

    if company_new_name and location_new and jobrole_new and industry_type_new:
        sql = sql + '''
                    c.companyName in ({}) AND
                    c.stateLocation in ({}) AND
                    c.industryType in ({}) AND
                    jr.jobType in ({});
                    '''.format(company_new_name, location_new, industry_type_new, jobrole_new)

    elif company_new_name and location_new and jobrole_new and industry_type_new == '':
        sql = sql + '''
                    c.companyName in ({}) AND
                    c.stateLocation in ({}) AND
                    jr.jobType in ({});
                    '''.format(company_new_name, location_new,jobrole_new)

    elif company_new_name and location_new and industry_type_new and jobrole_new == '':
        sql = sql + '''
                    c.companyName in ({}) AND
                    c.stateLocation in ({}) AND
                    c.industryType in ({});
                    '''.format(company_new_name, location_new, industry_type_new)

    elif company_new_name and jobrole_new and industry_type_new and location_new == '':
        sql = sql + '''
                    c.companyName in ({}) AND
                    jr.jobType in ({}) AND
                    c.industryType in ({});
                    '''.format(company_new_name, jobrole_new, industry_type_new)

    elif location_new and jobrole_new and industry_type_new and company_new_name == '':
        sql = sql + '''
                    c.stateLocation in ({}) AND
                    jr.jobType in ({}) AND
                    c.industryType in ({});
                    '''.format(location_new, jobrole_new, industry_type_new)

    elif company_new_name and location_new and jobrole_new == '' and industry_type_new == '':
        sql = sql + '''
                    c.companyName in ({}) AND
                    c.stateLocation in ({});
                    '''.format(company_new_name, location_new)

    elif company_new_name and location_new == '' and jobrole_new and industry_type_new == '':
        sql = sql + '''
                    c.companyName in ({}) AND
                    jr.jobType in ({});
                    '''.format(company_new_name, jobrole_new)

    elif company_new_name and location_new == '' and jobrole_new == '' and industry_type_new:
        sql = sql + '''
                    c.companyName in ({}) AND
                    c.industryType in ({});
                    '''.format(company_new_name, industry_type_new)

    elif company_new_name == '' and location_new  and jobrole_new  and industry_type_new == '':
        sql = sql + '''
                    c.stateLocation  in ({}) AND
                    jr.jobType in ({});
                    '''.format(location_new, jobrole_new)

    elif company_new_name == '' and location_new  and jobrole_new == '' and industry_type_new:
        sql = sql + '''
                    c.stateLocation  in ({}) AND
                    c.industryType in ({});
                    '''.format(location_new, industry_type_new)

    elif company_new_name == '' and location_new == ''  and jobrole_new  and industry_type_new:
        sql = sql + '''
                    jr.jobType in ({}) AND
                    c.industryType in ({});
                    '''.format(jobrole_new, industry_type_new)

    elif company_new_name and location_new == ''  and jobrole_new == ''  and industry_type_new == '':
        sql = sql + '''
                    c.companyName in ({});
                    '''.format(company_new_name)

    elif company_new_name == '' and location_new  and jobrole_new == ''  and industry_type_new == '':
        sql = sql + '''
                    c.stateLocation  in ({});
                    '''.format(location_new)

    elif company_new_name == '' and location_new  and jobrole_new == ''  and industry_type_new == '':
        sql = sql + '''
                    c.stateLocation  in ({});
                    '''.format(location_new)

    elif company_new_name == '' and location_new == '' and jobrole_new and industry_type_new == '':
        sql = sql + '''
                    jr.jobType in ({});
                    '''.format(jobrole_new)

    elif company_new_name == '' and location_new == '' and jobrole_new == '' and industry_type_new:
        sql = sql + '''
                    c.industryType in ({});
                    '''.format(industry_type_new)


    return rows_with_connection(sql)

def get_job_numbers_by_location():

    sql = '''
             SELECT 
             stateLocation, 
             COUNT(*) 
             FROM [LinkSmith.Company] 
             GROUP BY stateLocation 
             ORDER BY stateLocation
          '''

    return rows_with_connection(sql)

def get_job_numbers_by_industry():

    sql = '''
             SELECT 
             industryType, 
             COUNT(*) 
             FROM [LinkSmith.Company] 
             GROUP BY industryType 
             ORDER BY industryType
          '''

    return rows_with_connection(sql)


